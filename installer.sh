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
echo "Run with custom request per second: ./AdminPBuster.py -t example.com -th 10 -ua --rps 5" | lolcat
echo "Run with custom header: ./AdminPBuster.py -t example.com -th 10 -ua --rps 5 --header "X-Intigriti-Username: researcher@intigriti.me" \
  --header "Referer: https://exampletarget.com/search?q=test"" | lolcat
