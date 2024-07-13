import functools
from typing import ClassVar, TypeVar, Any, List, ParamSpec, Dict, Callable, Optional
from agentifyme.config import AgentifyMeConfig
from pydantic import BaseModel

from agentifyme.tools import Tool
from agentifyme.utilities.meta import function_metadata, Param

TaskOutputType = TypeVar("TaskOutputType")


class TaskConfig(AgentifyMeConfig):
    """
    Represents the configuration for a task.

    Attributes:
        name (str): The name of the task.
        description (str): The description of the task.
        tools (List[str]): The list of tools required for the task.
    """

    registry: ClassVar[Dict[str, "TaskConfig"]] = {}

    name: str
    description: str
    input_params: List[Param]
    output_params: List[Param]

    class Config:
        """Pydantic configuration."""

        frozen = True


class Task:

    objective: str
    instructions: str
    tools: List[Tool]

    def __init__(
        self,
        objective: str,
        instructions: str,
        tools: List[Tool],
        llm: str,
    ) -> None:
        self.objective = objective
        self.instructions = instructions
        self.tools = tools
        self.llm = llm

    def __call__(self, *args, **kwargs) -> TaskOutputType:
        return self.run(*args, **kwargs)

    def run(self, response_model) -> TaskOutputType:
        raise NotImplementedError


P = ParamSpec("P")
R = TypeVar("R", bound=Callable[..., Any])


def task(
    name: str, description: Optional[str] = None
) -> Callable[[Callable[P, R]], Callable[P, R]]:

    def decorator(func: Callable[P, R]) -> Callable[P, R]:

        fn_metadata = function_metadata(func)
        task_config = TaskConfig(
            name=fn_metadata.name,
            description=description or fn_metadata.description,
            input_params=fn_metadata.input_params,
            output_params=fn_metadata.output_params,
        )

        TaskConfig.register_task(task_config)

        @functools.wraps(func)
        def wrapped(*args: P.args, **kwargs: P.kwargs) -> R:
            return func(*args, **kwargs)

        return func

    return decorator
