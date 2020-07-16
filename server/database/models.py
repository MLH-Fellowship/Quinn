from db import db

class Survey(db.Document):
    skin_types = ('Acne Prone', 'Dry', 'Oily', 'Sensitive', 'Combo', 'Normal')
    skin_concerns = ('Dryness', 'Acne', 'Large Pores', 'Oiliness', 'Aging', 
    'Razor Bumps', 'Redness', 'Sun damage')
    product_types=('Cleanser', 'Moisturizer', 'SPF', 'Shaving Cream', 
    'Deoderant', 'Facial Hair Care', 'Face Masks')
    budget = ('$25 or Less', '$25-50', 'Any Amount')
    scent_type = ('Citrus', 'Fresh', 'Woodsy', 'None')

    q_1 = db.StringField(max_length=3, choices=skin_types)
    q_3 = db.StringField(max_length=3, choices=skin_concerns)
    q_4 = db.StringField(max_length=3, choices=product_types)
    q_5 = db.StringField(max_length=1, choices=budget)
    q_6 = db.StringField(max_length=3, choices=scent_type)