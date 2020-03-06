from django.shortcuts import render
from Book.models import BookInfo,PeopleInfo

# Create your views here.
def testProject(request):
    context = {'text': '测试数据'}
    return render(request, 'Book/testProject.html', context)

# 获取书籍信息的视图
def bookList(request):
    # 查询书籍列表信息：bookList内部包含了两个BookInfo对象
    bookList = BookInfo.objects.all()
    # 构造上下文
    context = {'bookList':bookList}

    # 调出模板，传递上下文给模板，返回经过动态渲染的网页给客户端
    return render(request, 'Book/bookList.html', context)

# 获取对应的书籍里面人物信息的视图
def peopleList(request, book_id):
    # 查询出客户端点击的是哪本书
    book = BookInfo.objects.get(id=book_id)
    # 以点击的那本书作为外键，查询书籍对应的人物信息
    peopleList = book.peopleinfo_set.all()

    # 构造上下文
    context = {'peopleList':peopleList}

    # 调出模板　
    return render(request, 'Book/peopleList.html', context)
