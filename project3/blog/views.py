from django.views import generic
from .models import Post

class IndexView(generic.ListView):
    model = Post

    def get_queryset(self): #記事を新しい順に並び替え
        return Post.objects.order_by('-creat_at')
