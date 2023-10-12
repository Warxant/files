with open('1.txt', 'r', encoding='utf-8') as a, open('2.txt', 'r', encoding='utf-8') as b, open('3.txt', 'r', encoding='utf-8') as c, open('Final_File.txt', 'w', encoding='utf-8' ) as d:

    dict_txt = {}

    count_1 = 0
    for i in a.readlines():
        count_1 += 1
    a.seek(0)
    dict_txt[count_1] = ['1.txt', count_1, a.read()]

    count_2 = 0
    for i in b.readlines():
        count_2 += 1
    b.seek(0)
    dict_txt[count_2] = ['2.txt', count_2, b.read()]

    count_3 = 0
    for i in c.readlines():
        count_3 += 1
    c.seek(0)
    dict_txt[count_3] = ['3.txt', count_3, c.read()]

    sorted_dict = dict(sorted(dict_txt.items()))

    for i in sorted_dict.values():
        for s in i:
            d.write(f'{s}\n')























































    # one = a.read()
    # two = b.read()
    # three = c.read()
    # name_1 = ('1.txt')
    # name_2 = ('2.txt')
    # name_3 = ('3.txt')
    # if len(one) > len(two) > len(three):
    #     d.write(f'{name_2}\n')
    #     d.write(f'{str(len(two))}\n')
    #     d.write(f'{two}\n')
    #     d.write(f'{name_1}\n')
    #     d.write(f'{str(len(one))}\n')
    #     d.write(one)
    # elif len(one) < len(two):
    #     d.write(f'{name_1}\n')
    #     d.write(f'{str(len(one))}\n')
    #     d.write(f'{one}\n')
    #     d.write(f'{name_2}\n')
    #     d.write(f'{str(len(two))}\n')
    #     d.write(f'{two}\n')
    #
    # else:
    #     print('Ошибка')
    #
    # a.close()
    # b.close()

