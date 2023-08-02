from django.shortcuts import render

# Create your views here.
d={'a':5,'b':2,'hobbies':['cricket','volleyball']}
def jinja(request):
    return render(request,'jinja.html',context=d)



def python(request):
    return render(request,'python.html',context=d)