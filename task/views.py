from django.shortcuts import render
from rest_framework import viewsets
from . import models,serializers
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from . import permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    # permission_classes = [permissions.AdminOrReadOnly]
    queryset=models.Task.objects.all()
    serializer_class=serializers.TaskSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['due_date','creation_date','is_complete','priority']
