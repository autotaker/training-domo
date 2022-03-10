import pytest

from day2.implementme import (
    count_ticket_for_milestone,
    rank_assignees,
    summarize_ticket_statuses,
)
from day2.model import Status

example_csv = [
    "Ticket No,Status,Author,Assignee,Approver,Milestone,MR List,Test Result\r\n",
    "50920,CLOSED,山本 千代,鈴木 裕美子,山本 くみ子,22-01,95798,https://tickets.domo.org/2599\r\n",
    '63574,CLOSED,中村 知実,山口 知実,林 香織,22-01,"65894\r\n97413\r\n',
    "10279\r\n",
    '85774",https://tickets.domo.org/4820\r\n',
    "66748,CLOSED,坂本 七夏,林 さゆり,山本 くみ子,22-02,91549,https://tickets.domo.org/7896\r\n",
    "44910,CLOSED,近藤 智也,田中 明美,中島 直子,22-02,80467,https://tickets.domo.org/2257\r\n",
    '93112,CLOSED,近藤 智也,田中 明美,山田 太一,22-02,"50912\r\n' "87401\r\n",
    "34368\r\n",
    '21402",https://tickets.domo.org/6198\r\n',
    "57334,DROPPED,佐藤 零,前田 千代,,22-03,,\r\n",
    "78844,ASSIGNED,山崎 直子,小川 涼平,,22-03,,\r\n",
    "59867,DROPPED,小林 直子,山口 知実,,22-03,,\r\n",
    "80539,DEVELOPED,中島 春香,,,22-03,91067,\r\n",
    "65911,CREATED,坂本 七夏,,,,,\r\n",
    "12505,CREATED,中村 知実,,,,,\r\n",
    "84009,CREATED,小林 直子,,,,,\r\n",
]


@pytest.mark.parametrize(
    "milestone, expected", [("22-01", 2), ("22-02", 3), ("22-03", 4)]
)
def test_count_ticket_for_milestone_return_2_for_22_01(milestone, expected):
    assert count_ticket_for_milestone(example_csv, milestone) == expected


def test_summarize_ticket_statuses():
    result = summarize_ticket_statuses(example_csv)
    assert result[Status.CREATED] == 3
    assert result[Status.ASSIGNED] == 1
    assert result[Status.DEVELOPED] == 1
    assert result[Status.CLOSED] == 5
    assert result[Status.DROPPED] == 2


def test_rank_assignees():
    result = rank_assignees(example_csv)
    assert len(result) == 4
    assert result[0] == ("田中 明美", 2)
    assert result.index(("鈴木 裕美子", 1)) >= 1
    assert result.index(("林 さゆり", 1)) >= 1
    assert result.index(("山口 知実", 1)) >= 1


if __name__ == "__main__":
    pytest.main([__file__])
