def 列表_去除重复(列表):
    """
    去除列表中的重复元素，并返回去重后的新列表。

    参数:
        - 列表 (list): 包含元素的列表，可以是数字，字符串

    返回:
        - 去重后的新列表 (list): 去除重复元素后的列表。如果处理过程中发生异常，则返回错误信息。
    """
    try:
        # 使用 set 去除重复元素，并将结果转换回列表
        去重后的新列表 = list(set(列表))
        return 去重后的新列表
    except Exception as e:
        # 捕获所有异常并返回错误信息
        return f"处理失败: {e}"