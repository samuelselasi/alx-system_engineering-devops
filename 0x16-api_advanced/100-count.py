#!/usr/bin/python3
"""
Script that parses title of hot topics and prints a
sorted count of given keywords from a subreddit
"""
import requests


def count_words(subreddit, word_list, after=None, count=None):
    """Count occurrences of words in subreddit titles"""
    if after is None:
        after = ""
        count = [0] * len(word_list)

    headers = {'User-Agent': 'selBot/2.2'}
    URL = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'after': after}
    response = requests.get(URL, params=params, headers=headers,
                            allow_redirects=False)
    if response.status_code == 200:
        data = response.json()

        for topic in data['data']['children']:
            for word in topic['data']['title'].split():
                for i, word_in_list in enumerate(word_list):
                    if word_in_list.lower() == word.lower():
                        count[i] += 1

        after = data['data']['after']
        if after is None:
            save = []
            for i in range(len(word_list)):
                for j in range(i + 1, len(word_list)):
                    if word_list[i].lower() == word_list[j].lower():
                        save.append(j)
                        count[i] += count[j]

            combined_data = sorted(zip(count, word_list),
                                   key=lambda x: (-x[0], x[1].lower()))
            for cnt, word in combined_data:
                if cnt > 0 and word_list.index(word) not in save:
                    print(f"{word.lower()}: {cnt}")
        else:
            count_words(subreddit, word_list, after, count)
