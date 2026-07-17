import logging
from .base import BaseOptimizer
from core.executor import CommandExecutor
from core.exceptions import CommandExecutionError

logger = logging.getLogger(__name__)

class TCPOptimizer(BaseOptimizer):
    """Optimizer strategy for TCP/IP stack parameters."""

    def apply_optimization(self) -> None:
        logger.info(f"Applying {self.get_name()}...")
        commands = [
            ("netsh int ip reset", "Reset TCP/IP configuration"),
            ("netsh int tcp set global autotuninglevel=normal", "Enable TCP Auto-Tuning"),
            ("netsh int tcp set global ecncapability=enabled", "Enable TCP ECN Capability")
        ]

        for cmd, desc in commands:
            logger.debug(f"Step: {desc}")
            try:
                # Silently fail if it's the notorious netsh int ip reset command
                is_reset_cmd = "ip reset" in cmd
                CommandExecutor.run(cmd, silent_error=is_reset_cmd)
                logger.info(f"Successfully applied: {desc}")
            except CommandExecutionError as e:
                # `netsh int ip reset` frequently returns a false-positive "Access Denied" error 
                # on a specific sub-registry key in Windows 10/11, despite succeeding partially. 
                # We gracefully skip and proceed to the next critical commands.
                if is_reset_cmd:
                    logger.warning(f"[SKIPPED] {desc} (Ignored Windows false-positive Access Denied).")
                else:
                    logger.warning(f"[SKIPPED] Failed to apply '{desc}', continuing to next step... Error: {e}")

    def get_name(self) -> str:
        return "TCP/IP Stack Optimizer"
