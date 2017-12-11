from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from .models import UserInfo, QuestionInfo, AnswerInfo
import re,hashlib

# Create your views here.
def index(request):
    return render(request, 'apps/index.html')

def register(request):
    return render(request,'apps/register.html')

# 重名检测
def uname_re_vf(request):
    dict = request.POST
    # print(type(dict))
    # nlength = 1
    nlength = len(UserInfo.objects.filter(user_name=dict.get('post_name')))
    # print(eval(JsonResponse({'nlength':nlength}).content))
    return JsonResponse({'nlength':nlength})

# 注册验证
def register_post(request):
    dict = request.POST
    post_name = dict.get('re_usename')
    post_pwd = dict.get('re_pwd')
    print(post_name)

    # 用户名密码格式验证
    uName_rgx = '^[a-zA-Z]\w{7,19}$'
    upwd_rgx = '^[a-zA-Z]\w{5,19}$'
    uName_vf = re.match(uName_rgx,post_name)
    upwd_vf = re.match(upwd_rgx,post_pwd)

    # 重名检测
    re_name = eval(uname_re_vf(request).content)['nlength']
    reName = int(re_name)

    #储存用户名和密码
    if uName_vf and upwd_vf and (not reName):

        #密码加密
        post_pwd = post_pwd.encode()
        sha1 = hashlib.sha1()
        sha1.update(post_pwd)
        sha1_pwd = sha1.hexdigest()

        print(len(sha1_pwd))
        # 储存用户名和密码
        user = UserInfo()
        user.user_name = post_name
        user.user_pwd = sha1_pwd
        user.save()
        return HttpResponseRedirect('/register')

    else:
        return HttpResponse('数据错误')

def login_post(request):
    post = request.POST

    post_name = post.get('post_name')
    post_pwd = post.get('post_pwd')
    post_type = post.get('post_type')
    print(post_name)
    print(post_pwd)
    # 密码加密
    post_pwd = post_pwd.encode()
    sha1 = hashlib.sha1()
    sha1.update(post_pwd)
    sha1_pwd = sha1.hexdigest()

    # 核对用户名和密码
    users = UserInfo.objects.filter(user_name=post_name)
    print(sha1_pwd)
    print(users)

    if post_type:
        if len(users) == 1:
            if users[0].user_pwd == sha1_pwd:
                return JsonResponse({'log_vf': True})
        else:
            return JsonResponse({'log_vf':False})
    else:
        render(request,'apps/index.html')


def ask(request):
    return render(request, 'apps/ask.html')