from django.urls import path
from Book.views import testProject,bookList,peopleList

urlpatterns = [
    path('test_project/', testProject),
    path('booklist/', bookList),
    # 匹配人物信息
    # path(r'^(\d+)/$', peopleList),
]
