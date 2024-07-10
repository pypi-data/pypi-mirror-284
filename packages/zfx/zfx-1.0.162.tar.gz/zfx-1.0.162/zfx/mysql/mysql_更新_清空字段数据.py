def mysql_更新_清空字段数据(连接对象, 表名, 字段名):
    """
    清空某个表的某个字段的所有数据。

    参数：
        - 连接对象: 数据库连接对象。
        - 表名: 需要清空字段数据的表的名称。
        - 字段名: 需要清空数据的字段名称。

    返回值：
        - 更新成功返回 True，失败返回 False。
    """
    游标 = None
    try:
        # 构造完整的更新 SQL 语句，将字段值设为空字符串或 NULL
        sql = f"UPDATE {表名} SET {字段名} = '';"

        # 获取游标对象，用于执行 SQL 语句
        游标 = 连接对象.cursor()
        # 执行 SQL 语句
        游标.execute(sql)
        # 提交事务，确保更改生效
        连接对象.commit()
        return True
    except Exception:
        return False
    finally:
        # 如果游标对象存在，关闭游标，释放资源
        if 游标:
            游标.close()