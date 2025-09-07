#!/usr/bin/env python3

import requests
import subprocess
import signal
import sys
import os
import queue
import argparse
import time
import random
<<<<<<< HEAD
=======
import collections
>>>>>>> 23b63c6 (feat: add enhanced version files)
from threading import Thread, Lock
from urllib.parse import urlparse
import urllib3
from pathlib import Path
from termcolor import colored

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

VERSION = "3.0"
AUTHOR = "Chris 'SaintDruG' Abou-Chabke"
TEAM = "Black Hat Ethical Hacking"
PATHS_URL = "https://raw.githubusercontent.com/blackhatethicalhacking/AdminPBuster/refs/heads/main/magic_admin_paths.txt"

request_counter = 0
counter_lock = Lock()

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; rv:125.0) Gecko/20100101 Firefox/125.0",
    "Mozilla/5.0 (X11; Linux x86_64; rv:125.0) Gecko/20100101 Firefox/125.0"
]

def handle_interrupt(signal, frame):
    print(colored("\n[!] Interrupted by user. Exiting...", "red", attrs=["bold"]))
    sys.exit(0)

signal.signal(signal.SIGINT, handle_interrupt)

def rainbow_text(text):
    colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']
    return ''.join(colored(char, colors[i % len(colors)], attrs=["bold"]) if char != " " else " " for i, char in enumerate(text))

def print_ascii_and_quote():
    subprocess.run("curl --silent https://raw.githubusercontent.com/blackhatethicalhacking/Subdomain_Bruteforce_bheh/main/ascii.sh | lolcat", shell=True)
    print("")
    quotes = [
        "The supreme art of war is to subdue the enemy without fighting.",
        "All warfare is based on deception.",
        "He who knows when he can fight and when he cannot, will be victorious.",
        "The whole secret lies in confusing the enemy, so that he cannot fathom our real intent.",
        "To win one hundred victories in one hundred battles is not the acme of skill. To subdue the enemy without fighting is the acme of skill."
    ]
    random_quote = random.choice(quotes)
    subprocess.run(f'echo "Offensive Security Tip: {random_quote} - Sun Tzu" | lolcat', shell=True)
    time.sleep(1)
    subprocess.run('echo "MEANS, IT\'S ☕ 1337 ⚡ TIME, 369 ☯" | lolcat', shell=True)
    time.sleep(1)
    print("\n" + rainbow_text("Press any key to enter the Matrix"))
    input()

def print_toilet_banner_lolcat():
    subprocess.run("clear", shell=True)
    os.system("toilet -f smblock 'AdminPBuster' | lolcat")

def print_help_colored():
    print_ascii_and_quote()
    print_toilet_banner_lolcat()
    print(colored(f"\nVersion: {VERSION}", "yellow"))
    print(colored(f"Author: {AUTHOR}", "yellow"))
    print(colored(f"Team: {TEAM}\n", "yellow"))

    print(colored("Usage: ", "cyan", attrs=["bold"]) + colored("./AdminPBuster.py -t example.com", "white"))
    print(colored("(Give domain only without brackets or https)\n", "yellow"))

    print(colored("Options:", "cyan", attrs=["bold"]))
<<<<<<< HEAD
    print(colored("  -h, --help             ", "white") + "Show this help message and exit")
    print(colored("  -t, --target TARGET    ", "white") + "Target domain (e.g., example.com)")
    print(colored("  -th, --threads THREADS ", "white") + "Number of threads (default: 5)")
    print(colored("  -ua, --random-agent    ", "white") + "Use random realistic User-Agent\n")
=======
    print(colored("  -h, --help                     ", "white") + "Show this help message and exit")
    print(colored("  -t, --target TARGET            ", "white") + "Target domain (e.g., example.com)")
    print(colored("  -th, --threads THREADS         ", "white") + "Number of threads (default: 5)")
    print(colored("  -ua, --random-agent            ", "white") + "Use random realistic User-Agent",)
    print(colored("  --rps REQUESTS_PER_SECOND      ", "white") + "Global rate limit (requests per second)")
    print(colored("  --header 'K: V'                ", "white") + "Custom header (repeatable)")
    print(colored("  --timeout SECONDS              ", "white") + "Per-request timeout (default: 5)\n")
