from django.db import models
from time import time

# Create your models here.
class UserInfo(models.Model):
    user_name = models.CharField(max_length=20)
    user_pwd = models.CharField(max_length=20)
    # reg_date = models.DateTimeField(default=time.datetime)
    user_email = models.CharField(max_length=50, default='')
    nickname = models.CharField(max_length=20, default='')
    user_avatar = models.ImageField(upload_to="", default='')


class QuestionInfo(models.Model):
    q_title = models.CharField(max_length=20)
    q_content = models.CharField(max_length=500)
    # q_date = models.DateTimeField(default=timezone.now)
    q_user = models.ForeignKey(UserInfo)

class AnswerInfo(models.Model):
    a_content = models.CharField(max_length=1500)
    # a_date = models.DateTimeField(default=timezone.now)
    a_question = models.ForeignKey(QuestionInfo)
    a_user = models.ForeignKey(UserInfo)

