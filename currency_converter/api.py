from flask import request, jsonify
from currency_converter import app, utils, config


@app.errorhandler(Exception)
def handle_exception(exc):
    return jsonify(error=str(exc))


@app.route('/api/convert', methods=['GET'])
def convert():

    if 'amount' not in request.args:
        raise Exception('You didn\'t specify the \'amount\' parameter')

    try:
        amount = float(request.args['amount'])
    except ValueError:
        raise Exception('Amount must be a number')

    if amount <= 0:
        raise Exception('Amount must be more than zero')

    if 'from' not in request.args:
        raise Exception('You didn\'t specify the \'from\' parameter')

    from_currency = request.args['from']

    if 'to' not in request.args:
        raise Exception('You didn\'t specify the \'to\' parameter')

    to_currency = request.args['to']

    if (from_currency not in config.CURRENCIES) or (to_currency not in config.CURRENCIES):
        raise Exception('Available currencies: %s' % ', '.join(config.CURRENCIES))

    if from_currency == to_currency:
        raise Exception('You specified the same currency')

    try:
        result = utils.call_oxr_api('latest.json')
    except:
        raise Exception('An error has occurred')

    return jsonify(response=round((amount / result['rates'][from_currency] * result['rates'][to_currency]), 6))
