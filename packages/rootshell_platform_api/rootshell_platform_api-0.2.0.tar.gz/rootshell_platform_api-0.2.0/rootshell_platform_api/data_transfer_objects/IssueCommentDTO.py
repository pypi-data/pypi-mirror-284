from typing import Optional, List

class IssueCommentDTO:
    def __init__(
        self,
        comment: str,
    ):
        self.comment = comment

    def to_dict(self):
        return {k: v for k, v in self.__dict__.items() if v is not None}