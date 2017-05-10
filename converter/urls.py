from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^services/$', views.services, name='services'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^faq/$', views.faq, name='faq'),
    url(r'^lost/$', views.lost, name='lost'),
    url(r'^donate/$', views.donate, name='donate'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
]
