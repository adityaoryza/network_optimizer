import subprocess
import logging
from typing import Tuple
from .exceptions import CommandExecutionError

logger = logging.getLogger(__name__)

class CommandExecutor:
    """Executes system commands robustly."""
    
    @staticmethod
    def run(command: str, silent_error: bool = False) -> Tuple[bool, str]:
        """
        Runs a shell command and returns the success status and output.
        """
        logger.debug(f"Executing command: {command}")
        try:
            result = subprocess.run(
                command,
                shell=True,
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            return True, result.stdout.strip()
        except subprocess.CalledProcessError as e:
            if not silent_error:
                logger.error(f"Command execution failed: {command}. Error: {e.stderr.strip()}")
            raise CommandExecutionError(f"Failed to execute '{command}': {e.stderr.strip()}") from e
