from .db import db
from wtforms import Form, fields, validators

class SurveyForm(Form):
    skin_types = ('Combination', 'Dry', 'Oily','Combo', 'Normal', 'Sensitive')
    product_types=('Cleanser', 'Moisturizer', 'SPF', 
    'Face Masks')
    budget = ('$25 or Less', '$25-50', 'Any Amount')


    q_1 = fields.SelectField(max_length=3, choices=skin_types, validators=[Required()])
    q_2 = fields.SelectField(max_length=3, choices=product_types, validators=[Required()])
    q_3 = fields.SelectField(max_length=1, choices=budget, validators=[Required()])
 

    submit = SubmitField('Submit')