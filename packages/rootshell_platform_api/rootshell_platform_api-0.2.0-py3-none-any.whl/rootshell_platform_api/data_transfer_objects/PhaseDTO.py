from typing import Optional
from datetime import datetime

class PhaseDTO:
    def __init__(
        self,
        project_id: int,
        name: str,
        status: int,
        executive_summary: str,
        caveat: str,
        assessment_context: str,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        location: Optional[str] = None,
        scope_summary: Optional[str] = None,
        tester_id: Optional[int] = None,
        test_type_id: Optional[int] = None,
        approved_at: Optional[datetime] = None,
        approved_by: Optional[int] = None,
        completed_by: Optional[int] = None,
        probability: Optional[int] = None,
        questionnaire_id: Optional[int] = None,
    ):
        self.project_id = project_id
        self.name = name
        self.status = status
        self.start_date = start_date
        self.end_date = end_date
        self.location = location
        self.executive_summary = executive_summary
        self.caveat = caveat
        self.assessment_context = assessment_context
        self.scope_summary = scope_summary
        self.tester_id = tester_id
        self.test_type_id = test_type_id
        self.approved_at = approved_at
        self.approved_by = approved_by
        self.completed_by = completed_by
        self.probability = probability
        self.questionnaire_id = questionnaire_id

    def to_dict(self):
        return {k: v for k, v in self.__dict__.items() if v is not None}