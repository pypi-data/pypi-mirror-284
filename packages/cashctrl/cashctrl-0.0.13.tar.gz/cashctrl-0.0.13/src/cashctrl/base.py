import xmltodict
class CashCtrlResource:
    def __init__(self, client, resource):
        self._client = client
        self._resource = resource

    def read(self, id):
        if not type(id) == int:
            raise ValueError('id must be an integer')
        data=self._client._make_request('GET', f'{self._resource}/read.json', params={'id': id})
        try:
            xml = xmltodict.parse(data["name"])
            localised_name=xml["values"][self._client.default_language]
        except:
            localised_name=data["name"]
        data["localisedName"]=localised_name
        return data

    def list(self,  filter=None, query=None, dir='ASC', sort='number',limit=1000000, **kwargs):
        """
            Retrieves a list of a Resource.

            :param filter: An array of filters to filter the list. All filters must match (AND).
            :type filter: list[dict], optional
            :param query: Fulltext search query.
                - comparison (str, optional): Comparison type. Possible values: 'eq', 'like', 'gt', 'lt'.
                - field (str, optional): The name of the column to filter by.
                - value (str or list, optional): Text to filter by, or a JSON array of multiple values (OR).
            :type query: str, optional
            :param sort: The column to sort the list by. Defaults to 'number'.
            :type sort: str, optional
            :param dir: The direction of the sort order. Defaults to 'ASC'.
            :param limit: The maximum number of items to return. Defaults to 1 mio.
            :type dir: str, optional
            :return: A list of filtered and sorted items.
            """
        #todo: what if there are more than 1'000'000 items?
        return self._client._make_request('GET', f'{self._resource}/list.json', {"filter": filter, "query": query, "sort": sort, "dir": dir, "limit": limit, **kwargs})

    def export(self, params=None):
        raise NotImplementedError
        #return self.client._make_request('GET', f'{self.resource}/export', params=params)

    def create(self, data):
        raise NotImplementedError
        #return self.client._make_request('POST', f'{self.resource}/create', json=data)

    def update(self, id, **kwargs):
        return self._client._make_request('POST', f'{self._resource}/update.json', params={id:id, **kwargs})

    def delete(self, id):
        return self._client._make_request('DELETE', f'{self._resource}/delete/{id}')
