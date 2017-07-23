from rest_framework import serializers
from restapi.models import Guest, Invitation


class GuestSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(read_only=True)
    # name = serializers.CharField(required=True, allow_blank=False, max_length=100)
    # attending = serializers.BooleanField(required=False)
    #
    # def create(self, validated_data):
    #     """
    #     Create and return a new `Guest` instance, given the validated data.
    #     """
    #     return Guest.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `Guest` instance, given the validated data.
    #     """
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.attending = validated_data.get('attending', instance.attending)
    #     instance.save()
    #     return instance

    class Meta:
        model = Guest
        fields = (
            'id', 'name', 'invitation_id', 'offered_plus_one',
            'bringing_plus_one',
            'attending', 'food_choice')


class InvitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invitation
        fields = ('id', 'sent', 'address', 'access_code')
