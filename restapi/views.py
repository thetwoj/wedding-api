from restapi.models import Gift, Guest, Invitation, Slider
from restapi.serializers import (
    GiftSerializer, GuestSerializer,
    InvitationSerializer, SliderSerializer,
    InvitationRSVPSerializer
)
from rest_framework import status, viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import permissions


class GiftViewSet(viewsets.ModelViewSet):
    serializer_class = GiftSerializer

    def get_queryset(self):
        return Gift.objects.filter()

    def list(self, request, invitations_pk=None):
        queryset = Gift.objects.filter(giver=invitations_pk)
        serializer = GiftSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, invitations_pk=None):
        queryset = Gift.objects.filter(pk=pk)
        gift = get_object_or_404(queryset, pk=pk)
        serializer = GiftSerializer(gift)
        return Response(serializer.data)

    def create(self, request, pk=None, invitations_pk=None):
        serializer = GiftSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # Make sure guest actually exists
        queryset = Invitation.objects.filter()
        invitation = get_object_or_404(queryset)
        serializer.validated_data['giver'] = invitation
        Gift.objects.create(**serializer.validated_data)
        return Response(serializer.data)


class GuestViewSet(viewsets.ModelViewSet):
    serializer_class = GuestSerializer

    def get_queryset(self):
        return Guest.objects.filter()

    def list(self, request, invitations_pk=None):
        queryset = Guest.objects.filter(invitation=invitations_pk)
        serializer = GuestSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, invitations_pk=None):
        queryset = Guest.objects.filter(pk=pk, invitation=invitations_pk)
        guest = get_object_or_404(queryset, pk=pk)
        serializer = GuestSerializer(guest)
        return Response(serializer.data)

    def create(self, request, pk=None, invitations_pk=None):
        serializer = GuestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # Make sure invitation actually exists
        queryset = Invitation.objects.filter()
        invitation = get_object_or_404(queryset, pk=invitations_pk)
        serializer.validated_data['invitation'] = invitation
        Guest.objects.create(**serializer.validated_data)
        return Response(serializer.data)


class InvitationViewSet(viewsets.ModelViewSet):
    serializer_class = InvitationSerializer
    queryset = Invitation.objects.filter()


class AllGiftViewSet(viewsets.ModelViewSet):
    serializer_class = GiftSerializer
    queryset = Gift.objects.filter()


class AllGuestViewSet(viewsets.ModelViewSet):
    serializer_class = GuestSerializer
    queryset = Guest.objects.filter()


class AllSliderViewSet(viewsets.ModelViewSet):
    serializer_class = SliderSerializer
    queryset = Slider.objects.filter()


class InvitationRSVPView(APIView):
    permission_classes = (permissions.AllowAny,)

    serializer_class = InvitationSerializer
    queryset = Invitation.objects.filter()

    def get(self, request, access_code):
        if request.user.is_authenticated:
            invitations = Invitation.objects.filter(access_code=access_code)
        else:
            invitations = Invitation.objects.filter(access_code=access_code)
        serializer = InvitationRSVPSerializer(invitations, many=True)
        return Response(serializer.data)
