#!/usr/bin/python3
"""
Get all the subscribers from a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    Gets all the subscribers from the subreddit passed as an argument
    """
    headers = {'User-Agent': 'Custom'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get('data')['subscribers']
    return 0
