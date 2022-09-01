# Project I for Cyber Security Base 2022 MOOC

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Contributing](../CONTRIBUTING.md)

## About

This is my first project work for [Cyber Security Base 2022 MOOC](https://cybersecuritybase.mooc.fi/), organized by University of Helsinki.

The application, called Gamez, is intentionally vulnerable (and pretty useless) video game cataloging application.

Anyone with basic hacking skills can take over the application, its database and potentially cause mess in your computer system or network. This application is meant to be ran locally behind a firewall, and only for educational purposes.

The assignment was to write an application that has at least 5 vulnerabilities from OWASP Top 10 list (2021). The ones that I chose to implement (or not to mitigate) are:

- [A01 Broken Access Control](https://owasp.org/Top10/A01_2021-Broken_Access_Control/)
  - Permitting viewing or editing someone else's account, by providing its unique identifier (insecure direct object references)
- [A03 Injection](https://owasp.org/Top10/A03_2021-Injection/)
  - User-supplied data is not validated, filtered, or sanitized by the application
- [A05 Security Misconfiguration](https://owasp.org/Top10/A05_2021-Security_Misconfiguration/)
  - Error handling reveals stack traces or other overly informative error messages to users
  - Unnecessary features are enabled or installed (e.g., unnecessary ports, services, pages, accounts, or privileges)
- [A07 Identification and Authentication Failures](https://owasp.org/Top10/A07_2021-Identification_and_Authentication_Failures/)
  - Permits automated attacks such as credential stuffing, where the attacker has a list of valid usernames and passwords
  - Permits brute force or other automated attacks.
  - Permits default, weak, or well-known passwords, such as "Password1" or "admin/admin"
  - Uses weak or ineffective credential recovery and forgot-password processes, such as "knowledge-based answers," which cannot be made safe
- [A09 Security Logging and Monitoring Failures](https://owasp.org/Top10/A09_2021-Security_Logging_and_Monitoring_Failures/)
  - Auditable events, such as logins, failed logins, and high-value transactions, are not logged
  - Warnings and errors generate no, inadequate, or unclear log messages
- [A10 Server Side Request Forgery](https://owasp.org/Top10/A10_2021-Server-Side_Request_Forgery_%28SSRF%29/)
  - non-sanitized inputs used when fetching external data
  - Application fetches a remote resource without validating the user-supplied URL

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites

- Python 3 (3.10)
- Django 4 (4.0.4, 4.1)

The application has been developed/tested on macOS 12.5. There's no known reason why it wouldn't work on Windows or Linux.

### Installing

Step 1: Clone the repository and change to the created directory

Step 2: Prepare the database

```bash
python3 manage.py makemigrations
python3 manage.py makemigrations gamez
python3 manage.py migrate
python3 manage.py initdata
```

The last line is optional. It creates automatically three test users that each have a game collection of three games:

- tupu/password (user/collection id: 1, game ids: 1-3)
- hupu/password (user/collection id: 2, game ids: 4-6)
- lupu/password (user/collection id: 3, game ids: 7-9)

_To reset the database at any time, delete the db.sqlite3 file and run commands above again._

## Running

```bash
python3 manage.py runserver
```

Browse to `http ://localhost:8000`, log in and start hacking. The vulnerabilities are described in a file called report.txt.

Have fun! :)
