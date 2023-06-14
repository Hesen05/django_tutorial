from django import forms    
from home.models import Contact, Subscribe,Comment

class ContactForm(forms.Form):

    name = forms.CharField( max_length = 20, min_length = 3,
                            widget = forms.TextInput( attrs = {
                                'class': 'form-control' ,
                                'placeholder':'Your name'
                                                        }))
    email = forms.CharField( max_length = 30, min_length = 10,
                            widget = forms.EmailInput( attrs = {
                                'class' : 'form-control',
                                'placeholder':'Email'

                            }))
    subject = forms.ChoiceField( choices=[(1, 'Teklif'), (2, 'Irad')],
                              widget = forms.Select( attrs = {
                                    'class' : 'form-control',

                                  }))
    
    message = forms.CharField( 
                              widget = forms.Textarea( attrs ={
                                  'class' : 'form-control',
                                  'placeholder' : "Message"
                              }))
    

class ContactForm2(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name','email','subject','message']

        widgets = {
            'name':forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder':'Your name'
            }),
            'email':forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder':'email' 
                
            }), 
            'subject':forms.Select(attrs={
                'class': 'form-control',
                'placeholder':'subject'
            }),
            'message':forms.Textarea(attrs={
                'class': 'form-control', 
                'placeholder':'Message'
            })
        }


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = ['email'] 

        widgets = {
            'email': forms.EmailInput(attrs={
                'class':'form-control',
                'placeholder': 'Enter your email adress'
                


            })
 }
        
class Comment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']