from django.urls import path
from rollover import views


urlpatterns = [
    path('', views.user_home, name='userHome'),
    path('review/', views.newReview, name='newReview'),
    path('all/reviews/', views.allReviews, name='allReviews'),
    path('wishlist/', views.user_wishlist, name='userWishlist'),
    path('all/wishlist', views.allWishlist, name='allWishlist'),
    path('all/', views.all, name='all')
]
