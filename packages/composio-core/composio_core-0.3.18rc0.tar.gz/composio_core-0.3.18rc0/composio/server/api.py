"""
API Endpoints.
"""

import importlib
from pathlib import Path
import subprocess
import traceback
import typing as t
from functools import update_wrapper

from composio.client.enums.base import get_runtime_actions
import typing_extensions as te
from fastapi import FastAPI
from pydantic import BaseModel, Field

from composio import Action, App
from composio.cli.context import get_context
from composio.client.collections import ActionModel, AppModel


ResponseType = t.TypeVar("ResponseType")

R = t.TypeVar("R")
T = t.TypeVar("T")
P = te.ParamSpec("P")
F = t.TypeVar("F")


class APIResponse(BaseModel, t.Generic[ResponseType]):
    """API Response."""

    data: t.Optional[ResponseType]
    error: t.Optional[str] = None
    traceback: t.Optional[str] = None


class GetApiResponse(BaseModel):
    """Response for GET /api."""

    version: str = Field(
        ...,
        description="Current API version.",
    )


class ToolUploadRequest(BaseModel):
    """Tool upload request."""

    content: str = Field(
        ...,
        description="Content from the tool description file.",
    )
    filename: str = Field(
        ...,
        description="Name of the file.",
    )
    dependencies: t.List[str] = Field(
        ...,
        description="List of dependencies.",
    )


def create_app() -> FastAPI:
    """Create Fast API app."""
    app = FastAPI()

    def with_exception_handling(f: t.Callable[P, R]) -> t.Callable[P, APIResponse[R]]:
        """Marks a callback as wanting to receive the current context object as first argument."""

        def wrapper(*args: P.args, **kwargs: P.kwargs) -> APIResponse[R]:
            try:
                return APIResponse[R](data=f(*args, **kwargs))
            except Exception as e:
                return APIResponse[R](
                    data=None,
                    error=str(e),
                    traceback=traceback.format_exc(),
                )

        return update_wrapper(wrapper, f)

    @app.get("/api", response_model=APIResponse[GetApiResponse])
    @with_exception_handling
    def _api() -> GetApiResponse:
        """Composio tooling server API root."""
        return GetApiResponse(
            version="0.3.19",
        )

    @app.get("/api/apps", response_model=APIResponse[t.List[AppModel]])
    @with_exception_handling
    def _get_apps() -> t.List[AppModel]:
        """Get list of all available apps."""
        return get_context().client.apps.get()

    @app.get("/api/apps/{name}", response_model=APIResponse[AppModel])
    @with_exception_handling
    def _get_apps_by_name(name: str) -> AppModel:
        """Get list of all available apps."""
        return get_context().client.apps.get(name=name)

    @app.get("/api/actions", response_model=APIResponse[t.List[ActionModel]])
    @with_exception_handling
    def _get_actions() -> t.List[ActionModel]:
        """Get list of all available actions."""
        return get_context().client.actions.get()

    @app.get("/api/actions/{name}", response_model=APIResponse[ActionModel])
    @with_exception_handling
    def _get_actions_by_name(name: str) -> ActionModel:
        """Get list of all available apps."""
        return get_context().client.actions.get(actions=[name])[0]

    @app.get("/api/enums/actions", response_model=APIResponse[t.List[str]])
    @with_exception_handling
    def _get_actions_enums() -> t.List[str]:
        """Get list of all available actions."""
        return [action.slug for action in Action.all()]

    @app.get("/api/enums/apps", response_model=APIResponse[t.List[str]])
    @with_exception_handling
    def _get_app_enums() -> t.List[str]:
        """Get list of all available actions."""
        return [app.slug for app in App.all()]

    @app.post("/api/actions/execute/{action}", response_model=APIResponse[t.Dict])
    @with_exception_handling
    def _execute_action(action: str, params: t.Dict) -> t.Dict:
        """Execute an action."""
        return get_context().toolset.execute_action(
            action=action,
            params=params,
        )

    @app.get("/api/workspace", response_model=APIResponse[t.Dict])
    @with_exception_handling
    def _get_workspace_information() -> t.Dict:
        """Get information on current workspace."""
        return {"type": get_context().toolset.workspace.__class__.__name__}

    @app.get("/api/tools", response_model=APIResponse[t.List[str]])
    @with_exception_handling
    def _get_workspace_tools() -> t.List[str]:
        """Get list of available developer tools."""
        return get_runtime_actions()

    @app.post("/api/tools", response_model=APIResponse[t.List[str]])
    @with_exception_handling
    def _upload_workspace_tools(request: ToolUploadRequest) -> t.List[str]:
        """Get list of available developer tools."""
        process = subprocess.run(
            args=["pip", "install", *request.dependencies],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        if process.returncode != 0:
            raise RuntimeError(
                f"Error installing dependencies: {process.stderr.decode()}"
            )

        import tempfile

        with tempfile.TemporaryDirectory() as tempdir:
            tempfile = Path(tempdir, request.filename)
            exec(request.content)

        return get_runtime_actions()

    return app
