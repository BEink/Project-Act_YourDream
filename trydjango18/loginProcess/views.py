from django.shortcuts import render
from . forms import SignUpForm
from .models import SignUp


def home(request):
    title = "My Title"
    form = SignUpForm(request.POST,request.FILES)
    context = {
        "template_title":title,
        "form": form
    }
    password = SignUp.objects.all()
    # print(type(email))
    #
    for i in password:
        print(i)

    #full_name = request.POST.getlist('full_name')


    #print(form.fields.values())

    if form.is_valid():
        # form.save()
        instance = form.save(commit = False)
        instance.save()
        context["template_title"] = "WELCOME" + "  " + instance.full_name

    return render(request,"home.html",context)