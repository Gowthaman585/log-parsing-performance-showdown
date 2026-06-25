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

test_runs = 10

for tool, cmd in scripts.items():
    times_cycles = []
    print(f"Running {tool} Engine...",flush=True)
    print("-"*30)
    for i in range(1,test_runs+1):
        start_time = time.perf_counter()
        """
        using subprocess execute the scritps one by one , considering only
        the speed and execution the stdout to terminal is un-necessary so
        redirect them to /dev/null.
        """
        subprocess.run(cmd, stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
        end_time = time.perf_counter()
        duration = end_time-start_time
        """
        storing each test duration into test_cycles
        """
        times_cycles.append(duration)
        print(f" cycle {i:2d}: {duration:.5f}sec")
    print("="*30)
    """
    calculate average, minium, maximum time taken for 
    each scripts clocked ten times frequently to 
    extract the tested bench marks and store into 
    the bench_marks[]
    """
    avg = sum(times_cycles)/ len(times_cycles)
    bench_marks[tool] = {
            "avg": avg,
            "min": min(times_cycles),
            "max": max(times_cycles)
            }
"""
displaying then bench marks result 
in a tabular formar
"""

print(" BENCHMARK RESULTS ")
print("="*30)
print(f"{'Tool':<7} {'Avg':>7} {'Min':>7} {'Max':>7}")
print("-"*30)
for tool, stats in bench_marks.items():
    print(f"{tool:<7}: {stats['avg']:>7.5f} {stats['min']:>7.5f} {stats['max']:>7.5f}")
print("="*30)
