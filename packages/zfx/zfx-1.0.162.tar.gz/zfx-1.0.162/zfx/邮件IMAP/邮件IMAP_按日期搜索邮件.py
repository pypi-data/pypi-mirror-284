def 邮件IMAP_按日期搜索邮件(连接对象, 年, 月, 日, 条件="SINCE"):
    """
    按日期搜索邮件。

    参数:
        连接对象 (IMAP4_SSL): IMAP4_SSL 连接对象。
        年 (int): 年份，例如 2024。
        月 (int): 月份，1 到 12。
        日 (int): 日期，1 到 31。
        条件 (str): 搜索条件，默认为 'SINCE'，表示搜索指定日期之后的邮件。可以为 'BEFORE' 表示搜索指定日期之前的邮件。

    返回:
        list: 包含符合搜索条件的邮件的邮件ID列表。

    示例:
        邮件ID列表 = 邮件IMAP_按日期搜索邮件(邮箱, 2024, 5, 4)
        邮件ID列表 = 邮件IMAP_按日期搜索邮件(邮箱, 2024, 5, 4, 'BEFORE')
    """
    try:
        月份名称 = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        日期 = f'{日}-{月份名称[月-1]}-{年}'
        搜索条件 = f'{条件} "{日期}"'
        状态, 邮件数据 = 连接对象.search(None, 搜索条件)
        if 状态 != "OK":
            return []
        邮件ID列表 = 邮件数据[0].split()
        return 邮件ID列表
    except Exception:
        return []