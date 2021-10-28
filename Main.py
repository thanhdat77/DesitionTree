import os
from typing import List, Set
import math
import pandas as pd
from pandas.core.series import Series

os = os.path.join("dataPlay.xlsx")


data = pd.read_excel(os, index_col=0)
att = list(set(data[data.columns[0]]))
target = list(set(data[data.columns[0]]))


def separateH(data: List, att_name: List, target_name: List):
    result = []
    temp = []
    for att in att_name:
        temp.append(att)
        for dt in data:
            if dt[0] == att:
                temp.append(dt[2])
        result.append(temp)
        temp = []
    return result


def find(data: Series, att: int, target: int) -> List:
    att = data.columns[att]
    target = data.columns[target]
    result: list = []

    attset = list(set(list(data[att])))
    target_set = list(set(list(data[target])))
    for k, v in enumerate(attset):
        for ke, va in enumerate(target_set):
            result.append(
                [
                    v,
                    va,
                    data[(data[att] == v) & (data[target] == va)][target].count(),
                ]
            )

    result = sorted(result, key=lambda r: r[0])
    print(result)
    print(separateH(sorted(result, key=lambda r: r[1]), attset, target_set))
    return separateH(sorted(result, key=lambda r: r[1]), attset, target_set)


def mathLog(a, b):
    c = -a / (a + b) * math.log2(a / (a + b)) - b / (a + b) * math.log2(b / (a + b))
    return c


def mathH(data: List):
    result = {}
    count = 0
    final = 0
    for k, v in enumerate(data):
        if v[1] == 0 or v[2] == 0:
            result[v[0]] = [0, (v[1] + v[2])]
            continue
        result[v[0]] = [round(mathLog(v[1], v[2]), 5), (v[1] + v[2])]
        count += v[1] + v[2]
    for j in result.values():
        final += j[1] / count * j[0]
    return result, final


# print(f"copy duong dan file")
# path = input()
# print(f"dong muon chon [Luu]")
# att= input()
# print(f"nhap dong quyet dinh")
print(mathH(find(data, 1, 4)), sep="\n")
