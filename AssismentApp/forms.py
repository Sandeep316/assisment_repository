from django import forms

class ReviewForm(forms.Form):
    product_id = forms.CharField(
        label="Product ID",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Product ID'
            }
        )
    )
    review_title=forms.CharField(
        label="Review Title",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Review Title'
            }
        )
    )
    review_ratings = forms.IntegerField(
        label="Review Rating",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Review Rating'
            }
        )
    )
    review_content = forms.CharField(
        label="Review Content",
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Review Title'
            }
        )
    )