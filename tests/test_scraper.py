import pytest
from twitter_scraper import scrape, process


def test_fetch_tweets():
    tweets = scrape.fetch_tweets("twitter", count=5)
    assert len(tweets) <= 5
    assert all(isinstance(tweet, dict) for tweet in tweets)


def test_tweets_to_txt(tmp_path):
    input_json = tmp_path / "test_tweets.json"
    output_txt = tmp_path / "test_tweets.txt"

    tweets = scrape.fetch_tweets("twitter", count=5)
    scrape.save_tweets(tweets, str(input_json))

    process.tweets_to_txt(str(input_json), str(output_txt))

    assert output_txt.exists()
