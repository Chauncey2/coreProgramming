import time
import pymysql
import re

# 路由：根据不一样的请求，不一样的函数去服务器
# key是浏览器中可能输入的url
# value是url需要调用的函数的引用
# 通过这个字典，做到了只要添加一行 key-value就完成了 对应服务的设定

url_func_dict = dict()  # 路由


def route(url):
    def set_func(func):
        url_func_dict[url] = func

    return set_func


# @route('/index.html')
def index():
    """
    打开对应的模板页
    :return: html
    """
    with open("../templates/index.html", encoding='utf-8') as f:
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
                    <input type="button" value="添加" id="toAdd" name="toAdd" systemidvaule="000007">
                </td>
            <tr>
    """
    code_html=""

    # 从数据库中读取数据
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='841211gw', database='stock_db',
                           charset='utf8')
    cursor = conn.cursor()
    sql = "SELECT * FROM info"
    cursor.execute(sql)
    data_from_mysql = cursor.fetchall()
    cursor.close()
    conn.close()
    print("数据库中的数据为：", data_from_mysql)

    for temp in data_from_mysql:
        code_html+=line_html % (temp[0],temp[1],temp[2],temp[3],
                                temp[4],temp[5],temp[6],temp[7])
    html_content = re.sub(r"\{% content %\}", code_html, html_content)

    return html_content


# @route('/center.html')
def center():
    """
    打开内容页
    :return: html page
    """
    with open("../templates/center.html", encoding="utf-8") as f:
        html_content = f.read()

    conn = pymysql.connect(host='localhost', port=3306, user='root', password='841211gw', database='stock_db',
                           charset='utf8')
    cursor = conn.cursor()
    sql = "SELECT * FROM info"
    cursor.execute(sql)
    data_from_mysql = cursor.fetchall()
    cursor.close()
    conn.close()
    print("数据库中的数据为：", data_from_mysql)
    html_content = re.sub("{% content %}", data_from_mysql, html_content)

    return html_content


@route('/register.html')
def register():
    return "-----注册页面----current time is %s" % time.ctime()


@route('/login.html')
def login():
    return "-----登陆页面----current time is %s" % time.ctime()


@route('/unregister.html')
def unregister():
    return "-----注销页面----current time is %s" % time.ctime()


def application(env, set_header):
    # 1. 调用set_header指向的函数，将response_header传递过去
    status = '200 OK'
    response_headers = [('Content-Type', 'text/html; charset=UTF-8')]
    set_header(status, response_headers)

    # 提取url
    path_info = env['PATH_INFO'].replace('.py', '.html')  # /index.py
    try:
        # url不一样，那么取出来的value，即函数的引用不一样
        func = url_func_dict[path_info]  # 如果path_info是/index.py那么也就意味着取 index函数的引用
        # 那么将来调用的时候，就调用了不一样的函数
        response_body = func()
    except Exception as ret:
        response_body = "-----not found you page-----"
    """
    if path_info == "/index.py":
        response_body = index()
    elif path_info == "/center.py":
        response_body = center() 
    elif path_info == "/register.py":
        response_body = register()
    elif path_info == "/login.py":
        response_body = login()
    else:
        response_body = "-----not found you page-----"
    """

    # 2. 通过return 将body返回
    return response_body


if __name__ == '__main__':
    print(index())
