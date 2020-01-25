from django.conf.urls import url
from ..personal_data.views import index_personal,personal_list

urlpatterns = [
    url(r'^$', index_personal),
    url('r|^listar$',personal_list, name='personal_data_list')
]
