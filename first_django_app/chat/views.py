from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import Chat, Message
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.core import serializers
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


@login_required(login_url="/login/")

# index view
def index(request):
    """
    This is a view to render the chat html.
    :param request: Request ofject with several infos os the request.
    """
    if request.method == "POST":
        print("Received data " + request.POST["textmessage"])
        myChat = Chat.objects.get(id=1)
        new_message = Message.objects.create(
            text=request.POST["textmessage"],
            chat=myChat,
            author=request.user,
            receiver=request.user,
        )
        serialized_obj = serializers.serialize(
            "json",
            [
                new_message,
            ],
        )
        return JsonResponse(serialized_obj[1:-1], safe=False)
    chatMessages = Message.objects.filter(chat__id=1)
    return render(request, "chat/index.html", {"messages": chatMessages})


# login view
def login_view(request):
    redirect = request.GET.get("next")
    if request.method == "POST":
        user = authenticate(
            username=request.POST.get("username"), password=request.POST.get("password")
        )

        if user:
            login(request, user)
            return HttpResponseRedirect(request.POST.get("redirect"))
        else:
            return render(
                request,
                "auth/login.html",
                {"wrongPassword": True, "redirect": redirect},
            )
    return render(request, "auth/login.html", {"redirect": redirect})


# signUp view
def signUp_view(request):
    if request.method == "POST":
        print(request.POST.get("username")),
        print(request.POST.get("password")),
        print(request.POST.get("email")),
        user = User.objects.create_user(
            username=request.POST.get("username"),
            password=request.POST.get("password"),
            email=request.POST.get("email"),
        )

    return render(request, "signUp/signUp.html")
