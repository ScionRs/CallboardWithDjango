from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .forms import AdsForm
from django.http import HttpResponse
from .forms import *

from ads.models import Ads
from ads.models import Category

def index(request):
        ads = Ads.objects.all()
        categories = Category.objects.all()
        context = {'ads': ads, 'categories': categories}
        return render(request, 'ads/index.html', context)

def by_category(request,category_id):
    ads = Ads.objects.filter(category=category_id)
    categories = Category.objects.all()
    current_category = Category.objects.get(pk=category_id)
    context = {'ads': ads, 'categories': categories, 'current_category': current_category}
    return render(request, 'ads/by_category.html', context)

def image_upload_view(request):
    if request.method == 'POST':
        form = AdsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'ads/index.html', {'form': form, 'img_obj': img_obj})
    else:
        form = AdsForm()
    return render(request, 'ads/create.html', {'form': form})

#class AdsCreateView(CreateView):
#    template_name = 'ads/create.html'
#    form_class = AdsForm(CreateView)
#    success_url = reverse_lazy('index')
#
#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        context['categories'] = Category.objects.all()
#        return context
