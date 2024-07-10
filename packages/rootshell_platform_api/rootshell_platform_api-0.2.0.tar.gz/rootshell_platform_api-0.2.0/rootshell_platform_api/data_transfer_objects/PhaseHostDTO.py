from typing import Optional
from datetime import datetime

class PhaseHostDTO:
    def __init__(
        self,
        ip: Optional[str] = None,
        name: Optional[str] = None,
        hostname: Optional[str] = None,
        location: Optional[str] = None,
        operating_system: Optional[str] = None,
    ):
        if not (name or hostname or ip):
            raise ValueError("At least one of 'name', 'hostname', or 'ip' must be provided.")

        self.ip = ip
        self.name = name
        self.hostname = hostname
        self.location = location
        self.operating_system = operating_system

    def to_dict(self):
        return {k: v for k, v in self.__dict__.items() if v is not None}