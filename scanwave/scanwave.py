import subprocess, sys

print('\n~ ScanWave ~ ping the void ~\n')
print('''Hey digital drifter - Only scan networks you own or have permissions to test.
We\'re here to vibe, not mess with others\' spaces. Let's keep it chill.''')

# Scanning function
def ping_ip(ip):
    result = subprocess.run([f'ping -c 1 {ip}'], shell=True, capture_output=True, text=True)
    return result.returncode

# Save data to file function
def drop_to_disk(data, fileName):
    subprocess.run([f'touch', fileName], capture_output=True, text=True)
    with open(fileName, 'w') as f:
        f.write(data)

# Function to ask user for ISP range and validate input
def get_isp_range():
    while True:
        ip_range = input('Enter IP range (e.g. 192.168.1.1-192.168.1.10): ')
        if '-' in ip_range and ip_range.count('.') == 6:
            try:
                start_ip, end_ip = ip_range.split('-')
                start_ip_parts = start_ip.split('.')
                end_ip_parts = end_ip.split('.')
                
                if len(start_ip_parts) == 4 and len(end_ip_parts) == 4:
                    return start_ip, end_ip
                else:
                    print('Invalid IP format. Please try again.')
            except ValueError:
                print('Invalid IP range format. Please try again.')
        else:
            print('''\nInvalid range. Ensure you use the correct format like \'192.168.1.1-192.168.1.10\'.
Please try again.''')

# Ask user if the want to scan a single IP or a range
print('''\nWould you like to scan a single IP address or a range of IP addresses?: (s)ingle,
(r)ange''')
single_range = input()

if single_range == 's':
    target = input('Enter a host (default: localhost): ') or 'localhost'
    # Use subprocess.run() to ping target once
    result = subprocess.run([f'ping -c 1 {target}'], shell=True, capture_output=True, text=True)
    # Return code 0 means host is up, otherwise host is down
    if ping_ip(target) == 0:
        print('\033[92mhost is UP\033[0m')
        print(result.stdout)
        # Option to save to disk
        print('Would you like to save the result to disk? (y)es or (n)o.')
        while True:
            save = input()
            if save == 'y':
                print('Please enter a file name: ')
                filename = input() or f'scanwave-{target}'
                drop_to_disk(result.stdout, filename)
                print(f'File saved to disk: {filename}.')
                sys.exit()
            elif save == 'n':
                print('Goodbye.')
                sys.exit()
            else:
                print('Not a valid choice - choose (y) or (n)')
    else:
        print('\033[91mhost id DOWN\033[0m')
        print(result.stderr)
elif single_range == 'r':
    # Get valid ISP range from the user
    start_isp, end_isp = get_isp_range()
    
    base_ip = '.'.join(start_isp.split('.')[:-1])
    start_octet = int(start_isp.split('.')[-1])
    end_octet = int(end_isp.split('.')[-1])
    range_dict = {}
    
    for i in range(start_octet, end_octet +1):
        ip = f'{base_ip}.{i}'
        print(f'Pinging {ip}...')
        if ping_ip(ip) == 0:
            print(f'{ip} is UP')
            range_dict[ip] = 'UP'
        else:
            print(f'{ip} is DOWN')
            range_dict[ip] = 'DOWN'
    print('\nWould you like to save the result to disk? (y)es or (n)o.')
    while True:
        save = input()
        if save == 'y':
            print('Please enter a file name: ')
            filename = input() or f'scanwave-{start_isp}-{end_isp}.txt'
            drop_to_disk(str(range_dict), filename)
            print(f'File saved to disk: {filename}.')
            sys.exit()
        elif save == 'n':
            print('Goodbye.')
            sys.exit()
        else:
            print('Not a valid choice - choose (y) or (n)')
        
else:
    print('Not a valid choice')
    sys.exit()