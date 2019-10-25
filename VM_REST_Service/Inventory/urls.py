from django.conf.urls import url
from Inventory.views import item_type_list, item_type_detail

urlpatterns = [
    url(r'^Inventory/$', item_type_list),
    url(r'^Inventory/(?P<pk>[0-9]+)/$', item_type_detail),
]
