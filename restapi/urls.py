from django.conf.urls import url, include
from restapi import views
from rest_framework_nested import routers

router = routers.SimpleRouter()
router.register(r'invitation', views.InvitationViewSet, base_name='invitations')

invitations_router = routers.NestedSimpleRouter(router, r'invitation',
                                                lookup='invitation')
invitations_router.register(r'guest', views.GuestViewSet,
                            base_name='guests')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(invitations_router.urls)),
]
