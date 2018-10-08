import subprocess
from CRABAPI.RawCommand import crabCommand

# define the ls command
ls = subprocess.Popen(["ls", "."],  
                      stdout=subprocess.PIPE,
                     )

# define the grep command
grep = subprocess.Popen(["grep", "IC"],  
                         stdin=ls.stdout,
			 stdout=subprocess.PIPE,
			)

# read from the end of the pipe (stdout)
endOfPipe = grep.stdout

# output the files line by line
for line in endOfPipe:  
    crabCommand('status', dir = line.rstrip('\n'))
