from django.views.generic.list import ListView
from django.utils import timezone

from .models import Photo

class DiscoveryPhotoList(ListView):
    model = Photo
    paginate_by = 10
    template_name = 'photos/feed-discovery.html'

    def get_context_data(self):
        context = super(DiscoveryPhotoList, self).get_context_data()
        context['available_colors'] = ('F44336', 'F4A1BE', '9575CD', '64B5F6', '4C4F51', '81C784', 'F5E25B', 'E3E7EA', 'FFB74D')
        context['color'] = self.request.GET.get('color', '')
        return context

    def get_queryset(self):
        color = self.request.GET.get('color', False)
        if color:
            return Photo.objects.filter(color_tag=color)
        return Photo.objects.all()