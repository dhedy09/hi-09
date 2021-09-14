import subprocess
import os
def handler():
    print('killing process ...')
    cmd = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
    output, error = cmd.communicate()
    target_process = ("python","pinger","screen","redsocks","proxification")
    for line in output.splitlines():
        if any(s in line for s in target_process):
            pid = int(line.split()[0])
            os.system(f'kill {pid}')

handler()
