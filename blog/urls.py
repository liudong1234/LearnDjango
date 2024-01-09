from django.urls import re_path
from rest_framework.urlpatterns import format_suffix_patterns
from blog import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'articles', viewset=views.ArticleViewSet)

# article_list = views.ArticleViewSet.as_view
# (
#     {
#         'get': 'list',
#         'post': 'create'
#     }
# )

# article_detail = views.ArticleViewSet.as_view
# (
#     {
#         'get': 'retrieve', #只处理get请求，获取单个记录
#     }
# )

urlpatterns = [
    # re_path(r'^articles/$', views.article_list),
    # re_path(r'^articles/(?P<pk>[0-9]+)$', views.article_detail),
    # re_path(r'^articles/$', views.ArticleList.as_view()),
    # re_path(r'^articles/(?P<pk>[0-9]+)$', views.ArticleDetail.as_view()),
    # re_path(r'^articles/$', article_list),
    # re_path(r'^articles/(?P<pk>[0-9]+)$', article_detail),

]

# urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += router.urls