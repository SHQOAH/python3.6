def move(man, sep):
    """
    将man列表向左移动sep单位，最左边的元素向列表后面添加，相当于队列顺时针移动
    """
    for i in range(sep):
        item = man.pop(0)
        man.append(item)

def play(man=41, sep=3, rest=2):
    """
    :param man:玩家个数
    :param sep:杀死数到的第几个人
    :param rest:幸存者数量
    :return:
    """
    print('总共有%d个人，每报数到第%d的人自杀，最后剩余%d个人'%(man, sep, rest))
    man = [i for i in range(1, man + 1)]  # 初始化玩家队列
    print("玩家队列：", man)
    sep = sep - 1
    while len(man) > rest:
        move(man, sep)
        print('kill', man.pop(0))
    return man

servive = play()

print("最后逃生的人编号是：", servive)