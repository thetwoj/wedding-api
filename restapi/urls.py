from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from restapi import views

urlpatterns = [
    url(r'^guests/$', views.GuestList.as_view()),
    url(r'^guests/(?P<pk>[0-9]+)/$', views.GuestDetail.as_view()),
    url(r'^invitations/$', views.InvitationList.as_view()),
    url(r'^invitations/(?P<pk>[0-9]+)/$', views.InvitationDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)