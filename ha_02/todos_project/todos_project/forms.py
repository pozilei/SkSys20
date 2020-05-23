from django.forms import ModelForm

class TodoForm(ModelForm):
    class Meta:        
        fields = ['description', 'due', 'accomplished',]