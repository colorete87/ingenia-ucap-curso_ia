# Transfer Learning Demo: Perros vs Gatos

Este directorio contiene una demostración práctica de Transfer Learning basada en el [tutorial oficial de TensorFlow](https://www.tensorflow.org/tutorials/images/transfer_learning).

## 🎯 Objetivo

Demostrar cómo usar modelos pre-entrenados (específicamente MobileNetV2) para clasificar imágenes de perros y gatos usando dos estrategias:

1. **Feature Extraction**: Congelar el modelo base y entrenar solo un nuevo clasificador
2. **Fine-tuning**: Descongelar algunas capas y ajustar el modelo completo

## 📁 Archivos

- `transfer_learning_demo.py`: Script principal con la demostración completa
- `requirements.txt`: Dependencias de Python necesarias
- `README.md`: Este archivo

## 🚀 Cómo ejecutar

### 1. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 2. Ejecutar la demo

```bash
python transfer_learning_demo.py
```

## 📊 Lo que hace la demo

1. **Descarga automática** del dataset de perros vs gatos
2. **Preparación de datos** con aumento de datos
3. **Creación del modelo** usando MobileNetV2 pre-entrenado
4. **Feature Extraction** (10 épocas)
5. **Fine-tuning** (10 épocas adicionales)
6. **Evaluación** del modelo final
7. **Visualizaciones** de resultados y predicciones

## 📈 Resultados esperados

- **Precisión final**: ~96-98%
- **Tiempo de ejecución**: 15-30 minutos (dependiendo del hardware)
- **Archivos generados**:
  - `transfer_learning_training_history.png`: Curvas de entrenamiento
  - `transfer_learning_predictions.png`: Predicciones en imágenes de test

## 🔧 Configuración

El script está configurado con parámetros conservadores para funcionar en la mayoría de hardware:

- **Batch size**: 32
- **Tamaño de imagen**: 160x160
- **Épocas**: 10 para cada fase
- **Learning rate**: 0.0001 (Feature Extraction), 0.00001 (Fine-tuning)

## 💡 Conceptos demostrados

- Uso de modelos pre-entrenados
- Feature Extraction vs Fine-tuning
- Data augmentation
- Regularización con Dropout
- Early stopping
- Visualización de resultados
- Evaluación de modelos

## 🛠️ Requisitos del sistema

- Python 3.7+
- TensorFlow 2.10+
- Al menos 4GB RAM
- Conexión a internet (para descargar dataset y modelo pre-entrenado)
- GPU opcional (acelera el entrenamiento)

## 📚 Recursos adicionales

- [Tutorial oficial de TensorFlow](https://www.tensorflow.org/tutorials/images/transfer_learning)
- [Documentación de Keras sobre modelos pre-entrenados](https://keras.io/api/applications/)
- [Guía de transfer learning](https://www.tensorflow.org/guide/keras/transfer_learning)
