def format_sandbox_timeout_exception(message: str):
    return TimeoutException(
        f"{message}: This error is likely due to sandbox timeout. You can modify the sandbox timeout by passing 'timeoutMs' when starting the sandbox or calling '.setTimeout' on the sandbox with the desired timeout."
    )


class SandboxException(Exception):
    """
    Raised when a sandbox exception occurs.

    Base class for all sandbox errors.
    """

    pass


class TimeoutException(SandboxException):
    """
    Raised when a timeout occurs.

    The [unavailable] exception type is caused by sandbox timeout.\n
    The [canceled] exception type is caused by exceeding request timeout.\n
    The [deadline_exceeded] exception type is caused by exceeding the timeout for process, watch, etc.\n
    The [unknown] exception type is sometimes caused by the sandbox timeout when the request is not processed correctly.\n
    """

    pass


class NotEnoughSpaceException(SandboxException):
    """
    Raised when there is not enough disk space.
    """

    pass


class NotFoundException(SandboxException):
    """
    Raised when a resource is not found.
    """

    pass


class InvalidArgumentException(SandboxException):
    """
    Raised when an invalid argument is provided.
    """

    pass


class AuthenticationException(SandboxException):
    """
    Raised when authentication fails.
    """

    pass


class TemplateException(SandboxException):
    """
    Exception raised when the template uses old envd version. It isn't compatible with the new SDK.
    """
