from django.urls import path, include
from account.views import *

urlpatterns = [
    path('login/', login),
    path('logout/', logout),
    path('signup/', signup),
]