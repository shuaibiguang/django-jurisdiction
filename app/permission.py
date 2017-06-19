from django.shortcuts import render
# from . import models
from app.models import Permission
from django.db.models import Q
from django.core.urlresolvers import resolve #此方法吧URL地址转换成urlname

def perm_check(request, *args, **kwargs):
    url_obj = resolve(request.path_info)
    url_name = url_obj.url_name
    # if url_name == "home":
    #     return True
    print (url_name)
    perm_name = ''
    # 权限必须和urlname配合
    if url_name:
        # 获取请求方法和请求参数
        url_method = 1 if request.method == "GET" else 2
        # 操作数据库
        get_prem = Permission.objects.filter(url = url_name).filter(per_method = url_method)
        if get_prem:
            for i in get_prem:
                perm_name = i.name
                perm_str = 'app.%s' % perm_name
                print (perm_str)
                if request.user.has_perm(perm_str):
                    print ('===>权限匹配')
                    return True
            else:
                print ('------>权限没有匹配')
                return False
        else:
            return False
    else:
        return True 

# 定义一个装饰器 ， 在views中使用
def check_permission(fun):
    def wapper(request, *args, **kwargs):
        if perm_check(request, *args, **kwargs):
            return fun(request, *args, **kwargs)
        return render(request,'403.html', locals())
    return wapper