#!/usr/bin/python3
"""
queries the Reddit API, parses the title of all hot articles,
and prints a sorted count of given keywords
"""

import requests


def get_articles(subreddit, word_list, words_dict, after=""):
    """ Get articles """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    url += "?limit=100&after={}".format(after)
    response = requests.get(url,
                            allow_redirects=False,
                            headers={'User-agent': 'Hb-pc'}
                            )
    if response.status_code != 200:
        return None
    articles = response.json().get("data").get("children")
    for article in articles:
        title_list = article.get("data").get("title").lower().split(" ")
        for title in title_list:
            if title in words_dict:
                words_dict[title]["count"] += 1
    after = response.json().get("data").get("after")
    if after is None:
        sorted_w = sorted(words_dict.items(), key=lambda t: t[::-1])
        sorted_w_desc = sorted(sorted_w, key=lambda tup: tup[1], reverse=True)
        for w in sorted_w_desc:
            if w[1]["count"] > 0:
                print("{}: {}".format(w[0], w[1]["count"] * w[1]["mul"]))
        return
    return get_articles(subreddit, word_list, words_dict, after)


def count_words(subreddit, word_list):
    """ Count words """
    words_dict = {}
    word_list = [word.lower() for word in word_list]
    for w in word_list:
        if w not in words_dict:
            words_dict[w] = {"count": 0, "mul": 1}
        else:
            words_dict[w]["mul"] += 1
    # words_dict = dict.fromkeys(word_list, 0)
    get_articles(subreddit, word_list, words_dict)
