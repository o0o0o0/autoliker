#!/usr/bin/env python

from autoliker.services.instagram import InstagramUserPhotoService
from autoliker.services.twitter import TwitterUserMentionService

if __name__ == '__main__':
    services = [InstagramUserPhotoService, TwitterUserMentionService]

    for service_cls in services:
        service = service_cls()

        print("Fetching the latest {} posts...".format(service.SERVICE_NAME))
        posts = service.latest_posts()

        print("Liking {} posts...".format(len(posts)))
        liked, skipped = service.like_posts(posts)
        print("Liked {} posts, skipped {} posts".format(liked, skipped))
