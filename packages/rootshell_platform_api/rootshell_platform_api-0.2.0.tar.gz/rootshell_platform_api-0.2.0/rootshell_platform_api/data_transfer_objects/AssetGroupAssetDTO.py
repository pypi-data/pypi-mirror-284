from typing import Optional, List

class AssetGroupAssetDTO:
    def __init__(
        self,
        asset_ids: str,
    ):
        self.asset_ids = asset_ids

    def to_dict(self):
        return {k: v for k, v in self.__dict__.items() if v is not None}