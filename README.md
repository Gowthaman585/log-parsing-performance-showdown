# 🪵 Log Parsing Performance Showdown

A hands-on benchmark that races three different tools — `grep`, `awk`, and `Python` — against each other to parse a real `auth.log` file and find login events.

The goal is simple: **which tool is fastest, and why?**

---

## 📁 Project Structure

```
log-parsing-performance-showdown/
│
├── auth.log                  # 100,000 line SSH auth log (the test data)
├── bench_mark.py             # Benchmark runner — races all 3 tools 10 times each
├── extract_log_grep.sh       # Parser using grep
├── extract_log_awk.sh        # Parser using awk
└── extract_log_python.py     # Parser using Python
```

---

## 💡 What This Project Does

Every server produces `auth.log` — a file that records every SSH login attempt: who connected, from which IP, and whether it was `Accepted` or `Failed`.

This project filters those events using 3 different tools and measures how fast each one completes the job across 10 repeated runs.

---

## 🚀 How To Run

Make sure the shell scripts have execute permission first:

```bash
chmod +x extract_log_grep.sh extract_log_awk.sh
```

Then run the benchmark:

```bash
python3 bench_mark.py Accepted
# or
python3 bench_mark.py Failed
```

The benchmark runs each tool 10 times, then prints a results table with **avg, min, and max** time for each.

---

## 📊 Benchmark Results

> Tested on: 100,000 line auth.log (~9.9 MB)  
> Runs per tool: 10  
> Filter: `Failed`

```
==============================
 LOG PARSING PERFORMANCE BREAKDOWN
==============================

 BENCHMARK RESULTS
==============================
Tool      Avg       Min       Max
------------------------------
awk    : 0.07669 0.07482 0.08089
grep   : 0.00526 0.00500 0.00561
python : 0.09079 0.08908 0.09161
==============================
````

---

## 🧠 Why Does Each Tool Perform Differently?

This is the most important part. The speed difference is not random — each tool works in a fundamentally different way.

### 🥇 grep — The Pure Speed Demon

`grep` is the fastest for simple text matching. It is written in optimized C and uses an algorithm called **Boyer-Moore pattern matching** — instead of reading every single character, it skips chunks of text intelligently to find the match faster.

Most importantly, `grep` doesn't care about structure. It treats the log file as a raw stream of bytes and just looks for the word `"Failed"` or `"Accepted"` anywhere in the line. No extra thinking, no extra work.

**Think of it like:** scanning a book by only looking at the last few letters of each word to decide if it could possibly match, skipping everything else.

### 🥈 awk — The Smart Speed Demon

`awk` is also written in C and runs at hardware speed — but it does more work per line than `grep`.

Every time `awk` reads a line, it **tokenizes** it — meaning it splits the line into columns (`$1`, `$2`, `$3`... `$6`) so you can target specific fields. In this project, the awk script checks `$6 == "Accepted"` — only column 6. This is more precise than grep (which matches the word anywhere in the line), but that column-splitting step adds a small overhead on every single line.

**Think of it like:** not just scanning the book, but actively cutting each sentence into individual words before checking — more powerful, slightly slower.

**Where awk wins over grep:** if your log had the word "Failed" in a username or IP address, grep would accidentally match it. awk targets only column 6, so it's more accurate. For complex real-world tasks, awk is the smarter choice.

### 🥉 Python — The Flexible Interpreter

Python is the slowest of the three here, but for a good reason: it is an **interpreted language**, not a compiled C program. Every line of Python code is translated at runtime, which adds overhead that grep and awk don't have.

That said, this project uses **buffered file reading** (`buffering=4096`) instead of loading the entire 9.9 MB file into memory at once — which is a good practice and keeps memory usage low.

Python's real strength is not raw speed but **flexibility**. If you needed to parse logs, calculate statistics, write results to a database, and send an alert email — Python handles all of that in one script. grep and awk can't.

---

## 🏁 Summary

| Tool   | Speed | Why |
|--------|-------|-----|
| `grep`   | 🥇 Fastest | Raw byte scanning, no structure parsing, optimized C |
| `awk`    | 🥈 Fast    | Column-aware parsing, slightly more work per line |
| `python` | 🥉 Slower  | Interpreted language, but most flexible and scalable |

---

## 📌 Key Takeaway

> Use `grep` when you just need to find lines fast.  
> Use `awk` when you need to match specific columns or fields.  
> Use `Python` when the task is too complex for a one-liner.

The right tool depends on the job — not just the speed.

---

## 🛠️ Requirements

- Python 3.x
- Bash (Linux / macOS)
- `grep` and `awk` (pre-installed on all Unix systems)
