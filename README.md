# mallerenga

Mallerenga is a toolkit for communities to handle their Twitter accounts.

## Features

Currently, mallerenga supports the following features:
- Update status

## Requirements

In order to use mallerenga, a Python 3 environment with Pipenv installed is required.

A Twitter account with development credentials (consumer key and secret and access token and secret) are also required.

## Install and setup

The install steps are:
```
git clone https://github.com/pybcn/mallerenga
cd mallerenga
pipenv install
```

In order to have mallerenga setup, a `.env` file must be created, with the following content:
```
export PYTHONPATH=$PYTHONPATH:.
export TWITTER_CONSUMER_KEY=<your Twitter account consumer key>
export TWITTER_CONSUMER_SECRET=<your Twitter account consumer secret>
export TWITTER_ACCESS_TOKEN=<your Twitter account access token>
export TWITTER_ACCESS_TOKEN_SECRET=<your Twitter account access token secret>
```

## Usage

To update the Twitter status, use the following command:
```
pipenv run bin/mallerenga New status message
```
