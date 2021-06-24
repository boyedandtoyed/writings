from django import forms
from ckeditor.widgets import CKEditorWidget
from . import models

class WritingCreationForm(forms.ModelForm):
    class Meta:
        model = models.Writing
        fields = '__all__'
        exclude = ('main_author',"post_date", "updated_at", "slug")
        
        labels ={
            'headline':'Enter your consice Headline in less than 120 characters to grab reader.',
            'cover':'Upload a great cover image for you writing. Make sure, it is either in jpg, gif, png or webp format',
            'textarea':"Write your writings that is at least 100 words and no more than 2000 words. So that you can pin point your ideas and make room for people to read more in less time."
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['textarea'].widget = CKEditorWidget(attrs={'id': ("textarea"), })
        self.fields['headline'].widget.attrs={'placeholder': ("e.g:- A question for liberty, that changed me."), }
        
        
    

