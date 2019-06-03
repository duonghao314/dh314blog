from cProfile import label

from django import forms


class CommentForms(forms.Form):
    replyFormComment = forms.CharField(label='replyFormComment')
    replyFormName = forms.CharField(label='replyFormName')
    replyFormEmail = forms.CharField(label='replyFormEmail')
