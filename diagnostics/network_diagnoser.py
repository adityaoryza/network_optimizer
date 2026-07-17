import socket
import logging
from typing import List
from core.executor import CommandExecutor
from utils.colors import Colors

logger = logging.getLogger(__name__)

class NetworkDiagnoser:
    """Diagnoses common network issues before optimization."""
    
    def __init__(self):
        self.issues_found: List[str] = []

    def test_internet_connectivity(self) -> bool:
        """Pings a reliable server to check for general connectivity."""
        logger.debug("Testing basic internet connectivity...")
        # Ping 1.1.1.1 with 1 packet, wait max 2 seconds
        success, output = CommandExecutor.run("ping -n 1 -w 2000 1.1.1.1", silent_error=True)
        if not success or "unreachable" in output.lower() or "100% loss" in output.lower():
            self.issues_found.append("No active internet connection or severe packet loss detected.")
            return False
        return True

    def test_dns_resolution(self) -> bool:
        """Tests if DNS is resolving domain names properly."""
        logger.debug("Testing DNS resolution...")
        try:
            # Set a timeout so it doesn't hang forever
            socket.setdefaulttimeout(3)
            socket.gethostbyname("google.com")
            return True
        except socket.gaierror:
            self.issues_found.append("DNS Resolution Failed. Your DNS cache might be corrupted or your ISP DNS is down.")
            return False
        except socket.timeout:
            self.issues_found.append("DNS Resolution Timed Out. Connection is extremely slow or dropping.")
            return False

    def run_diagnostics(self) -> None:
        """Executes all health checks and logs the results."""
        print(f"    {Colors.OKCYAN}Analyzing Network Health...{Colors.ENDC}")
        
        has_internet = self.test_internet_connectivity()
        
        # Only test DNS if we actually have internet routing
        if has_internet:
            self.test_dns_resolution()
            
        print(f"    {Colors.BOLD}--- DIAGNOSIS REPORT ---{Colors.ENDC}")
        if not self.issues_found:
            print(f"    {Colors.OKGREEN}✓ Network is generally healthy. Optimization will focus on maximizing speed/throughput.{Colors.ENDC}\n")
        else:
            print(f"    {Colors.WARNING}⚠ Issues Detected:{Colors.ENDC}")
            for issue in self.issues_found:
                print(f"      - {Colors.FAIL}{issue}{Colors.ENDC}")
            print(f"    {Colors.OKCYAN}The optimizer will attempt to resolve these issues...{Colors.ENDC}\n")
