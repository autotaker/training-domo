from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum, auto
from functools import total_ordering
from typing import Optional


@total_ordering
class Status(Enum):
    CREATED = auto()
    """
    起票ずみ状態
    """
    PLANNED = auto()
    """
    計画済み。Milestoneがnon-null
    """
    ASSIGNED = auto()
    """
    担当者決定ずみ。Assigneeがnon-null
    """
    DROPPED = auto()
    """
    マイルストーンで中止された状態。
    """
    DEVELOPED = auto()
    """
    開発完了。MR ListおよびTest Resultがnon-null
    """
    CLOSED = auto()
    """
    対応完了。Approverがnon-null
    """

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        else:
            return NotImplemented


@dataclass
class Ticket:
    ticket_no: int
    author: str
    status: Status
    assignee: Optional[str] = None
    approver: Optional[str] = None
    milestone: Optional[str] = None
    mr_list: list[str] = field(default_factory=list)
    test_result: Optional[str] = None

    @classmethod
    def headers(cls) -> list[str]:
        return [
            "Ticket No",
            "Status",
            "Author",
            "Assignee",
            "Approver",
            "Milestone",
            "MR List",
            "Test Result",
        ]

    def to_row(self) -> list[Optional[str]]:
        return [
            str(self.ticket_no),
            self.status.name,
            self.author,
            self.assignee,
            self.approver,
            self.milestone,
            "\r\n".join(self.mr_list),
            self.test_result,
        ]

    @classmethod
    def from_row(self, row: list[str]) -> Ticket:
        return Ticket(
            ticket_no=int(row[0]),
            status=Status[row[1]],
            author=row[2],
            assignee=row[3] if row[3] else None,
            approver=row[4] if row[4] else None,
            milestone=row[5] if row[5] else None,
            mr_list=row[6].split("\r\n") if row[6] else [],
            test_result=row[7] if row[7] else None,
        )
