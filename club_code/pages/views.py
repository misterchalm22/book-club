from django.shortcuts import render, redirect
from pages.models import Review
from pages.forms import NewReview

# Create your views here.
def all(request):
	if request.user.is_authenticated:
		return render(request, 'all_home.html')
	else:
		return redirect('../../accounts/login/')


def allReviews(request):
	if request.user.is_authenticated:
		return render(request, 'all_reviews.html')
	else:
		return redirect('../../accounts/login/')


def allWishlist(request):
	if request.user.is_authenticated:
		return render(request, 'all_wishlist.html')
	else:
		return redirect('../../accounts/login/')


def newReview(request):
	if request.user.is_authenticated:
		# if this is a POST request we need to process the form data
		if request.method == 'POST':
		# create a form instance and populate it with data from the request:
			form = NewReview(request.POST)
			# check whether it's valid:
			if form.is_valid():
				# process the data in form.cleaned_data as required
				# ...
				# redirect to a new URL:
				return HttpResponseRedirect('/club/')
		# if a GET (or any other method) we'll create a blank form
		else:
			form = NewReview()
		return render(request, 'new_review.html', {'form': form})
	else:
		return redirect('../../accounts/login/')


def user_home(request):
	if request.user.is_authenticated:
		return render(request, 'userhome.html')
	else:
		return redirect('../../accounts/login/')

def userReviews(request):
	if request.user.is_authenticated:
		return render(request, 'user_reviews.html')
	else:
		return redirect('../../accounts/login/')

def user_wishlist(request):
	if request.user.is_authenticated:
		return render(request, 'user_wishlist.html')
	else:
		return redirect('../../accounts/login/')

def welcome(request):
	if request.user.is_authenticated:
		return render(request, 'welcome.html')
	else:
		return redirect('../../accounts/login/')
