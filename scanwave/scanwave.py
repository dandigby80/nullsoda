# scanwave.py
# Scanwave v0.1
# A simple live-host scanner for the NullSoda suite

import subprocess, sys

print('\n~ scanwave ~ a NullSoda tool ~\n')

# Ask for a target IP/hostname
# If none entered, default to localhost
target = input('Enter a host (default: localhost): ') or 'localhost'

# Use subprocess.run() to ping target once
result = subprocess.run([f'ping -c 1 {target}'], shell=True, capture_output=True, text=True)
# Return code 0 means host is UP, otherwise host is DOWN
rc = result.returncode
# Print a stylised message
if rc == 0:
    print('\033[92mhost is UP\033[0m')
    print(result.stdout)
else:
    print('\033[91mhost is DOWN\033[0m')
    print(result.stderr)