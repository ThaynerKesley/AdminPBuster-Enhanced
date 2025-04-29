#!/bin/bash

echo "Installing AdminPBuster dependencies..." | lolcat

apt update
apt install -y toilet lolcat curl | lolcat

echo "Installing Python packages..." | lolcat
pip3 install requests termcolor urllib3 --break-system-packages

echo "Making AdminPBuster.py executable..." | lolcat
chmod +x AdminPBuster.py

echo -e "\nInstallation complete!" | lolcat
echo "Run tool: ./AdminPBuster -t example.com -th 10" | lolcat
echo "Run with random agent: ./AdminPBuster.py -t example.com -th 10 -ua" | lolcat
