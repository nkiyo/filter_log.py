import sys
import glob
import re
from datetime import datetime

if len(sys.argv) != 3:
    print(f"Usage: Python3 {sys.argv[0]} <start_time> <end_time>")
    sys.exit(1)
s = datetime.strptime(sys.argv[1], "%Y-%m-%d %H:%M:%S")
e = datetime.strptime(sys.argv[2], "%Y-%m-%d %H:%M:%S")

files = glob.glob("log/log.*")
# print(files)

for file in files:
    with open(file, 'r') as f:
        for line in f:
            pattern = r"^\[(.*)\].*$"
            match = re.search(pattern, line)

            if match:
                time = datetime.strptime(match.group(1), "%Y-%m-%d %H:%M:%S.%f")
                if s < time < e:
                    print(time)
            
