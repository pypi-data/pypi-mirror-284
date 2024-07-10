def 列表_按元素数量分组(列表, 组大小):
    """
    将列表按指定大小分组。

    参数:
        - 列表 (list): 要分组的列表。
        - 组大小 (int): 每个组的大小。

    返回:
        - list: 包含分组后的子列表的列表。如果出现异常，返回空列表。
    """
    try:
        # 使用列表推导式和切片进行分组
        分组结果 = [列表[i:i + 组大小] for i in range(0, len(列表), 组大小)]
        return 分组结果
    except Exception:
        return []