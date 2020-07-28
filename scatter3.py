#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 散布図
# プロットにラベルをつける
# 東西南北で方向を指定する
# csv読み込み機能追加版

from matplotlib.transforms import offset_copy
import numpy as np
import matplotlib.transforms as mtransforms
import sys
import matplotlib.pyplot as plt
import pandas as pd


def calc_axis_range(list_in):

    maxnum = max(list_in)  # 最大値取得
    maxnum = int(maxnum)  # 整数化
    maxdigit = len(str(maxnum))  # 整数値の文字数=桁数
    return maxdigit


def main():

    tgt_file = 'graph_data.csv'
    df = pd.read_csv(tgt_file)
    list_x = list(df['list_x'])
    list_y = list(df['list_y'])
    list_label = list(df['list_label'])
    list_edge = list(df['list_edge'])

    print(list_x)
    print(list_y)
    print(list_label)
    print(list_edge)

    fig = plt.figure()
    ax1 = fig.add_subplot(111)

    # ラベルのオフセットを決める
    label_offset_x = {"north": 0,
                      "east": 0.05,
                      "south": 0,
                      "west": -0.05}
    label_offset_y = {"north": 0.05,
                      "east": 0,
                      "south": -0.05,
                      "west": 0}
    label_rotate = {"north": 90,
                    "east": 0,
                    "south": 270,
                    "west": 0}
    label_halign = {"north": "center",
                    "east": "left",
                    "south": "center",
                    "west": "right"}
    label_valign = {"north": "bottom",
                    "east": "center",
                    "south": "top",
                    "west": "center"}

    for x, y, label, edge in zip(list_x, list_y, list_label, list_edge):

        # 一要素ごとにプロットを追加
        ax1.plot(x,                # xの値
                 y,                 # yの値
                 marker='d',             # マーカーの形状
                 markersize=6,           # マーカー全体のサイズ
                 markerfacecolor='#66DDDD',  # マーカーの色は白
                 markeredgewidth=1,      # マーカーエッジのサイズ
                 markeredgecolor='#44BBBB',  # マーカーエッジを赤にする
                 linestyle='None')       # ライン非表示

        # ラベルの追加
        trans_offset = mtransforms.offset_copy(
            ax1.transData,
            fig=fig,
            x=label_offset_x[edge],
            y=label_offset_y[edge],
            units='inches'
        )
        ax1.text(x,                # xの値
                 y,                 # yの値
                 label,
                 transform=trans_offset,
                 horizontalalignment=label_halign[edge],
                 verticalalignment=label_valign[edge],
                 rotation=label_rotate[edge])

    # 軸のスケール
    axis_max_x = 10 ** calc_axis_range(list_x)
    axis_max_y = 10 ** calc_axis_range(list_y)
    ax1.axis([0, axis_max_x, 0, axis_max_y])

    plt.show()


if __name__ == '__main__':

    main()
