import os

import pytest

empty_environment = {}
incomplete_environment = {
    'TWITTER_CONSUMER_KEY': 'oreqiui298y',
}
empty_credentials_environment = {
    'TWITTER_CONSUMER_KEY': 'oreqiui298y',
    'TWITTER_CONSUMER_SECRET': '',
    'TWITTER_ACCESS_TOKEN': '',
    'TWITTER_ACCESS_TOKEN_SECRET': '',
}
valid_environment = {
    'TWITTER_CONSUMER_KEY': 'oreqiui298y',
    'TWITTER_CONSUMER_SECRET': 'oreqiui298y',
    'TWITTER_ACCESS_TOKEN': 'oreqiui298y',
    'TWITTER_ACCESS_TOKEN_SECRET': 'oreqiui298y',
}
environs = {
    'missing': empty_environment,
    'incomplete': incomplete_environment,
    'empty': empty_credentials_environment,
    'valid': valid_environment,
}


@pytest.fixture
def environ(request, monkeypatch):
    monkeypatch.setattr(os, 'environ', environs[request.param])


@pytest.fixture
def valid_environ(monkeypatch):
    monkeypatch.setattr(os, 'environ', environs['valid'])


class OAuthHandlerMock(object):
    def __init__(self, consumer_key, consumer_secret):
        if not hasattr(self, 'instances'):
            self.instances = 0
        self.instances += 1
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = None

    def set_access_token(self, access_token, access_token_secret):
        self.access_token = (access_token, access_token_secret)


class APIMock(object):
    def __init__(self, auth):
        if not hasattr(self, 'instances'):
            self.instances = 0
        self.instances += 1
        self.auth_handler = auth
        self.invocations = {}
        self.tweets = []

    def update_status(self, message):
        if 'tweet' not in self.invocations:
            self.invocations['tweet'] = 0
        self.invocations['tweet'] += 1
        self.tweets.append(message)
        return StatusMock(message)


class UserMock(object):
    def __init__(self, screen_name):
        self.screen_name = screen_name


class StatusMock(object):
    def __init__(self, message):
        self.id = '32140984532498'
        self.user = UserMock('twitter_handle')
        self.text = message
        self.link = 'https://twitter.com/twitter_handle/status/32140984532498'


@pytest.fixture
def tweepy(monkeypatch):
    monkeypatch.setattr('tweepy.OAuthHandler', OAuthHandlerMock)
    monkeypatch.setattr('tweepy.API', APIMock)
