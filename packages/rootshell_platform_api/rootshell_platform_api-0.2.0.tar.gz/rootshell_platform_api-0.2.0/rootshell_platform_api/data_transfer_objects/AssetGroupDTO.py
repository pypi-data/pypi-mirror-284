from typing import Optional, List

class AssetGroupDTO:
    def __init__(
        self,
        name: str,
        merge_setting_id: int,
        description: str
    ):
        self.name = name
        self.merge_setting_id = merge_setting_id
        self.description = description

    def to_dict(self):
        return {k: v for k, v in self.__dict__.items() if v is not None}