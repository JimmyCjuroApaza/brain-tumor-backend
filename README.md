# 🧠 App movil de Clasificación de Tumores Cerebrales en Imágenes MRI

[cite_start]Este repositorio contiene la implementación de una aplicación móvil cliente-servidor capaz de analizar y clasificar imágenes de resonancia magnética (MRI) para la detección de tumores cerebrales[cite: 5, 12]. 

## Enlaces y Demostración

* ** API Backend Pública (Render):** [https://brain-tumor-api-k4my.onrender.com](https://brain-tumor-api-k4my.onrender.com)
* **📱 Descarga de la Aplicación (APK):** [Instalador de Android (EAS Build)](https://expo.dev/accounts/jimmycjuro/projects/BrainTumorApp/builds/c6b37ffc-db10-4c54-9710-338537c071ad)

<img width="720" height="1600" alt="brain-tumor-backend" src="https://github.com/user-attachments/assets/5911c7b5-aea3-4936-90c5-168a948af6ea" />

##  Arquitectura del Sistema

[cite_start]El sistema mantiene una arquitectura orientada a servicios dividida en tres componentes principales[cite: 109, 110]:

* [cite_start]**📱 Frontend Móvil (React Native + Expo):** Interfaz de usuario intuitiva que permite al usuario seleccionar imágenes de la galería, enviarlas a análisis y visualizar los resultados médicos junto con un gráfico de probabilidades[cite: 110].
* [cite_start]**⚙️ Backend API (Flask - Python):** Servidor RESTful que recibe la imagen mediante peticiones POST (`multipart/form-data`) en el endpoint `/api/clasificar`, ejecuta la inferencia y devuelve la predicción en formato JSON[cite: 76, 110].
* [cite_start]**🧠 Modelo de IA (TensorFlow Lite):** Modelo de Red Neuronal Convolucional (CNN) previamente entrenado, encargado de clasificar la imagen en 4 categorías: *glioma*, *meningioma*, *notumor* (sin tumor) y *pituitary* (tumor pituitario)[cite: 68, 110].

## 🛠️ Tecnologías Utilizadas

**Frontend:**
* [cite_start]React Native (JavaScript / ES6+) [cite: 110, 582]
* [cite_start]Expo (npx create-expo-app) [cite: 118, 582]
* [cite_start]Axios (Cliente HTTP) [cite: 122, 582]
* [cite_start]Expo Image Picker [cite: 121, 582]

**Backend:**
* [cite_start]Python 3 [cite: 18]
* [cite_start]Flask & Flask-CORS [cite: 19, 21]
* [cite_start]TensorFlow Lite (CPU) [cite: 22, 110]
* [cite_start]Gunicorn (Para despliegue en Render) [cite: 20]

##  Instalación y Ejecución Local

Si deseas ejecutar este proyecto en tu entorno local, sigue estos pasos:

### 1. Configuración del Backend (Flask)
```bash
# Clonar el repositorio
git clone <tu-url-del-repositorio>

# Navegar a la carpeta del backend
cd backend

# Crear y activar entorno virtual (Ubuntu/Linux)
python3 -m venv .venv
source .venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar el servidor
python backend.py
