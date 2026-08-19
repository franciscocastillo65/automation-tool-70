import time
import requests

class RetryException(Exception):
    pass

def retry_request(url, retries=3, delay=2):
    attempt = 0
    while attempt < retries:
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            attempt += 1
            if attempt == retries:
                raise RetryException(f'Failed after {retries} attempts: {e}')
            time.sleep(delay)
    return None

if __name__ == '__main__':
    try:
        result = retry_request('https://api.example.com/data')
        print(result)
    except RetryException as e:
        print(e)