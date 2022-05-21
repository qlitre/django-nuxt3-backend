from rest_framework import generics, pagination, response
from .models import Post, Category, Tag, About
from .serializers import PostSerializer, SimplePostSerializer, CategoryWithPostCountSerializer, \
    TagWithPostCountSerializer, AboutSerializer
from django.db.models import Q

from rest_framework_api_key.permissions import HasAPIKey
from rest_framework.permissions import IsAdminUser


class CategoryList(generics.ListAPIView):
    permission_classes = [HasAPIKey | IsAdminUser]
    queryset = Category.objects.all()
    serializer_class = CategoryWithPostCountSerializer


class TagList(generics.ListAPIView):
    permission_classes = [HasAPIKey | IsAdminUser]
    queryset = Tag.objects.all()
    serializer_class = TagWithPostCountSerializer


class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 10

    def get_paginated_response(self, data):
        return response.Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'current_page': self.page.number,
            'results': data,
            'page_size': self.page_size,
        })


class PostList(generics.ListAPIView):
    permission_classes = [HasAPIKey | IsAdminUser]
    queryset = Post.objects.filter(is_public=True)
    serializer_class = SimplePostSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        keyword = self.request.query_params.get('keyword', None)
        if keyword:
            queryset = queryset.filter(
                Q(title__icontains=keyword) | Q(description__icontains=keyword) | Q(main_text__icontains=keyword))
        tag = self.request.query_params.get('tagSlug', None)
        if tag:
            queryset = queryset.filter(tag__slug=tag)

        category = self.request.query_params.get('categorySlug', None)
        if category:
            queryset = queryset.filter(category__slug=category)

        return queryset


class PostDetail(generics.RetrieveAPIView):
    permission_classes = [HasAPIKey | IsAdminUser]
    queryset = Post.objects.filter(is_public=True)
    serializer_class = PostSerializer
    lookup_field = 'slug'


class AboutDetail(generics.RetrieveAPIView):
    permission_classes = [HasAPIKey | IsAdminUser]
    queryset = About.objects.all()
    serializer_class = AboutSerializer
