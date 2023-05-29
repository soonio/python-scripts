# 导入所需的库
import os
import pymysql
import pandas as pd
import click


@click.command()
@click.option('--env', prompt='选择环境', help='选择使用那个环境变量配置')
@click.option('--db', prompt='选择数据库', help='选择对应的数据库')
@click.option('--table', prompt='选择数据表', help='选择对应的数据表')
def run(env, db, table):

    SQL = """SELECT column_name, COLUMN_TYPE, column_comment
    FROM information_schema.columns
    WHERE table_schema = '{db}'
    AND table_name = '{table}'
    ORDER BY ORDINAL_POSITION;
    """

    # 创建数据库连接
    connection = pymysql.connect(
        host=os.environ.get('{env}_HOST'.format(env=env)),
        user=os.environ.get('{env}_USER'.format(env=env)),
        port=int(os.environ.get('{env}_PORT'.format(env=env))),
        password=os.environ.get('{env}_PASSWORD'.format(env=env)),
        charset='utf8'
    )

    cursor = connection.cursor()
    cursor.execute(SQL.format(db=db, table=table))
    table_schema = cursor.fetchall()
    cursor.close()

    pd.set_option('display.unicode.ambiguous_as_wide', True)
    pd.set_option('display.unicode.east_asian_width', True)
    # pd.set_option("display.colheader_justify", "left")
    pd.set_option("styler.latex.multicol_align", "l")
    df = pd.DataFrame(table_schema, columns=[
                      col for col in ['列名', '类型', '评论']])
    print(df)


if __name__ == '__main__':
    run()
