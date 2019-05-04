# 28项数值的分箱 正常返回1，大于正常值2，小于正常值3


def item_conv(item_list):
    result = []
    sex = item_list[0]
    result.append(sex)
    if len(item_list)>2:
        result.append(fx_item_11089_11090(item_list[1]))
        result.append(fx_item_11089_11090(item_list[2]))
        result.append(fx_item_2001(sex,item_list[3]))
        result.append(fx_item_2003(item_list[4]))
        result.append(fx_item_2005(item_list[5]))
        result.append(fx_item_2007(item_list[6]))
        result.append(fx_item_2009(item_list[7]))
        result.append(fx_item_2011(item_list[8]))
        result.append(fx_item_2013(item_list[9]))
        result.append(fx_item_2015(item_list[10]))
        result.append(fx_item_2017(item_list[11]))
        result.append(fx_item_2019(item_list[12]))
        result.append(fx_item_2021(item_list[13]))
        result.append(fx_item_2023(sex,item_list[14]))
        result.append(fx_item_2025(sex,item_list[15]))
        result.append(fx_item_2027(sex,item_list[16]))
        result.append(fx_item_2029(sex,item_list[17]))
        result.append(fx_item_2031(item_list[18]))
        result.append(fx_item_2033(item_list[19]))
        result.append(fx_item_2035(sex,item_list[20]))
        result.append(fx_item_2037(item_list[21]))
        result.append(fx_item_2039(item_list[22]))
        result.append(fx_item_2041(item_list[23]))
        result.append(fx_item_2043(item_list[24]))
        result.append(fx_item_2051(sex,item_list[25]))
        result.append(fx_item_2053(sex,item_list[26]))
        result.append(fx_item_2056(item_list[27]))
        result.append(fx_item_2062(item_list[28]))
    return result

def fx_item_11089_11090(item):
    if item == 0:
        return 0
    else:
        return 1


def fx_item_2001(sex, item):
    # 男性和女性患者
    if sex:
        if item < 4:
            return 3
        elif item > 10:
            return 2
        else:
            return 1
    # 新生儿
    else:
        if item < 15:
            return 3
        elif item > 20:
            return 2
        else:
            return 1


def fx_item_2003(item):
    if item < 50:
        return 3
    elif item > 70:
        return 2
    else:
        return 1


def fx_item_2005(item):
    if item < 17:
        return 3
    elif item > 50:
        return 2
    else:
        return 1


def fx_item_2007(item):
    if item < 3:
        return 3
    elif item > 10:
        return 2
    else:
        return 1


def fx_item_2009(item):
    if item < 0.4:
        return 3
    elif item > 8:
        return 2
    else:
        return 1


def fx_item_2011(item):
    if item < 3:
        return 3
    elif item > 8:
        return 2
    else:
        return 1


def fx_item_2013(item):
    if item < 2:
        return 3
    elif item > 7.5:
        return 2
    else:
        return 1


def fx_item_2015(item):
    if item < 0.8:
        return 3
    elif item > 4.0:
        return 2
    else:
        return 1


def fx_item_2017(item):
    if item < 0.3:
        return 3
    elif item > 0.8:
        return 2
    else:
        return 1


def fx_item_2019(item):
    if item < 0.05:
        return 3
    elif item > 0.5:
        return 2
    else:
        return 1


def fx_item_2021(item):
    if item < 0.12:
        return 3
    elif item > 0.8:
        return 2
    else:
        return 1


def fx_item_2023(sex, item):
    if sex == 1:
        if item < 4:
            return 3
        elif item > 5.5:
            return 2
        else:
            return 1
    elif sex == 2:
        if item < 3.5:
            return 3
        elif item > 5:
            return 2
        else:
            return 1
    else:
        if item < 6:
            return 3
        elif item > 7:
            return 2
        else:
            return 1


def fx_item_2025(sex, item):
    if sex == 1:
        if item < 120:
            return 3
        elif item > 160:
            return 2
        else:
            return 1

    elif sex == 2:
        if item < 110:
            return 3
        elif item > 150:
            return 2
        else:
            return 1

    else:
        if item < 170:
            return 3
        elif item > 200:
            return 2
        else:
            return 1


def fx_item_2027(sex, item):
    if sex == 1:
        if item < 40:
            return 3
        elif item > 50:
            return 2
        else:
            return 1
    elif sex == 2:
        if item < 36:
            return 3
        elif item > 45:
            return 2
        else:
            return 1
    else:
        if item < 36:
            return 3
        elif item > 50:
            return 2
        else:
            return 1


def fx_item_2029(sex, item):
    if sex:
        if item < 80:
            return 3
        elif item > 100:
            return 2
        else:
            return 1
    else:
        if item < 97:
            return 3
        elif item > 109:
            return 2
        else:
            return 1


def fx_item_2031(item):
    if item < 26:
        return 3
    elif item > 37:
        return 2
    else:
        return 1


def fx_item_2033(item):
    if item < 300:
        return 3
    elif item > 360:
        return 3
    else:
        return 1


def fx_item_2035(sex, item):
    if sex:
        if item < 10:
            return 3
        elif item > 16:
            return 2
        else:
            return 1
    else:
        if item < 10:
            return 3
        elif item > 18:
            return 2
        else:
            return 1


def fx_item_2037(item):
    if item < 100:
        return 3
    elif item > 300:
        return 2
    else:
        return 1


def fx_item_2039(item):
    if item < 0.1:
        return 3
    elif item > 0.35:
        return 2
    else:
        return 1


def fx_item_2041(item):
    if item < 7:
        return 3
    elif item > 13:
        return 2
    else:
        return 1


def fx_item_2043(item):
    if item < 10:
        return 3
    elif item > 18:
        return 2
    else:
        return 1


def fx_item_2051(sex, item):
    if sex:
        if item < 0.5:
            return 3
        elif item > 1.5:
            return 2
        else:
            return 1
    else:
        if item < 3:
            return 3
        elif item > 6:
            return 2
        else:
            return 1


def fx_item_2053(sex, item):
    if sex:
        if item < 24:
            return 3
        elif item > 84:
            return 2
        else:
            return 1
    else:
        if item < 144:
            return 3
        elif item > 336:
            return 2
        else:
            return 1


def fx_item_2056(item):
    if item < 0.26:
        return 3
    elif item > 0.34:
        return 2
    else:
        return 1


def fx_item_2062(item):
    if item < 0.24:
        return 3
    elif item > 0.52:
        return 2
    else:
        return 1

if __name__ == '__main__':

    list = [1,0.02,0.1,14.27,76.7,16.9,5.8,0.3,0.3,10.95,2.41,0.83,
            0.04,0.04,1.94,61,0.181,93.3,31.4,337,15.9,201,0.23,11.3,
            13.2,5.02,0.0974,29,12.2]
    l = item_conv(list)
    print(l)