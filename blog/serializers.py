from rest_framework import serializers
from .models import Post, Category, Tag, About
import markdown
from django.conf import settings
from .utils import replace_img_relative_path_to_absolute


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug',)


class CategoryWithPostCountSerializer(serializers.ModelSerializer):
    post_count = serializers.IntegerField(
        source='post_set.count',
        read_only=True
    )

    class Meta:
        model = Category
        fields = ('id', 'name', 'slug', 'post_count')


class TagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name', 'slug',)


class TagWithPostCountSerializer(serializers.ModelSerializer):
    post_count = serializers.IntegerField(
        source='post_set.count',
        read_only=True
    )

    class Meta:
        model = Tag
        fields = ('id', 'name', 'slug', 'post_count')


class SimplePostSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    tag = TagSerializers(read_only=True, many=True)

    class Meta:
        model = Post
        exclude = ('main_text',)


class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    tag = TagSerializers(read_only=True, many=True)

    main_text = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = '__all__'

    @staticmethod
    def get_main_text(instance):
        txt = replace_img_relative_path_to_absolute(instance.main_text)
        return markdown.markdown(txt, extensions=settings.MARKDOWN_EXTENSIONS)


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'

    body = serializers.SerializerMethodField()

    @staticmethod
    def get_body(instance):
        txt = replace_img_relative_path_to_absolute(instance.body)
        return markdown.markdown(txt, extensions=settings.MARKDOWN_EXTENSIONS)
