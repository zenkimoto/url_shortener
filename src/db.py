import redis

def get_current_id():
    # Increments the counter key in Redis and gets the current counter atomically.
    # If the counter does not exist, go ahead and create it with the default value.

    r = redis.Redis(host='localhost', port=6379, db=0)

    # Create counter if it doesn't exist
    if r.get('counter') == None:
        r.set('counter', 100)

    r.incr('counter')
    return r.get('counter')
