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
    count = 0
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
    #   Chon thuat toan
    a = mathHID3(separateH(sorted(result, key=lambda r: r[1]), attset, target_set))
    print(
        separateH(sorted(result, key=lambda r: r[1]), attset, target_set)
    )  ## dem so yes no cua mot att ##
    p = f"H({att})= "
    for k in a[0]:
        print(
            f"I({att}/{k})= -{a[0][k][1]}/{a[0][k][1]+a[0][k][2]}*LOG({a[0][k][1]}/{a[0][k][1]+a[0][k][2]})-{a[0][k][2]}/{a[0][k][1]+a[0][k][2]}*LOG({a[0][k][2]}/{a[0][k][1]+a[0][k][2]})={a[0][k][0]}",
            end="\n\n",
        )
        count += a[0][k][1] + a[0][k][2]
    for k in a[0]:
        p += f" + {a[0][k][1]+a[0][k][2]}/{count}*{a[0][k][0]}"
    print(p + f" = {a[1]}")
    return a[1], att


def mathLog(a, b):
    c = -a / (a + b) * math.log2(a / (a + b)) - b / (a + b) * math.log2(b / (a + b))
    return c


def mathHID3(data: List):
    result = {}
    count = 0
    final = 0
    for k, v in enumerate(data):
        if v[1] == 0 or v[2] == 0:
            result[v[0]] = [0, (v[1] + v[2])]
            continue
        result[v[0]] = [round(mathLog(v[1], v[2]), 5), v[1], v[2]]
        count += v[1] + v[2]
    for j in result.values():
        final += j[1] / count * j[0]
    return result, final


def separateData(data, name):
    atts = list(set(data[name]))
    result = []
    for att in atts:
        temp = data[data[name] == att]

        result.append(temp)
    return result


# print(f"copy duong dan file")
# path = input()
# print(f"dong muon chon [Luu y bat dau tu 0]")
# att = int(input())
# print(f"nhap dong quyet dinh")
# target = int(input())
find(data, 3, 4)
# print(separateData(data, "temperature"), sep="\n\n")
