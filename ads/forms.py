from django.forms import ModelForm

from ads.models import Ads


class AdsForm(ModelForm):
    class Meta:
        model = Ads
        fields = ('title', 'content', 'price', 'photo', 'category')
