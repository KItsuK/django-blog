from .models import Category

def commons(request):
    """テンプレートに毎回渡すデータ"""
    context = {
        'category_list':Category.objects.all()
    }
    return context
