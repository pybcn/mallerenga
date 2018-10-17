import pytest

from mallerenga.twitter.twitter import Twitter


@pytest.mark.parametrize(
    'environ,exception_message',
    [
        (
            'missing',
            'Invalid or incomplete Twitter credentials in environment',
        ),
        (
            'incomplete',
            'Invalid or incomplete Twitter credentials in environment',
        ),
        (
            'empty',
            'Invalid or incomplete Twitter credentials in environment',
        ),
        (
            'valid',
            None,
        ),
    ],
    indirect=['environ'],
)
def test_creation(environ, exception_message, tweepy):
    if exception_message is not None:
        with pytest.raises(Exception) as e:
            _ = Twitter()
        assert exception_message == str(e.value)
    else:
        t = Twitter()
        assert t._api.instances == 1
        assert t._api.auth_handler.instances == 1
        assert len(t._api.auth_handler.consumer_key) > 1
        assert len(t._api.auth_handler.consumer_secret) > 1
        assert len(t._api.auth_handler.access_token[0]) > 1
        assert len(t._api.auth_handler.access_token[1]) > 1


def test_tweet(valid_environ, tweepy):
    t = Twitter()
    status = t.tweet('message')
    assert t._api.invocations['tweet'] == 1
    assert 'message' in t._api.tweets
    assert 'message' == status.text
    expected_link = 'https://twitter.com/{}/status/{}'.format(
        status.username[1:],
        status.id,
    )
    assert expected_link == status.link
