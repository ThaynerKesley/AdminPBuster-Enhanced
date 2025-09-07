# BHEH's AdminPBuster — Bug Bounty Enhanced Fork 🔎

<p align="center">
<a href="https://www.blackhatethicalhacking.com"><img src="https://www.blackhatethicalhacking.com/wp-content/uploads/2022/06/BHEH_logo.png" width="300px" alt="BHEH"></a>
</p>

<p align="center">
<strong>If you think you can hide your Admin Panel, think again... Find it with AdminPBuster.</strong>
</p>

---

**AdminPBuster** is written by **Chris "SaintDruG" Abou-Chabke** from **Black Hat Ethical Hacking** and is designed specifically for **Red Teams**, **Offensive Security Experts**, and **Bug Bounty Hunters** looking to discover hidden or obscured admin panels efficiently.

> This fork adds features tailored for **bug bounty workflows**: custom headers, global RPS limiting, and per-request timeouts—keeping the original spirit, but more flexible for real targets.

---

<p align="center">
<img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExdnFyZDBza3luMnl2c2gwNDcwMmp3YTY5YnA0dWI0ZjBocmR2Z3J0byZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/11shDO8NnZDYpa/giphy.gif" width="500px" alt="Matrix Animation">
</p>

---

## Description

**AdminPBuster** is a Red Teaming Recon tool to find hidden admin panels on web applications using brute-forcing.  
Instead of bundling a static wordlist and bloating the tool, it **fetches an updated admin panel wordlist** directly from our GitHub repository.

- This keeps the tool **lightweight** and **easy to maintain**.
- Whenever we update the hosted wordlist, **the tool automatically benefits**, without needing to update the script itself.

**Key technical goodies:**
- Multithreaded scanning using curl
- Proper HTTPS and `www.` handling to fix SSL issues
- Real redirect following (`-L` curl flag) bypasses WAFs and Cloudflare protections and logs only valid 200 responses
- No proxychains/Tor dependency (due to their unreliability for professional offensive operations)
- Optional randomized User-Agent headers (`-ua`) to simulate real traffic

AdminPBuster focuses on **speed**, **reliability**, and **accuracy** while staying very simple to operate going through 10,000+ wordlists.

---

## 🔧 Enhancements in This Fork (Bug Bounty Focus)

- **Custom Headers (`--header`)**  
  Add one or more HTTP headers to each request (repeat the flag). Helpful for:  
  - Testing authenticated endpoints (tokens, sessions)  
  - Adding bug bounty identifiers  
  - Trying custom bypass values  

  ```bash
  python3 AdminPBuster.py -t target.com \
    --header "Authorization: Bearer TOKEN123" \
    --header "X-Intigriti-Username: hunter@intigriti.me"
  ```

* **Global Requests-Per-Second Control (`--rps`)**
  Token-bucket style limiter to control scan pressure and respect program boundaries:

  ```bash
  python3 AdminPBuster.py -t target.com --rps 20
  ```

* **Per-Request Timeout (`--timeout`, default: 5s)**
  Avoid hanging on slow targets:

  ```bash
  python3 AdminPBuster.py -t target.com --timeout 8
  ```