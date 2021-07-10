class ResultProcessor:
    def run(self, result, per_page):
        items = {}
        items['data'] = result['data'][:per_page]
        items['metadata'] = result['metadata']
        items['metadata'].update({'perPage': per_page or 100})
        items['metadata'].update({'page': int(result['metadata']['page'])})

        return items
