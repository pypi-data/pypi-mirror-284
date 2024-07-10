def 文本文件_取关键词出现次数(文件名, 关键词):
    """
    从指定的文本文件中获取特定关键词的出现次数。

    参数:
        文件名 (str): 要读取的文本文件的文件名。
        关键词 (str): 要查找并计数出现次数的关键词。

    返回值:
        int: 关键词在文件中出现的总次数。如果文件无法打开或处理出现错误，则返回 None。

    异常:
        如果文件无法打开或处理出现错误，将捕获异常并打印错误消息，然后返回 None。
    """
    try:
        出现次数 = 0
        with open(文件名, 'r', encoding='utf-8') as 文件:
            for 行 in 文件:
                出现次数 += 行.count(关键词)
        return 出现次数
    except Exception:
        return None