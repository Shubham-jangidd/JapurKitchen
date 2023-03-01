import imp
from unicodedata import name
from django.shortcuts import render
from django.views import View
from .forms import ContactForm, CustomerRegistrationForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
# from TasteOfJaipur.models import contactus
from .models import contactus as contactusmodel
from django.contrib import messages



# Create your views here.
class Home(View):
    def get(self, request):
        return render(request, "app/index.html")

class about(View):
    def get(self, request):
    
        
        return render(request, "app/about.html")




def contactus(request):
    return render(request, "app/contact.html")



def saveEnquiry(request):
    print("running save enq")
    print(request.method)
    print("running the save enquiry function")
    if request.method == "POST":
        form = ContactForm(request.POST)
        first_name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        reg = contactusmodel(
                email=email,
                first_name=first_name,
                message=message
            )
        reg.save()
        messages.success(
                request,
                "Congrulations we have recieved your enquire. We will get back to you soon !!",
            )

        return redirect("/")

class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, "app/customerregistration.html", {"form": form})

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        # form.email = form.username
        print(form)
        print(type(form))
        # help(form)
        if form.is_valid():
            # form.email = form.username
            # instanceform.save(updated_)
            email = form.cleaned_data["email"]
            instance = form.save(commit=False)
            instance.username = email
            instance.save()

            messages.success(
                request,
                "Congrulations!! Registered Successfully, Please Login to Continue",
            )
            # return render(request, 'app/login.html')
            return redirect("login")
        else:
            return render(request, "app/customerregistration.html", {"form": form})