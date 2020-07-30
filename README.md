# URL Shortener

A sample Flask project to shorten URLs like [bitly](https://bitly.com/) and [goo.gl](https://goo.gl/) using a Redis data store.

## Requirements

Below are instructions on setting up this project using a machine running Mac OS Catalina with [Homebrew](https://brew.sh/) installed and Python 3.

To install Python 3 with Homebrew:

`$ brew install python3`

## Setup

1. Clone repository
2. Run _setup.sh_ from terminal to setup the Python Virtual Environment
3. Run _dev.sh_ for development and _prod.sh_ for production.

_Note: Running prod.sh still uses the Python Development Server for local development.  See deployment instructions on deployment on a Ubuntu server._

## Install Redis

In the terminal, type the following to install Redis:

`$ brew install redis`

* [Install and config Redis on Mac OS X via Homebrew](https://medium.com/@petehouston/install-and-config-redis-on-mac-os-x-via-homebrew-eb8df9a4f298)
* [Redis GUI Tools](https://redislabs.com/blog/so-youre-looking-for-the-redis-gui/)
* [Redis Desktop](https://redisdesktop.com/)

To have launchd start redis now and restart at login:
` $ brew services start redis`
Or, if you don't want/need a background service you can just run:
` $ redis-server /usr/local/etc/redis.conf`

A script _redis.sh_ is included to start Redis not as a background service.