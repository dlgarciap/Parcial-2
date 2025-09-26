from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class SiteUser(models.Model):
    full_name = models.CharField('Nombre completo', max_length=150)
    email = models.EmailField('Correo electrónico', unique=True)
    phone = models.CharField('Teléfono', max_length=30, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['full_name']

    def __str__(self):
        return f"{self.full_name} ({self.email})"


class Video(models.Model):
    title = models.CharField('Título', max_length=255)
    slug = models.SlugField('Slug', max_length=255, unique=True, blank=True)
    description = models.TextField('Descripción', blank=True)
    video_url = models.URLField('URL del video')
    instructor = models.CharField('Instructor', max_length=150, blank=True)
    duration_minutes = models.PositiveIntegerField('Duración (min)', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField('Publicado', default=True)

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Crear slug único automático a partir del título
        if not self.slug:
            base = slugify(self.title)[:200]
            slug = base
            counter = 1
            while Video.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('cursos:videos_list')

