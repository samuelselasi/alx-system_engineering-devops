#!/usr/bin/python3
"""Recursive function that counts the number of hot articles for a subreddit"""
import requests
after = None


def recurse(subreddit, hot_list=[]):
    """Recursive function that returns a list of hot posts"""
    global after

    if subreddit is None or not isinstance(subreddit, str):
        return None

    headers = {'User-Agent': 'selBot/2.1'}
    URL = f'https://www.reddit.com/r/{subreddit}/hot.json'

    if after:
        URL += f'?after={after}'
    try:
        response = requests.get(URL, headers=headers, allow_redirects=False)
        response.raise_for_status()
        data = response.json()
        posts = data['data']['children']

        if not posts:
            return hot_list

        for post in posts:
            title = post['data']['title']
            hot_list.append(title)

        after = data['data']['after']
        if after:
            return recurse(subreddit, hot_list=hot_list)
        else:
            return hot_list

    except requests.exceptions.RequestException:
        return None

    except (KeyError, ValueError):
        return None
