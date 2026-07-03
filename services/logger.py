#logger functionality with color codes for different log levels

class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def log_info(message: str, color: str = Color.BLUE):
    print(f"{color}[INFO] {message}{Color.END}")

def log_warning(message: str, color: str = Color.YELLOW):
    print(f"{color}[WARNING] {message}{Color.END}")

def log_error(message: str, color: str = Color.RED):
    print(f"{color}[ERROR] {message}{Color.END}")

def log_success(message: str, color: str = Color.GREEN):
    print(f"{color}[SUCCESS] {message}{Color.END}") 

    