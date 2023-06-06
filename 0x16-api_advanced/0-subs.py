#!/usr/bin/python3
"""
Get all the subscribers from a given subreddit
"""
import requests
import sys


def number_of_subscribers(subreddit):
    """
    Gets all the subscribers from the subreddit passed as an argument
    """
    url = 'https://www/reddit.com/r/{}/about'.format(subreddit)
    response = requests.get(url)
    if response:
        return response.json().get('data')['subscribers']
    return 0
