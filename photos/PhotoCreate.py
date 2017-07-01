from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Photo

class PhotoCreate(CreateView):
    model = Photo
    fields = ['pic', 'color_tag', 'contents',]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PhotoCreate, self).form_valid(form)

    def get_success_url(self):
        return '/photos/'