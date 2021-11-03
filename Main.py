import os
from typing import List, Set
import math
import pandas as pd
from pandas.core.series import Series


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


def find(data: Series, att: str) -> List:
    target = data.columns[-1]
    result: list = []
    count = 0
    attset = list(sorted(set(data.loc[:, att])))
    target_set = list(sorted(set(data.iloc[:, -1])))
    for k, v in enumerate(attset):
        for ke, va in enumerate(target_set):
            result.append(
                [
                    v,
                    va,
                    data[(data[att] == v) & (data[target] == va)][target].count(),
                ]
            )
    #   Chon thuat toan
    a = mathHID3(separateH(sorted(result, key=lambda r: r[1]), attset, target_set))
    b = separateH(sorted(result, key=lambda r: r[1]), attset, target_set)

    # print(b)  ## dem so yes no cua mot att ##
    # print(a)

    for k, v in enumerate(b):
        print(f"I({att}/{v[0]})= ")
        print(
            f"-{v[1]}/{v[1]+v[2]}*LOG({v[1]}/{v[1]+v[2]})-{v[2]}/{v[1]+v[2]}*LOG({v[2]}/{v[1]+v[2]})={a[k]}",
            end="\n\n",
        )
        count += v[1] + v[2]
    p = f"------------->>H({att})= "
    r = 0
    for k, v in enumerate(b):
        p += f" + {v[1]+v[2]}/{count}*{a[k]}"
        r += (v[1] + v[2]) / count * a[k]
    r = round(r, 5)
    print(p + f" = {r}")
    return r, att


def mathLog(a, b):
    if a == 0 or b == 0:
        return 0
    c = -a / (a + b) * math.log2(a / (a + b)) - b / (a + b) * math.log2(b / (a + b))
    return c


def mathHID3(data: List):
    result = []
    for k, v in enumerate(data):
        result.append(round(mathLog(v[1], v[2]), 5))
    return result


def separateData(data, name):
    atts = list(set(data[name]))
    result = []
    for att in atts:
        temp = data[data[name] == att]
        temp = temp.drop([name], axis=1)
        result.append([temp, att])
    return result


def checkout(data):
    target = data.columns[-1]
    temp = list(set(data[target]))[0]
    for i in data[target]:
        if temp != i:
            return False
    return temp


def main(data: List, floor: int):

    print(data, end="\n\n")
    result = {}
    print(list(data.columns))
    columns = list(data.columns)
    columns.pop()
    if checkout(data):
        return print(f"Tang {floor} co {checkout(data)}")

    else:
        for column in columns:
            print(column + "-----", end="\n\n")
            h = find(data, column)
            result[h[0]] = h[1]
        print(f"Chon thuoc tinh  -->{result[min(result)]}<--")
        for i in separateData(data, result[min(result)]):
            print(f"----------tang {floor+1}-----------", end="\n\n")
            print(f"----{i[1]}----")
            main(i[0], floor + 1)


print(f"copy duong dan file")
path = input()
os = os.path.join(path)
data = pd.read_excel(os)
main(data, 0)
