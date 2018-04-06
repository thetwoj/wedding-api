from restapi.models import Gift, Guest, Invitation, Slider
from restapi.serializers import (
    GiftSerializer, GuestSerializer,
    InvitationSerializer, SliderSerializer,
    InvitationRSVPSerializer
)
from rest_framework import permissions, viewsets
from rest_framework.response import Response
from django.http import HttpResponse
from django.shortcuts import get_object_or_404


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


class InvitationRSVPView(viewsets.ViewSet):
    permission_classes = (permissions.AllowAny,)

    def retrieve(self, _, access_code):
        queryset = Invitation.objects.filter(access_code=access_code)
        invitation = get_object_or_404(queryset)
        serializer = InvitationRSVPSerializer(invitation)
        return Response(serializer.data)


class RsvpGuestView(viewsets.ViewSet):
    permission_classes = (permissions.AllowAny,)
    serializer_class = GuestSerializer

    def create(self, request, invitation_pk=None):
        request.data['offered_plus_one'] = False
        request.data['bringing_plus_one'] = False
        request.data['attending'] = True

        # Make sure invited_by was provided
        inviter_id = request.data.get('invited_by')
        if not inviter_id:
            return HttpResponse(status=404)

        # Make sure invited_by is legit
        queryset = Guest.objects.filter()
        inviter = get_object_or_404(queryset, pk=inviter_id)

        # Make sure inviter was allowed +1
        if not inviter.offered_plus_one:
            return HttpResponse(status=404)

        # Make sure inviter hasn't invited anyone else already
        if Guest.objects.filter(invited_by=inviter_id).count() > 0:
            return HttpResponse(status=404)

        # Make sure request JSON for guest is valid
        serializer = GuestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Add to inviter's invitation
        serializer.validated_data['invitation'] = inviter.invitation
        serializer.validated_data['invited_by'] = inviter

        Guest.objects.create(**serializer.validated_data)
        return Response(serializer.data)

    def update(self, request, guest_pk, invitation_pk=None):
        # Make sure guest actually exists
        queryset = Guest.objects.filter()
        guest = get_object_or_404(queryset, pk=guest_pk)

        # Make sure request JSON for guest is valid
        serializer = GuestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Don't let request change name, offered_plus_one, invitation
        guest.attending = request.data['attending']
        guest.bringing_plus_one = guest.offered_plus_one and request.data['bringing_plus_one']

        guest.save()
        return Response(serializer.data)
