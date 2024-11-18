from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def portfolio(request):
    return render(request, 'portfolio-details.html')

def services(request):
    return render(request, 'service-details.html')

def starters(request):
    return render(request, 'starter-page.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent. Thank you!')
            return redirect('contact')
        else:
            messages.error(request, 'There was an error sending your message. Please try again.')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
