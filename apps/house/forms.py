from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, HTML, Field, Div, Fieldset
from django import forms
from django.forms import inlineformset_factory

from apps.helpers.custom_layout_object import Formset
from apps.project.models import Projects, Apartment, Floor, ProjectImage, Plot


class ApartmentProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ['title', 'area', 'floor', 'apartment', 'parking', 'lift', 'stair', 'address', 'geo_location',
                  'thumbnail', 'file', 'description', 'division', 'district', 'thana', 'union']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['area'].label = 'Area (ft2)'

        for fieldname in self.fields:
            self.fields[fieldname].help_text = None

        self.helper = FormHelper()
        # self.helper.form_show_labels = False
        self.helper.layout = Layout(
            Row(
                Column('title', css_class='form-group col-md-6 mb-0'),
                Column('area', css_class='form-group col-md-3 mb-0'),
                Column('floor', css_class='form-group col-md-3 mb-0'),
            ),
            Row(
                Column('division', css_class='form-group col-md-3 mb-0'),
                Column('district', css_class='form-group col-md-3 mb-0'),
                Column('thana', css_class='form-group col-md-3 mb-0'),
                Column('union', css_class='form-group col-md-3 mb-0'),
            ),
            Row(
                Column('apartment', css_class='form-group col-md-3 mb-0'),
                Column('parking', css_class='form-group col-md-3 mb-0'),
                Column('lift', css_class='form-group col-md-3 mb-0'),
                Column('stair', css_class='form-group col-md-3 mb-0'),
            ),
            Row(
                Column('address', css_class='form-group col-md-6 mb-0'),
                Column('geo_location', css_class='form-group col-md-6 mb-0'),
            ),
            Row(
                Column('thumbnail', css_class='form-group col-md-6 mb-0'),
                Column('file', css_class='form-group col-md-6 mb-0'),
            ),
            Row(
                Column('description', css_class='form-group col-md-12 mb-0'),
            ),
            Row(
                Column(
                    Submit('submit', 'Create Projects')
                )
            )
        )


class ProjectFiltersForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'get'
        self.helper.layout = Layout(
            Row(
                Column('title', css_class='form-group col-md-4 mb-0'),
                Column(HTML("""<button class="btn btn-lg btn-primary">Filter</button>"""),
                       css_class='form-group col-md-1 p-5 mb-0'),
            ),
        )