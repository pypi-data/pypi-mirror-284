from typing import Optional, List, Dict, Any
from datetime import datetime

class PhaseHostIssueDTO:
    def __init__(
        self,
        id: Optional[int],
        host_id: int,
        port: str,
        protocol: str,
        service: str,
    ):
        self.id = id,
        self.host_id = host_id,
        self.port = name
        self.protocol = cvss_vector
        self.service = cvss_base_score

    def to_dict(self):
        return {k: v for k, v in self.__dict__.items() if v is not None}