from rest_framework import serializers
from restapi.models import Gift, Guest, Invitation


class GiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gift
        fields = ('id', 'name', 'ty_sent')


class GuestSerializer(serializers.ModelSerializer):
    gifts = GiftSerializer(many=True, read_only=True)

    class Meta:
        model = Guest
        fields = (
            'id', 'name', 'invitation', 'offered_plus_one', 'bringing_plus_one',
            'attending', 'food_choice', 'gifts')


class InvitationSerializer(serializers.ModelSerializer):
    guests = GuestSerializer(many=True, read_only=True)

    class Meta:
        model = Invitation
        fields = ('id', 'sent', 'address', 'access_code', 'guests')
