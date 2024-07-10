from typing import Optional, List

class AssetDTO:
    def __init__(
        self,
        name: Optional[str] = None,
        hostname: Optional[str] = None,
        ip: Optional[str] = None,
        operating_system: Optional[str] = None,
        priority_rating: Optional[int] = None,
        location: Optional[str] = None,
        system_owner: Optional[str] = None,
        technical_owner: Optional[str] = None,
        team_system_owner: Optional[str] = None,
        team_technical_owner: Optional[str] = None,
        company_id: Optional[int] = None,
        abbreviated_asset_value: Optional[str] = "",
        notes: Optional[str] = None,
        tags: Optional[List[str]] = None
    ):
        if not (name or hostname or ip):
            raise ValueError("At least one of 'name', 'hostname', or 'ip' must be provided.")

        self.name = name
        self.hostname = hostname
        self.ip = ip
        self.operating_system = operating_system
        self.priority_rating = priority_rating
        self.location = location
        self.system_owner = system_owner
        self.technical_owner = technical_owner
        self.team_system_owner = team_system_owner
        self.team_technical_owner = team_technical_owner
        self.company_id = company_id
        self.abbreviated_asset_value = abbreviated_asset_value
        self.notes = notes
        self.tags = tags if tags is not None else []

    def to_dict(self):
        return {k: v for k, v in self.__dict__.items() if v is not None}