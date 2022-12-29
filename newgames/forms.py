from django import forms
from .models import Game,Comment
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        labels={
		 'body': 'Write Comment',
        
	 }
        widgets = {
			'body': forms.Textarea(attrs={'class': 'form-control'}),			
		}
  
class AddGameForm(forms.ModelForm):
    class Meta:
     model = Game
     fields=('title','dev','pub','gen','gtype','syn','title_img','sc1','sc2','sc3','trailer','plat')
     labels={
		 'title': 'Title',
         'dev': 'Developer',
         'pub': 'Publisher',
         'gen': 'Genre',
         'gtype': 'Game Type',
         'syn': 'Synopsis',
         'title_img': 'Title Image',
         'sc1': 'Screenshot 1',
         'sc2': 'Screenshot 2',
         'sc3': 'Screenshot 3',
         'trailer': 'Trailer',
         'plat': 'Platform',
	 }
     widgets= {
         'title': forms.TextInput(attrs={'class': 'form-control'}),
         'dev': forms.TextInput(attrs={'class': 'form-control'}),
         'pub': forms.TextInput(attrs={'class': 'form-control'}),
         'gen': forms.TextInput(attrs={'class': 'form-control'}),
         'gtype': forms.TextInput(attrs={'class': 'form-control'}),
         'syn': forms.Textarea(attrs={'class': 'form-control'}),
         'title_img': forms.FileInput(attrs={'class': 'form-control'}),
         'sc1': forms.FileInput(attrs={'class': 'form-control'}),
         'sc2': forms.FileInput(attrs={'class': 'form-control'}),
         'sc3': forms.FileInput(attrs={'class': 'form-control'}),
         'trailer': forms.TextInput(attrs={'class': 'form-control'}),
         'plat': forms.TextInput(attrs={'class': 'form-control'}),
         }
