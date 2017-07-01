from django.views.generic.list import ListView
from django.utils import timezone

from .models import Photo

class MyPhotoList(ListView):
    model = Photo

    def get_queryset(self):
        return Photo.objects.filter(user=self.request.user)