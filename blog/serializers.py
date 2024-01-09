from rest_framework import serializers
from blog.models import Article
from django.contrib.auth import get_user_model

User = get_user_model()
'''
class ArticleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, allow_blank=True, max_length=90)
    body = serializers.CharField(required=False, allow_blank=True)
    author = serializers.ReadOnlyField(source="author.id")
    status = serializers.ChoiceField(choices=Article.STATUS_CHOICES, default='p')
    create_date = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):

        #Create a new "article" instance


        return Article.objects.create(**validated_data)
    
    def update(self, instance, validated_data):

        #Use validated data to return an existing `Article` instance

        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.status = validated_data.get('status', instance.status)
        instance.save()

        return instance
'''

class UserSerializer(serializers.ModelSerializer):
    articles = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'articles')
        read_only_fields = ('id', 'username')

class ArticleSerializer(serializers.ModelSerializer):
    
    # author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    author = UserSerializer() #required=False表示可接受匿名用户， many=True表示多用户
    full_status = serializers.ReadOnlyField(source="get_status_display")
    cn_status = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('id', 'author', 'create_date')
    
    def get_cn_status(self, obj):
        if obj.status == 'p':
            return '已发表'
        elif obj.status == 'd':
            return '草稿'
        else:
            return ''