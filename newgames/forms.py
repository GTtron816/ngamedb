from django import forms
from .models import Game,Comment

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('body',)

		widgets = {
			'body': forms.Textarea(attrs={'class': 'form-control'}),			
			
		}
  
class AddGameForm(forms.ModelForm):
	class Meta:
		model = Game
		fields=('title','dev','pub','gen','gtype','syn','title_img','sc1','sc2','sc3','trailer','plat')
		
