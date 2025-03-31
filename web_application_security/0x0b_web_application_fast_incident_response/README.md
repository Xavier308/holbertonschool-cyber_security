# Web Application Fast Incident Response

## Description

This project focuses on analyzing web server logs to detect and respond quickly to potential web application attacks. The objective is to develop scripts that help identify attack patterns, analyze attacker behavior, and propose actionable mitigation strategies. This incident response simulation centers around a suspected Denial of Service (DoS) attack, with a series of tasks that explore log parsing, attacker identification, and threat mitigation.

---

## Tasks Overview

### `0-attack_ip.sh`
Identifies the IP address responsible for the most requests in the log file.
🔍 **Purpose**: Detect the potential attacker source.

### `1-endpoint.sh`
Finds the most requested endpoint (URL), indicating the target of the attack.
🎯 **Purpose**: Determine which resource was targeted.

### `2-count_attack.sh`
Counts the number of requests made by the attacker IP.
📊 **Purpose**: Measure the scale of the attack.

### `3-library.sh`
Extracts the User-Agent used by the attacker to identify the tool or library used.
🛠 **Purpose**: Understand attacker tooling (e.g., python-requests/2.31.0).

### `4-incident_report.md` (Google Doc)
A structured and concise incident report summarizing the findings, attack analysis, and mitigation recommendations.
📝 **Purpose**: Help organizations understand and act on the incident.

---

## Usage

Each script accepts an optional input file (`logs.txt` by default) and prints a result directly to the console.

```bash
./0-attack_ip.sh
./1-endpoint.sh
./2-count_attack.sh
./3-library.sh
```

## Requirements

- Scripts must use only Bash (no &&, ||, or backticks).
- All scripts are limited to 2 lines maximum.
- Must be executable: `chmod +x <script_name>`
- Compatible with Kali Linux.
- Editors allowed: vi, vim, emacs.
- Use $1 without quotes to avoid argument type issues.
- Each file must end with a newline.
- A detailed Google Docs report is required for Task 4.

## Learning Objectives

By completing this project, you will be able to:
- Describe the stages of web application incident response.
- Detect and analyze web-based attacks using logs.
- Use log management and EDR tools effectively.
- Propose mitigation strategies aligned with cybersecurity standards.
- Communicate and document incidents professionally.
