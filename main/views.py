from django.shortcuts import render,redirect,get_object_or_404
from .models import PortfoiloItem
from .forms import ContactForm,PortfoiloForm
from django.core.mail import send_mail

def home(request):
    return render(request, 'main/home.html')


def portfolio(request):
    item = PortfoiloItem.objects.all()

    return render(request, 'main/portfolio.html',{"items":item})

def add_portfolio(request):
    success = False
    if request.method == 'POST':
        form = PortfoiloForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            success = True
    else:
        form = PortfoiloForm()
        return render(request, 'main/add_portfolio.html',{'form':form},{'success':success})
    


def edit_portfoilo(request,pk):
    item = get_object_or_404(PortfoiloItem,pk=pk)
    if request.method == 'POST':
        form = PortfoiloForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('porttfoilo')

    else:
        form = PortfoiloForm()
        return render(request, "main/edit_portfoilo", {"form" : form})
    

def delete_portfoilo(request,pk):
    item = get_object_or_404(PortfoiloItem, pk=pk)
    if request.methode == "POST":
        item.delete()
        return redirect("portfoilo")
    return render(request,"main/delete_portfoilo",{"item":item})



def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = form.save()

            # ارسال ایمیل
            send_mail(
                subject=f"پیام جدید از {contact_message.name}",
                message=f"ایمیل: {contact_message.email}\n\n{contact_message.message}",
                from_email=None,  # از DEFAULT_FROM_EMAIL استفاده می‌کنه
                recipient_list=['your_email@gmail.com'],  # ایمیل مقصد
                fail_silently=False,
            )

            return render(request, 'main/contact.html', {
                'form': ContactForm(),
                'success': True
            })
    else:
        form = ContactForm()
    return render(request, 'main/contact.html', {'form': form})
# Create your views here.
