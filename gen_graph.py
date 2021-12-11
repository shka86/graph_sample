#!/usr/bin/python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

list_x = [1, 2, 3, 4]
list_y = [1, 4, 9, 16]


def gen_graph_waku1():
    """ 枠だけ生成する
        グラフを一枚作成するならこれだけでOK
    """
    fig, ax = plt.subplots()
    # fig, ax = plt.subplots(1,1)
    ax.plot(list_x, list_y)
    plt.show()


def gen_graph_waku1_2():
    """ 枠だけ生成する
        複数のサブプロットにする場合は、squeezeとtight_layoutを設定しておいたほうが吉
        squeeze=False: axの選択が常に二次元になる。defaultだと1x2のサブプロット場合は一次元での指定になる。指定方法が変わるのは面倒。
        tight_layout=True: 見た目をよくする。外部にお出しする時にお直しするくらいなら初めからやっておく。
    """
    fig, ax = plt.subplots(2, 2, squeeze=False, tight_layout=True)
    ax[0,1].plot(list_x, list_y)
    plt.show()


def gen_graph_waku2():
    """ 枠だけ生成する
        こういう方法もある
    """
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    # ここの add_subplot(111) のように表記もできるが、
    # 二けたになったときにどうなるのかわからんので避ける。
    # やり方があるとしても、同じような疑問を持つ人がいるはずで、
    # 可読性が下がるから避けるのがベターでしょ。

    ax.plot(list_x, list_y)
    plt.show()


if __name__ == '__main__':
    gen_graph_waku1()
    gen_graph_waku1_2()
    gen_graph_waku2()
