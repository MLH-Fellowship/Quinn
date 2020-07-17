from .db import db
from wtforms import Form, fields, validators
from wtforms.validators import Required

class SurveyForm(Form):
    skin_types = ('Combination', 'Dry', 'Oily','Combo', 'Normal', 'Sensitive')
    product_types=('Cleanser', 'Moisturizer', 'SPF', 
    'Face Masks')
    budget = ('$25 or Less', '$25-50', 'Any Amount')


    q_1 = fields.SelectField(choices=skin_types, validators=[Required()])
    q_2 = fields.SelectField(choices=product_types, validators=[Required()])
    q_3 = fields.SelectField(choices=budget, validators=[Required()])
 

    submit = fields.SubmitField('Submit')