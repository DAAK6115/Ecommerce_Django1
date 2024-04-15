import graphene
from graphene_django.types import DjangoObjectType
from .models import Profile, Product, Category, Post
from django.contrib.auth.models import User

class ProfileType(DjangoObjectType):
    class Meta:
        model = Profile

class ProductType(DjangoObjectType):
    class Meta:
        model = Product

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category

class PostType(DjangoObjectType):
    class Meta:
        model = Post

class UserType(DjangoObjectType):
    class Meta:
        model = User

class Query(graphene.ObjectType):
    # Définissez les champs de requête pour chaque modèle
    profile = graphene.Field(ProfileType)
    product = graphene.Field(ProductType)
    category = graphene.Field(CategoryType)
    post = graphene.Field(PostType)
    user = graphene.Field(UserType)

    # Définissez les résolveurs pour chaque champ de requête
    def resolve_profile(self, info):
        return Profile.objects.first()

    def resolve_product(self, info):
        return Product.objects.first()

    def resolve_category(self, info):
        return Category.objects.first()

    def resolve_post(self, info):
        return Post.objects.first()

    def resolve_user(self, info):
        return User.objects.first()

schema = graphene.Schema(query=Query)
