from django.shortcuts import render

def admin_job(request):
    return render(request, 'admin.html', locals())
