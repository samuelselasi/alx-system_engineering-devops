#!/usr/bin/python3
"""Script that returns no. of subscribers of a subreddit"""
import requests


def number_of_subscribers(subreddit):
    """Function that returns no. of subs of a subreddit"""
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    headers = {'User-Agent': 'selBot/1.0'}
    URL = f'https://www.reddit.com/r/{subreddit}/about.json'

    try:
        response = requests.get(URL, headers=headers, allow_redirects=False)
        response.raise_for_status()
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers

    except requests.exceptions.RequestException:
        return 0

    except (KeyError, ValueError):
        return 0
