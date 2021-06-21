import hashlib, uuid

salt = uuid.uuid4().hex
cache_url = {}

def get_page(url):
    if cache_url.get(url):
        print(f'Ссылка: {url} уже в кэше')
    else:
        hashed_url = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
        cache_url[url] = hashed_url
        print(cache_url)


get_page('https://google.com')
get_page('https://google.com')
get_page('https://yandex.ru')