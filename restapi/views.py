from restapi.models import Gift, Guest, Invitation
from restapi.serializers import GiftSerializer, GuestSerializer, \
    InvitationSerializer
from rest_framework import status, viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class GiftViewSet(viewsets.ModelViewSet):
    serializer_class = GiftSerializer

    def get_queryset(self):
        return Gift.objects.filter()

    def list(self, request, guest_pk=None):
        queryset = Gift.objects.filter(giver=guest_pk)
        serializer = GiftSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, guest_pk=None, invitation_pk=None):
        queryset = Gift.objects.filter(pk=pk, giver=guest_pk)
        gift = get_object_or_404(queryset, pk=pk)
        serializer = GiftSerializer(gift)
        return Response(serializer.data)

    def create(self, request, pk=None, guest_pk=None, invitation_pk=None):
        serializer = GiftSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # Make sure guest actually exists
        queryset = Guest.objects.filter()
        guest = get_object_or_404(queryset, pk=guest_pk)
        serializer.validated_data['giver'] = guest
        Gift.objects.create(**serializer.validated_data)
        return Response(serializer.data)


class GuestViewSet(viewsets.ModelViewSet):
    serializer_class = GuestSerializer

    def get_queryset(self):
        return Guest.objects.filter()

    def list(self, request, invitation_pk=None):
        queryset = Guest.objects.filter(invitation=invitation_pk)
        serializer = GuestSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, invitation_pk=None):
        queryset = Guest.objects.filter(pk=pk, invitation=invitation_pk)
        guest = get_object_or_404(queryset, pk=pk)
        serializer = GuestSerializer(guest)
        return Response(serializer.data)

    def create(self, request, pk=None, invitation_pk=None):
        serializer = GuestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # Make sure invitation actually exists
        queryset = Invitation.objects.filter()
        invitation = get_object_or_404(queryset, pk=invitation_pk)
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
