import sys
import time
import subprocess

problem = sys.argv[1]

start_time = time.time()
subprocess.check_call('python problem-'+problem+'.py',shell=True)
print '\nRuntime:', time.time() - start_time, 's'
