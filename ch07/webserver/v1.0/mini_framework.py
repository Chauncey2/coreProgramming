import time


def index():
    return "----主页---current time is %s" % time.ctime()


def center():
    html_content = """"<!DOCTYPE html>
        <html lang="zh-CN">
        <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>个人中心 - 个人选股系统 V5.87</title>
        <link href="/css/bootstrap.min.css" rel="stylesheet">
        </head>
        <body>
        <div class="navbar navbar-inverse navbar-static-top ">
        <div class="container">
        <div class="navbar-header">
        <button class="navbar-toggle" data-toggle="collapse" data-target="#mymenu">
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        </button>
        <a href="#" class="navbar-brand">选股系统</a>
        </div>
        <div class="collapse navbar-collapse" id="mymenu">
        <ul class="nav navbar-nav">
        <li ><a href="/index.py">股票信息</a></li>
        <li class="active"><a href="/center.py">个人中心</a></li>
        </ul>

        </div>
        </div>
        </div>
        <div class="container">

        <div class="container-fluid">

        <table class="table table-hover">
        <tr>
        <th>股票代码</th>
        <th>股票简称</th>
        <th>涨跌幅</th>
        <th>换手率</th>
        <th>最新价(元)</th>
        <th>前期高点</th>
        <th style="color:red">备注信息</th>
        <th>修改备注</th>
        <th>del</th>
        </tr>
        {%content%}                     
        </table>
        </div>
        </div>
        <script src="/js/bootstrap.min.js"></script>
        </body>
        </html>
        """
    return html_content


def register():
    return "------注册页面-----current time is %s" % time.ctime()


def application(env, set_header):
    status = '200 ok'
    response_headers = [('Content-Type', 'text/html; charset=UTF-8')]
    set_header(status, response_headers)

    # 提取url
    path_info = env['PATH_INFO']
    if path_info == "/index.py":
        response_body = index()
    elif path_info == "/center.py":
        response_body = center()
    elif path_info == "/register.py":
        response_body = register()
    else:
        response_body = "-----not found you page-----"
    return response_body
