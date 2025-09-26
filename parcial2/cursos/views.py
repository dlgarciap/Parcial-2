from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, TemplateView
from .models import Video, SiteUser
from .forms import VideoForm, SiteUserForm

# Videos
class VideoListView(ListView):
    model = Video
    template_name = 'cursos/videos_list.html'
    context_object_name = 'videos'
    queryset = Video.objects.filter(published=True).order_by('-created_at')

class VideoCreateView(CreateView):
    model = Video
    form_class = VideoForm
    template_name = 'cursos/video_form.html'
    success_url = reverse_lazy('cursos:videos_list')

class VideoUpdateView(UpdateView):
    model = Video
    form_class = VideoForm
    template_name = 'cursos/video_form.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('cursos:videos_list')

# Usuarios
class UserListView(ListView):
    model = SiteUser
    template_name = 'cursos/users_list.html'
    context_object_name = 'users'
    queryset = SiteUser.objects.all().order_by('full_name')

class UserCreateView(CreateView):
    model = SiteUser
    form_class = SiteUserForm
    template_name = 'cursos/user_form.html'
    success_url = reverse_lazy('cursos:users_list')

class UserUpdateView(UpdateView):
    model = SiteUser
    form_class = SiteUserForm
    template_name = 'cursos/user_form.html'
    success_url = reverse_lazy('cursos:users_list')

# Créditos
class CreditsView(TemplateView):
    template_name = 'cursos/credits.html'