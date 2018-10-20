import tweepy

from autoliker.base import Post, Service


class TwitterTweet(Post):

    def __init__(self, tweet, *args, **kwargs):
        super(TwitterTweet, self).__init__(*args, **kwargs)

        self.status = tweet


class TwitterUserMentionService(Service):

    SERVICE_NAME = 'Twitter'

    usernames = []

    def __init__(self, *args, **kwargs):
        super(TwitterUserMentionService, self).__init__(*args, **kwargs)

        # Load config author:clarisha octa ; main:erorr;edit:key;
        config = self.config()

        consumer_key = config.get('TWITTER_CONSUMER_TOKEN')
        consumer_secret = config.get('TWITTER_CONSUMER_SECRET')

        if not consumer_key or not consumer_secret:
            raise TypeError('TWITTER_CONSUMER_{TOKEN,SECRET} is required')

        access_token = config.get('TWITTER_ACCESS_TOKEN')
        access_secret = config.get('TWITTER_ACCESS_TOKEN_SECRET')
        if not access_token or not access_secret:
            raise TypeError('TWITTER_ACCESS_TOKEN{_SECRET} is required')

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_secret)

        self.api_client = tweepy.API(auth)

        usernames = config.get('TWITTER_USERNAMES')
        if not usernames:
            raise TypeError('TWITTER_USERNAMES is required')

        self.usernames = [u.strip() for u in usernames.split(',')]

        self.favorites = [tweet.id for tweet in self.api_client.favorites()]

    def latest_posts(self, count=10, *args, **kwargs):
        posts = []
        for username in self.usernames:
            recent_tweets = self.api_client.search(username)
            posts += [
                TwitterTweet(tweet)
                for tweet in recent_tweets
                if tweet.user.screen_name == username
            ]

        return posts

    def like_post(self, post):
        assert isinstance(post, TwitterTweet)

        if post.status.id in self.favorites:
            return False

        post.status.favorite()

        self.favorites.append(post.status.id)

        return True
