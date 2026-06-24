#!/bin/bash
# Direct kernel pipelined script
# ==============================
# Almost all the process are handover to kernel.
# ==============================
# The latency completely depends upon the 
# hardware processing speed.
# ==============================

# if no arguments passed to the script
# alert and acknowledge the user 
# How to use the script!
if test $# -eq 0; then
	echo -e "No arguments provided\nUSAGE: ./<script-name> Accepted/Failed"
	exit 1;
# if more then 1 arguments passed
# stop the program and alert the user.
elif test $# -gt 1; then
	echo -e "Too many arguments\nFAILED!"
fi

# store the first argument in 
# a variable 'arg'
arg="$1"
# depends upon the argument stream the 
# output to the terminal.
if test "$arg" = "Failed" || test "$arg" = "Accepted"; then
	grep "$arg" auth.log
# is there any typo in the argument or
# unsupported acknowledge the user
else 
	echo "Invalid arguments!"
fi
