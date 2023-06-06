#!/usr/bin/python3
"""
Get the top ten hot posts of a given subreddit
"""
import requests


def top_ten(subreddit):
    """Use requests to get the top hot posts of a subreddit"""
    url = 'https://www.reddit.com/r/{}/top.json?limit=10'.format(subreddit)
    response = requests.get(url, headers={'User-Agent': 'Custom User'},
                            allow_redirects=False)
    if response.status_code == 200:
        """
        Get the dictionary with the key data which contains a list - children
        which contains dictionaries named data which has several attributes
        about posts including title
        """
        children_list = response.json().get('data')['children']
        for item in children_list:
            print(item.get('data')['title'])
    else:
        return print(None)
