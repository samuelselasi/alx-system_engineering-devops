#!/usr/bin/python3
"""
Script that parses title of hot topics and prints a
sorted count of given keywords from a subreddit
"""
import requests


def count_words(subreddit, word_list, after="", word_dic={}):
    """Count occurrences of words in subreddit titles"""
    if not word_dic:
        for word in word_list:
            word_dic[word] = 0

    if after is None:
        word_list = [[key, value] for key, value in word_dic.items()]
        word_list = sorted(word_list, key=lambda x: (-x[1], x[0]))
        for w in word_list:
            if w[1]:
                print("{}: {}".format(w[0].lower(), w[1]))
        return None

    URL = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'selBot/2.2'}

    params = {'after': after}

    r = requests.get(URL, headers=headers, params=params,
                     allow_redirects=False)

    if r.status_code != 200:
        return None

    try:
        js = r.json()

    except ValueError:
        return None

    try:

        data = js.get("data")
        after = data.get("after")
        children = data.get("children")
        for child in children:
            post = child.get("data")
            title = post.get("title")
            lower = [s.lower() for s in title.split(' ')]

            for w in word_list:
                word_dic[w] += lower.count(w.lower())

    except Exception:
        return None

    count_words(subreddit, word_list, after, word_dic)
