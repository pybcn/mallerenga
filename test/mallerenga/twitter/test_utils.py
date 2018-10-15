import pytest

from mallerenga.twitter.utils import validate_credentials


@pytest.mark.parametrize(
    'environ, expected',
    [
        ('missing', False),
        ('incomplete', False),
        ('empty', False),
        ('valid', True),
    ],
    indirect=['environ'],
)
def test_validate_credentials(environ, expected):
    assert validate_credentials() == expected
