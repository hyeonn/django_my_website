from django import forms
from .models import Board,Post,Comment,ProjectComment
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class BoardForm(forms.ModelForm): # 모델 폼 정의
	class Meta:
		model = Board
		fields = ['name', 'description','category']

class PostForm(forms.ModelForm): # 모델 폼 정의
	class Meta:
		model = Post
		fields = ['Board','title', 'content','note']
		widgets = {
			'Board': forms.Select(
				attrs={'class': 'custom-select'},
			),
			'title': forms.TextInput(
				attrs={'class': 'form-control', 'style': 'width: 100%', 'placeholder': '제목을 입력하세요.'}
			),

			'content': forms.CharField(widget=CKEditorUploadingWidget()),

			'note': forms.TextInput(
				attrs={'class': 'form-control', 'style': 'width: 82.2%', 'placeholder': '제목을 입력하세요.'}
			),
		}


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['writer','content','password']

class ProjectCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['writer','content','password']
