import subprocess, sys

print('\n~ Scanwave ~ ping the void ~\n')

# scanning function
def ping_ip(ip):
        result = subprocess.run([f'ping -c 1 {ip}'], shell=True, capture_output=True, text=True)
        return result.returncode

# Ask user if they want to scan a single ip or a range
print('''Would you like to scan a single IP address or a range of IP addresses?: (s)ingle,
(r)ange''')
single_range = input()

if single_range == 's':
    target = input('Enter a host (default: localhost): ') or 'localhost'
# Use subprocess.run() to ping target once
    result = subprocess.run([f'ping -c 1 {target}'], shell=True, capture_output=True, text=True)
# Return code 0 means host is UP, otherwise host is DOWN
    rc = result.returncode
# Print a stylised message
    if ping_ip(target) == 0:
        print('\033[92mhost is UP\033[0m')
        print(result.stdout)
    else:
        print('\033[91mhost is DOWN\033[0m')
        print(result.stderr)
elif single_range == 'r':
    ip_range = input('Enter IP range (e.g. 192.168.1.1-192.168.1.10): ')
    
    start_ip, end_ip = ip_range.split('-')
    
    base_ip = '.'.join(start_ip.split('.')[:-1])
    
    start_octet = int(start_ip.split('.')[-1])
    end_octet = int(end_ip.split('.')[-1])
    
    for i in range(start_octet, end_octet + 1):
        ip = f'{base_ip}.{i}'
        print(f'Pinging {ip}...')
        if ping_ip(ip) == 0:
            print(f'{ip} is UP')
        else:
            print(f'{ip} is Down')
else:
    print('Not a valid choice')
    sys.exit()
    