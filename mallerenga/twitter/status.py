class Status(object):
    def __init__(self, status):
        self._status = status

    @property
    def id(self):
        return self._status.id

    @property
    def username(self):
        return '@{}'.format(self._status.user.screen_name)

    @property
    def link(self):
        return 'https://twitter.com/{0.user.screen_name}/status/{0.id}'.format(
            self._status,
        )

    @property
    def text(self):
        return self._status.text

    @property
    def time(self):
        return self._status.created_at

    def __repr__(self):
        return '{0.time} {0.id} {0.username} {0.text}'.format(self)
