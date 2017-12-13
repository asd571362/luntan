from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from .models import UserInfo, QuestionInfo, AnswerInfo
import re,hashlib


#是否登陆
def is_login(request,temPath):
    username = request.session.get('username')
    if username:
        context = {'username': username}
        return render(request, temPath, context)
    return render(request, temPath)

#首页页面
def index(request):
    temPath = 'apps/index.html'
    username = request.session.get('username')
    questions = QuestionInfo.objects.all()

    if username:
        context = {'username': username,
                   'questions':questions}
    else:
        context = {'questions': questions}

    return render(request, temPath, context)


#注册页面
def register(request):
    temPath = 'apps/register.html'
    username = request.session.get('username')
    if username:
        context = {'username': username}
        return render(request, temPath, context)
    return render(request, temPath)


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


# 登陆验证
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

    if post_type:  #ajax 验证
        if len(users) == 1:
            if users[0].user_pwd == sha1_pwd:
                request.session['username'] = users[0].user_name
                request.session.set_expiry(3*24*3600)
                return JsonResponse({'log_vf': True})
        else:
            return JsonResponse({'log_vf':False})
    else: #非正常提交，返回首页
        render(request,'apps/index.html')

# 退出登陆
def logout(request):
    request.session.clear()
    return HttpResponseRedirect('/')

# 提问页面
def ask(request):
    temPath = 'apps/ask.html'
    ret = is_login(request,temPath)
    return ret

# 问题提交
def ask_post(request):
    dict = request.POST
    uername = request.session.get('username')
    print(uername)
    if uername:
        user = UserInfo.objects.get(user_name=uername)
        print(user)
        question = QuestionInfo()
        question.q_title= dict.get('q_title')
        question.q_content = dict.get('q_content')
        question.q_user = user
        question.save()
        context={'tip':'发布成功！'}

    else:
        context = {'tip': '您未登陆,请先登陆！'}

    return render(request, 'apps/q_post_re.html', context)

# 问题详情页面
def question(request,q_id):
    q = QuestionInfo.objects.get(id=q_id)
    username = request.session.get('username')
    if q:
        answers = q.answerinfo_set.all()
        context = {
            'q_username':q.q_user.user_name,
            'q_title':q.q_title,
            'q_content':q.q_content,
            'answers':answers,
            'q_id':q_id,
            'username':username
        }
        return render(request,'apps/question.html',context)
    else:
        context = {'tip':'问题不存在！'}
        return render(request,'apps/q_post_re.html',context)

# 回答提交
def answer_post(request):
    dict = request.POST
    uername = request.session.get('username')
    q_id = dict.get('q_id')
    print(q_id)
    q = QuestionInfo.objects.get(id=q_id)

    if uername:
        user = UserInfo.objects.get(user_name=uername)
        answer = AnswerInfo()
        answer.a_content = dict.get('a_content')
        answer.a_user = user
        answer.a_question = q

        answer.save()
        # context={'tip':'发布成功！'}
        return HttpResponseRedirect('/question/%s' % q_id)
    else:
        context = {'tip': '您未登陆,请先登陆！'}
        return render(request, 'apps/q_post_re.html', context)

# 搜索功能
def search(request):
    dict = request.GET
    kw = dict.get('kw')
    if kw:
        questions = QuestionInfo.objects.filter(q_title__contains=kw)
        username = request.session.get('username')
        if username:
            context = {'username': username,
                       'questions': questions}
        else:
            context = {'questions': questions}

        return render(request, 'apps/index.html', context)

    return HttpResponseRedirect('/')

# test页面
def setcook(request):
    return