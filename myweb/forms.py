from django import forms
from .models import Board


class BoardForm(forms.ModelForm): # 모델 폼 정의
	class Meta:
		model = Board
		fields = ['name', 'description','category']