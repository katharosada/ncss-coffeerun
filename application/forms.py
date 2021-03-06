"""
forms.py

Web forms based on Flask-WTForms

See: http://flask.pocoo.org/docs/patterns/wtforms/
     http://wtforms.simplecodes.com/

"""

from flask.ext.wtf import Form
from wtforms import validators, SelectField, TextField, IntegerField, DateTimeField, FloatField, BooleanField


class CoffeeForm(Form):
    person = SelectField("Addict", coerce=int)
    coffee = TextField("Coffee", [validators.Required()])
    price = FloatField("Price", default=0)
    runid = SelectField("Run", coerce=int)

class RunForm(Form):
    person = SelectField("Person", coerce=int)
    time = DateTimeField("Time of Run", [validators.Required()], format="%Y/%m/%d %H:%M")
    cafeid = SelectField("Cafe", coerce=int)
    pickup = TextField("Pickup Location")

class CafeForm(Form):
    name = TextField("Name", [validators.Required()])
    location = TextField("Location")

class PriceForm(Form):
    cafeid = SelectField("Cafe", coerce=int)
    size = SelectField("Size", [validators.Required()], choices=[("S", "S"), ("M", "M"), ("L", "L")])
    amount = FloatField("Amount", [validators.Required()])
