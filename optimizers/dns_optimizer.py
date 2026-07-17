import logging
from .base import BaseOptimizer
from core.executor import CommandExecutor
from core.exceptions import CommandExecutionError

logger = logging.getLogger(__name__)

class DNSOptimizer(BaseOptimizer):
    """Optimizer strategy for DNS related settings."""

    def apply_optimization(self) -> None:
        logger.info(f"Applying {self.get_name()}...")
        try:
            CommandExecutor.run("ipconfig /flushdns")
            logger.info("Successfully flushed DNS cache.")
        except CommandExecutionError as e:
            logger.error(f"Failed during DNS optimization: {e}")
            raise

    def get_name(self) -> str:
        return "DNS Cache Optimizer"
