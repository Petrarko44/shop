from django.shortcuts import render
from rest_framework import generics, viewsets
from goods.models import Goods, Subcategory, Category, Type, Brand
from goods.serializers import GoodsSerializer, SubcategorySerializer, CategorySerializer, TypeSerializer, \
    BrandSerializer
from django_filters.rest_framework import DjangoFilterBackend
from goods.filters import GoodsFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from goods.permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

# class GoodsAPIList(generics.ListCreateAPIView):
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializer
#     authentication_classes = [SessionAuthentication, BasicAuthentication]
#     permission_class = (IsAuthenticatedOrReadOnly, )
# #
# class GoodsAPIDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializer

class GoodsViewSet(viewsets.ModelViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = GoodsFilter
    permission_classes = (IsAdminOrReadOnly,)
    authentication_classes = [SessionAuthentication, BasicAuthentication]

# class SubcategoryAPIList(generics.ListCreateAPIView):
#     queryset = Subcategory.objects.all()
#     serializer_class = SubcategorySerializer
#
# class SubcategoryAPIDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Goods.objects.all()
#     serializer_class = SubcategorySerializer

class SubcategoryViewSet(viewsets.ModelViewSet):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer