from rest_framework import serializers
from restapi.models import Guest, Invitation


class GuestSerializer(serializers.ModelSerializer):
    invitation = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Guest
        fields = (
            'id', 'name', 'invitation', 'offered_plus_one',
            'bringing_plus_one',
            'attending', 'food_choice')


class InvitationSerializer(serializers.ModelSerializer):
    guests = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Invitation
        fields = ('id', 'sent', 'address', 'access_code', 'guests')
