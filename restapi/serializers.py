from rest_framework import serializers
from restapi.models import Gift, Guest, Invitation, Slider


class GiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gift
        fields = ('id', 'name')


class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = ('id', 'name', 'description')


class GuestSerializer(serializers.ModelSerializer):
    sliders = SliderSerializer(many=True, read_only=True)

    class Meta:
        model = Guest
        fields = (
            'id', 'name', 'invitation', 'offered_plus_one', 'bringing_plus_one',
            'attending', 'sliders')


class InvitationSerializer(serializers.ModelSerializer):
    guests = GuestSerializer(many=True, read_only=True)
    gifts = GiftSerializer(many=True, read_only=True)

    class Meta:
        model = Invitation
        fields = ('id', 'sent', 'address', 'access_code', 'guests', 'gifts')
