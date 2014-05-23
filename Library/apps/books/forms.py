
from django import forms

class LoginForm(forms.Form):
	username = forms.CharField(widget = forms.TextInput())
	password = forms.CharField(widget = forms.PasswordInput(render_value = False))

class addNewsForm(forms.Form):
	title 		= forms.CharField(max_length=50)
	newsImage	= forms.ImageField(required=False)#cambiar para poder agregarla
	date 		= forms.DateField()
	description = forms.CharField(widget = forms.Textarea)

	def clean(self):#sirve para validar la informacion ingresada por el usuario
		return self.cleaned_data

class addPublisherForm(forms.Form):
	name 			= forms.CharField(max_length = 30)
	address 		= forms.CharField(max_length = 50)
	city 			= forms.CharField(max_length = 60)
	state_province 	= forms.CharField(max_length = 50)
	website 		= forms.URLField(max_length=200)
	logotype 		= forms.ImageField(required=False)#cambiar....
	

	def clean(self):#sirve para validar la informacion ingresada por el usuario
		return self.cleaned_data


class addAuthorForm(forms.Form):
	first_name 		= forms.CharField(max_length = 30)
	last_name 		= forms.CharField(max_length = 40)
	email 			= forms.EmailField()
	biography 		= forms.CharField(widget = forms.Textarea)
	photo 			= forms.ImageField(required=False)#cmabir.........
	
	

	def clean(self):#sirve para validar la informacion ingresada por el usuario
		return self.cleaned_data
	
