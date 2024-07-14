from dubidoc.enum import HttpMethod


__all__ = ('DocumentAPI',)


class DocumentAPI:
    PATH = 'documents'

    def __init__(self, client):
        self.client = client

    def list(self):
        return self.client.make_request(HttpMethod.GET, self.PATH)

    def create(self, body, organization_id=None):
        return self.client.make_request(HttpMethod.POST, self.PATH, body)

    def get(self, document_id):
        path = f'{self.PATH}/{document_id}'
        return self.client.make_request(HttpMethod.GET, path)

    def edit(self, document_id, title):
        path = f'{self.PATH}/{document_id}'
        body = {
            'title': title,
        }
        return self.client.make_request(HttpMethod.PUT, path, body)

    def delete(self, document_id):
        """
        Title: Видалення документа
        Description: Увага, видалити документ можливо лише за умови, що він не був підписаний або надісланий отримувачу
        """
        path = f'{self.PATH}/{document_id}'
        return self.client.make_request(HttpMethod.DELETE, path)

    def download(self):
        raise NotImplementedError

    def unarchive(self):
        raise NotImplementedError

    def participants(self):
        raise NotImplementedError

    def sign(self):
        raise NotImplementedError

    def signatures(self):
        raise NotImplementedError

    def archive(self):
        raise NotImplementedError
