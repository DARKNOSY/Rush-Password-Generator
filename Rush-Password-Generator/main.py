import os
import random
import string

import requests

def _header():
    header_text = f"Rush Password Generator by @DARKNOSY - Stars: {stars_count}, Forks: {forks_count}, Watchers: {watchers_count}"
    console_width = os.get_terminal_size().columns
    padding_width = (console_width - len(header_text)) // 2
    header_line = "=" * console_width
    print("\033[1m")  
    print("\033[95m" + header_line)
    print("\033[94m" + " " * padding_width + header_text + " " * padding_width)
    print("\033[95m" + header_line + "\033[0m")
    print("\033[0m") 

def _success(message):
    print("\033[92m" + message + "\033[0m")

def _error(message):
    print("\033[91m" + message + "\033[0m")

def _stats():
    global stars_count, forks_count, watchers_count

    username = "DARKNOSY"
    repo_name = "Rush-Password-Generator"
    url = f"https://api.github.com/repos/{username}/{repo_name}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        repo_data = response.json()
        stars_count = repo_data["stargazers_count"]
        forks_count = repo_data["forks_count"]
        watchers_count = repo_data["watchers_count"]

    else:
        _error("Failed to fetch repository details.")

print("\033]0;Rush Password Generator by DARKNOSY\007")

_stats()

_header()

def generate_password(length=16, exclude_similar=True, no_repeats=True):
    if length < 4:
        raise ValueError("Password length must be at least 4 for complexity.")

    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    symbols = "!@#$%^&*()-_=+[]{}|;:,.<>?/"

    if exclude_similar:
        similar_chars = "il1Lo0O"
        upper = ''.join([c for c in upper if c not in similar_chars])
        lower = ''.join([c for c in lower if c not in similar_chars])
        digits = ''.join([c for c in digits if c not in similar_chars])

    all_chars = upper + lower + digits + symbols

    password = [
        random.choice(upper),
        random.choice(lower),
        random.choice(digits),
        random.choice(symbols)
    ]

    while len(password) < length:
        char = random.choice(all_chars)
        if no_repeats and char in password:
            continue
        password.append(char)

    random.shuffle(password)
    return ''.join(password)

if __name__ == "__main__":
    try:
        lngt = int(input("\033[96mEnter the length of the password you want generated (number):\033[0m "))
        pwd = generate_password(length=lngt, exclude_similar=True, no_repeats=True)
        _success(f"\nGenerated password: {pwd}\n")
    except ValueError as e:
        _error(f"\nError: {e}\n")
    os.system("pause")
