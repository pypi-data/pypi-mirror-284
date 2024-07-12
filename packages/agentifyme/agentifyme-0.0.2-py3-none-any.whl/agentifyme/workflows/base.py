import time
import functools

import trace
from typing import (
    List,
    Union,
    Callable,
    ParamSpec,
    Any,
    TypeVar,
    Optional,
    Dict,
    ClassVar,
)
from uuid import uuid4
from agentifyme.config import AgentifyMeConfig
from agentifyme.utilities.meta import Param, function_metadata
from agentifyme.utilities.log import getLogger, send_tracing_event


P = ParamSpec("P")
R = TypeVar("R", bound=Callable[..., Any])

logger = getLogger()


class WorkflowError(Exception):
    pass


class WorfklowExecutionError(WorkflowError):
    pass


class WorkflowConfig(AgentifyMeConfig):
    """
    Represents a workflow in the system.

    Attributes:
        name (str): The name of the workflow.
        slug (str): The slug of the workflow.
        description (Optional[str]): The description of the workflow (optional).
        func (Callable[..., Any]): The function associated with the workflow.
        input_params (List[Param]): The list of input parameters for the workflow.
        output_params (List[Param]): The list of output parameters for the workflow.
    """

    name: str
    slug: str
    description: Optional[str]
    func: Callable[..., Any]
    input_params: List[Param]
    output_params: List[Param]


def workflow(
    name: str,
    description: Optional[str] = None,
) -> Callable[[Callable[P, R]], Callable[P, Union[R, WorkflowConfig, None]]]:
    """
    Decorator function for defining a workflow.

    Args:
        name (str): The name of the workflow.
        description (Optional[str], optional): The description of the workflow. Defaults to None.

    Returns:
        Callable[[Callable[P, R]], Callable[P, Union[R, Workflow]]]: The decorator function.

    """

    def decorator(func: Callable[P, R]) -> Callable[P, Union[R, WorkflowConfig, None]]:
        """
        Decorator function that wraps the workflow function.

        Args:
            func (Callable[P, R]): The function to be wrapped.

        Returns:
            Callable[P, Union[R, Workflow]]: The wrapped function.

        """
        fn_metadata = function_metadata(func)
        _workflow = WorkflowConfig(
            name=fn_metadata.name,
            description=description or fn_metadata.description,
            slug=name.lower().replace(" ", "_"),
            func=func,
            input_params=fn_metadata.input_params,
            output_params=fn_metadata.output_params,
        )
        WorkflowConfig.register_workflow(_workflow)

        @functools.wraps(func)
        def wrapped(
            *args: P.args, **kwargs: P.kwargs
        ) -> Union[R, WorkflowConfig, None]:
            """
            Wrapped function that executes the workflow.

            Args:
                *args (P.args): Positional arguments for the function.
                **kwargs (P.kwargs): Keyword arguments for the function.

            Returns:
                Union[R, Workflow]: The result of the function or the workflow object.

            """
            start_time = time.perf_counter()
            result = None

            trace_id = str(uuid4().hex)
            span_id = str(uuid4().hex)
            workflow_id = str(uuid4())
            event_dict = {
                "id": str(uuid4()),
                "timestamp": time.time_ns(),
                "type": "on_workflow_start",
                "data": "{}",
                "trace_id": trace_id,
                "span_id": span_id,
                "parent_span_id": "",
                "source": "",
                "project_id": "",
                "workflow_id": workflow_id,
            }
            print(trace_id, span_id)
            send_tracing_event(event_dict)

            # try:
            #     result = func(*args, **kwargs)
            # except Exception as e:
            #     logger.error(f"Error executing workflow {name}: {str(e)}")

            result = func(*args, **kwargs)

            end_time = time.perf_counter()

            print(f"Workflow {name} executed in {end_time - start_time:.2f} seconds")

            event_dict = {
                "id": str(uuid4()),
                "timestamp": time.time_ns(),
                "type": "on_workflow_end",
                "data": "{}",
                "trace_id": trace_id,
                "span_id": span_id,
                "parent_span_id": "",
                "source": "",
                "project_id": "",
                "workflow_id": workflow_id,
            }
            send_tracing_event(event_dict)

            return result

        return wrapped

    return decorator
