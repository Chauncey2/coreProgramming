from django.db import models


class BookInfoManager(models.Model):
    """
    自定义管理器类
    """

    def get_queryset(self):
        """
        读取父类原始的结果集，然后进行二次筛选
        :return: super
        """
        return super(BookInfoManager, self).get_queryset().filter(isDelete=False)

    def create_model(self, name):
        """
        在自定义管理器类当中给模型增加初始化方法
        :param name:
        :return:
        """
        book = BookInfo()
        # 属性赋值
        book.name = name
        book.readcount = 0
        book.commentcount = 0

        # 返回模型对象
        return book


# Create your models here.
class BookInfo(models.Model):
    """ 书籍信息模型类"""
    name = models.CharField(max_length=10)
    pub_date = models.DateField(null=True)  # 发布日期
    readcount = models.IntegerField(default=0)  # 阅读量
    commentcount = models.IntegerField(default=0)  # 评论量
    isDelete = models.BooleanField(default=False)  # 逻辑删除

    class Meta:
        db_table = 'bookinfo'

    books = models.Manager()

class PeopleInfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    book = models.ForeignKey('BookInfo', on_delete=models.CASCADE)
    isDelete = models.BooleanField(default=False)  # 逻辑删除

    # 元类信息 : 修改表名
    class Meta:
        db_table = 'peopleinfo'
