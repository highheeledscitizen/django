from django.shortcuts import render

# Create your views here.


def courses_page(request):
    user = request.user
    return render(request, 'courses.html', {'user': user })

