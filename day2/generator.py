import csv
import sys
from typing import Optional

import faker

from day2.model import Status, Ticket


def noise(ticlet: Ticket, fake: faker.Faker) -> None:
    max_value = 30
    if fake.pyint(max_value=max_value) == 0:
        ticket.assignee = None
    if fake.pyint(max_value=max_value) == 0:
        ticket.approver = None
    if fake.pyint(max_value=max_value) == 0:
        ticket.milestone = None
    if fake.pyint(max_value=max_value) == 0:
        ticket.mr_list = []
    if fake.pyint(max_value=max_value) == 0:
        ticket.test_result = None


def generate(n: int, fake: faker.Faker) -> list[Ticket]:

    reporters = [fake.name() for _ in range(30)]
    developers = [fake.name() for _ in range(30)]
    managers = [fake.name() for _ in range(10)]
    milestones = [
        f"{year:02d}-{month:02d}" for year in [22, 23] for month in range(1, 13)
    ]
    current_milestone = "22-03"
    current_milestone_idx = milestones.index(current_milestone)

    def generate_ticket() -> Ticket:
        status = fake.random_element(Status)
        ticket_no = fake.unique.random_int(min=10000, max=99999)
        author = fake.random_element(reporters)
        assignee = (
            fake.random_element(developers) if status >= Status.ASSIGNED else None
        )
        approver = fake.random_element(managers) if status >= Status.CLOSED else None

        milestone: Optional[str] = current_milestone
        if status == Status.PLANNED:
            milestone = fake.random_element(milestones[current_milestone_idx:])
        elif status == Status.CLOSED:
            milestone = fake.random_element(milestones[: current_milestone_idx + 1])
        elif status == Status.CREATED:
            milestone = None

        test_result = (
            f"https://tickets.domo.org/{fake.random_int()}"
            if status >= Status.DEVELOPED
            else None
        )
        mr_list = (
            [fake.numerify("%####") for _ in range(fake.random_int(min=1, max=4))]
            if status >= Status.DEVELOPED
            else []
        )
        return Ticket(
            ticket_no=ticket_no,
            author=author,
            assignee=assignee,
            approver=approver,
            milestone=milestone,
            mr_list=mr_list,
            test_result=test_result,
            status=status,
        )

    result = [generate_ticket() for i in range(n)]
    result.sort(key=lambda x: str(x.milestone))
    return result


if __name__ == "__main__":

    fake = faker.Faker("ja_JP")
    filename = sys.argv[1] if len(sys.argv) >= 2 else "day2/data/tickets.csv"
    with open(filename, "w", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(Ticket.headers())
        for ticket in generate(100, fake):
            # noise(ticket, fake)
            writer.writerow(ticket.to_row())
