from restapi.models import Guest, Invitation
from restapi.serializers import GuestSerializer, InvitationSerializer
from rest_framework import status, viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


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
        queryset = Invitation.objects.filter()
        # Make sure invitation actually exists
        invitation = get_object_or_404(queryset, pk=invitation_pk)
        Guest.objects.create(invitation=invitation, **serializer.validated_data)
        return Response(serializer.data)


class InvitationViewSet(viewsets.ModelViewSet):
    serializer_class = InvitationSerializer
    queryset = Invitation.objects.filter()