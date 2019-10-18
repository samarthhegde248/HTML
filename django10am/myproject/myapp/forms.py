from django import forms
from myapp.models import Register
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

class Register_ModelForm(forms.ModelForm):
	class Meta:
		model = Register
		fields = "__all__"

	def __init__(self,*args,**kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-4 mb-0'),
                Column('email', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('mobile', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Submit',css_class="btn btn-secondary")
        )



class Register_Form(forms.Form):
	name=forms.CharField(max_length=25)
	email=forms.CharField(max_length=25)
	mobile=forms.CharField(max_length=10)


	def __init__(self,*args,**kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-4 mb-0'),
                Column('email', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('mobile', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Submit',css_class="btn btn-secondary")
        )