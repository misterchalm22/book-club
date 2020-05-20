from django.urls import path
from pages import views


urlpatterns = [
    path('', views.user_home, name='userHome'),
    path('all/', views.all, name='all'),
    path('all/reviews/', views.allReviews, name='allReviews'),
    path('all/wishlist', views.allWishlist, name='allWishlist'),
    path('review/', views.newReview, name='newReview'),
    path('reviews/', views.userReviews, name='userReviews'),
    path('wishlist/', views.user_wishlist, name='userWishlist')
]
