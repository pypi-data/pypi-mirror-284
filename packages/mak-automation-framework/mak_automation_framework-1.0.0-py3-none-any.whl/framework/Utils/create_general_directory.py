import os
from datetime import datetime

RESULTS_DIR = ""


def create_directories():
    global RESULTS_DIR
    reports_dir = os.path.join("D:\\", "Reports")
    os.makedirs(reports_dir, exist_ok=True)

    timestamp = datetime.now().strftime('%d-%m-%Y--%H-%M-%S')
    RESULTS_DIR = os.path.join(reports_dir, f"Results--{timestamp}")
    os.makedirs(RESULTS_DIR, exist_ok=True)

    return RESULTS_DIR


RESULTS_DIR = create_directories()
