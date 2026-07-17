import os
import logging

# Enable ANSI Escape Sequences for Windows 10/11 Terminal
os.system("")

class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class ColoredFormatter(logging.Formatter):
    """Custom logging formatter to inject colors into the terminal output."""
    
    FORMATS = {
        logging.DEBUG: Colors.OKCYAN + "[-] " + Colors.ENDC + "%(message)s",
        logging.INFO: Colors.OKGREEN + "[+] " + Colors.ENDC + "%(message)s",
        logging.WARNING: Colors.WARNING + "[!] WARNING: " + Colors.ENDC + "%(message)s",
        logging.ERROR: Colors.FAIL + "[x] ERROR: " + Colors.ENDC + "%(message)s",
        logging.CRITICAL: Colors.BOLD + Colors.FAIL + "[X] CRITICAL: %(message)s" + Colors.ENDC
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)