>>>>>>> 23b63c6 (feat: add enhanced version files)

    print(colored("Written by ", "green") + colored("Chris 'SaintDruG' Abou-Chabke", "magenta") + colored(" for Black Hat Ethical Hacking", "green"))
    print(colored("© All Rights Reserved 2025 — Use For Ethical Testing Only.", "yellow"))
    print(colored("BHEH is not responsible for misuse of this tool.", "red"))

def print_rainbow_banner():
    os.system("clear")
    print("\n" + rainbow_text("Admin Panel Buster"))
    print(colored(f"\nVersion: {VERSION}", "yellow"))
    print(colored(f"Author: {AUTHOR}", "yellow"))
    print(colored(f"Team: {TEAM}", "yellow"))

def countdown():
    print(colored("\nStarting the attack in:", "cyan", attrs=["bold"]))
    for i in range(5, 0, -1):
        print(colored(str(i), "cyan", attrs=["bold"]))
        time.sleep(1)
    print(colored("\n[+] Attack Started!\n", "green", attrs=["bold"]))

def fetch_admin_paths():
    try:
        response = requests.get(PATHS_URL, timeout=10)
        response.raise_for_status()
        return [line.strip() for line in response.text.splitlines() if line.strip()]
    except Exception as e:
        print(colored(f"[!] Failed to fetch admin paths: {e}", "red", attrs=["bold"]))
        sys.exit(1)

def check_internet_connection():
    try:
        requests.get("https://www.google.com", timeout=5)
    except:
        print(colored("[!] No internet connection!", "red", attrs=["bold"]))
        sys.exit(1)

def clean_domain(domain_url):
    parsed = urlparse(domain_url)
    domain = parsed.netloc or parsed.path
    return domain.replace(":", "_")

def color_for_status(code):
    if code == "200":
        return "green"
    elif code in ["301", "302"]:
        return "cyan"
    elif code == "403":
        return "yellow"
    elif code == "404":
        return "red"
    else:
        return "magenta"

<<<<<<< HEAD
def scan_url(target_domain, path_queue, results, timeout=5, random_ua=False):
    global request_counter
=======
# -------- NEW: Simple global rate limiter (token bucket via deque) --------
class RateLimiter:
    def __init__(self, rps: int | None):
        self.rps = rps if (isinstance(rps, int) and rps > 0) else None
        self.lock = Lock()
        self.timestamps = collections.deque()  # of monotonic timestamps

    def acquire(self):
        if not self.rps:
            return
        while True:
            with self.lock:
                now = time.monotonic()
                # remove tokens older than 1s
                while self.timestamps and (now - self.timestamps[0] >= 1.0):
                    self.timestamps.popleft()
                if len(self.timestamps) < self.rps:
                    self.timestamps.append(now)
                    return
                # need to wait until the oldest token leaves the 1s window
                sleep_for = 1.0 - (now - self.timestamps[0])
            if sleep_for > 0:
                time.sleep(sleep_for)
            else:
                # edge-case: loop again
                time.sleep(0)

def scan_url(target_domain, path_queue, results, timeout=5, random_ua=False, rate_limiter: RateLimiter | None = None, custom_headers: list[str] | None = None):
    global request_counter
    custom_headers = custom_headers or []

>>>>>>> 23b63c6 (feat: add enhanced version files)
    while not path_queue.empty():
        path = path_queue.get()

        if not target_domain.startswith("www."):
            fixed_domain = "www." + target_domain
        else:
            fixed_domain = target_domain

        full_url = f"https://{fixed_domain.rstrip('/')}/{path.lstrip('/')}"

<<<<<<< HEAD
=======
        # rate limit (global)
        if rate_limiter:
            rate_limiter.acquire()

>>>>>>> 23b63c6 (feat: add enhanced version files)
        with counter_lock:
            request_counter += 1
            number = request_counter

