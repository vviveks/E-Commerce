from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

PAYMENT_CHOICES = (
    ('S', 'Stripe'),
    ('P', 'PayPal'),
)

class CheckoutForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs = {
            # 'class': 'form-control',
            'placeholder': 'First Name'
        }
    ))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs = {
            # 'class': 'form-control',
            'placeholder': 'Last Name'
        }
    ))
    street_address = forms.CharField(widget=forms.TextInput(
        attrs = {
            # 'class': 'form-control',
            'placeholder': 'Street Address'
        }
    ))
    apartment_address = forms.CharField(required=False, widget=forms.TextInput(
        attrs = {
            # 'class': 'form-control',
            'placeholder': 'Apartment Address'
        }
    ))
    country = CountryField(blank_label='(Select Country)').formfield(
        widget = CountrySelectWidget(attrs={
            'class': 'custom-select d-block w-100'
        }))
    zip = forms.CharField(widget=forms.TextInput(
        attrs = {
            'class': 'form-control'
        }
    ))
    same_billing_address = forms.BooleanField(widget=forms.CheckboxInput(), required=False)
    save_info = forms.BooleanField(widget=forms.CheckboxInput(), required=False)
    payment_option = forms.ChoiceField(widget=forms.RadioSelect(), choices=PAYMENT_CHOICES)

class CouponForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Promo code',
            'aria-label': "Recipient's username",
            'aria-describedby': "basic-addon2"
        }
    ))


