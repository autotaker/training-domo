import csv

import pytest

from day2.model import Status, Ticket

example_csv = [
    "Ticket No,Status,Author,Assignee,Approver,Milestone,MR List,Test Result\r\n",
    '17349,CLOSED,長谷川 晃,青木 花子,山本 太郎,22-01,"67029\r\n',
    '37653",https://tickets.domo.org/223\r\n',
    "79408,CREATED,佐藤 直樹,,,,,\r\n",
]


def test_Ticket_headers():
    reader = csv.reader(example_csv)
    assert Ticket.headers() == next(reader)


def test_Ticket_from_row():
    reader = csv.reader(example_csv)
    next(reader)
    assert Ticket.from_row(next(reader)) == Ticket(
        ticket_no=17349,
        author="長谷川 晃",
        assignee="青木 花子",
        approver="山本 太郎",
        milestone="22-01",
        mr_list=["67029", "37653"],
        test_result="https://tickets.domo.org/223",
        status=Status.CLOSED,
    )
    assert Ticket.from_row(next(reader)) == Ticket(
        ticket_no=79408, status=Status.CREATED, author="佐藤 直樹"
    )


def test_Ticket_to_row():
    ticket = Ticket(
        ticket_no=17349,
        status=Status.CLOSED,
        author="長谷川 晃",
        assignee="青木 花子",
        approver="山本 太郎",
        milestone="22-01",
        mr_list=["67029", "37653"],
        test_result="https://tickets.domo.org/223",
    )
    assert ticket.to_row() == [
        "17349",
        "CLOSED",
        "長谷川 晃",
        "青木 花子",
        "山本 太郎",
        "22-01",
        "67029\r\n37653",
        "https://tickets.domo.org/223",
    ]


if __name__ == "__main__":
    pytest.main([__file__])
