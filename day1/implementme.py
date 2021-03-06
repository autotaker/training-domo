def categorize_triangle(a: int, b: int, c: int) -> str | None:
    """
    引数で三辺の長さが与えられます。
    その長さを持つ三角形の種類を返してください。

    Args:
      a b c (int): 三辺の長さ（整数）

    Returns:
      None: 三角形が構成できない時
      '直角三角形': 一つの角が90度である場合
      '正三角形': 三辺の長さが等しい時
      '二等辺三角形': 二辺の長さが等しく、正三角形でない時
      '鋭角三角形': 三辺の長さが全て異なり、三つの角のいずれもが90度未満の時
      '鈍角三角形': 三辺の長さが全て異なり、一つの角が90度を超える時
    """
    pass
