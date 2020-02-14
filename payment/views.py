from django.conf.urls.static import static
from .models import Student, Teacher, Contract
from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Q, Sum, F
from django.urls import reverse
from django.shortcuts import render, redirect


def search_users(request):
    q = request.POST.get('search')
    user = Student.objects.filter(Q(name__icontains=q) )[:5]
    data={'data':[]}
    
    for u in user:
      
        data['data'].append(
        {
            'username': u.name,
            'url': f'/uz/admin/payment/student/{u.id}/change/',
        })
        
    # else:
    #     users_list = {'success': 'false'}
    print(data)
    return render(request,'m.html',data)


def debt(request):
    if request.method=="POST":
        teacher = Teacher.objects.get(id=request.POST.get('teacher'))
        time = request.POST.get('time')
        parity = request.POST.get('parity')
        data = Contract.objects.filter(teacher=teacher, group_time=time, parity=parity).annotate(debt=Sum(F('payments__has_to_pay')-F('payments__paid'))).filter(debt__gt=0)
        return render(request, 'print.html',{ 'data':data})
    teachers  = Teacher.objects.all()
    TIMES = [f'{t}.00' for t in range(6, 24)]
    return render(request,'debt.html',{'teachers':teachers, 'times':TIMES})






