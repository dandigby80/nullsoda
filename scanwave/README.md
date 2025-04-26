# Scanwave

Scanwave is a lightweight network scanner built as part of the NullSoda suite.

## Description

A simple tool designed to scan networks, discover live hosts, and gradually evolve into a more powerful recon companion.  
Built for learning, experimentation, and fun.

## Features (current)

- Basic ping sweep scanning
- Friendly, readable output
- Lightweight and easy to modify

## Planned Features:

## Short-Term (v0.2, v0.3 stuff)

- **Scan a range of IP addresses**
    - e.g. 192.168.1.1 to 192.168.1.20 - list which ones are online
- **Scan a subnet automatically**
    - e.g. 192.168.1.0/24 - find all alive hosts in that network
- **Save results to a file**
    - e.g. scan_results.txt
- **Prettier output**
    - Table/grid-style results or ASCII art title at the start
- **Faster scan mode**
    - Don't wait full ping timeout if host is obviously dead

## Medium-Term (later upgrades)

- **Scan for open ports**
    - Like a mini *nmap* (only basic - scan ports 22, 80, 443 etc)
- **Host OS guessing**
    - Basic fingerprinting based on ping TTL values
- **Customisable scan settings**
    - Pick number of pings, timeout values, which ports etc
- **Multiple target input**
    - User pastes a list of IP's, and Scanwave cycles throught them

## Long-Term / Advanced 

- **Simple Web UI**
    - Open browser tab and watch live scanning results
- **Export as JSON**
    - Good for data nerds who want to parse results later
- **Add module/plugin system**
    - Other NullSoda tools can eventually plug into ScanWave for more powerful stuff



