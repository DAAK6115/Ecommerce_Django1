from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static
from ecommerce import urls as ecommerce_urls

from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from .schema import schema
 
from django.urls import path
from . import views
urlpatterns = [
   
path('', views.index, name="index" ),
path('about/', views.about, name='about'),
path('register/', views.register, name='register'),
path('login/', views.login, name='login'),
path('logout/', views.logout, name='logout'),
path('contact/', views.contact, name='contact'),
path('forgot/', views.forgot, name='forgot'),
path('menuArticle/', views.menuArticle, name='menuArticle'),
path('reset/', views.reset, name='reset'),
path('blog/', views.blog, name='blog'),
path('blog/<int:post_id>/', views.blog_detail, name='blog_detail'),
path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
path('api', views.ProductSerializer, name='product-list'),
   
] + static (settings.STATIC_URL, document_root=settings.STATIC_ROOT)