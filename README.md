# Project I for Cyber Security Base 2022 MOOC

## About

This is my first project work for [Cyber Security Base 2022 MOOC](https://cybersecuritybase.mooc.fi/), organized by University of Helsinki.

The application, called Gamez, is intentionally vulnerable (and pretty useless) video game cataloging application.

Anyone with basic hacking skills can take over the application, its database and potentially cause mess in your computer system or network. This application is meant to be ran locally behind a firewall, and only for educational purposes.

The assignment was to write an application that has at least 5 vulnerabilities from OWASP Top 10 list (2021).

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

- Python 3 (3.10)
- Django 4 (4.0.4, 4.1)

The application has been developed/tested on macOS 12.5. There's no known reason why it wouldn't work on Windows or Linux.

### Installing

Step 1: Clone the repository and change to the created directory

Step 2: Install requirements

```bash
pip install django==4.1 --quiet --no-input
pip install pyyaml --quiet --no-input
```

Step 3: Prepare the database

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

Browse to `http://localhost:8000`, log in and start hacking. The vulnerabilities are described in a file called report.txt.

Have fun! :)
