from falu.client.api_client import ApiClient


class PostApiRequest(ApiClient):

    @classmethod
    def create(cls, base_url=None, path=None, data=None, api_key=None, idempotency_key: str = None, workspace=None,
               live: bool = None, params=None):
        return cls._execute(method="POST", base_url=base_url, path=path, data=data, key=api_key,
                            idempotency_key=idempotency_key, workspace=workspace, live=live, params=params)
