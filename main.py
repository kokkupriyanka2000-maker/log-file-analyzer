
import sys
from analyzer import analyze_log

analyze_log("app.log", "ERROR")


if len(sys.argv) < 2:
    print("Usage: python3 main.py <log_file> [LEVEL]")
    sys.exit(1)

log_file = sys.argv[1]

level = None
if len(sys.argv) == 3:
    level = sys.argv[2].upper()

analyze_log(log_file, level)
