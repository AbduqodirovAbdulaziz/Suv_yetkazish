from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status, filters
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .serializers import *
from .models import *


class SuvlarApiView(APIView):
    def get(self, request):
        suv = Suv.objects.all()
        serializer = SuvSerializer(suv, many=True)
        return Response(serializer.data)

    def post(self, request):
        suv = request.data
        serializer = SuvSerializer(data=suv)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True, 'create_data': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class MijozlarApiView(APIView):
#     def get(self, request):
#         mijoz = Mijoz.objects.all()
#         serializer = MijozSerializer(mijoz, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         mijoz = request.data
#         serializer = MijozSerializer(data=mijoz)
#         if serializer.is_valid():
#             return Response({'success': True, "ma'lumot kiritildi": serializer.data})
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class MijozEditApiView(APIView):
#     def get(self, request, pk):
#         mijoz = get_object_or_404(Mijoz, id=pk)
#         serializer = MijozSerializer(mijoz)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         mijoz = get_object_or_404(Mijoz, id=pk)
#         serializer = MijozSerializer(mijoz, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"success": True, "updated_data": serializer.data})
#         return Response(serializer.errors)
class MijozModelViewSet(ModelViewSet):
    queryset = Mijoz.objects.all()
    serializer_class = MijozSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ['ism', 'tel']


class BuyurtmaApiView(APIView):
    def get(self, request):
        buyurtma = Buyurtma.objects.all()
        serializer = BuyurtmaSerializer(buyurtma, many=True)
        return Response(serializer.data)

    def post(self, request):
        buyurtma = request.data
        serializer = SuvSerializer(data=buyurtma)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True, 'create_data': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdminlarApiView(APIView):
    def get(self, request):
        admin = Adminlik.objects.all()
        serializer = AdminSerializer(admin, many=True)
        return Response(serializer)


class AdminApiViewSet(APIView):
    def get(self, request, pk):
        admin = Adminlik.objects.get(id=pk)
        serializer = AdminSerializer(admin)
        return Response(serializer.data)


# class haydovchiModelViewSet(ModelViewSet):
#     queryset = Haydovchi.objects.all()
#     serializer_class = HaydovchiSerializer

class HaydovchilarApiView(APIView):
    def get(self, request):
        haydovchi = Haydovchi.objects.all()
        serializer = HaydovchiSerializer(haydovchi, many=True)
        return Response(serializer.data)


class HaydovchiApiView(APIView):
    def get(self, request, pk):
        haydovchi = Haydovchi.objects.get(id=pk)
        serializer = HaydovchiSerializer(haydovchi)
        return Response(serializer.data)
