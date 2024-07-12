def mysql_查询_表结构(连接对象, 表名):
    """
    导出指定表的结构信息：字段名、数据类型、长度、是否允许为 NULL 等，获得的 表结构信息 可直接用于创建表单。

    参数：
        - 连接对象：MySQL 数据库连接对象。
        - 表名：要导出结构的表名。

    返回值：
        - 表结构信息：反悔了一个列表，包含每个字段的元组 (字段名, 数据类型, 长度, 是否允许为 NULL)。
          如果获取结构失败，返回空列表。
    """
    字段信息列表 = []

    try:
        # 查询表结构信息
        查询语句 = f"SELECT COLUMN_NAME, COLUMN_TYPE, CHARACTER_MAXIMUM_LENGTH, IS_NULLABLE " \
                   f"FROM information_schema.COLUMNS " \
                   f"WHERE TABLE_SCHEMA = '{连接对象.database}' AND TABLE_NAME = '{表名}'"

        cursor = 连接对象.cursor()
        cursor.execute(查询语句)

        # 获取所有字段信息
        结果 = cursor.fetchall()

        # 遍历每个字段的信息
        for row in 结果:
            字段名 = row[0]
            数据类型 = row[1]
            长度 = row[2]
            是否允许为空 = row[3]

            # 将字段信息添加到列表中
            字段信息列表.append((字段名, 数据类型, 长度, 是否允许为空))

        return 字段信息列表

    except Exception:
        return []