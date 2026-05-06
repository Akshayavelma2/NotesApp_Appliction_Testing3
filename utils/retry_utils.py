import time

def retry_action(action, retries=3, delay=1):

    last_exception = None

    for attempt in range(retries):
        try:
            return action()
        except Exception as e:
            last_exception = e
            time.sleep(delay)

    raise last_exception