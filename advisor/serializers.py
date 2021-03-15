from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError, AuthenticationFailed
from .models import Advisor, Booking


class AdvisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advisor
        fields = ('id' ,'name', 'profile_pic')

    def create(self, validated_data):
        advisor = Advisor.objects.create(profile_pic=validated_data['profile_pic'], name=validated_data['name'])
        return advisor


class BoookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ('time',)

class GetMyBookingsSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    time = serializers.DateTimeField()
    advisor = AdvisorSerializer(read_only=True)
    class Meta:
        model = Booking
        fields = ('id', 'time', 'advisor')
    def to_representation(self, obj):
        bid = obj.id
        btime = obj.time
        aname = obj.advisor.name
        aid = obj.advisor.id
        app = obj.advisor.profile_pic
        return {
            "Advisor Id": aid,
            "Advisor Name": aname,
            "Advisor Profile Pic": app,
            "Booking Id": bid,
            "Booking Time":btime
        }
