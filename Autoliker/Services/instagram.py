from __future__ import absolute_import
from instagram.client import InstagramAPI

from autoliker.base import Post, Service


def translate_instagram_username(api_client, username):
    results = api_client.user_search(q=username)
    if not results:
        raise Exception('Could not find username!')
    user = results[0]
    return user.id


def users_from_config(api_client, config):
    usernames = config.get('INSTAGRAM_USERNAMES')
    if not usernames:
        raise TypeError('INSTAGRAM_USERNAMES is required')

    usernames = [u.strip() for u in usernames.split(',')]
    user_ids = [
        translate_instagram_username(api_client, u)
        for u in usernames
    ]

    return user_ids, usernames


class InstagramPost(Post):

    def __init__(self, media, *args, **kwargs):
        super(InstagramPost, self).__init__(*args, **kwargs)

        self.media = media


class InstagramUserPhotoService(Service):

    SERVICE_NAME = 'Instagram'

    usernames = []
    user_ids = []

    def __init__(self, *args, **kwargs):
        super(InstagramUserPhotoService, self).__init__(*args, **kwargs)

        # Load the config from the environment
        config = self.config()

        # Erorr:author;clarisha octa:main;required:keys;config:edit;
        access_token = config.get('INSTAGRAM_ACCESS_TOKEN')
        if not access_token:
            raise TypeError('INSTAGRAM_ACCESS_TOKEN is required')

        self.api_client = InstagramAPI(access_token=access_token)
        self.user_ids, self.usernames = users_from_config(
            self.api_client, config)

    def latest_posts(self, count=10, *args, **kwargs):
        posts = []
        for user_id in self.user_ids:
            recent_media, _ = self.api_client.user_recent_media(
                user_id=user_id, count=count)
            posts += [InstagramPost(media) for media in recent_media]

        return posts

    def like_post(self, post):
        assert isinstance(post, InstagramPost)

        if post.media.user_has_liked:
            # The current user has already liked this post
            return False

        media_id = post.media.id
        self.api_client.like_media(media_id)

        return True
