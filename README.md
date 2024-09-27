# Twitter Scraper

A simple command-line tool to fetch and process tweets.

## Features

- Fetch tweets from a specific user (most recent -- up to 3200)
- Save tweets to JSON
- Convert JSON tweets to a readable text format
- Retrieve a specific tweet by ID

## Installation

```sh
$ pip install twitter-scraper
```

## Usage

First, set up your Twitter Bearer Token:

```sh
$ twitter-scraper setup
```

### Fetching Tweets

Fetch the latest tweets from a user:

```sh
$ twitter-scraper fetch-tweets <username> <count>
```

This will save the tweets to a JSON file.

To generate a text file output, use the `--to-txt` flag when fetching tweets:

```sh
$ twitter-scraper fetch-tweets <username> <count> --to-txt
```
