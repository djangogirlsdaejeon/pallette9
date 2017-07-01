from django.views.generic.list import ListView
from django.utils import timezone

from .models import Photo

class DiscoveryPhotoList(ListView):
    model = Photo

    paginate_by = 25

    def get_queryset(self):
        color = self.request.GET.get('color', False)
        if color:
            return Photo.objects.filter(color=color)
        return Photo.objects.all()