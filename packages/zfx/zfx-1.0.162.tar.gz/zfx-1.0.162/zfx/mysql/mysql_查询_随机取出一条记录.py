import random


def mysql_查询_随机取出一条记录(连接对象, 表名):
    """
    从 MySQL 表中随机取出一条记录。

    参数：
        - 连接对象: 数据库连接对象。
        - 表名: 需要查询的表的名称。

    返回值：
        - 随机取出的记录（元组形式），如果查询失败返回 None。
    """
    游标 = None
    try:
        # 获取游标对象，用于执行 SQL 查询
        游标 = 连接对象.cursor()
        # 获取表中的记录总数
        游标.execute(f"SELECT COUNT(*) FROM {表名};")
        总记录数 = 游标.fetchone()[0]

        if 总记录数 == 0:
            return None

        # 随机生成一个记录的偏移量
        随机偏移量 = random.randint(0, 总记录数 - 1)

        # 根据随机偏移量取出一条记录
        游标.execute(f"SELECT * FROM {表名} LIMIT 1 OFFSET {随机偏移量};")
        记录 = 游标.fetchone()

        return 记录
    except Exception:
        return None
    finally:
        # 如果游标对象存在，关闭游标，释放资源
        if 游标:
            游标.close()