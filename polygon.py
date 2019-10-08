#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# polygon.py
#

import math    # for math.sqrt()

class Polygon(object):
    # コンストラクタ 一辺の長さを登録する
    def __init__(self, side):
        self.side = side

    # 周囲長を返す
    def get_perimeter(self):
        print('Not implemented')
        return 0

    # 面積を返す
    def get_area(self):
        print('Not implemented')
        return 0

# 以下、Polygonを継承してget_perimeter, get_areaをもつ
# サブクラス、Triangle, Squareを作りなさい

# Triangleのクラス定義




# Squareのクラス定義



# 上で定義したクラスを使うメインプログラム
if __name__ == '__main__':
    polygons = [Triangle(3.0), Triangle(4.5), Square(2.5)]
    for s in polygons:
        print('Type: {0},  Perimeter: {1}, Area: {2}'.
              format(type(s), s.get_perimeter(), s.get_area()))
