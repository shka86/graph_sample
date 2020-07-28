#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pandas as pd

def main():

    list_x = [5, 7, 5, 3]
    list_y = [7, 5, 3, 5]
    list_label = ["north", "east", "south", "west"]
    list_edge = ["north", "east", "south", "west"]

    data = {
        'list_x': list_x,
        'list_y': list_y,
        'list_label': list_label,
        'list_edge': list_edge,
    }
    df = pd.DataFrame(data)

    tgt_file = 'graph_data.csv'
    df.to_csv(tgt_file, encoding='utf-8')


if __name__ == '__main__':

    main()
