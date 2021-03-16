from django.shortcuts import render
from rest_framework import generics, permissions, status
from .serializers import AdvisorSerializer, BoookingSerializer, GetMyBookingsSerializer
from .models import Advisor, Booking
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class AdminAddAdvisor(generics.GenericAPIView):
    serializer_class = AdvisorSerializer

    def post(self, request):
        advisor = request.data
        serializer = self.get_serializer(data=advisor)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)

class GetAdvisors(generics.GenericAPIView):
    serializer_class = AdvisorSerializer
    queryset = Advisor.objects.all()
    permission_classes = (IsAuthenticated, )

    def get(self, request, user_id):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BookAdvisors(generics.GenericAPIView):
    serializer_class = BoookingSerializer
    permission_classes = (IsAuthenticated, )

    def post(self, request, user_id, advisor_id):
        data = {
            'time':request.data['time'],
            'user_id':user_id,
            'advisor_id':advisor_id
        }
        try:
            Booking.objects.create(**data)
        except:
            return Response({'error':"No advisor or user with Provided Id"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_200_OK)

class GetMyBookings(generics.GenericAPIView):
    serializer_class = GetMyBookingsSerializer
    queryset = Booking.objects.all()
    permission_classes = (IsAuthenticated, )
    
    def get(self, request, user_id):
        queryset = Booking.objects.filter(user_id=user_id)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
