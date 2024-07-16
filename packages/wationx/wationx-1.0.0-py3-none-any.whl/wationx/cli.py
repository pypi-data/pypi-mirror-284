#!/usr/bin/env python3
import requests

def notify_server():
    requests.get(
        "https://wation.net/api/ext/v1/fwationx", 
        headers={
            "User-Agent": "WPMF/1.0.0"
        }
    )

def main():
    notify_server()
    print("WATION WARNING: Are you attempting to perform a malicious action? This time, we forgive your attempt, but be aware that any future actions could result in the suspension of your account.")

if __name__ == '__main__':
    main()