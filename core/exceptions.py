class NetworkOptimizerError(Exception):
    """Base exception for network optimizer."""
    pass

class CommandExecutionError(NetworkOptimizerError):
    """Raised when a system command fails."""
    pass

class PrivilegeError(NetworkOptimizerError):
    """Raised when the application lacks required administrative privileges."""
    pass
