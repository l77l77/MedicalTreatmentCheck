from .vtcheck import Disease
from .vtcheck import DiseaseList


def dcode_to_dname(code):
    dict = {'110000':'真性红细胞增多症',
            '120000':'肺原性心脏病',
            '130000':'贫血',
            '131100': '溶血性贫血',
            '131111':'获得性溶血性贫血',
            '131112':'全身性溶血性贫血',
            '131200':'出血性贫血',
            '131300':'细胞低色素贫血',
            '131400':'缺铁性贫血',
            '131500':'再生障碍性贫血',
            '131600':'镰刀细胞性贫血',
            '131700':'营养不良性巨幼红细胞性贫血',
            '140000':'均一性贫血',
            '141100':'小细胞均一性贫血',
            '141200':'小细胞非均一性贫血',
            '141300':'正常细胞非均一性贫血',
            '141400':'大细胞均一性贫血',
            '141500':'大细胞非均一性贫血',
            '141600':'正常细胞均一性贫血',
            '150000':'血小板增多症',
            '151100':'原发性血小板增多症',
            '151200':'症状性血小板增多症',
            '160000':'甲状腺功能低下',
            '170000':'白血病 ',
            '171100':'慢性白血病',
            '171200':'粒细胞白血病',
            '171300':'单核细胞白血病',
            '171400':'淋巴细胞性白血病',
            '171500':'慢性粒细胞白血病',
            '180000':'骨髓纤维化',
            '190000':'感染',
            '191100':'急性化脓感染',
            '191200':'病毒感染',
            '191300':'炎性感染',
            '210000':'炎症',
            '220000':'原发性血小板减少性紫癜',
            '250000':'播散性红斑狼疮',
            '260000':'骨髓造血机能障碍',
            '270000':'药物引起的骨髓抑制',
            '280000':'脾功能亢进',
            '290000':'血栓性疾病及血栓前状态',
            '310000':'慢粒',
            '320000':'巨大血小板综合症',
            '330000':'尿毒症',
            '340000':'酸中毒',
            '350000':'急性汞中毒',
            '360000':'急性铅中毒',
            '370000':'伤寒',
            '371100':'副伤寒',
            '380000':'疟疾',
            '390000':'流感',
            '410000':'寄生虫病',
            '430000':'何杰金病',
            '440000':'淋巴瘤',
            '450000':'骨髓增生异常综合征',
            '460000':'细胞增多症',
            '461100':'传染性单核细胞增多症',
            '461200':'急性传染性淋巴细胞增多症',
            '470000':'粒细胞缺乏症',
            '480000':'营养不良性巨幼红细胞性贫血',
            }
    return dict[code]
