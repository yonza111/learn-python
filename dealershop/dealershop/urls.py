from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    path('inventory/', include('inventory.urls')),
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='inventory/')),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('allauth.urls')),
    path('signup/', views.SignUpView.as_view(), name='signup'),
]
