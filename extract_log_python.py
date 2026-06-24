import sys
""" 
if No arguments or found notify the user
to input the necessary argument to the 
script.
"""
if len(sys.argv) == 1:
    print(f"No argument found!\nUsage: python3 <script-name.py> Accepted/Failed\n")
    sys.exit(1)
elif len(sys.argv) > 2:
    print(f"Too many argument found!\n");
    sys.exit(1);
elif len(sys.argv) == 2:
    print("Arguments founded!: ",sys.argv[1],end='\n')
    if sys.argv[1] not in ["Accepted","Failed"] :
        print(f"Invalid argument!: try <Accepted/Failed>\n")
        sys.exit(1)

arg = sys.argv[1]

"""
open the source log file in read mode
with also buffering limit of 10240 (10 MB)
instead of dumping all the logs into
memory use batch style processing.
"""
with open("auth.log",'r',buffering=4096) as log:
    try:
        for line in log:
            if arg in line:
                print(line)
    except FileNotFoundError:
        print("File not found!")
        sys.exit(1)

