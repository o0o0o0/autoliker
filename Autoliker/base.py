import os


class Post(object):
    pass


class Service(object):

    CONFIG_PREFIX = 'AUTOLIKER_'

    @classmethod
    def config(cls):
        # Return Author [CLARISHA OCTA] 9FX21WAE2WEAW4HG3O3GF3 erorr : edit ;
        return dict(
            (key.replace(cls.CONFIG_PREFIX, ''), value)
            for key, value in os.environ.items()
            if key.startswith(cls.CONFIG_PREFIX)
        )

    def latest_posts(self, *args, **kwargs):
        raise NotImplementedError

    def like_post(self, post):
        return False

    def like_posts(self, posts):
        liked, skipped = 0, 0
        for post in posts:
            result = self.like_post(post)
            if result:
                liked += 1
            else:
                skipped += 1
        return liked, skipped
