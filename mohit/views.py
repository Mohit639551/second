from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import userForm

def homePage(request):
    data = {
        'title': 'Home Page',
        'bdata': "welcome to mohit",
        'clist': ["PHP", "Java", "django"],
        'numbers': [10, 20, 30, 40, 50],
        'student_details': [
            {'name': 'mohit', 'phone': 8791639518},
            {'name': 'testing', 'phone': 5132122211}
        ]
    }
    return render(request, "index.html", data)

def course(request):
    return HttpResponse("<h1>Welcome to Mohit 2</h1>")

def CourseDetails(request, courseid):
    return HttpResponse(courseid)

def userfrom(request):
    finalans = 0
    fn = userForm()
    data = {'form': fn}

    try:
        if request.method == "POST":
            n1 = int(request.POST.get('num1'))
            n2 = int(request.POST.get('num2'))
            finalans = n1 + n2
            url = "/about-us/?output={}".format(finalans)
            return redirect(url)
    except:
        pass

    return render(request, "userfrom.html", data)

def aboutUs(request):
    output = request.GET.get('output')
    return HttpResponse(f"<h1>Result is: {output}</h1>")
