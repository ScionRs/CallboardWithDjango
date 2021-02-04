from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from ads.views import index, by_category, image_upload_view #AdsCreateView

urlpatterns = [
    #path('add/', AdsCreateView.as_view(), name='add'),
    path('add/', image_upload_view,name='add'),
    path('<int:category_id>/', by_category, name='by_category'),
    path('', index, name='index')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)