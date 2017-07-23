from restapi.models import Guest, Invitation
from restapi.serializers import GuestSerializer, InvitationSerializer
from rest_framework import status, viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class GuestViewSet(viewsets.ViewSet):
    serializer_class = GuestSerializer

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

        if serializer.is_valid():
            queryset = Invitation.objects.filter()
            # Make sure invitation actually exists
            invitation = get_object_or_404(queryset, pk=invitation_pk)
            Guest.objects.create(invitation=invitation, **serializer.validated_data)
            return Response(serializer.data)
        return Response({
            'status': 'Bad request'
        }, status=status.HTTP_400_BAD_REQUEST)


class InvitationViewSet(viewsets.ViewSet):
    serializer_class = InvitationSerializer

    def list(self, request):
        queryset = Invitation.objects.filter()
        serializer = InvitationSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Invitation.objects.filter()
        invitation = get_object_or_404(queryset, pk=pk)
        serializer = InvitationSerializer(invitation)
        return Response(serializer.data)