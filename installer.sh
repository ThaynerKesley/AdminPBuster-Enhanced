#!/bin/bash

echo "Installing Admin Panel Fetcher dependencies..." | lolcat

apt update
apt install -y toilet lolcat curl | lolcat

echo "Installing Python packages..." | lolcat
pip3 install requests termcolor urllib3 --break-system-packages

echo "Making admin_panel_fetcher.py executable..." | lolcat
chmod +x admin_panel_fetcher.py

echo -e "\nInstallation complete!" | lolcat
echo "Run tool: ./admin_panel_fetcher.py -t example.com -th 10" | lolcat
echo "Run with random agent: ./admin_panel_fetcher.py -t example.com -th 10 -ua" | lolcat
