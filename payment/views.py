from django.conf.urls.static import static
from .models import Student
from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Q
from django.urls import reverse
from django.shortcuts import render, redirect


def search_users(request):
    q = request.POST.get('search')
    user = Student.objects.filter(Q(name__contains=q) )
    data={'data':[]}
    global users_list_search
    global users_list_search_count
    users_list_search = [user, ]
    users_list_search_count = [user.count()]
    count = user.count() if user else 0
    for u in user:
      
        data['data'].append(
        {
            'username': u.name,
           # 'photo': str(avatar),
            'url': f'/uz/admin/payment/student/{u.id}/change/',
        })
        
    # else:
    #     users_list = {'success': 'false'}
    print(data)
    return render(request,'m.html',data)






