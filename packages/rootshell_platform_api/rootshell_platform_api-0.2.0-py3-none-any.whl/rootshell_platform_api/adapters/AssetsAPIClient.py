from typing import List, Dict, Union, Optional
from .BaseAPIClient import BaseAPIClient
from rootshell_platform_api.config import API_ENDPOINT, BEARER_TOKEN
from rootshell_platform_api.data_transfer_objects.AssetDTO import AssetDTO

class AssetsAPIClient(BaseAPIClient):
    def __init__(self):
        super().__init__(base_url=f"{API_ENDPOINT}/assets")

    def get_entities(
        self,
        limit: int = 10,
        page: int = 1,
        orderByColumn: Optional[str] = "name",
        orderByDirection: Optional[str] = "asc",
        search: Optional[str] = None,
    ) -> Union[Dict, str]:
        params = {
            "limit": limit,
            "page": page,
            "orderBy[column]": orderByColumn,
            "orderBy[direction]": orderByDirection,
        }
        if search:
            params["search"] = search

        return self.get("", params=params)

    from typing import Dict, Union, List, Optional

    def create_entity(self, entity: AssetDTO) -> Union[Dict, str]:
        data = entity.to_dict()
        return self.post("", data)

    def get_entity(self, entity_id: int) -> Union[Dict, str]:
        return self.get(f"/{entity_id}")

    def update_entity(self, entity_id: int, entity: AssetDTO) -> Union[Dict, str]:
        data = entity.to_dict()
        return self.put(f"/{entity_id}", data)

    def delete_entity(self, entity_id: int) -> Union[Dict, str]:
        return self.delete(f"/{entity_id}")
