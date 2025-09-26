from django.urls import path
from .views import (
    VideoListView, VideoCreateView, VideoUpdateView,
    UserListView, UserCreateView, UserUpdateView, CreditsView
)

app_name = 'cursos'

urlpatterns = [
    # Página principal: lista de videos
    path('', VideoListView.as_view(), name='videos_list'),
    path('videos/nuevo/', VideoCreateView.as_view(), name='video_create'),
    path('videos/<slug:slug>/editar/', VideoUpdateView.as_view(), name='video_edit'),

    # Usuarios
    path('usuarios/', UserListView.as_view(), name='users_list'),
    path('usuarios/nuevo/', UserCreateView.as_view(), name='user_create'),
    path('usuarios/<int:pk>/editar/', UserUpdateView.as_view(), name='user_edit'),

    # Créditos
    path('creditos/', CreditsView.as_view(), name='credits'),
]
