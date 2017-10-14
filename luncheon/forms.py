from django import forms
    
class AddFavoriteEateryForm(forms.Form):
    confirm_favorite = forms.BooleanField(label="Favorite this eatery?")
