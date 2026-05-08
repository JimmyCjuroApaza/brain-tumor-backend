from flask import Flask, request, jsonify
from flask_cors import CORS
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
import os
from werkzeug.utils import secure_filename
import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt

app = Flask(__name__)
CORS(app)

# Cargar modelo TFLite
interpreter = tf.lite.Interpreter(
    model_path='brain_tumor_cnn.tflite'
)

interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Clases del modelo
class_names = [
    'glioma',
    'meningioma',
    'notumor',
    'pituitary'
]

# Carpeta uploads
UPLOAD_FOLDER = os.path.join('static', 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def predict_with_tflite(img_array):
    """
    Ejecuta inferencia usando TensorFlow Lite
    """

    # Normalizar imagen
    img_array = img_array.astype(np.float32) / 255.0

    # Enviar tensor al modelo
    interpreter.set_tensor(
        input_details[0]['index'],
        img_array
    )

    # Ejecutar inferencia
    interpreter.invoke()

    # Obtener salida
    output_data = interpreter.get_tensor(
        output_details[0]['index']
    )

    return output_data[0]


@app.route('/')
def home():
    return jsonify({
        'message': 'API Flask funcionando correctamente'
    })


@app.route('/api/clasificar', methods=['POST'])
def clasificar_api():

    # Verificar si llegó imagen
    file = request.files.get('image')

    if not file:
        return jsonify({
            'error': 'No se envio imagen'
        }), 400

    # Guardar imagen
    filename = secure_filename(file.filename)

    filepath = os.path.join(
        app.config['UPLOAD_FOLDER'],
        filename
    )

    file.save(filepath)

    # Cargar imagen
    img = image.load_img(
        filepath,
        target_size=(128, 128)
    )

    # Convertir a array
    img_array = image.img_to_array(img)

    # Expandir dimensiones
    img_array = np.expand_dims(
        img_array,
        axis=0
    )

    # Predicción
    prediction = predict_with_tflite(img_array)

    # Clase con mayor probabilidad
    predicted_class = class_names[
        np.argmax(prediction)
    ]

    # Probabilidades
    probabilities = {
        class_names[i]: float(f'{prob:.4f}')
        for i, prob in enumerate(prediction)
    }

    # Respuesta JSON
    return jsonify({
        'prediction': f'Prediccion: {predicted_class.upper()}',
        'image_name': filename,
        'probs': probabilities
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)