def cmp_item(list):
    result = DiseaseList()

    # 白细胞计数
    if list[3] == 2:
        d3_19 = Disease('191300')
        d3_17 = Disease('170000')
        result.adds(d3_17, d3_19)
    if list[3] == 3:
        d3_28 = Disease('280000')
        d3_37 = Disease('370000')
        d3_38 = Disease('380000')
        d3_39 = Disease('390000')
        result.adds(d3_28, d3_37, d3_38, d3_39)

    # 中性粒细胞比率
    if list[4] == 2:
        d4_19 = Disease('191100')
        d4_17 = Disease('171200')
        d4_13 = Disease('131100')
        d4_33 = Disease('330000')
        d4_34 = Disease('340000')
        result.adds(d4_19, d4_17, d4_13, d4_33, d4_34)
    elif list[4] == 3:
        d4_37 = Disease('370000')
        d4_13 = Disease('131500')
        d4_47 = Disease('470000')
        d4_39 = Disease('390000')
        d4_38 = Disease('380000')
        result.adds(d4_37, d4_13, d4_47, d4_39, d4_38)

    # 淋巴细胞
    if list[5] == 2:
        d5_46 = Disease('461100')
        d5_17 = Disease('171500')
        result.adds(d5_46, d5_46)

    # 单核细胞
    if list[6] == 2:
        d6_17 = Disease('171300')
        d6_46 = Disease('461100')
        result.adds(d6_17, d6_46)

    # 嗜酸性粒细胞
    if list[7] == 2:
        d7_41 = Disease('410000')
        result.adds(d7_41)
    elif list[7] == 3:
        d7_37 = Disease('371100')
        result.adds(d7_37)

    # 嗜碱性粒细胞
    if list[8] == 2:
        d8_17 = Disease('171500')
        d8_43 = Disease('430000')
        result.adds('430000', '171500')
    elif list[8] == 3:
        d8_37 = Disease('371100')
        result.adds(d8_37)

    #####这几项与前面的重复。（比率与计数 相似
    # 中性粒细胞计数

    # 淋巴细胞计数

    # 单核细胞计数

    # 嗜酸粒细胞计数

    # 嗜碱粒细胞计数

    # 红细胞计数
    if list[14] == 2:
        d14_11 = Disease('110000')
        d14_12 = Disease('120000')
        result.adds(d14_11, d14_12)
    elif list[14] == 3:
        d14_13 = Disease('130000')
        result.adds(d14_13)

    #####前14项 完毕
    ###############

    # 血红蛋白
    if list[15] == 2:
        d15_11 = Disease('110000')
        result.adds(d15_11)
    elif list[15] == 3:
        d15_13 = Disease('130000')
        result.adds(d15_13)

    # 红细胞比积
    if list[16] == 2:
        d16_11 = Disease('160000')
        result.adds(d16_11)
    elif list[16] == 3:
        d16_13 = Disease('130000')
        result.adds(d16_13)

    # 红细胞平均容量
    if list[17] == 2:
        d17_48 = Disease('480000')
        d17_13 = Disease('131111')
        result.adds(d17_48, d17_13)
    elif list[17] == 3:
        d17_13 = Disease('131112')
        result.add(d17_13)

    # 平均血红蛋白 和 红细胞体积分布一起进行判断
    # if list[18] == 2 :
    #     d18_11 = Disease('110000')
    #     d18_12 = Disease('120000')
    #     result.adds(d18_11,d18_12)
    # elif list[18] == 3:
    #     d18_13 = Disease('130000')
    #     result.add(d18_13)

    # 平均血红蛋白浓度
    if list[19] == 2:
        d19_11 = Disease('110000')
        d19_12 = Disease('120000')
        result.adds(d19_11, d19_12)
    elif list[19] == 3:
        d19_13 = Disease('130000')

    # 红细胞体积分布 平均血红蛋白 一起进行判断
    if list[20] == 2:
        if list[18] == 1:
            d20_14 = Disease('141400')
        elif list[18] == 2:
            d20_14 = Disease('141500')
    elif list[20] == 3:
        if list[18] == 1:
            d20_14 = Disease('141100')
        elif list[18] == 2:
            d20_14 = Disease('141200')
    elif list[20] == 1:
        if list[18] == 1:
            d20_14 = Disease('141600')
        elif list[18] == 2:
            d20_14 = Disease('141300')
    result.add(d20_14)

    # 血小板计数
    if list[21] == 2:
        d21_15_1 = Disease('151100')
        d21_11 = Disease('110000')
        d21_15_2 = Disease('151200')
        d21_13 = Disease('131400')
        d21_21 = Disease('210000')
        result.adds(d21_11, d21_13, d21_15_1, d21_15_2, d21_21)
    elif list[21] == 3:
        d21_22 = Disease('220000')
        d21_23 = Disease('230000')
        d21_24 = Disease('240000')
        d21_25 = Disease('250000')
        d21_13 = Disease('131500')
        result.adds(d21_22, d21_23, d21_24, d21_25, d21_25, d21_13)

    # 血小板比率

    # 血小板平均体积
    if list[23] == 2:
        d22_22 = Disease('220000')
        d22_31 = Disease('310000')
        d22_32 = Disease('320000')
        d22_13 = Disease('131600')
        result.adds(d22_22, d22_31, d22_32, d22_13)
    elif list[23] == 3:
        d22_13 = Disease('131500')
        d22_28 = Disease('280000')
        result.adds(d22_13, d22_28)

    # 血小板分布宽度
    if list[24] == 2:
        d23_48 = Disease('480000')
        d23_17 = Disease('171500')
        d23_29 = Disease('290000')
        d23_32 = Disease('320000')
        result.adds(d23_48, d23_17, d23_29, d23_32)

    # 网织红细胞百分比
    if list[25] == 3:
        d24_13 = Disease('131500')
        result.adds(d24_13)

    # 网织红细胞绝对值
    # 未成熟网织红细胞指数
    # 高光散网织红百分比

    result.sort_by_vote()
    return result


if __name__ == '__main__':
    # test = [1, 1, 1, 1, 1, 1, 1,
    #         1, 1, 1, 1, 1, 1, 1,
    #         1, 1, 1, 1, 1, 1, 1,
    #         1, 1, 1, 1, 1, 1, 1, 1]
    test = [1, 1, 1, 2, 2, 3, 1,
            3, 3, 2, 1, 2, 3, 3,
            3, 3, 3, 1, 1, 1, 1,
            1, 1, 1, 3, 2, 3, 3, 2]
    l = cmp_item(test)
    l.show_list(vote=True)
    d_code = l.diseases[0].get_code()
    print(d_code)
    print(dcode_to_dname(d_code))
