from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from house.models import houseintro
from house.models import User

'''登录系统界面'''


def loginSystem(request):
    if request.method == "POST":  # 当传递参数后 submit
        user_name = request.POST.get("username", None)  # 获得输入的用户名
        pass_word = request.POST.get("password", None)  # 获得输入的密码
        user = User.objects.filter(username=user_name).filter(password=pass_word)
        print(user.values('rentorsell'))
        if user.count() == 1:  # 检查用户名和密码是否为空 (注册界面通过前端js来判断)
            if user.values("rentorsell")[0]['rentorsell'] == 1:
                # rentorsell ==1 为sell
                request.session["rentorsell"] = 1
                return redirect('/sell')
            else:
                # rentorsell ==0 为rent
                request.session["rentorsell"] = 0
                return redirect('/rent')
        else:
            return HttpResponse("登录失败请检查用户名或密码")
    return render(request, 'login.html')


'''注册界面'''


def registerSystem(request):
    # 先查数据库当中是否有数据、然后没有数据后再添加
    if request.method == "POST":
        ''' 获得相关数据 '''
        user_name = request.POST.get("username", None)
        pass_word = request.POST.get("password", None)
        gender = request.POST.get("gender", None)
        rentorsell = request.POST.get("rentorsell", None)
        identify_number = request.POST.get("Id", None)
        address = request.POST.get("address", None)
        email = request.POST.get("Email", None)
        phone = request.POST.get("Phone", None)
        # 根据输入的user_name 来查询数据库有没有当前用户
        result = User.objects.filter(username=user_name).count()
        if result > 0:
            return HttpResponse("注册失败,存在该用户")
        else:
            # 写入注册信息
            try:
                User.objects.create(username=user_name,
                                    password=pass_word,
                                    rentorsell=rentorsell,
                                    gender=gender,
                                    identifyid=identify_number,
                                    address=address,
                                    email=email,
                                    phone=phone)
            except Exception as e:
                return HttpResponse('注册失败')
            return redirect('/login')

    return render(request, 'register.html')


# 下面是房屋信息的传递
def sell_gain(request):
    if request.method == "POST":
        '''获得相关数据'''
        housename = request.POST.get("mc", None)
        housetype = request.POST.get("hx", None)
        housesize = request.POST.get("pm", None)
        househighmessage1 = request.POST.get("lc", None)
        househighmessage2 = request.POST.get("lc2", None)
        houserentmoney = request.POST.get("zj", None)
        housefacility = request.POST.get("jj", None)
        houserenterphone = request.POST.get("dh", None)
        housets=request.POST.getlist('ts',None)
        img = request.FILES.get('image')
        houseintro.objects.create(house_name=housename,
                                  house_type=housetype,
                                  house_size=housesize,
                                  house_high_message1=househighmessage1,
                                  house_high_message2=househighmessage2,
                                  house_facility=housefacility,
                                  house_rent_money=houserentmoney,
                                  house_renter_phone=houserenterphone,
                                  house_ts=housets,
                                  img_url=img
                                  )
        return HttpResponseRedirect('/rent/')
    else:
        return HttpResponse('done')


'''主页面'''


def mainPageSystem(request):
    return render(request, 'main.html')


'''跳转界面函数'''


def sell(request):
    return render(request, 'sell.html')


def rent(request):
    if request.method=="GET":
        screen = request.GET.get('screen', None)
        if screen:
            house_list = houseintro.objects.filter(house_ts__contains=screen)
            return render(request, 'rent.html', {'house_list': house_list})
        else:
            house_list = houseintro.objects.all()
            return render(request, 'rent.html',{'house_list': house_list})
    if request.method=="POST":
        search = request.POST.get('search', None)
        if search:
            house_list = houseintro.objects.filter(house_name__contains=search)
            return render(request, 'rent.html', {'house_list': house_list})
        else:
            house_list = houseintro.objects.all()
            return render(request, 'rent.html', {'house_list': house_list})


def analyze(request):
    return render(request, 'sell.html')


def registers(request):
    return render(request, 'register.html')

# def search(request):
#         search=request.GET.get('search')
#         error_msg=''
#         if search:
#             error_msg = '查找成功'
#             search_done = houseintro.objects.filter(house_name__contains=search)#模糊查询 contains
#             return render(request, 'result.html', {'error_msg2': error_msg,
#                                                    'search_done': search_done
#                                                    })
#
#         else:
#             error_msg2 = '请输入正确关键词'
#             return render(request, 'error.html', {'error_msg': error_msg2})
#
#
#
# def screen(request):
#     if request.method == "GET":
#         screen=request.GET.get('screen')
#         print(screen)
#         if screen:
#             screen_done1=houseintro.objects.filter(house_ts__contains=screen)
#             print(screen_done1)
#             return render(request,'result.html',{'screen_done1':screen_done1})
#         else:
#             return render(request,'result.html')
#     else:
#         return render(request, 'result.html')