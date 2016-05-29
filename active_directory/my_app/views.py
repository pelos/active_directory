from django.shortcuts import render
from .forms import add_user_form, remove_user_form
# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect

def index(request):
    # return HttpResponse("Hello, world. You're at the my_app index.")
    context = {'my_app_key': ["this is my_app_value1", "this is my_app_value2", "this is my_app_value3"]}
    return render(request, 'my_app_template.html', context)


def add_user(request):
    if request.method == 'POST':
        form = add_user_form(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = add_user_form()


    context = {
            "message": "Add User",
            'my_app_key': ["this is my_app_value1x", "this is my_app_value2x", "this is my_app_value3x"],
            "form": form,
            }
    return render(request, 'my_app_template.html', context)













def remove_user(request):
    if request.method == 'POST':
        form = remove_user_form(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = remove_user_form()

    list_of_users =[
        "Martin Bacon",
        "Kandy Tellier",
        "Graig Liggins",
        "Edith Amy",
        "Jamika Yanes",
        "Reva Ruggerio",
        "Cary Stocks",
        "Daisy Soderman",
        "Jeannie Paolucci",
        "Kristie Screws",
        "Fernanda Toki",
        "Rebekah Clawson",
        "Owen Grossi",
        "Erlinda Soriano",
        "Yasmin Newlin",
        "Kaitlyn Trial",
        "Chantel Daw",
        "Esperanza Dominguez",
        "Mirtha Gossard",
        "Zelma Lemus",
    ]



    context = {
        "list_of_users": list_of_users,
        "message": "Remove User",
        'my_app_key': ["this is my_app_value1x", "this is my_app_value2x", "this is my_app_value3x"],
        "form": form,
        }


    return render(request, 'my_app_template.html', context)









def list_users(request):
    # return HttpResponse("Hello, world. You're at the my_app index.")
    context = {'my_app_key': ["this is my_app_value1z", "this is my_app_value2z", "this is my_app_value3z"]}
    return render(request, 'my_app_template.html', context)



def main_page(request):
    return render(request, "main_page.html")
