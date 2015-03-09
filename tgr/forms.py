from django.forms import ModelForm
from tgr.models import Feedback

class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        exclude = ['community']