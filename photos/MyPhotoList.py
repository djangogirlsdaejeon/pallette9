from django.views.generic.list import ListView
from django.utils import timezone

from .models import Photo

class MyPhotoList(ListView):
    model = Photo
    paginate_by = 10
    template_name = 'photos/feed-user.html'

    def get_context_data(self):
        context = super(MyPhotoList, self).get_context_data()
        context['available_colors'] = ('F44336', 'F4A1BE', '9575CD', '64B5F6', '4C4F51', '81C784', 'F5E25B', 'E3E7EA', 'FFB74D')
        context['color'] = self.request.GET.get('color', '')
        return context

    def get_queryset(self):
        color = self.request.GET.get('color', False)
        if color:
            return Photo.objects.filter(author=self.request.user, color_tag=color).order_by('-modify_date')
        return Photo.objects.filter(author=self.request.user).order_by('-modify_date')