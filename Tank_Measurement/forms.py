from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from models import KulindrikesDexamenes
from models import Kausima

class ExampleForm(forms.Form):
    like_website = forms.TypedChoiceField(
        label = "Do you like this website?",
        choices = ((1, "Yes"), (0, "No")),
        coerce = lambda x: bool(int(x)),
        widget = forms.RadioSelect,
        initial = '1',
        required = True,
    )
    checkbox_input = forms.TypedChoiceField(
        label = "Do you like this website?",
        choices = ((1, "Yes"), (0, "No")),
        coerce = lambda x: bool(int(x)),
        widget = forms.RadioSelect,
        initial = '1',
        required = True,
    )
    favorite_food = forms.CharField(
        label = "What is your favorite food?",
        max_length = 80,
        required = True,
    )
    favorite_color = forms.CharField(
        label = "What is your favorite color?",
        max_length = 80,
        required = True,
    )
    favorite_number = forms.IntegerField(
        label = "Favorite number",
        required = False,
    )
    favorite_number1 = forms.ModelChoiceField(
        queryset=KulindrikesDexamenes.objects.all(),
        initial=1,
        label="Favorite number",
        required=False,
    )
    favorite_number2 = forms.ModelChoiceField(
        queryset=Kausima.objects.all(),
        empty_label=None,
        help_text='Fuels',
        label="Favorite number2222",
        required=True,
    )
    favorite_number3 = forms.ModelMultipleChoiceField(
        queryset=Kausima.objects.all(),
        initial=1,
        label="Favorite number",
        required=False,
    )

    notes = forms.CharField(
        label = "Additional notes or feedback",
        required = False,
    )

    def __init__(self, *args, **kwargs):
        super(ExampleForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.add_input(Submit('submit', 'Submit'))

    def save(self, **kwargs):
        self.clean()
        return super(ExampleForm, self).save(**kwargs)

    def clean(self):
        cleaned_data = super(ExampleForm, self).clean()
        checkbox_input = cleaned_data.get("checkbox_input")

        if checkbox_input and checkbox_input == True:
            raise forms.ValidationError([
                'This is a global error',
                'This is another global error',
                'Uncheck the "Checkbox input" to ignore these errors']
            )

        # Always return the full collection of cleaned data.
        print cleaned_data
        print 'Leonidas'
        return cleaned_data

