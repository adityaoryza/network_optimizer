import sys
import logging
import time
from typing import List

from utils.privilege import PrivilegeChecker
from utils.colors import ColoredFormatter, Colors
from core.exceptions import NetworkOptimizerError
from optimizers.base import BaseOptimizer
from optimizers.dns_optimizer import DNSOptimizer
from optimizers.tcp_optimizer import TCPOptimizer
from benchmarks.ping_tester import PingTester

# Configure colored logging for the root logger
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(ColoredFormatter())

root_logger = logging.getLogger()
root_logger.setLevel(logging.INFO)
# Clear default handlers and attach the custom colored formatter
if root_logger.hasHandlers():
    root_logger.handlers.clear()
root_logger.addHandler(handler)

logger = logging.getLogger("NetworkOptimizerApp")

class NetworkOptimizationFacade:
    """Facade to manage and orchestrate various network optimizers."""

    def __init__(self, optimizers: List[BaseOptimizer]):
        self._optimizers = optimizers
        self.ping_tester = PingTester(target_host="1.1.1.1", ping_count=4)

    def print_banner(self, title: str):
        print(f"\n{Colors.OKBLUE}{Colors.BOLD}╔{'═' * 58}╗{Colors.ENDC}")
        print(f"{Colors.OKBLUE}{Colors.BOLD}║ {title.center(56)} ║{Colors.ENDC}")
        print(f"{Colors.OKBLUE}{Colors.BOLD}╚{'═' * 58}╝{Colors.ENDC}")

    def run_all(self) -> None:
        """Executes benchmarks and all registered optimizers."""
        
        # TITLE BANNER
        print(f"{Colors.HEADER}{Colors.BOLD}")
        print(r"  _   _      _                      _      ____        _   ")
        print(r" | \ | | ___| |___      _____  _ __| | __ / __ \ _ __ | |_ ")
        print(r" |  \| |/ _ \ __\ \ /\ / / _ \| '__| |/ // / _` | '_ \| __|")
        print(r" | |\  |  __/ |_ \ V  V / (_) | |  |   <| | (_| | |_) | |_ ")
        print(r" |_| \_|\___|\__| \_/\_/ \___/|_|  |_|\_\\ \__,_| .__/ \__|")
        print(r"                                          \____/|_|        ")
        print(f"                                   v1.0 - by adityaoryza{Colors.ENDC}\n")

        self.print_banner("COLLECTING PRE-OPTIMIZATION METRICS (BEFORE)")
        before_ping = self.ping_tester.measure_average_latency()
        if before_ping is not None:
            print(f"    {Colors.OKCYAN}Average Latency (Before): {Colors.BOLD}{before_ping} ms{Colors.ENDC}\n")
        else:
            logger.warning("Failed to collect initial latency metrics.\n")

        self.print_banner("NETWORK HEALTH DIAGNOSTICS")
        from diagnostics.network_diagnoser import NetworkDiagnoser
        diagnoser = NetworkDiagnoser()
        diagnoser.run_diagnostics()

        self.print_banner("INITIATING NETWORK OPTIMIZATION SEQUENCE")

        
        for optimizer in self._optimizers:
            try:
                optimizer.apply_optimization()
            except NetworkOptimizerError as e:
                logger.warning(f"Optimization '{optimizer.get_name()}' failed. Error: {e}")
            except Exception as e:
                logger.critical(f"Unexpected error during '{optimizer.get_name()}': {e}", exc_info=True)

        self.print_banner("COLLECTING POST-OPTIMIZATION METRICS (AFTER)")
        # Introduce a brief delay to allow the network adapter to fully initialize new configurations
        time.sleep(2) 
        after_ping = self.ping_tester.measure_average_latency()
        if after_ping is not None:
            print(f"    {Colors.OKCYAN}Average Latency (After): {Colors.BOLD}{after_ping} ms{Colors.ENDC}\n")
        else:
            logger.warning("Failed to collect post-optimization latency metrics.")

        self.print_banner("OPTIMIZATION SUMMARY")
        if before_ping is not None and after_ping is not None:
            if after_ping < before_ping:
                improvement = before_ping - after_ping
                print(f"  {Colors.OKGREEN}{Colors.BOLD}★ LATENCY IMPROVED BY {improvement} MS! ★{Colors.ENDC}")
            elif after_ping == before_ping:
                print(f"  {Colors.OKCYAN}{Colors.BOLD}≈ LATENCY STABLE (Optimization primarily affects packet loss & throughput) ≈{Colors.ENDC}")
            else:
                print(f"  {Colors.WARNING}{Colors.BOLD}▼ LATENCY SLIGHTLY INCREASED (Expected behavior during immediate post-DNS flush) ▼{Colors.ENDC}")
        
        print(f"\n{Colors.WARNING}>> A SYSTEM RESTART is highly recommended to fully apply TCP Auto-Tuning parameters! <<{Colors.ENDC}\n")

def main():
    if not PrivilegeChecker.is_admin():
        logger.warning("Administrator privileges are required.")
        logger.warning("Spawning an elevated Administrator terminal (UAC)... Please grant access.")
        
        import ctypes
        # Auto-elevate the process via ShellExecuteW to prompt UAC.
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        sys.exit(0)

    # Dependency Injection of Optimizers
    optimizers = [
        DNSOptimizer(),
        TCPOptimizer()
    ]

    app = NetworkOptimizationFacade(optimizers)
    app.run_all()
    
    # Pause execution to prevent the newly spawned elevated terminal from closing immediately
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
