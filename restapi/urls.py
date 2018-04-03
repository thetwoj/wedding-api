from django.conf.urls import url, include
from restapi import views
from rest_framework_nested import routers
from rest_framework.authtoken import views as auth_views

# /invitations
router = routers.SimpleRouter()
router.register(r'invitations', views.InvitationViewSet, base_name='invitations')
# /invitations/<#>/guests
invitations_router = routers.NestedSimpleRouter(router, r'invitations', lookup='invitations')
invitations_router.register(r'guests', views.GuestViewSet, base_name='guests')
# /invitations/<#>/gifts
invitations_router.register(r'gifts', views.GiftViewSet, base_name='gifts')

# All gifts
router.register(r'gifts', views.AllGiftViewSet)

# All guests
router.register(r'guests', views.AllGuestViewSet)

# All sliders
router.register(r'sliders', views.AllSliderViewSet)

urlpatterns = [
    url(r'^(?:api/)?rsvp/(?P<access_code>[\w]+)/$', views.InvitationRSVPView.as_view()),
    url(r'^(?:api/)?', include(router.urls)),
    url(r'^(?:api/)?', include(invitations_router.urls)),
    url(r'^(?:api/)?login/', auth_views.obtain_auth_token)
]
