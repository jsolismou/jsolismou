from flask import Flask, jsonify, request
from flask_cors import cross_origin
from random import randint
app = Flask(__name__)

# EJERCICIO

# POST -> localhost/order
# json -> {"numbers": [23, 432, 88, 90, 90, 70]} Números positivos del 1 al 1000, se pueden repetir.
# SIEMPRE SE RECIBE LISTA NUMERICA (no pasan strings, ni números negativos, y no se presupone que
# el usuario la va a liar.

# se pide:
# eliminar elementos repetidos
# ordenar de menor a mayor los restantes
# devolver en formato json:
# {"ordered_numbers" : [23, 70, 88, 90, 432]}


@app.route('/random')
@cross_origin()
def random_number():
    first_num = int(request.args.get('first_num'))
    second_num = int(request.args.get('second_num'))
    pupil_name = request.args.get('pupil_name')
    print(f'{pupil_name} holaaaaaaaaaa')
    return str(randint(first_num, second_num))



@app.route('/order', methods=['POST'])
def order():
    data = request.json
    numbers = data.get('numbers')
    numbers = set(numbers)
    numbers = list(numbers)
    numbers = sorted(numbers)
    return jsonify(numbers)



app.run(host='0.0.0.0', port=80, debug=True)
