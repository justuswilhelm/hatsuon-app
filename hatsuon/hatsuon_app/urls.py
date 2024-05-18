from django.urls import include, path
from rest_framework.routers import DefaultRouter
from hatsuon_app import views


router = DefaultRouter()
router.register(r"collections", views.CollectionViewSet)
router.register(r"users", views.UserViewSet)
router.register(r"phrases", views.PhraseViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
frontend_urlpatterns = [
    path(r"", views.SpaView.as_view(), name="spa"),
    path(r"login", views.SpaView.as_view(), name="spa"),
    path(r"collection/<slug:id>", views.SpaView.as_view(), name="spa"),
    path(r"collection/<slug:collection_id>/phrase/<slug:phrase_id>", views.SpaView.as_view(), name="spa"),
]
