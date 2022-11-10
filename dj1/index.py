from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators import csrf
import re
from django.contrib import messages

# 表单
def inedx_page(request):
    return render(request, 'pl_sql.html')

def function_list(request):
    request.encoding = 'utf-8'
    if request.POST:
        if 'pl_sql' in request.POST:
            return render(request, "pl_sql.html")
        elif 'function2' in request.POST:
            return render(request, "pl_sql.html")
        else :
            message = '你提交了空表单'
            return HttpResponse(message)




# 接收POST请求数据
def function_list_plsql(request):
    request.encoding = 'utf-8'
    ctx = {}

    if request.POST:
        if 'zdy_num' not in request.POST or 'input_text' not in request.POST:
            ctx['err_message']='请输入正确的参数'
            return render(request, 'pl_sql.html',ctx)
        try:
            num = int(request.POST['zdy_num'])
            if num<=0:
                ctx['err_message']='请输入正确的参数'
                return render(request, 'pl_sql.html',ctx)
        except:
            ctx['err_message'] = '请输入正确的参数'
            return render(request, 'pl_sql.html',ctx)
        input_sql = request.POST['input_text']
        pattern = re.compile(r'(\$i)([0-9]+)')
        list1 = re.findall(pattern, input_sql)
        list_len = len(list1)
        exp_sql=''
        for i in range(1,num+1):
            exp_sql = exp_sql + input_sql + '\n'
            for j in range(0, list_len):
                exp_sql=re.sub(r'(\$i)([0-9]+)',str(int(list1[j][1])+i-1),exp_sql,1)
        ctx['exp_sql'] = exp_sql
        ctx['zdy_num'] = str(num)
        ctx['input_sql'] = input_sql
    return render(request, "pl_sql.html", ctx)


# 接收请求数据
# def search(request):
#     request.encoding = 'utf-8'
#     if 'q' in request.GET and request.GET['q']:
#         message = '你搜索的内容为: ' + request.GET['q']
#     else:
#         message = '你提交了空表单'
#     return HttpResponse(message)