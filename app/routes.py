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
        result=result,
        value=value,
        from_unit=from_unit,
        to_unit=to_unit,
        units=LENGTH_UNITS,
    )
