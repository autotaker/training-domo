# Day 2: CSV操作1

# アジェンダ

1. （ハンズオン）CSVを読み込んでみよう
2. （モブプログラミング）CSVからデータを抜き出そう


# 1. CSVを読み込んでみよう

## 学習目標
CSVの読み込みができるようになる

## 1-0. CSVの確認
`day2/data/tickets.csv`にチケット情報の一覧を置いています。
CSVには以下の情報が含まれています。

- `Ticket No`: ID(整数)
- `Status`: 状態( CREATED, PLANNED, DROPPED ASSIGNED, DEVELOPED, CLOSED)のいずれか
- `Author`:　起票者
- `Assignee`: 開発担当者
- `Approver`: 承認担当者
- `Milestone`: マイルストーン
- `MR List`:　修正MR Iidのリスト（改行区切り）
- `Test Result`: テスト結果のURL

## 1-1. ファイルの作成
`day2/handson.py`を作成しましょう。

## 1-2. ヘッダの読み込み
まずはCSVのヘッダーを読み込んでみましょう。

`handson.py`に以下のコードを入力してください。

```python
import csv
if __name__ == "__main__":
    with open("day2/data/tickets.csv", "r", newline="", encoding="utf-8") as csvfile:
        # readerを作成`
        reader = csv.reader(csvfile)
        # headerの読み込み
        header = next(reader)
        print("header: ", header)
```

実行するとヘッダーが表示されます。

```
header:  ['Ticket No', 'Status', 'Author', 'Assignee', 'Approver', 'Milestone', 'MR List', 'Test Result']
```

### FAQ
- Q. csvパッケージのドキュメントはどこ？
  - A. https://docs.python.org/ja/3/library/csv.html 
- Q. withって何？
  - A. ファイル等のリソースリークが起きないようにブロックを抜けたら確実に閉じるための構文です。 [参考](https://www.python.jp/pages/with-statement-3.9.html)
- Q. `newline=""`の意味は？
  - A. https://docs.python.org/ja/3/library/csv.html#id3 


## 1-3.　データの読み込み

データを読み込む際には以下のようにfor文で一エントリずつ読み込むことができます。

```diff
         header = next(reader)
+        # 本体データの読み込み
+        for row in reader:
+            print(row)
```

実行すると読み込んだデータが表示されます。

```
header:  ['Ticket No', 'Status', 'Author', 'Assignee', 'Approver', 'Milestone', 'MR List', 'Test Result']
['17349', 'CLOSED', '長谷川 晃', '青木 花子', '山本 太郎', '22-01', '67029\r\n37653', 'https://tickets.domo.org/223']
['79408', 'CLOSED', '佐藤 直樹', '井上 英樹', '山本 太郎', '22-01', '23531\r\n41870\r\n31282\r\n60130', 'https://tickets.domo.org/9524']
['46434', 'CLOSED', '清水 明美', '田中 明美', '中島 直子', '22-01', '89854\r\n80225\r\n55011\r\n45990', 'https://tickets.domo.org/6774']
['51646', 'CLOSED', '山崎 くみ子', '山口 学', '三浦 学', '22-01', '94991\r\n15872', 'https://tickets.domo.org/9279']
['86418', 'CLOSED', '藤田 零', '高橋 明美', '山田 太一', '22-01', '53266\r\n71124', 'https://tickets.domo.org/902']
['87313', 'CLOSED', '加藤 和也', '佐々木 七夏', '山田 太一', '22-02', '53837\r\n14800\r\n96111', 'https://tickets.domo.org/9395']
['55514', 'CLOSED', '佐藤 直樹', '山田 舞', '三浦 学', '22-02', '36527', 'https://tickets.domo.org/9466']
```

### FAQ
- Q. `for row in reader`になぜ`reader`って書けるの？
  - A. Pythonのfor文では`in`の後に任意の[イテレータ](https://docs.python.org/ja/3/library/stdtypes.html#iterator-types)を渡すことができます。[csv.reader](https://docs.python.org/ja/3/library/csv.html#csv.reader)はイテレータのプロトコルを実装しています。

# 2. CSVからデータを抜き出そう 

## 学習目標
CSVからデータを抽出する頻出パターンの実装方法の習得

## 課題説明
`implementme.py`の各関数を仕様通りに実装してください。

## 実行方法
ファイルを実行すると`day2/data/tickets.csv`に対してチケットを分析した結果が出力されます。

また、各関数ごとに単体テストを用意しています。Testingパネルからテストを実行できます。

## ヒント
`model.py`にチケットのデータをPythonのクラスにマッピングするコードを用意しています。
以下のようにするとデータをTicketクラスのオブジェクトとして扱えます。

```python
from day2.model import Ticket

...
for row in reader:
    ticket = Ticket.from_row(row)
```
