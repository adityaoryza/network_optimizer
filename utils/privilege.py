import ctypes
import logging

logger = logging.getLogger(__name__)

class PrivilegeChecker:
    """Utility class for checking system privileges."""

    @staticmethod
    def is_admin() -> bool:
        """
        Checks if the current process has Administrator privileges on Windows.
        """
        try:
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
            logger.debug(f"Admin privilege check: {is_admin}")
            return is_admin
        except Exception as e:
            logger.error(f"Failed to verify admin privileges: {e}")
            return False
