from blog.models import Category

def cats(request):
    return {
        'catgs': Category.objects.all()
    }