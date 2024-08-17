from django.urls import path
from .views import RegisterUserView, SearchView, SearchByPhoneView, SpamView, SpamLikelihoodView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register_user'),
    path('search/', SearchView.as_view(), name='search'),
    path('search-by-phone/', SearchByPhoneView.as_view(), name='search_by_phone'),
    path('spam/', SpamView.as_view(), name='spam'),
    path('spam/<str:phone_number>/', SpamLikelihoodView.as_view(), name='spam_likelihood'),
]
