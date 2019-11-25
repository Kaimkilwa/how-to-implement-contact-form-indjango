from django.shortcuts import render
from .forms import ContactForm
from django.shortcuts import redirect
# from django.views.generic import ListView
# Create your views here.

def Homebview(request):
    """A view of all bands."""
    return render(request, 'dsl/index.html')
      
def About(request):
    """A view of all bands."""
    return render(request, 'dsl/about.html')
      
def Service(request):
    """A view of all bands."""
    return render(request, 'dsl/service.html')

def Contact(request):
	form = ContactForm
	if request.method == "POST":
		form = ContactForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			
			post.save()
			return redirect('contact')
		else:
			form = ContactForm()
	return render(request, 'dsl/contact.html', {'form': form})