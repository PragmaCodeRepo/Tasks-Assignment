from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tasks.views import MyTaskViewSet, ObtainTokenView
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt

router = DefaultRouter()
router.register(r"tasks", MyTaskViewSet, basename="my-tasks")

urlpatterns = [
    path("api/token/", ObtainTokenView.as_view(), name="api-token"),
    path("api/", include(router.urls)),
    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True))),
]
