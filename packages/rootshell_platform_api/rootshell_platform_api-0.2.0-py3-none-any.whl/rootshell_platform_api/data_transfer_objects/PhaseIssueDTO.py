from typing import Optional, List, Dict, Any
from datetime import datetime

class PhaseIssueDTO:
    def __init__(
        self,
        id: Optional[int],
        phase_id: Optional[int],
        name: str,
        cvss_vector: str,
        cvss_base_score: float,
        cvss_temporal_score: float,
        cvss_environmental_score: float,
        risk_rating: int,
        finding: str,
        references: str,
        summary: str,
        technical_details: str,
        recommendation: str,
        status: int,
        confirmed_at: datetime,
        published_at: datetime,
        exploit_available: bool = False,
        active_exploit: int = 0,
        hosts: Optional[List[Dict[str, Any]]] = None
    ):
        self.id = id,
        self.phase_id = phase_id,
        self.name = name
        self.cvss_vector = cvss_vector
        self.cvss_base_score = cvss_base_score
        self.cvss_temporal_score = cvss_temporal_score
        self.cvss_environmental_score = cvss_environmental_score
        self.risk_rating = risk_rating
        self.finding = finding
        self.references = references
        self.summary = summary
        self.technical_details = technical_details
        self.recommendation = recommendation
        self.status = status
        self.confirmed_at = confirmed_at
        self.published_at = published_at
        self.exploit_available = exploit_available
        self.active_exploit = active_exploit
        self.hosts = hosts if hosts else []

    def to_dict(self):
        return {k: v for k, v in self.__dict__.items() if v is not None}