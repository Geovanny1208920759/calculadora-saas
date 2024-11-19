from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Ruta para la página de inicio
@app.route('/')
def home():
    return '¡Bienvenido a la calculadora en línea!'

# Ruta para la calculadora
@app.route('/calcular', methods=['POST'])
def calcular():
    data = request.json
    num1 = data.get('num1')
    num2 = data.get('num2')
    operacion = data.get('operacion')

    # Validación de datos
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return jsonify({'error': 'Los números deben ser válidos'}), 400

    # Realizar la operación
    if operacion == 'suma':
        resultado = num1 + num2
    elif operacion == 'resta':
        resultado = num1 - num2
    elif operacion == 'multiplicacion':
        resultado = num1 * num2
    elif operacion == 'division':
        if num2 == 0:
            return jsonify({'error': 'No se puede dividir entre 0'}), 400
        resultado = num1 / num2
    else:
        return jsonify({'error': 'Operación no válida'}), 400

    return jsonify({'resultado': resultado})

if __name__ == '__main__':
    app.run(debug=True, port=3000)
