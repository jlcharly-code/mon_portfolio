from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from projects.models import Project
from .forms import ContactForm

def home(request):
    projects = Project.objects.all()

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            send_mail(
                subject=f"Nouveau message de {name} (portfolio)",
                message=f"De : {name} ({email})\n\n{message}",
                from_email=None,  # utilise DEFAULT_FROM_EMAIL
                recipient_list=["jlcharly@gmail.com"],  # ← mets TON email ici
            )
            messages.success(request, "Message envoyé, merci !")
            return redirect("home")
    else:
        form = ContactForm()

    return render(request, "pages/home.html", {"projects": projects, "form": form})