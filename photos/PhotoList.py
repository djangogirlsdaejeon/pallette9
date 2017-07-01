from django.views.generic.list import ListView
from django.utils import timezone

from .models import Photo

class PhotoList(ListView):
    model = Photo
    template_name = 'photos/photo_list.twig'

    def get_context_data(self, **kwargs):
        context = super(PhotoList, self)\
            .get_context_data(**kwargs)

        return context