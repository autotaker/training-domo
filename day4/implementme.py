import json
from typing import Any, Tuple

import requests

API_URL = "https://api.data.metro.tokyo.lg.jp/v1"


def pprint(data: Any) -> None:
    """
    JSONデータを整形して表示します
    """
    print(json.dumps(data, indent=2, ensure_ascii=False))


def fetch_api_page(endpoint: str, params: dict[str, str]) -> Tuple[Any, Any]:
    """
    指定したAPIから1ページ分データを取得します。
    """
    r = requests.get(API_URL + endpoint, params=params)
    if r.status_code != 200:
        raise Exception(f"Status code is {r.status_code}, Request: {API_URL+endpoint}")
    page_data, page_info = r.json()
    return page_data, page_info


def fetch_api_all(endpoint: str, params: dict[str, str]) -> list[Any]:
    """
    指定したAPIから全ページ分のデータを取得します。
    """
    page_no = 1
    print(f"Fetch Page: {page_no}")
    page_data, page_info = fetch_api_page(endpoint, params)
    result = list(page_data)
    while page_info["moreResults"] == "MORE_RESULTS_AFTER_LIMIT":
        params["cursor"] = page_info["endCursor"]
        page_no += 1
        print(f"Fetch Page: {page_no}")
        page_data, page_info = fetch_api_page(endpoint, params)
        result.extend(page_data)
    return result


def print_public_facilities() -> None:
    """
    公共施設一覧`/PublicFacility`から施設名称・住所・説明を表示する
    """
    pass


def group_covid19_patiens_by_age(day: str) -> dict[str, int]:
    """
    コロナウイルス陽性者`/Covid19Patient`から年代別の陽性者数サマリを返す

    Args:
      day (str): 公表日

    Return:
      年代別の陽性者数をまとめたdict
    """
    pass


def find_nearest_multipurpose_toilet(
    latitude: float, longitude: float
) -> dict[str, Any]:
    """
    指定した地点の最寄りのだれでもトイレを検索して返す

    Args:
      latitude (float):  緯度
      longitude (float): 経度

    Return:
      最寄りのトイレのデータ（JSON）
    """
    pass
