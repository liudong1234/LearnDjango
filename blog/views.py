from rest_framework import viewsets
from django.http import Http404
from blog.models import Article
from blog.serializers import ArticleSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def perfrom_create(self, serializer):
        serializer.save(author=self.request.user)


'''
# 使用Generic APIView & Mixins
from rest_framework import mixins
from rest_framework import generics
class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    #将request.user 与author绑定
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
'''

'''
#推荐
class ArticleList(mixins.ListModelMixin, mixins.CreateModelMixin, 
                  generics.GenericAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    #列出整个列表
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    
class ArticleDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,generics.GenericAPIView):
   queryset = Article.objects.all()
   serializer_class = ArticleSerializer

    #获取单个对象
   def get(self, request, *args, **kwargs):
       return self.retrieve(request, *args, **kwargs)

   def put(self, request, *args, **kwargs):
       return self.update(request, *args, **kwargs)

   def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, *kwargs)
'''
        
'''
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
#重写，采用视图类
class ArticleList(APIView):
    # List all articles, or create a new article
    def get(self, request, fromat=None):
        articles = Article.objects.all()
        serilalizer = ArticleSerializer(articles, many=True)
        return Response(serilalizer.data)

    def post(self, request, format=None):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            #注意：手动将request.user与author绑定
            serializer.save(author=request.user)
            return Response(serializer.data, stauts=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ArticleDetail(APIView):
    #retrieve, update or delete an article instance.
    def get_object(self, pk):
        try:
            return Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        article = self.get_object(pk)
        serializer = ArticleSerializer(isinstance=article, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''
'''
#视图函数
@api_view(['GET', 'POST'])
def article_list(request, format=None):
    # List all articles, or create a new article.
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            #Very import. Associate rquest.user with author
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, pk, format=None):
    # retrivev, update or delete an article instance
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoseNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''