import redis

def _get_connection():
    return redis.Redis(host='localhost', port=6379, db=0)

def get_current_id():
    # Increments the counter key in Redis and gets the current counter atomically.
    # If the counter does not exist, go ahead and create it with the default value.

    r = _get_connection()

    # Create counter if it doesn't exist
    if r.get('counter') == None:
        r.set('counter', 100)

    r.incr('counter')
    return int(r.get('counter'))


def set_url(key, url):
    r = _get_connection()

    r.set(key, url)


def get_url(key):
    r = _get_connection()

    return r.get(key)