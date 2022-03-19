from django.shortcuts import redirect, render
from .forms import FormContact
from django.core.mail import EmailMessage

def contact(request):

    form_contact = FormContact()

    if request.method == "POST":

        form_contact = FormContact(request.POST)

        if form_contact.is_valid():

            name = request.POST.get("name")
            email = request.POST.get("email")
            content = request.POST.get("content")

            email = EmailMessage("Message from App Django",
            "The user {} whose email address is {} say:\n\n {}".format(name,email,content),
            "",
            ["guidogamerro@gmail.com"],
            reply_to=[email])

            try:
                email.send()

                return redirect("/contact/?valid")

            except:
                return redirect("/contact/?novalid")

    ctx = {'myForm' : form_contact}

    return render(request, "contact/contact.html", ctx)