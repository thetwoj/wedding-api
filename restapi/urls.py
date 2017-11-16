from django.conf.urls import url, include
from restapi import views
from rest_framework_nested import routers
from rest_framework.authtoken import views as auth_views

# /invitations
router = routers.SimpleRouter()
router.register(r'api/invitations', views.InvitationViewSet, base_name='invitations')
# /invitations/<#>/guests
invitations_router = routers.NestedSimpleRouter(router, r'api/invitations',
                                                lookup='invitations')
invitations_router.register(r'api/guests', views.GuestViewSet, base_name='guests')
# /invitations/<#>/guests/<#>/gifts
guests_router = routers.NestedSimpleRouter(invitations_router, r'api/guests',
                                           lookup='guests')
guests_router.register(r'api/gifts', views.GiftViewSet, base_name='gifts')

# All gifts
router.register(r'api/gifts', views.AllGiftViewSet)

# All guests
router.register(r'api/guests', views.AllGuestViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(invitations_router.urls)),
    url(r'^', include(guests_router.urls)),
    url(r'^api/login/', auth_views.obtain_auth_token)
]