<<<<<<< HEAD
        if random_ua:
            user_agent = random.choice(USER_AGENTS)
            curl_cmd = ["curl", "-A", user_agent, "-s", "-o", "/dev/null", "-w", "%{http_code}", "--max-time", str(timeout), "-L", full_url]
        else:
            curl_cmd = ["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}", "--max-time", str(timeout), "-L", full_url]
=======
        # build curl command
        curl_cmd = ["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}", "--max-time", str(timeout), "-L"]

        if random_ua:
            user_agent = random.choice(USER_AGENTS)
            curl_cmd += ["-A", user_agent]

        for h in custom_headers:
            curl_cmd += ["-H", h]

        curl_cmd.append(full_url)
>>>>>>> 23b63c6 (feat: add enhanced version files)

        try:
            result = subprocess.check_output(curl_cmd)
            http_code = result.decode().strip()

            if http_code == "000":
                http_code = "Connection Failed"

            color = color_for_status(http_code)

            print(colored(f"[{number}] {full_url} -> (HTTP {http_code})", color, attrs=["bold"]))

            if http_code == "200":
                results.append(full_url)

        except subprocess.CalledProcessError:
            print(colored(f"[{number}] {full_url} -> (Connection Failed)", "red", attrs=["bold"]))

<<<<<<< HEAD
        path_queue.task_done()

def admin_panel_buster(target_domain, threads, random_ua):
=======
        finally:
            path_queue.task_done()

def admin_panel_buster(target_domain, threads, random_ua, rps, timeout, custom_headers):
>>>>>>> 23b63c6 (feat: add enhanced version files)
    paths = fetch_admin_paths()
    q = queue.Queue()
    for path in paths:
        q.put(path)

    results = []
    thread_list = []

    domain_folder = f"results/{clean_domain(target_domain)}"
    os.makedirs(domain_folder, exist_ok=True)
    output_file = os.path.join(domain_folder, "found_panels.txt")

<<<<<<< HEAD
    for _ in range(threads):
        t = Thread(target=scan_url, args=(target_domain, q, results, 5, random_ua))
=======
    limiter = RateLimiter(rps)

    for _ in range(threads):
        t = Thread(
            target=scan_url,
            args=(target_domain, q, results, timeout, random_ua, limiter, custom_headers),
            daemon=True,
        )
>>>>>>> 23b63c6 (feat: add enhanced version files)
        thread_list.append(t)
        t.start()

    for t in thread_list:
        t.join()

    if results:
        print(colored(f"\n[✓] Found {len(results)} possible admin panels!", "green", attrs=["bold"]))
        for url in results:
            print(colored(f" - {url}", "green"))
        with open(output_file, "w") as f:
            for url in results:
                f.write(url + "\n")
        print(colored(f"\n[+] Results saved to {output_file}", "cyan", attrs=["bold"]))
    else:
        print(colored("\n[!] No admin panels found.", "yellow"))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("-t", "--target", help="Target domain (e.g., example.com)")
    parser.add_argument("-th", "--threads", type=int, default=5, help="Number of threads (default: 5)")
    parser.add_argument("-ua", "--random-agent", action="store_true", help="Use random realistic User-Agent")
<<<<<<< HEAD
=======
    parser.add_argument("--rps", type=int, help="Global requests per second limit (e.g., 5)")
    parser.add_argument("--header", action="append", help="Custom header (repeatable), e.g., --header 'X-Api-Key: 123' --header 'X-Foo: bar'")
    parser.add_argument("--timeout", type=int, default=5, help="Per-request timeout in seconds (default: 5)")
>>>>>>> 23b63c6 (feat: add enhanced version files)
    parser.add_argument("-h", "--help", action="store_true", help="Show help message and exit")
    ARGS = parser.parse_args()

    if ARGS.help or not ARGS.target:
        print_help_colored()
        sys.exit(0)

    print_rainbow_banner()
    check_internet_connection()
    countdown()
<<<<<<< HEAD
    admin_panel_buster(ARGS.target, ARGS.threads, ARGS.random_agent)
=======
    admin_panel_buster(
        ARGS.target,
        ARGS.threads,
        ARGS.random_agent,
        ARGS.rps,
        ARGS.timeout,
        ARGS.header or [],
    )
>>>>>>> 23b63c6 (feat: add enhanced version files)
