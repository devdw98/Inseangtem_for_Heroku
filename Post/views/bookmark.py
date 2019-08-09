from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from ..serializers.bookmark import BookMarkSerializer
from ..models.bookmark import BookMark
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status
from django.core import serializers
from Auth.models import IstUser
from ..models.post import Post


class BookMarkViewSet(viewsets.ModelViewSet):
    queryset = BookMark.objects.all()
    serializer_class = BookMarkSerializer

    # def list(self, request, *args, **kwargs):
    #     # user_id = request.data.get("user_id")
    #     # queryset = self.get_queryset()
    #     # queryset = queryset.filter(user_id=user_id)
    #     # serializer = self.get_serializer(queryset, many=True)
    #     # if serializer.is_valid():
    #     #     return Response(serializer.data, status=200)
    #     # return Response(serializer.error, status=500)
    #     user_id = request.data.get("user_id")

    def get_queryset(self):
        user_id = self.request.query_params.get("user_id")
        qs = super().get_queryset()        
        qs = qs.filter(user_id=user_id)
        return qs

    def create(self, request, *args, **kwargs):
        bookmark_user_id = request.data.get("user_id")
        bookmark_post_id = request.data.get("post_id")
        user_id = IstUser.objects.get(pk=bookmark_user_id)
        post_id = Post.objects.get(pk=bookmark_post_id)

        bookmark = BookMark.objects.create(user_id=user_id, post_id=post_id)

        serialized_obj = serializers.serialize('json', [bookmark, ])

        return HttpResponse(serialized_obj, content_type="application/json")
