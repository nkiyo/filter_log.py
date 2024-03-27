# 引数で指定した開始～終了時刻のログだけ出力する
import sys
import glob
import re
from datetime import datetime

if len(sys.argv) != 3:
    print(f"Usage: Python3 {sys.argv[0]} <start_time> <end_time>")
    sys.exit(1)
s = datetime.strptime(sys.argv[1], "%Y-%m-%d %H:%M:%S")
e = datetime.strptime(sys.argv[2], "%Y-%m-%d %H:%M:%S")

logfiles = glob.glob("log/log.*")

for file in logfiles:
    with open(file, 'r') as f:
        for line in f:
            log_pattern = r"^\[(.*)\].*$"
            match = re.search(log_pattern, line)

            if match:
                time = datetime.strptime(match.group(1), "%Y-%m-%d %H:%M:%S.%f")
                if s < time < e:
                    print(f"{file}: {time}")
