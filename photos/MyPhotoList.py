from django.views.generic.list import ListView
from django.utils import timezone

from .models import Photo

class MyPhotoList(ListView):
    model = Photo
    paginate_by = 1

    def get_queryset(self):
        return Photo.objects.filter(author=self.request.user)