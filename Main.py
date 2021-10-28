import os
from typing import List, Set
import numpy as np
import pandas as pd
from pandas.core.series import Series

os = os.path.join("dataPlay.xlsx")


data = pd.read_excel(os, index_col=0)
att = list(set(data[data.columns[0]]))
target = list(set(data[data.columns[0]]))


def loop(list, name: str):
    result = []
    for i in list:
        if i[0] in name:
            result.append(i)
    return result


def separateH(data: List, att_name: List, target_name: List):

    result = []
    for att in att_name:
        for dt in data:
            print(dt[0])
            result.append(loop(data, att))
    return result


def find(data: Series, att: int, target: int) -> List:
    att = data.columns[att]
    target = data.columns[target]

    result: list = []
    attset = list(set(list(data[att])))  # value in att
    # print(attset)
    target_set = list(set(list(data[target])))  # value in target
    # print(target_set)
    for k, v in enumerate(attset):
        for ke, va in enumerate(target_set):
            result.append(
                [
                    v,
                    va,
                    data[(data[att] == v) & (data[target] == va)][target].count(),
                ]
            )
    return result


print(find(data, 1, 4))
print(separateH(find(data, 1, 4), att, target))
