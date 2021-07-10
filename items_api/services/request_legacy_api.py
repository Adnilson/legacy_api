import requests

LEGACY_URL = 'https://sf-legacy-api.now.sh/items'

class RequestLegacyAPI:
    def __init__(self, page, per_page):
        self.page = page
        self.per_page = per_page

    def run(self, processor):
        return processor().run(self.request(), self.per_page)

    def request(self):
        return requests.get(LEGACY_URL, params={'page': self.page}).json()
