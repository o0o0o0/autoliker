Autoliker
=========

Like all accounts by some service, like Facebook or Instagram.

Currently supports Instagram

created by clarisha octa

Usage
-----

You'll need to install the requirements for the project:

```sh
pip install -r requirements.txt
```

Then you'll need to make sure that you have some environment variables set up. See [the config section](#config) for which variables to need to be set. Run the `main.py` script and stuff will be liked/favorited

Putting it all together, you get the following:

```sh
> export AUTOLIKER_INSTAGRAM_ACCESS_TOKEN='some.access.token'
> export AUTOLIKER_INSTAGRAM_USERNAMES='cjstreeter,rowdydoggy'
> python main.py
Fetching the latest Instagram posts...
Liking 20 posts...
Liked 20 posts, skipped 0 posts
```

Adjust `main.py` to configure which services are run.


Config
------

### Instagram

Requires the following environment variables:

- `AUTOLIKER_INSTAGRAM_ACCESS_TOKEN`. Can be fetched with [this gist][ig-gist], which takes in values after you set up a [new API client][ig-api-client].
- `AUTOLIKER_INSTAGRAM_USERNAMES` a comma-separated list of usernames to like posts from

### Twitter

Requires the environment variables which you can get from the
[app management page][twitter-app]:

- `AUTOLIKER_TWITTER_CONSUMER_TOKEN`
- `AUTOLIKER_TWITTER_CONSUMER_SECRET`
- `AUTOLIKER_TWITTER_ACCESS_TOKEN`
- `AUTOLIKER_TWITTER_ACCESS_TOKEN_SECRET`

Set the `AUTOLIKER_TWITTER_USERNAMES` env variable to a list of usernames that should be favorited.


License
-------

Uses the [MIT][mit-license] license. Copyright (c) 2018 Clarisha octa


[ig-auth]: https://instagram.com/developer/authentication/
[ig-gist]: https://gist.github.com/o0o0o0/58a30a5d8be6b50c05645d21e8e89e9d
[ig-api-client]: https://instagram.com/developer/clients/manage/
[twitter-app]: https://apps.twitter.com/
[mit-license]: http://opensource.org/licenses/MIT
