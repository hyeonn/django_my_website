from django import forms
from .models import Board,Post


class BoardForm(forms.ModelForm): # 모델 폼 정의
	class Meta:
		model = Board
		fields = ['name', 'description','category']

class PostForm(forms.ModelForm): # 모델 폼 정의
	class Meta:
		model = Post
		fields = ['title', 'content','note']