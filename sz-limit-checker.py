import sys
import os

for path in sys.argv[1:]:
    for root, _, files in os.walk(path):
        for name in files:
            p = os.path.join(root, name)
            if os.stat(p).st_size > 99*1024**2:
                print(p)
