import re
import logging
from typing import Optional
from core.executor import CommandExecutor
from core.exceptions import CommandExecutionError

logger = logging.getLogger(__name__)

class PingTester:
    """Measures network latency (ping) to a specific host."""
    
    def __init__(self, target_host: str = "8.8.8.8", ping_count: int = 4):
        self.target_host = target_host
        self.ping_count = ping_count

    def measure_average_latency(self) -> Optional[float]:
        """
        Executes a ping command and parses the average latency.
        Returns the average latency in milliseconds, or None if it fails.
        """
        logger.info(f"Testing ping to {self.target_host} ({self.ping_count} packets)...")
        command = f"ping -n {self.ping_count} {self.target_host}"
        
        try:
            success, output = CommandExecutor.run(command)
            if not success:
                return None
                
            # Regex to capture "Average = Xms" or "Rata-rata = Xms" (accommodating localized Windows builds)
            match = re.search(r'(?:Average|Rata-rata)\s*=\s*(\d+)ms', output, re.IGNORECASE)
            if match:
                avg_latency = float(match.group(1))
                return avg_latency
            else:
                logger.warning("Failed to parse the ping output for average latency metrics.")
                return None
                
        except CommandExecutionError as e:
            logger.error(f"Ping test failed: {e}")
            return None
