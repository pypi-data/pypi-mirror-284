def 列表_并集(列表1, 列表2):
    """
    返回两个列表的并集(将两个列表合并，想同的元素只会出现一次)。

    参数:
        - 列表1 (list): 第一个列表。
        - 列表2 (list): 第二个列表。

    返回:
        - list: 包含两个列表中所有不同元素的列表。如果出现异常，返回空列表。
    """
    try:
        # 使用集合求并集，然后转换回列表
        并集结果 = list(set(列表1) | set(列表2))
        return 并集结果
    except Exception:
        return []