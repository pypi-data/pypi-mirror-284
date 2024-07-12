import typing
from logging import Logger

from azure.functions import AppExtensionBase, Context, HttpResponse
import time

class TracerExtension(AppExtensionBase):
    """A Python worker extension to start Datadog tracer for Azure Functions
    """

    @classmethod
    def init(cls):
        print("=========== in init NEW2 =============")

    @classmethod
    def pre_invocation_app_level(
        cls, logger: Logger, context: Context,
        func_args: typing.Dict[str, object],
        *args, **kwargs
    ) -> None:
        
        from ddtrace import patch_all, tracer
        patch_all()

        time.sleep(3)
        # spanZero = tracer.trace('span')  # span is started once created
        # print("span id: ", spanZero)
        # spanZero.finish()

    @classmethod
    def post_invocation_app_level(
        cls, logger: Logger, context: Context,
        func_args: typing.Dict[str, object],
        func_ret: typing.Optional[object],
        *args, **kwargs
    ) -> None:
        pass