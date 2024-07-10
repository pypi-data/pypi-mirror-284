from typing import List, Dict, Union, Optional
from .BaseAPIClient import BaseAPIClient
from rootshell_platform_api.config import API_ENDPOINT, BEARER_TOKEN

class PhaseTagsAPIClient(BaseAPIClient):
    def __init__(self, asset_id):
        super().__init__(base_url=f"{API_ENDPOINT}/phases/{asset_id}/tags")

    def get_entities(self, limit: int = 10, page: int = 1) -> Union[Dict, str]:
        params = {"limit": limit, "page": page}

        return self.get("", params=params)

    from typing import Dict, Union, List, Optional

    def update_entity(self, tag_id: int) -> Union[Dict, str]:
        return self.put(f"/{tag_id}")

    def delete_entity(self, tag_id: int) -> Union[Dict, str]:
        return self.delete(f"/{tag_id}")