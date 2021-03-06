import time
import pymysql
import re
import urllib.parse
import logging

logging.basicConfig(level=logging.DEBUG,
                    filename='./log.txt',
                    filemode='a',
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

url_func_dict = dict()  # 路由


def route(url):
    """
    路由函数，返回函数对象
    :param url:
    :return:
    """

    def set_func(func):
        url_func_dict[url] = func

    return set_func


@route(r'/index\.html')
def index(res):
    """
    打开对应的模板页
    :return: html
    """
    with open("./templates/index.html", encoding='utf-8') as f:
        html_content = f.read()

    # 将mysql查询出来的数据替换到模板中
    line_html = """
            <tr>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>
                    <input type="button" value="添加" id="toAdd" name="toAdd" systemidvaule="%s">
                </td>
            <tr>
    """
    code_html = ""

    # 从数据库中读取数据
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='841211gw', database='stock_db',
                           charset='utf8')
    cursor = conn.cursor()
    sql = "SELECT * FROM info"
    cursor.execute(sql)
    data_from_mysql = cursor.fetchall()
    cursor.close()
    conn.close()

    for temp in data_from_mysql:
        code_html += line_html % (temp[0], temp[1], temp[2], temp[3],
                                  temp[4], temp[5], temp[6], temp[7], temp[1])
    html_content = re.sub(r"{% content %}", code_html, html_content)

    return html_content


@route(r'/center\.html')
def center(res):
    """
    打开内容页
    :return: html page
    """
    with open("./templates/center.html", encoding="utf-8") as f:
        html_content = f.read()

    conn = pymysql.connect(host='localhost', port=3306, user='root', password='841211gw', database='stock_db',
                           charset='utf8')
    cursor = conn.cursor()
    sql = """select i.code,i.short,i.chg,i.turnover,i.price,i.highs,f.note_info from info as i 
    inner join focus as f on i.id=f.info_id;"""
    cursor.execute(sql)
    data_from_mysql = cursor.fetchall()
    cursor.close()
    conn.close()
    # 这是一行的模板
    line_html = """<tr>
                           <td>%s</td>
                           <td>%s</td>
                           <td>%s</td>
                           <td>%s</td>
                           <td>%s</td>
                           <td>%s</td>
                           <td>%s</td>
                           <td>
                           <a type="button" class="btn btn-default btn-xs" href="/update/%s.html"> <span class="glyphicon glyphicon-star" aria-hidden="true"></span> 修改 </a>
                           </td>
                           <td>
                           <input type="button" value="删除" id="toDel" name="toDel" systemidvaule="%s">
                           </td>
                       </tr>
                   """

    code_html = ""
    for temp in data_from_mysql:
        code_html += line_html % (temp[0], temp[1], temp[2], temp[3], temp[4], temp[5], temp[6], temp[0], temp[0])

    # 3. 替换数据
    html_content = re.sub(r"{% content %}", code_html, html_content)
    return html_content


@route(r'/register\.html')
def register(res):
    return "-----注册页面----current time is %s" % time.ctime()


@route(r'/login\.html')
def login(res):
    return "-----登陆页面----current time is %s" % time.ctime()


@route(r'/unregister\.html')
def unregister(res):
    return "-----注销页面----current time is %s" % time.ctime()


@route(r'^/add/(\d+)\.html$')
def add_focus(res):
    # 1、获取股票代码参数
    stock_code = res.group(1)
    print("股票代码", stock_code)

    # 2. 判断是否有这个股票
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='841211gw', database='stock_db',
                           charset='utf8')
    cursor = conn.cursor()  # 获取游标
    sql = """ select * from info where code=%s; """
    cursor.execute(sql, [stock_code])
    data_from_mysql = cursor.fetchall()
    if not data_from_mysql:
        cursor.close()
        conn.close()
        return '查询无果'
    # 3. 判断是否之前关注过这个股票
    sql = """ select * from info as i inner join focus as f on i.id=f.info_id where i.code=%s; """
    cursor.execute(sql, [stock_code])
    data_from_mysql = cursor.fetchall()
    if data_from_mysql:
        # 如果要是关注过这个股票，那么就退出
        cursor.close()
        conn.close()
        return "请误重复关注...."

    # 4.写入数据库
    sql = """ insert into focus (info_id) select id from info where code=%s; """
    cursor.execute(sql, [stock_code])
    conn.commit()
    cursor.close()
    conn.close()

    return "-----添加关注成功----"


@route(r'^/del/(\d+)\.html$')
def del_focus(res):
    # 1.获取股票代码参数
    stock_code = res.group(1)
    print("待删除股票代码：", stock_code)
    # 2.检验股票代码是否存在
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='841211gw', database='stock_db',
                           charset='utf8')
    cursor = conn.cursor()
    sql = """ select * from info where code=%s; """
    cursor.execute(sql, [stock_code])
    data_from_mysql = cursor.fetchall()

    if not data_from_mysql:
        cursor.close()
        conn.close()
        return '查无数据'

    # 3.判断是关注过这个股票
    sql = """ select * from info as i inner join focus as f on i.id=f.info_id where i.code=%s; """
    cursor.execute(sql, [stock_code])
    data_from_mysql = cursor.fetchall()

    if not data_from_mysql:
        cursor.close()
        conn.close()
        return '没有关注过这个股票...'

    # 4.删除股票
    sql = """delete from focus where info_id = (select id from info where code=%s);"""
    cursor.execute(sql, [stock_code])
    conn.commit()
    cursor.close()
    conn.close()
    return "取消关注成功"


@route(r'^/update/(\d+)\.html$')
def show_edit_page(ret):
    # 1.接收股票代码
    stock_code = ret.group(1)
    # 2.读取更新页原始页面
    with open('./templates/update.html', 'r', encoding='utf-8') as f:
        html = f.read()
    # 3.填充页面
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='841211gw', database='stock_db',
                           charset='utf8')
    cursor = conn.cursor()
    sql = """select note_info from focus where info_id=(select id from info where code=%s);"""
    cursor.execute(sql, [stock_code])
    data_from_mysql = cursor.fetchone()
    cursor.close()
    conn.close()
    # 4.合并数据
    html = re.sub(r"\{% note_info %\}", data_from_mysql[0], html)
    html = re.sub(r"\{% code %\}", stock_code, html)

    return html


@route(r"/update/(\d+)/(.*)\.html")
def save_edit_message(ret):
    # 1，接收信息
    stock_code = ret.group(1)  # 股票代码
    note_info = urllib.parse.unquote(ret.group(2))  # 备注
    # 2，更新数据库
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='841211gw', database='stock_db',
                           charset='utf8')
    cursor = conn.cursor()
    sql = """update focus as f inner join info as i on i.id=f.info_id set f.note_info=%s where i.code=%s;"""
    cursor.execute(sql, [note_info, stock_code])
    conn.commit()
    cursor.close()
    conn.close()

    return '修改备注成功'


def application(env, set_header):
    # 1. 调用set_header指向的函数，将response_header传递过去
    status = '200 OK'
    response_headers = [('Content-Type', 'text/html; charset=UTF-8')]
    set_header(status, response_headers)

    # 提取url
    response_body = '页面加载中...'
    path_info = env['PATH_INFO']
    logging.info("用户访问了url: %s" % path_info)

    try:
        for r_url, func in url_func_dict.items():
            ret = re.match(r_url, path_info)
            if ret:
                response_body = func(ret)
    except Exception as ret:
        response_body = "-----not found you page-----"
        logging.warning("没有对应的url....")
    # 2. 通过return 将body返回
    return response_body


if __name__ == '__main__':
    pass
