from flask import render_template, request

from app import app

LENGTH_UNITS = {
    'cm': 0.01,
    'm': 1.0,
    'km': 1000.0,
    'inch': 0.0254,
    'foot': 0.3048,
    'yard': 0.9144,
    'mile': 1609.344,
}

WEIGHT_UNITS = {
    'mg': 0.000001,
    'g': 0.001,
    'kg': 1.0,
    't': 1000.0,
    'oz': 0.028349523125,
    'lb': 0.45359237,
    'stone': 6.35029318,
}

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/length', methods=['GET', 'POST'])
def length():
    result = None
    value = ''
    from_unit = 'm'
    to_unit = 'cm'

    if request.method == 'POST':
        value = request.form.get('value', '').strip()
        from_unit = request.form.get('from_unit', 'm')
        to_unit = request.form.get('to_unit', 'cm')

        try:
            if not value or len(value) > 20:
                raise ValueError
            amount = float(value)
            if amount != amount or amount in (float('inf'), float('-inf')):
                raise ValueError
            if from_unit not in LENGTH_UNITS or to_unit not in LENGTH_UNITS:
                raise ValueError
        except ValueError:
            result = 'Please enter a valid number.'
        else:
            converted = amount * LENGTH_UNITS[from_unit] / LENGTH_UNITS[to_unit]
            result = f'{amount:.10g} {from_unit} = {converted:.10g} {to_unit}'

    return render_template(
        'length.html',
        unit_of='length',
        result=result,
        value=value,
        from_unit=from_unit,
        to_unit=to_unit,
        units=LENGTH_UNITS,
    )

@app.route('/weight', methods=['GET', 'POST'])
def weight():
    result = None
    value = ''
    from_unit = 'kg'
    to_unit = 'g'

    if request.method == 'POST':
        value = request.form.get('value', '').strip()
        from_unit = request.form.get('from_unit', 'kg')
        to_unit = request.form.get('to_unit', 'g')

        try:
            if not value or len(value) > 20:
                raise ValueError
            amount = float(value)
            if amount != amount or amount in (float('inf'), float('-inf')):
                raise ValueError
            if from_unit not in WEIGHT_UNITS or to_unit not in WEIGHT_UNITS:
                raise ValueError
        except ValueError:
            result = 'Please enter a valid number'
        else:
            converted = amount * WEIGHT_UNITS[from_unit] / WEIGHT_UNITS[to_unit]
            result = f'{amount:.10g} {from_unit} = {converted:.10g} {to_unit}'


    return render_template(
        'weight.html',
        unit_of='weight',
        result=result,
        value=value,
        from_unit=from_unit,
        to_unit=to_unit,
        units=WEIGHT_UNITS,
    )
