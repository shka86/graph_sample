#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 散布図
# 軸の範囲を10の乗数区切りで自動調整

import sys
import matplotlib.pyplot as plt

def calc_axis_range(list_in):

    maxnum = max(list_in)   #最大値取得
    maxnum = int(maxnum)    #整数化
    maxdigit = len(str(maxnum))    #整数値の文字数=桁数
    return maxdigit

def main():

    list_x = [1, 2, 3, 4]
    list_y = [1, 4, 9, 16]

    plt.plot(   list_x,                # xの値
                list_y,                 # yの値
                marker='d',             # マーカーの形状
                markersize=6,           # マーカー全体のサイズ
                markerfacecolor='#66DDDD',  # マーカーの色は白
                markeredgewidth=1,      # マーカーエッジのサイズ
                markeredgecolor='#44BBBB',  # マーカーエッジを赤にする
                linestyle='None')       # ライン非表示

    # 軸のスケール
    axis_max_x = 10 ** calc_axis_range(list_x)
    axis_max_y = 10 ** calc_axis_range(list_y)
    plt.axis([0, axis_max_x, 0, axis_max_y])          

    plt.show()

if __name__ == '__main__':

    main()
