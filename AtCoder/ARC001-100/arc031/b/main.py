#!/usr/bin/env python3
from itertools import product
field = [list(input()) for i in range(10)]
H,W=10,10
def walk(x, y, fp):
    """
        探索関数
    Parameters:
        x : int
            x座標
        y : int
            y座標
        fp: list
            探索済座標記憶配列
    Returns:
        fp : list
            更新したfp
    """
    # 範囲外または探索済なら調べない
    if (x < 0 or 9 < x) or (y < 0 or 9 < y) or (field[y][x] == "x") or (fp[y][x] == "o"):
        return fp
    else:
        # 探索済にする
        fp[y][x] = "o"
        # 上下左右のマスを調べる
        fp = walk(x, y+1, fp)
        fp = walk(x+1, y, fp)
        fp = walk(x, y-1, fp)
        fp = walk(x-1, y, fp)
        return fp

for (x, y) in product(range(10), repeat=2):
    point = field[y][x]
    # ある地点を埋め立てる
    field[y][x] = "o"
    # 探索済記憶用配列
    fp = walk(x, y, [["x"]* 10 for _ in range(10)])
    # 埋め立てた結果、全てのマスに到達可能かどうか
    if all(field[y][x] == fp[y][x]
        for (x, y) in product(range(10), repeat=2)):
            print("YES")
            exit()
    # 埋め立てをやめる
    field[y][x] = point
print("NO")