# Day4: REST APIを叩いてみよう

## 学習目標

REST APIから目的のデータを取得できるようになる

## アジェンダ
- APIからデータを取得しよう（ハンズオン）
- 他のAPIにもアクセスしてみよう（モブプロ）

## APIからデータを取得しよう

今回は[東京都OpenData API](https://portal.data.metro.tokyo.lg.jp/opendata-api/)を利用してみます。
このサイトではいくつかのOpen DataをAPIから取得できます。

まずは、Webページのインターフェースから`/Covid19Patient`を選択して実行してみましょう。

実行できたら今度はPythonから呼び出してみます。


### データの取得

PythonでAPIを叩くには[requests](https://requests-docs-ja.readthedocs.io/en/latest/)と言うライブラリを使います。Pythonのインタプリタを開いて以下のコードを実行してみましょう。

```python
>>> import requests
>>> r = requests.get("https://api.data.metro.tokyo.lg.jp/v1/Covid19Patient")
>>> r.status_code
200
>>> r.json()
[[{'全国地方公共団体コード': '130001', '都道府県名': '東京都'...
```

### データの整形
データは表示されましたが、整形されていないのでみにくいですね。jsonライブラリを使うとデータを整形できます。

```python
>>> data = r.json()
>>> import json
>>> print(json.dumps(data, indent=2))
[
  [
    {
      "\u5168\u56fd\u5730\u65b9\u516c\u5171\u56e3\u4f53\u30b3\u30fc\u30c9": "130001",
      "\u90fd\u9053\u5e9c\u770c\u540d": "\u6771\u4eac\u90fd",
      "\u60a3\u8005_\u5e74\u4ee3": "10\u6b73\u672a\u6e80",
      "\u516c\u8868_\u5e74\u6708\u65e5": "2022-05-08T00:00:00.000Z",
      "\u60a3\u8005_\u6027\u5225": "\u7537\u6027",
      "No": 1455432
    },
    ...
  ]
]
```

データは整形されたのですが、日本語がエスケープされていて読めません。

```python
>>> print(json.dumps(data,indent=2,ensure_ascii=False))
[
  [
    {
      "全国地方公共団体コード": "130001",
      "都道府県名": "東京都",
      "患者_年代": "10歳未満",
      "公表_年月日": "2022-05-08T00:00:00.000Z",
      "患者_性別": "男性",
      "No": 1455432
    },
    ...
  ]
]
```

無事データを表示する事ができました。

handson.pyの`print_covid19_patients()`にコード例を載せています。

### パラメータの指定
さて、今度は日付で絞り込んでみましょう。以下のようなURLでアクセスすれば2022年5月8日公表のデータだけを絞り込む事ができます。

```url
https://api.data.metro.tokyo.lg.jp/v1/Covid19Patient?from=2022-05-08&till=2022-05-08
```

requestsでは[`params`オプション引数](https://requests-docs-ja.readthedocs.io/en/latest/user/quickstart/#url)を指定することでURLパラメータを指定する事ができます。

```python
>>> params = {'from': '2022-05-08', 'till': '2022-05-08'}
>>> r = requests.get("https://api.data.metro.tokyo.lg.jp/v1/Covid19Patient", params = params)
>>> data = r.json()
>>> print(json.dumps(data, indent=2, ensure_ascii=False))
```

handson.pyの`print_covid19_patients_of_day(day)`にコード例を載せています。

### ページネーション

さて、取得したデータの中身を見てみるとちょうど100件のデータが取得されています。

```python
>>> len(data[0])
100
```

これはページネーションと呼ばれ、REST APIでは一回のリクエストで取得できる件数に上限があります。

APIの説明ページを読むと、この上限を引き上げる事ができます。

```python
>>> params = {'from': '2022-05-08', 'till': '2022-05-08', 'limit': '1000'}
>>> r = requests.get("https://api.data.metro.tokyo.lg.jp/v1/Covid19Patient", params = params)
>>> data = r.json()
>>> len(data[0])
1000
```

まだ残りのデータがあるようです。`limit`パラメータはこれ以上引き上げられないため、残りのデータを指定する必要があります。

データのJSONを分析すると、第二要素にページネーションに関する情報が入っている事がわかります。

```
>>> data[1]
{'moreResults': 'MORE_RESULTS_AFTER_LIMIT', 'endCursor': 'Cn8KHQoQ5YWs6KGoX+W5tOaciOaXpRIJCICAyK7MzvcCElpqGmJ+dG9reW8tY2F0YWxvZy1wcm9kdWN0aW9ucjwLEghSZXZpc2lvbiITQ292aWQxOVBhdGllbnQ6MTY3OAwLEg5Db3ZpZDE5UGF0aWVudBiAgICt+brsCAwYACAB', 'revision': 1678, 'updated': '2022-05-08T10:45:06.567Z'}
```

`moreResults`が`MORE_RESULTS_AFTER_LIMIT`の場合は次のページがあります。`endCursor`で返された文字列を`cursor`パラメータで指定すると次のページを取得する事ができます。

少しややこしいですが、`handson.py`の`get_covide_patients_of_day`関数のようにすると全件データを取得できます。

```python
>>> from day4.handson import *
>>> result = get_covid19_patients_of_day('2022-05-08')
Fetch Page: 1
Fetch Page: 2
Fetch Page: 3
Fetch Page: 4
Fetch Page: 5
>>> len(result)
4711
```

## 他のAPIにもアクセスしてみよう

### `/Covid19Patient`以外のエンドポイントからデータを取得してみよう
[東京都OpenData API](https://portal.data.metro.tokyo.lg.jp/opendata-api/)の他のAPIからもデータを取得してみましょう。

どのようなデータがあるか簡単に分析してみましょう。

### [httpbin.org](http://httpbin.org/#/)で遊んでみよう

REST APIの練習サイトとしてhttpbin.orgというものがあります。
このサイトではさまざまなリクエストの送り方を試す事ができます。

試しにリクエストを送ってみましょう。
