"""VM_REST_Service URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.conf.urls import url, include
from RestService import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('players', views.PlayerViewSet)
router.register('locations', views.LocationViewSet)
router.register('item-types', views.ItemTypeViewSet)
router.register('items', views.ItemViewSet)
router.register('messages', views.MessageViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^', include('Inventory.urls')),
    url(r'^api-path/', include('rest_framework.urls', namespace='rest_framework'))
]
