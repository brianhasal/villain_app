"""villaincollector URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('villains/', views.villains_index, name='index'),
    path('villains/<int:villain_id>', views.villains_detail, name='detail'),
    path('villains/<int:villain_id>/add_surveillance/', views.add_surveillance, name='add_surveillance'),
    path('villains/create/', views.VillainCreate.as_view(), name='villains_create'),
    path('villains/<int:pk>/update/', views.VillainUpdate.as_view(), name='villains_update'),
    path('villains/<int:pk>/delete/', views.VillainDelete.as_view(), name='villains_delete'),
    path('henchmen/', views.HenchmenList.as_view(), name='henchmen_index'),
    path('henchmen/<int:pk>/', views.HenchmenDetail.as_view(), name='henchmen_detail'),
    path('henchmen/<int:pk>/update/', views.HenchmenUpdate.as_view(), name='henchmen_update'),
    path('henchmen/<int:pk>/delete/', views.HenchmenDelete.as_view(), name='henchmen_delete'),
    path('henchmen/create/', views.HenchmenCreate.as_view(), name='henchmen_create'),

]
