from __future__ import annotations

from typing import Iterable

from day2.model import Status


# (課題1)
def count_ticket_for_milestone(csvfile: Iterable[str], milestone: str) -> int:
    """
    指定されたマイルストーンのチケット数を返します。

    Args:
      csvfile: CSVファイルオブジェクトまたは文字列を返すイテレータ
      milestone (str): 対象のマイルストーン

    Returns:
      (int) 指定されたマイルストーンのチケット数
    """
    return 0


# (課題2)
def summarize_ticket_statuses(csvfile: Iterable[str]) -> dict[Status, int]:
    """
    チケットステータスごとに該当するチケット数をカウントします。

    Args:
      csvfile: CSVファイルオブジェクトまたは文字列を返すイテレータ

    Returns:
      各ステータスをキーとし、そのステータスのチケット数を値とするdict
    """
    return {}


# (発展課題)
def rank_assignees(
    csvfile: Iterable[str],
) -> list[tuple[str, int]]:
    """
    最も多くチケットをCloseした順でAssigneeをランク付けします。

    Args:
      csvfile: CSVファイルオブジェクトまたは文字列を返すイテレータ

    Returns:
      CLOSEDにしたチケット数の多い順でAssigneeを並び替えたリスト。
      - リストの各要素はAssigneeの名前と、その人がCLOSEDにしたチケット数のペア。
    """
    return []


if __name__ == "__main__":
    with open("day2/data/tickets.csv", "r", newline="", encoding="utf-8") as f:
        print("22-02のチケット数:", count_ticket_for_milestone(f, "22-02"))
        f.seek(0)
        print("22-03のチケット数:", count_ticket_for_milestone(f, "22-03"))
        f.seek(0)
        print("ステータスごとのチケット数:")
        for status, count in summarize_ticket_statuses(f).items():
            print(f"  {status.name:9}: {count:3d}")
        print("解決数ランキング:")
        f.seek(0)
        for assignee, count in rank_assignees(f):
            print(f"  {assignee}: {count}")
