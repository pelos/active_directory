from django.shortcuts import render
from .forms import add_user_form, remove_user_form
# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import User, Emails, Phones

def index(request):
    # return HttpResponse("Hello, world. You're at the my_app index.")
    context = {'my_app_key': ["this is my_app_value1", "this is my_app_value2", "this is my_app_value3"]}
    return render(request, 'my_app_template.html', context)


def add_user(request):
    if request.method == 'POST':
        form = add_user_form(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            last_name = form.cleaned_data['last_name']
            email1 = form.cleaned_data['email1']
            email2 = form.cleaned_data['email2']
            phone1 = form.cleaned_data['phone1']
            phone2 = form.cleaned_data['phone2']
            user_name = name+"_"+last_name

            # if the user_name already exists
            user_name_q = User.objects.filter(user_name=user_name)
            if len(user_name_q) == 0:

                user_model = User(name=name, last_name=last_name, user_name=user_name)
                user_model.save()
                emails_model = Emails(user_name=user_model, email1=email1, email2=email2)
                emails_model.save()
                phones_model = Phones(user_name=user_model, phone1=phone1, phone2=phone2)
                phones_model.save()

                form = add_user_form()
                context = {
                    "page_redirect": "/my_app/add_user/",
                    "message": "User " + user_name + " has been added to the database",
                    "form": form,
                    }
                return render(request, 'my_app_template.html', context)
                # return HttpResponseRedirect('/my_app/add_user/')
            else:
                form = add_user_form()
                context = {
                    "page_redirect": "/my_app/add_user/",
                    "message": "User " + user_name + " already exists database",
                    "form": form,
                }
                return render(request, 'my_app_template.html', context)

    else:
        form = add_user_form()


    context = {
            "page_redirect": "/my_app/add_user/",
            "message": "Add User Email2 and Phone2 can be leave blank",
            "form": form,
            }
    return render(request, 'my_app_template.html', context)


def remove_user(request):
    all_users = User.objects.all()
    list_of_users = []
    for i in all_users:
        list_of_users.append(i.user_name)

    if request.method == 'POST':
        form = remove_user_form(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['user_name']
            try:
                message = "User " + user_name + " has been Remove from the database"
                user_name_q = User.objects.get(user_name=user_name)
                user_name_q.delete()
            except:
                message = "User " + user_name + " was not found in the database, no action perform"

            form = remove_user_form()
            context = {
                "list_of_users": list_of_users,
                "page_redirect": "/my_app/remove_user/",
                "message": message,
                "form": form,
            }
            return render(request, 'my_app_template.html', context)
            #return HttpResponseRedirect('/my_app/remove_user/')
    else:
        form = remove_user_form()

    context = {
        "list_of_users": list_of_users,
        "page_redirect": "/my_app/remove_user/",
        "message": "Remove User",
        "form": form,
        }

    return render(request, 'my_app_template.html', context)














def list_users(request):
    all_users = User.objects.all()
    list_of_users = []
    for i in all_users:
        list_of_users.append(i.user_name)

    context = {
        "list_of_users": list_of_users,
        "page_redirect": "/my_app/list_users/",
        "message": "Remove User",
        }

    return render(request, 'my_app_template_list.html', context)


def run_delete(request, user_del):
    print(1)
    print(user_del)
    print(2)
    return HttpResponseRedirect('/my_app/blablabla/')







def main_page(request):
    return render(request, "main_page.html")
