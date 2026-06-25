#!/bin/bash
if test $# -eq 0; then
	echo -e "No arguments found\nUsage: ./<scrip-name> Accepted/Failed"
	exit 1
elif test $# -gt 1 ; then
	echo -e "Too many arguments found!\nTry: ./<script-name> Accepted/Failed"
	exit 1
fi
arg=$1
if test "$arg" != "Accepted" && test "$arg" != "Failed"; then
	echo -e "Invalid arguments!\n Use: Accepted/Failed"
	exit 1
fi
awk -v status="$arg" '$6 == status {print $0 }' auth.log
