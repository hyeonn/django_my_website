from django.db import models
from django.utils.timezone import now
from ckeditor.fields import RichTextField

class Board(models.Model):
    name = models.CharField(max_length=50,null=False,verbose_name="게시판 이름")
    description = models.TextField(null=True,verbose_name="게시판 설명")
    category = models.CharField(max_length=30,null=False,verbose_name="카테고리")

    def __str__(self):
        return '{}'.format(self.name)

class Post(models.Model):
    Board_id = models.ForeignKey(Board,null=False,on_delete=models.CASCADE,verbose_name="게시판")
    title = models.CharField(max_length=70,null=False,default="Untitled",verbose_name="게시물 제목")
    content = RichTextField(verbose_name="게시물 내용")
    note = models.TextField(blank=True,null=True,verbose_name="참조")
    date = models.DateTimeField(auto_now_add=True,verbose_name="게사물 작성일")
    delete = models.BooleanField(default=False,verbose_name="삭제여부")
    likes = models.IntegerField(default=0,verbose_name="공감")
    views = models.IntegerField(null=False,default=1,verbose_name="조회수")

    def __str__(self):
        return '{}'.format(self.title)

class Project(models.Model):
    title = models.CharField(max_length=70,null=False,default="프로젝트 이름을 적어주세요",verbose_name="프로젝트 제목")
    content = RichTextField(verbose_name="게시물 내용")
    note = models.TextField(null=True,blank=True,verbose_name="참조")
    date = models.DateTimeField(null=False,default=now,verbose_name="프로젝트 작성일")
    projectStart = models.DateTimeField(null=False, default=now, verbose_name="프로젝트 시작일")
    projectEnd = models.DateTimeField(null=False, default=now, verbose_name="프로젝트 종료일")
    likes = models.IntegerField(default=0,verbose_name="공감")
    views = models.IntegerField(null=False,default=1,verbose_name="조회수")

    def __str__(self):
        return '{}'.format(self.title)

class VisitorsBook(models.Model):
    writer = models.CharField(max_length=30, null=False,verbose_name="방명록 작성자")
    writer_id = models.IntegerField(null=False,verbose_name="작성자 식별자")
    content = models.TextField(null=False,verbose_name="방명록 내용")
    canSee = models.BooleanField(default=True,verbose_name="공개여부")
    password = models.IntegerField(null=True,verbose_name="비밀번호")
    date = models.DateTimeField(null=False, default=now,verbose_name="작성일")

class Comment(models.Model):
    Post_num = models.ForeignKey(Post,null=False,on_delete=models.CASCADE,verbose_name="게시물")
    writer = models.CharField(max_length=30,null=False,verbose_name="댓글 작성자")
    writer_id = models.IntegerField(null=False,verbose_name="작성자 식별자")
    content = models.TextField(null=False,verbose_name="댓글 내용")
    canSee = models.BooleanField(default=True,verbose_name="공개여부")
    delete = models.BooleanField(default=False,verbose_name="삭제여부")
    password = models.IntegerField(null=True,verbose_name="비밀번호")
    date = models.DateTimeField(null=False,default=now,verbose_name="작성일")
    #Comment_num = models.ForeignKey('self', null=True, on_delete=models.CASCADE,verbose_name="댓글 답글 대상")
    # 댓글 답글일경우 어떤 댓글인지 대상을 저장
    #VB_num = models.ForeignKey(VisitorsBook,null=True, on_delete=models.CASCADE,verbose_name="방명록 답글 대상")
    # 방명록 답글일경우 어떤 방명록인지 대상을 저장

"""
class Recomment(models.Model):
    number = models.IntegerField()
    Post_num = models.IntegerField()
    Board_id = models.IntegerField()
    writer = models.CharField(max_length=30)
    writer_id = models.IntegerField()
    content = models.TextField()
    canSee = models.BooleanField()
    delete = models.BooleanField()
    password = models.IntegerField()
    date = models.DateTimeField()
"""

