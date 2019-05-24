from django.urls import path
from django.conf.urls import url
from .views import CardTemplateView, CardListView, CardDetailView, CardUpdateView, CardDeleteView, CardAddView


urlpatterns = [
    path('', CardTemplateView.as_view(), name='index'),
    path('card_view', CardListView.as_view(), name='card_view'),
    url(r'^detail/(?P<pk>[0-9]+)/$', CardDetailView.as_view(), name='card_detail'),
    url(r'^update/(?P<pk>\d+)$', CardUpdateView.as_view(), name='card_update'),
    url(r'^delete/(?P<pk>\d+)/$', CardDeleteView.as_view(), name='card_delete'),
    url(r'card_image/', CardAddView.as_view(), name='card_image'),
]
