#!/usr/bin/env python3
"""
Transfer Learning Demo: Clasificación de Perros vs Gatos
Basado en el tutorial oficial de TensorFlow:
https://www.tensorflow.org/tutorials/images/transfer_learning

Este script demuestra:
1. Feature Extraction con MobileNetV2
2. Fine-tuning del modelo
3. Evaluación y predicciones
"""

import os
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras import layers, Model
from tensorflow.keras.preprocessing import image_dataset_from_directory
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping
import warnings
warnings.filterwarnings('ignore')

# Configurar GPU si está disponible
print("GPU disponible:", tf.config.list_physical_devices('GPU'))

# Configuración de parámetros
BATCH_SIZE = 32
IMG_SIZE = (160, 160)
LEARNING_RATE = 0.0001
EPOCHS_FEATURE_EXTRACTION = 10
EPOCHS_FINE_TUNING = 10

class TransferLearningDemo:
    def __init__(self):
        self.model = None
        self.history_feature_extraction = None
        self.history_fine_tuning = None
        self.class_names = ['cat', 'dog']
        
    def download_and_prepare_data(self):
        """
        Descarga y prepara el dataset de perros vs gatos
        """
        print("🔄 Preparando datos...")
        
        # URL del dataset (versión pequeña para demo)
        dataset_url = "https://storage.googleapis.com/mledu-datasets/cats_and_dogs_filtered.zip"
        path_to_zip = tf.keras.utils.get_file('cats_and_dogs.zip', origin=dataset_url, extract=True)
        PATH = os.path.join(os.path.dirname(path_to_zip), 'cats_and_dogs_filtered')
        
        # Crear datasets
        train_dir = os.path.join(PATH, 'train')
        validation_dir = os.path.join(PATH, 'validation')
        
        train_dataset = image_dataset_from_directory(
            train_dir,
            shuffle=True,
            batch_size=BATCH_SIZE,
            image_size=IMG_SIZE
        )
        
        validation_dataset = image_dataset_from_directory(
            validation_dir,
            shuffle=True,
            batch_size=BATCH_SIZE,
            image_size=IMG_SIZE
        )
        
        # Optimizar para rendimiento
        AUTOTUNE = tf.data.AUTOTUNE
        train_dataset = train_dataset.prefetch(buffer_size=AUTOTUNE)
        validation_dataset = validation_dataset.prefetch(buffer_size=AUTOTUNE)
        
        print(f"✅ Datos preparados:")
        print(f"   - Conjunto de entrenamiento: {len(train_dataset)} batches")
        print(f"   - Conjunto de validación: {len(validation_dataset)} batches")
        print(f"   - Tamaño de imagen: {IMG_SIZE}")
        print(f"   - Tamaño de batch: {BATCH_SIZE}")
        
        return train_dataset, validation_dataset
    
    def create_model(self):
        """
        Crea el modelo con MobileNetV2 como base
        """
        print("🏗️ Creando modelo...")
        
        # Cargar MobileNetV2 pre-entrenado
        base_model = MobileNetV2(
            input_shape=IMG_SIZE + (3,),
            include_top=False,
            weights='imagenet'
        )
        
        # Congelar el modelo base
        base_model.trainable = False
        
        # Agregar capas de clasificación
        inputs = tf.keras.Input(shape=IMG_SIZE + (3,))
        
        # Preprocesamiento (normalización)
        x = tf.keras.applications.mobilenet_v2.preprocess_input(inputs)
        
        # Modelo base
        x = base_model(x, training=False)
        
        # Global Average Pooling
        x = layers.GlobalAveragePooling2D()(x)
        
        # Dropout para regularización
        x = layers.Dropout(0.2)(x)
        
        # Capa de salida
        outputs = layers.Dense(1)(x)
        
        # Crear modelo
        model = Model(inputs, outputs)
        
        print("✅ Modelo creado:")
        print(f"   - Modelo base: MobileNetV2 (congelado)")
        print(f"   - Capas totales: {len(model.layers)}")
        print(f"   - Parámetros entrenables: {model.count_params():,}")
        
        return model, base_model
    
    def train_feature_extraction(self, train_dataset, validation_dataset):
        """
        Entrena el modelo usando Feature Extraction
        """
        print("\n🔒 Iniciando Feature Extraction...")
        
        # Compilar modelo
        self.model.compile(
            optimizer=Adam(learning_rate=LEARNING_RATE),
            loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
            metrics=['accuracy']
        )
        
        # Callbacks
        early_stopping = EarlyStopping(
            monitor='val_accuracy',
            patience=3,
            restore_best_weights=True
        )
        
        # Entrenar
        print(f"🚀 Entrenando por {EPOCHS_FEATURE_EXTRACTION} épocas...")
        self.history_feature_extraction = self.model.fit(
            train_dataset,
            epochs=EPOCHS_FEATURE_EXTRACTION,
            validation_data=validation_dataset,
            callbacks=[early_stopping],
            verbose=1
        )
        
        print("✅ Feature Extraction completado")
        return self.history_feature_extraction
    
    def fine_tune_model(self, base_model, train_dataset, validation_dataset):
        """
        Fine-tuning del modelo
        """
        print("\n🔧 Iniciando Fine-tuning...")
        
        # Descongelar las últimas 100 capas
        base_model.trainable = True
        
        # Encontrar cuántas capas descongelar
        fine_tune_at = len(base_model.layers) - 100
        print(f"📊 Descongelando {len(base_model.layers) - fine_tune_at} capas")
        
        # Congelar las capas anteriores
        for layer in base_model.layers[:fine_tune_at]:
            layer.trainable = False
        
        # Recompilar con learning rate más bajo
        self.model.compile(
            optimizer=Adam(learning_rate=LEARNING_RATE/10),
            loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
            metrics=['accuracy']
        )
        
        print(f"📈 Parámetros entrenables: {self.model.count_params():,}")
        print(f"🚀 Fine-tuning por {EPOCHS_FINE_TUNING} épocas...")
        
        # Entrenar
        self.history_fine_tuning = self.model.fit(
            train_dataset,
            epochs=EPOCHS_FINE_TUNING,
            initial_epoch=self.history_feature_extraction.epoch[-1],
            validation_data=validation_dataset,
            verbose=1
        )
        
        print("✅ Fine-tuning completado")
        return self.history_fine_tuning
    
    def plot_training_history(self):
        """
        Grafica las curvas de entrenamiento
        """
        print("\n📊 Generando gráficos de entrenamiento...")
        
        # Combinar historiales
        acc = self.history_feature_extraction.history['accuracy']
        val_acc = self.history_feature_extraction.history['val_accuracy']
        
        loss = self.history_feature_extraction.history['loss']
        val_loss = self.history_feature_extraction.history['val_loss']
        
        if self.history_fine_tuning:
            acc += self.history_fine_tuning.history['accuracy']
            val_acc += self.history_fine_tuning.history['val_accuracy']
            
            loss += self.history_fine_tuning.history['loss']
            val_loss += self.history_fine_tuning.history['val_loss']
        
        # Crear gráfico
        plt.figure(figsize=(12, 8))
        
        # Gráfico de precisión
        plt.subplot(2, 1, 1)
        plt.plot(acc, label='Precisión de Entrenamiento', color='blue')
        plt.plot(val_acc, label='Precisión de Validación', color='red')
        plt.axvline(x=len(self.history_feature_extraction.history['accuracy'])-1, 
                   color='green', linestyle='--', alpha=0.7, label='Inicio Fine-tuning')
        plt.ylim([0.7, 1.0])
        plt.legend()
        plt.title('Precisión de Entrenamiento y Validación')
        plt.ylabel('Precisión')
        
        # Gráfico de pérdida
        plt.subplot(2, 1, 2)
        plt.plot(loss, label='Pérdida de Entrenamiento', color='blue')
        plt.plot(val_loss, label='Pérdida de Validación', color='red')
        plt.axvline(x=len(self.history_feature_extraction.history['loss'])-1, 
                   color='green', linestyle='--', alpha=0.7, label='Inicio Fine-tuning')
        plt.ylim([0, 1.0])
        plt.legend()
        plt.title('Pérdida de Entrenamiento y Validación')
        plt.xlabel('Época')
        plt.ylabel('Pérdida')
        
        plt.tight_layout()
        plt.savefig('transfer_learning_training_history.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        print("✅ Gráficos guardados como 'transfer_learning_training_history.png'")
    
    def evaluate_model(self, validation_dataset):
        """
        Evalúa el modelo en el conjunto de validación
        """
        print("\n📊 Evaluando modelo...")
        
        loss, accuracy = self.model.evaluate(validation_dataset, verbose=0)
        print(f"✅ Resultados de evaluación:")
        print(f"   - Precisión: {accuracy:.4f} ({accuracy*100:.2f}%)")
        print(f"   - Pérdida: {loss:.4f}")
        
        return loss, accuracy
    
    def make_predictions(self, validation_dataset, num_images=9):
        """
        Hace predicciones en un conjunto de imágenes
        """
        print(f"\n🔮 Haciendo predicciones en {num_images} imágenes...")
        
        # Obtener un batch de imágenes
        image_batch, label_batch = next(iter(validation_dataset))
        
        # Hacer predicciones
        predictions = self.model.predict(image_batch, verbose=0)
        
        # Convertir a clases (0 = gato, 1 = perro)
        predicted_classes = tf.where(predictions < 0, 0, 1).numpy().flatten()
        true_classes = label_batch.numpy()
        
        # Crear gráfico de predicciones
        plt.figure(figsize=(12, 12))
        for i in range(min(num_images, len(image_batch))):
            plt.subplot(3, 3, i + 1)
            
            # Desnormalizar imagen
            img = image_batch[i].numpy()
            img = (img - img.min()) / (img.max() - img.min())
            
            plt.imshow(img)
            
            # Color del título según si la predicción es correcta
            predicted_class = self.class_names[predicted_classes[i]]
            true_class = self.class_names[true_classes[i]]
            
            if predicted_classes[i] == true_classes[i]:
                title_color = 'green'
                status = '✓'
            else:
                title_color = 'red'
                status = '✗'
            
            plt.title(f'{status} Pred: {predicted_class}\nReal: {true_class}', 
                     color=title_color, fontsize=10)
            plt.axis('off')
        
        plt.suptitle('Predicciones del Modelo', fontsize=16)
        plt.tight_layout()
        plt.savefig('transfer_learning_predictions.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        print("✅ Predicciones guardadas como 'transfer_learning_predictions.png'")
        
        # Mostrar estadísticas
        correct_predictions = sum(predicted_classes[:num_images] == true_classes[:num_images])
        accuracy_sample = correct_predictions / num_images
        print(f"📈 Precisión en muestra: {accuracy_sample:.2%} ({correct_predictions}/{num_images})")
    
    def run_complete_demo(self):
        """
        Ejecuta la demostración completa
        """
        print("🚀 Iniciando Demo de Transfer Learning")
        print("=" * 50)
        
        try:
            # 1. Preparar datos
            train_dataset, validation_dataset = self.download_and_prepare_data()
            
            # 2. Crear modelo
            self.model, base_model = self.create_model()
            
            # 3. Feature Extraction
            self.train_feature_extraction(train_dataset, validation_dataset)
            
            # 4. Fine-tuning
            self.fine_tune_model(base_model, train_dataset, validation_dataset)
            
            # 5. Evaluación
            loss, accuracy = self.evaluate_model(validation_dataset)
            
            # 6. Gráficos
            self.plot_training_history()
            
            # 7. Predicciones
            self.make_predictions(validation_dataset)
            
            print("\n🎉 Demo completado exitosamente!")
            print(f"📊 Precisión final: {accuracy:.2%}")
            
        except Exception as e:
            print(f"❌ Error durante la demo: {str(e)}")
            print("💡 Asegúrate de tener una conexión a internet para descargar el dataset")

def main():
    """
    Función principal
    """
    print("🐱🐶 Transfer Learning Demo: Perros vs Gatos")
    print("Basado en: https://www.tensorflow.org/tutorials/images/transfer_learning")
    print("=" * 60)
    
    # Crear y ejecutar demo
    demo = TransferLearningDemo()
    demo.run_complete_demo()

if __name__ == "__main__":
    main()
