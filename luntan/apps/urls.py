from django.conf.urls import url
from apps import views

urlpatterns = [

    # 首页部分
    url(r'^$', views.index),
    url(r'^index/$', views.index,name='index'),

    #注册 部分
    url(r'^register/$', views.register,name='register'),
    url(r'^register/register_post/$', views.register_post,name='register_post'),

    #登陆 部分
    url(r'^register/uname_re_vf/$', views.uname_re_vf,name='uname_re_vf'),
    url(r'^register/login_post/$', views.login_post,name='login_post'),

    #退出登陆
    url(r'^logout$', views.logout,name='logout'),

    # 提问 部分
    url(r'^ask/$', views.ask,name='ask'),
    url(r'^ask/ask_post$', views.ask_post,name='ask_post'),

    #问题详情 部分
    url(r'^question/(\d+)$', views.question,name='question'),

    #问题回复 部分
    url(r'^question/answer_post$', views.answer_post,name='answer_post'),

    #问题回复 部分
    url(r'^search$', views.search,name='search'),

    #test 部分
    url(r'^setcook$', views.setcook),
]
