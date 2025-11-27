import time
import subprocess
import sys

if len(sys.argv) < 2:
    print("Usage: python timer.py <command>")
    exit(1)

start = time.time()
subprocess.call(sys.argv[1:], shell=False)
end = time.time()

print(f"Execution time: {end - start:.4f} seconds")
