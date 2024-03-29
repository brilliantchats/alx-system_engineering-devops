#!/usr/bin/python3
"""
Recursively queries reddit api and returns all titles of articles
in a list
"""
import requests


def recurse_func(subreddit, hot_list, url):
    """ Recursively calls subreddit pagination and gets all titles
    of hot articles in a list
    """
    ln = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(subreddit, url)
    response = requests.get(ln, headers={'User-Agent': 'Custom'},
                            allow_redirects=False)
    if response.status_code != 200:
        return hot_list
    after = response.json().get('data')['after']
    data = response.json().get('data')['children']
    hot_list = hot_list + [item.get('data')['title'] for item in data]
    if after is None:
        return hot_list
    return recurse_func(subreddit, hot_list, after)


def recurse(subreddit, hot_list=[]):
    """Gets all titles of hot articles and returns them in hot_list"""
    link = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    response = requests.get(link, headers={'User-Agent': 'Custom'},
                            allow_redirects=False)
    if response.status_code != 200:
        return None
    data = response.json().get('data')['children']
    hot_list = hot_list + [item.get('data')['title'] for item in data]
    new_url = response.json().get('data')['after']
    return recurse_func(subreddit, hot_list, new_url)
