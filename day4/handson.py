import json
from typing import Any, Tuple

import requests

API_URL = "https://api.data.metro.tokyo.lg.jp/v1"


def pprint(data: Any) -> None:
    print(json.dumps(data, indent=2, ensure_ascii=False))


def print_covid19_patients() -> None:
    r = requests.get(API_URL + "/Covid19Patient")
    print(r.status_code)
    if r.status_code != 200:
        raise Exception(f"Status code is {r.status_code}")
    pprint(r.json())


def print_covid19_patients_of_day(day: str) -> None:
    params = {"from": day, "till": day}
    r = requests.get(API_URL + "/Covid19Patient", params=params)
    if r.status_code != 200:
        raise Exception(f"Status code is {r.status_code}")
    pprint(r.json())


def get_covid19_patients(params: dict[str, str]) -> Tuple[list[Any], dict[str, Any]]:
    r = requests.get(API_URL + "/Covid19Patient", params=params)
    if r.status_code != 200:
        raise Exception(f"Status code is {r.status_code}")
    return r.json()


def get_covid19_patients_of_day(day: str) -> list[dict[str, Any]]:
    params = {"from": day, "till": day, "limit": "1000"}
    page_no = 1
    print(f"Fetch Page: {page_no}")
    page_data, page_info = get_covid19_patients(params)
    result = list(page_data)
    while page_info["moreResults"] == "MORE_RESULTS_AFTER_LIMIT":
        page_no += 1
        print(f"Fetch Page: {page_no}")
        params["cursor"] = page_info["endCursor"]
        page_data, page_info = get_covid19_patients(params)
        result.extend(page_data)
    return result


if __name__ == "__main__":
    print_covid19_patients()
    print_covid19_patients_of_day("2022-05-08")
    result = get_covid19_patients_of_day("2022-05-08")
    pprint(result[:10])
    print(len(result))
