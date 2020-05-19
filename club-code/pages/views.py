from django.shortcuts import render, redirect
from pages.models import Review

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
		return render(request, 'new_review.html')
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
