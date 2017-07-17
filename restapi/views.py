from restapi.models import Guest, Invitation
from restapi.serializers import GuestSerializer, InvitationSerializer
from rest_framework import generics


# class GuestList(APIView):
#     def get(self, request, format=None):
#         guests = Guest.objects.all()
#         serializer = GuestSerializer(guests, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = GuestSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class GuestDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Guest.objects.get(pk=pk)
#         except Guest.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         guest = self.get_object(pk)
#         serializer = GuestSerializer(guest)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         guest = self.get_object(pk)
#         serializer = GuestSerializer(guest, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         guest = self.get_object(pk)
#         guest.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class GuestList(generics.ListCreateAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer


class GuestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer


class InvitationList(generics.ListCreateAPIView):
    queryset = Invitation.objects.all()
    serializer_class = InvitationSerializer


class InvitationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Invitation.objects.all()
    serializer_class = InvitationSerializer
