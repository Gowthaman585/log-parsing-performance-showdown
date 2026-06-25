"""
Python script to benchmark different scripts
execution speeds.
"""
import sys
import time
import subprocess
"""
Handling arguments usages
"""
if len(sys.argv)!= 2 or sys.argv[1] not in ["Accepted","Failed"]:
    print("Usage: python3 bench-mark.py <Accepted/Failed>")
    sys.exit(1)
arg = sys.argv[1]
"""
Bind all the script executing commands 
into scripts dictinary.
"""
scripts = {
        "awk": ["./extract_log_awk.sh", arg],
        "grep": ["./extract_log_grep.sh",arg],
        "python": ["python3" ,"extract_log_python.py",arg]
        }
bench_marks = {}
print("="*30)
print(" LOG PARSING PERFORMANCE BREAKDOWN ")
print("="*30)
for tool, cmd in scripts.items():
    print(f"Running {tool} Engine...", end="",flush=True)
    start_time = time.perf_counter()
    """
    using subprocess execute the scritps one by one , considering only
    the speed and execution the stdout to terminal is un-necessary so
    redirect them to /dev/null.
    """
    subprocess.run(cmd, stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    end_time = time.perf_counter()
    duration = end_time-start_time
    bench_marks[tool] = duration
    print(f"\n{tool} script: {duration:.5f} sec")
print("="*30)
