# Sección 4: Práctica y Aplicación

## Material de Soporte para el Curso de Fine-Tuning

---

# 4.1 Ejercicio Práctico: Dos Caminos para Fine-Tuning

## 🎯 Objetivos de esta Sección

Al finalizar esta sección, los participantes podrán:
- **Elegir entre dos enfoques:** OpenAI (sin código) o programático (con código)
- **Superar el desafío principal:** Preparación efectiva del dataset
- Aplicar fine-tuning en un caso real
- Evaluar y mejorar sus modelos

---

## 🚀 Introducción: El Gran Desafío

### **La Realidad del Fine-Tuning**
**El 80% del trabajo está en los datos, no en el modelo.**

Como construir una casa:
- **20% del tiempo:** Construir la estructura
- **80% del tiempo:** Preparar los cimientos y materiales

### **¿Por qué es difícil preparar el dataset?**
- **Calidad inconsistente** - Datos reales son "sucios"
- **Cantidad insuficiente** - Necesitas más ejemplos de los que crees
- **Formato específico** - Cada herramienta tiene sus reglas
- **Sesgos ocultos** - Los datos reflejan prejuicios no deseados

---

## 🛤️ Dos Caminos, Una Meta

### **Camino 1: OpenAI (Sin Código) 👨‍💼**
- **Para quien:** Profesionales, managers, consultores
- **Ventajas:** Interfaz visual, rápido, resultados profesionales
- **Desventajas:** Costo por uso, menos control
- **Tiempo:** 2-4 horas

### **Camino 2: Código (Técnico) 👨‍💻**
- **Para quien:** Desarrolladores, científicos de datos
- **Ventajas:** Control total, gratuito, personalizable
- **Desventajas:** Requiere programación, más tiempo
- **Tiempo:** 1-2 días

### **Ambos enfrentan el mismo desafío: ¡Los datos!**

---

## 📋 Casos de Uso Sugeridos

### **Nivel Principiante (Recomendado)**
1. **Chatbot de FAQ** - Responder preguntas frecuentes de tu negocio
2. **Clasificador de emails** - Organizar mensajes por prioridad
3. **Generador de respuestas** - Crear respuestas consistentes

### **Nivel Intermedio**
4. **Asistente de ventas** - Ayudar en conversaciones comerciales
5. **Analizador de sentimientos** - Evaluar feedback de clientes
6. **Redactor de contenido** - Generar posts para redes sociales

### **Nivel Avanzado**
7. **Tutor personalizado** - Enseñar conceptos específicos
8. **Analista de documentos** - Extraer información de contratos
9. **Asistente especializado** - Dominio técnico específico

---

# 4.2 OPCIÓN 1: Fine-Tuning con OpenAI (Sin Código)

## 🎯 Para Profesionales y Managers

### **Ventajas de este enfoque:**
- **Sin programación** - Interfaz web intuitiva
- **Resultados rápidos** - 2-4 horas total
- **Soporte técnico** - Documentación y ayuda oficial
- **Modelos potentes** - GPT-3.5 y GPT-4

---

## 🚧 El Desafío Principal: Preparar el Dataset

### **Paso 1: Recolección de Datos (El 60% del trabajo)**

#### **Estrategias para obtener datos de calidad:**

**A. Método de Observación Directa**
- **Registra conversaciones reales** de tu negocio (con permisos)
- **Documenta preguntas frecuentes** que recibes
- **Anota respuestas exitosas** que funcionan bien

**B. Método de Simulación**
- **Role-playing:** Actúa como cliente y como empresa
- **Escenarios variados:** Diferentes tipos de consultas
- **Casos extremos:** Situaciones difíciles o poco comunes

**C. Método de Expansión**
- **Partir de 5-10 casos reales** bien documentados
- **Crear variaciones** de cada caso
- **Cambiar contexto** manteniendo la estructura

### **Ejemplo Práctico: Chatbot de Restaurante**

**Caso base real:**
```
Cliente: "¿Tienen opciones vegetarianas?"
Restaurante: "Sí, tenemos ensalada César, pasta primavera y hamburguesa de quinoa."
```

**Expansión del dataset (crear 20+ variaciones):**
```
"¿Qué platos vegetarianos ofrecen?"
"Soy vegetariano, ¿qué me recomiendan?"
"¿Tienen comida sin carne?"
"Mi novia no come carne, ¿qué opciones hay?"
```

---

## 📋 Paso a Paso: OpenAI Fine-Tuning

### **Paso 2: Formato JSONL (15 minutos)**

**Plantilla obligatoria para OpenAI:**
```json
{"messages": [{"role": "system", "content": "Eres el asistente de Restaurante Bella Vista. Eres amable, conoces bien el menú y ayudas a los clientes a elegir."}, {"role": "user", "content": "¿Tienen opciones vegetarianas?"}, {"role": "assistant", "content": "¡Por supuesto! Tenemos varias opciones deliciosas: ensalada César con aderezo casero, pasta primavera con vegetales frescos, y nuestra popular hamburguesa de quinoa con papas. ¿Te interesa alguna en particular?"}]}
```

**Herramienta para crear JSONL:**
- **Google Sheets/Excel:** Crear columnas y exportar
- **ChatGPT:** "Convierte estos datos a formato JSONL"
- **Plantilla online:** Usar generadores web gratuitos

### **Paso 3: Subir a OpenAI (5 minutos)**

1. **Ir a platform.openai.com**
2. **Fine-tuning → Create**
3. **Upload training file**
4. **Elegir modelo base:** GPT-3.5-turbo
5. **Configurar parámetros básicos**

### **Paso 4: Entrenar y Esperar (1-6 horas)**

**Configuración recomendada:**
- **Epochs:** 3-5 (más puede ser contraproducente)
- **Batch size:** Automático
- **Learning rate:** Automático

**Durante la espera:**
- **Preparar casos de prueba** para evaluar el modelo
- **Documentar el proceso** para futuras iteraciones

### **Paso 5: Probar el Modelo (30 minutos)**

**Casos de prueba obligatorios:**
- **Casos del dataset:** Debe responder perfectamente
- **Casos similares:** Variaciones de los ejemplos
- **Casos nuevos:** Situaciones no vistas
- **Casos límite:** Preguntas difíciles o fuera de contexto

---

# 4.3 OPCIÓN 2: Fine-Tuning con Código

## 🎯 Para Desarrolladores y Científicos de Datos

### **Ventajas de este enfoque:**
- **Control total** - Todos los parámetros ajustables
- **Costo cero** - Usar Hugging Face gratuito
- **Flexibilidad** - Cualquier modelo, cualquier formato
- **Aprendizaje profundo** - Entender cada paso

---

## 🚧 El Mismo Desafío: Dataset de Calidad

### **Paso 1: Recolección Avanzada de Datos**

#### **Técnicas programáticas para dataset:**

**A. Web Scraping Ético**
```python
# Ejemplo: Extraer FAQs de tu sitio web
import requests
from bs4 import BeautifulSoup

def extract_faqs(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    faqs = []
    for faq in soup.find_all('div', class_='faq-item'):
        question = faq.find('h3').text.strip()
        answer = faq.find('p').text.strip()
        faqs.append({'question': question, 'answer': answer})
    
    return faqs
```

**B. Síntesis de Datos con IA**
```python
# Usar GPT para generar más ejemplos
import openai

def generate_variations(base_examples):
    variations = []
    for example in base_examples:
        prompt = f"""
        Genera 5 variaciones de esta conversación manteniendo el mismo tono y propósito:
        Pregunta: {example['question']}
        Respuesta: {example['answer']}
        """
        response = openai.Completion.create(
            model="gpt-3.5-turbo",
            prompt=prompt,
            max_tokens=500
        )
        variations.extend(parse_variations(response.choices[0].text))
    return variations
```

**C. Augmentación de Datos**
```python
# Crear variaciones automáticas
import random

def augment_data(examples):
    augmented = []
    
    # Sinónimos y variaciones
    synonyms = {
        "hola": ["buenos días", "saludos", "qué tal"],
        "ayuda": ["asistencia", "soporte", "apoyo"],
        "producto": ["artículo", "item", "mercancía"]
    }
    
    for example in examples:
        # Original
        augmented.append(example)
        
        # Con sinónimos
        text = example['text']
        for word, syns in synonyms.items():
            if word in text.lower():
                for syn in syns:
                    new_text = text.replace(word, syn)
                    augmented.append({
                        'text': new_text,
                        'label': example['label']
                    })
    
    return augmented
```

---

## 💻 Implementación Completa con Hugging Face

### **Paso 2: Preparación del Dataset**
```python
from datasets import Dataset
import pandas as pd

# Cargar y preparar datos
def prepare_dataset():
    # Tus datos en formato simple
    data = {
        'text': [
            "¿Tienen opciones vegetarianas?",
            "¿Qué platos sin carne ofrecen?",
            "Soy vegetariano, ¿qué me recomiendan?"
        ],
        'labels': [
            "Sí, tenemos ensalada César, pasta primavera y hamburguesa de quinoa.",
            "Ofrecemos varias opciones sin carne: ensaladas, pastas y hamburguesas vegetales.",
            "Te recomiendo nuestra hamburguesa de quinoa, es muy popular entre vegetarianos."
        ]
    }
    
    # Convertir a Dataset de Hugging Face
    dataset = Dataset.from_dict(data)
    return dataset

dataset = prepare_dataset()
```

### **Paso 3: Configuración del Modelo**
```python
from transformers import (
    AutoTokenizer, 
    AutoModelForCausalLM, 
    TrainingArguments, 
    Trainer
)

# Cargar modelo base
model_name = "microsoft/DialoGPT-small"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Configurar tokenizer
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

# Función para procesar datos
def tokenize_function(examples):
    # Combinar pregunta y respuesta
    conversations = []
    for text, label in zip(examples['text'], examples['labels']):
        conversation = f"Usuario: {text} Asistente: {label}"
        conversations.append(conversation)
    
    return tokenizer(
        conversations,
        truncation=True,
        padding=True,
        max_length=512
    )

# Tokenizar dataset
tokenized_dataset = dataset.map(tokenize_function, batched=True)
```

### **Paso 4: Entrenamiento**
```python
# Configurar entrenamiento
training_args = TrainingArguments(
    output_dir="./fine-tuned-model",
    num_train_epochs=3,
    per_device_train_batch_size=4,
    per_device_eval_batch_size=4,
    warmup_steps=100,
    weight_decay=0.01,
    logging_dir="./logs",
    logging_steps=10,
    save_strategy="epoch",
    evaluation_strategy="epoch"
)

# Crear trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset,
    tokenizer=tokenizer
)

# ¡Entrenar!
trainer.train()

# Guardar modelo
trainer.save_model("./mi-modelo-final")
tokenizer.save_pretrained("./mi-modelo-final")
```

### **Paso 5: Usar el Modelo Entrenado**
```python
# Cargar modelo entrenado
from transformers import pipeline

# Crear pipeline de conversación
chatbot = pipeline(
    "text-generation",
    model="./mi-modelo-final",
    tokenizer="./mi-modelo-final"
)

# Probar el modelo
def chat_with_model(user_input):
    prompt = f"Usuario: {user_input} Asistente:"
    
    response = chatbot(
        prompt,
        max_length=100,
        num_return_sequences=1,
        temperature=0.7,
        pad_token_id=chatbot.tokenizer.eos_token_id
    )
    
    # Extraer solo la respuesta del asistente
    full_response = response[0]['generated_text']
    assistant_response = full_response.split("Asistente:")[-1].strip()
    
    return assistant_response

# Ejemplo de uso
user_message = "¿Tienen opciones vegetarianas?"
response = chat_with_model(user_message)
print(f"Respuesta: {response}")
```

---

# 4.4 Superando el Desafío del Dataset

## 🚧 La Verdad Incómoda sobre los Datos

### **Por qué es TAN difícil preparar un buen dataset:**

**1. El Problema de la Calidad**
- **Datos del mundo real son "sucios"** - Errores, inconsistencias, ruido
- **Contexto faltante** - ¿Qué significa realmente esta respuesta?
- **Sesgos ocultos** - Los datos reflejan prejuicios no deseados

**2. El Problema de la Cantidad**
- **"Necesito solo 20 ejemplos"** ← Falso, necesitas 200+ para calidad
- **Diversidad vs Cantidad** - Mejor 50 casos diversos que 200 similares
- **Long tail** - Casos raros pero importantes son difíciles de capturar

**3. El Problema del Formato**
- **Cada herramienta es diferente** - JSONL vs CSV vs XML
- **Estructura específica** - System/User/Assistant vs Input/Output
- **Encoding y caracteres** - UTF-8, emojis, caracteres especiales

---

## 🛠️ Kit de Supervivencia para Datasets

### **Herramientas para Ambos Caminos**

#### **1. Generadores de Datos Sintéticos**
```python
# Para OpenAI y Código
import openai

def generate_training_data(topic, examples_count=50):
    """
    Genera datos de entrenamiento usando GPT-4
    """
    base_prompt = f"""
    Genera {examples_count} conversaciones realistas sobre {topic}.
    Formato: Una línea para pregunta del usuario, una línea para respuesta del asistente.
    Varía el estilo, tono y complejidad.
    
    Ejemplo:
    Usuario: ¿Cómo puedo cancelar mi pedido?
    Asistente: Puedes cancelar tu pedido desde tu cuenta en "Mis Pedidos" si aún no ha sido enviado.
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": base_prompt}],
        max_tokens=2000
    )
    
    return parse_generated_data(response.choices[0].message.content)
```

#### **2. Validador de Calidad de Datos**
```python
def validate_dataset_quality(dataset):
    """
    Valida la calidad del dataset antes del entrenamiento
    """
    issues = []
    
    # Verificar cantidad
    if len(dataset) < 30:
        issues.append("⚠️ Muy pocos ejemplos (mínimo 30)")
    
    # Verificar diversidad
    unique_inputs = len(set([item['input'] for item in dataset]))
    if unique_inputs / len(dataset) < 0.8:
        issues.append("⚠️ Poca diversidad en las preguntas")
    
    # Verificar longitud de respuestas
    avg_response_length = sum([len(item['output']) for item in dataset]) / len(dataset)
    if avg_response_length < 20:
        issues.append("⚠️ Respuestas muy cortas")
    
    # Verificar consistencia de tono
    tones = analyze_tone_consistency(dataset)
    if tones['consistency_score'] < 0.7:
        issues.append("⚠️ Tono inconsistente en las respuestas")
    
    return issues
```

#### **3. Expansor Automático de Datasets**
```python
def expand_dataset(small_dataset, target_size=100):
    """
    Expande un dataset pequeño a uno más grande manteniendo calidad
    """
    expanded = small_dataset.copy()
    
    techniques = [
        paraphrase_questions,      # Parafrasear preguntas
        add_context_variations,    # Agregar contexto
        create_negative_examples,  # Crear ejemplos negativos
        add_edge_cases,           # Agregar casos límite
        vary_response_style       # Variar estilo de respuesta
    ]
    
    while len(expanded) < target_size:
        for technique in techniques:
            new_examples = technique(small_dataset)
            expanded.extend(new_examples)
            if len(expanded) >= target_size:
                break
    
    return expanded[:target_size]
```

---

## 📊 Estrategias Específicas por Tipo de Modelo

### **Para Chatbots (Conversacional)**

#### **Estructura de datos recomendada:**
```json
{
  "messages": [
    {"role": "system", "content": "Contexto y personalidad del bot"},
    {"role": "user", "content": "Pregunta del usuario"},
    {"role": "assistant", "content": "Respuesta del asistente"}
  ]
}
```

#### **Técnicas de expansión:**
- **Variaciones de saludo** - "Hola", "Buenos días", "Qué tal"
- **Diferentes niveles de formalidad** - Formal vs casual
- **Contextos variados** - Primera vez vs cliente recurrente
- **Emociones del usuario** - Frustrado, contento, confundido

### **Para Clasificadores (Categorización)**

#### **Estructura de datos recomendada:**
```json
{
  "text": "Texto a clasificar",
  "label": "categoria_asignada",
  "confidence": 0.95
}
```

#### **Técnicas de expansión:**
- **Augmentación semántica** - Sinónimos y paráfrasis
- **Variaciones de longitud** - Textos cortos y largos
- **Casos ambiguos** - Textos que pueden ser de múltiples categorías
- **Ruido controlado** - Errores tipográficos y gramaticales

### **Para Generadores (Creativos)**

#### **Estructura de datos recomendada:**
```json
{
  "prompt": "Instrucción o tema",
  "completion": "Texto generado esperado",
  "style": "formal|casual|creativo",
  "length": "corto|medio|largo"
}
```

#### **Técnicas de expansión:**
- **Variaciones de estilo** - Formal, casual, técnico
- **Diferentes longitudes** - Tweets, párrafos, artículos
- **Tonos variados** - Serio, humorístico, inspiracional
- **Formatos diversos** - Lista, narrativa, instructivo

---

# 4.5 Evaluación y Mejora Continua

## 🎯 Métricas que Realmente Importan

### **Métricas Técnicas (Automáticas)**
- **Precisión:** % de respuestas correctas
- **Recall:** % de casos relevantes capturados
- **F1-Score:** Balance entre precisión y recall
- **Perplexity:** Qué tan "sorprendido" está el modelo

### **Métricas de Negocio (Humanas)**
- **Satisfacción del usuario:** ¿Les gusta la respuesta?
- **Tiempo de resolución:** ¿Resuelve problemas más rápido?
- **Escalación:** ¿Reduce consultas a humanos?
- **Conversión:** ¿Mejora ventas/objetivos?

---

## 🔄 Proceso de Mejora Iterativa

### **Semana 1: MVP (Minimum Viable Product)**
- **20-30 ejemplos** de alta calidad
- **Casos básicos** más comunes
- **Probar funcionamiento** básico

### **Semana 2: Expansión**
- **50-100 ejemplos** con variaciones
- **Casos edge** y situaciones difíciles
- **Métricas de calidad** implementadas

### **Semana 3: Refinamiento**
- **100+ ejemplos** diversos y balanceados
- **A/B testing** con usuarios reales
- **Optimización** basada en feedback

### **Mensual: Actualización**
- **Nuevos datos** de casos reales
- **Re-entrenamiento** con datos actualizados
- **Métricas de negocio** evaluadas

---

## 💡 Consejos de Supervivencia

### **Para el Camino OpenAI:**
1. **Empieza con ChatGPT** para generar tus primeros ejemplos
2. **Usa Google Sheets** para organizar y convertir a JSONL
3. **Prueba con pocos datos** antes de hacer dataset grande
4. **Documenta todo** - vas a necesitar iterar

### **Para el Camino Código:**
1. **Empieza con modelos pequeños** (DialoGPT-small)
2. **Usa Google Colab** si no tienes GPU
3. **Guarda checkpoints** frecuentemente
4. **Monitorea métricas** durante entrenamiento

### **Para Ambos Caminos:**
1. **La calidad vence a la cantidad** - 30 ejemplos perfectos > 100 mediocres
2. **Diversidad es clave** - Diferentes formas de preguntar lo mismo
3. **Casos edge importan** - Qué pasa cuando preguntan algo raro
4. **Mide lo que importa** - Métricas de negocio, no solo técnicas

---

## 🎯 Checklist Final

### **Antes de Entrenar:**
- [ ] Dataset tiene al menos 30 ejemplos diversos
- [ ] Formato correcto para la herramienta elegida
- [ ] Casos de prueba preparados
- [ ] Métricas de evaluación definidas

### **Durante el Entrenamiento:**
- [ ] Monitorear progreso y métricas
- [ ] Tener plan B si algo falla
- [ ] Documentar configuraciones y decisiones

### **Después del Entrenamiento:**
- [ ] Probar con casos no vistos
- [ ] Medir métricas de negocio
- [ ] Planificar próxima iteración
- [ ] Compartir aprendizajes con el equipo

---

*Recuerda: El fine-tuning es un proceso iterativo. Tu primer modelo no será perfecto, ¡y eso está bien! Lo importante es empezar, medir, aprender y mejorar.*

---

# 4.6 Plantilla de Proyecto Final

## 📝 Estructura de Presentación

### **Para Ambos Caminos (5 minutos por participante):**

#### **1. Introducción (1 minuto)**
- **Nombre y caso de uso elegido**
- **¿Qué problema resuelve?**
- **¿Por qué elegiste este enfoque? (OpenAI vs Código)**

#### **2. El Desafío del Dataset (2 minutos)**
- **¿Cómo obtuviste los datos?**
- **¿Qué técnicas usaste para expandir/mejorar el dataset?**
- **¿Cuáles fueron los principales obstáculos?**

#### **3. Demostración (1.5 minutos)**
- **Muestra el modelo funcionando en vivo**
- **Casos de éxito y casos donde falla**
- **Comparación: antes vs después del fine-tuning**

#### **4. Lecciones Aprendidas (0.5 minutos)**
- **¿Qué funcionó mejor de lo esperado?**
- **¿Qué fue más difícil de lo esperado?**
- **¿Qué harías diferente la próxima vez?**

---

## 🎯 Criterios de Evaluación Actualizados

### **Enfoque en la Realidad del Dataset (60%)**
- **Calidad de los datos:** ¿Son realistas y diversos?
- **Estrategia de obtención:** ¿Cómo resolviste el problema de los datos?
- **Proceso documentado:** ¿Puedes explicar tu metodología?

### **Funcionalidad del Modelo (25%)**
- **¿El modelo responde correctamente?**
- **¿Las respuestas son útiles y coherentes?**
- **¿Maneja casos edge apropiadamente?**

### **Aprendizaje y Reflexión (15%)**
- **¿Entiendes las limitaciones de tu modelo?**
- **¿Puedes explicar por qué funciona (o no funciona)?**
- **¿Tienes un plan de mejora iterativa?**

---

## 🚀 Recursos de Apoyo

### **Para OpenAI (Sin Código):**
- **[OpenAI Fine-tuning Guide](https://platform.openai.com/docs/guides/fine-tuning)**
- **[JSONL Validator](https://jsonlint.com/)**
- **[ChatGPT para generar datos](https://chat.openai.com/)**
- **[Google Sheets templates](https://sheets.google.com/)**

### **Para Código (Técnico):**
- **[Hugging Face Transformers](https://huggingface.co/docs/transformers)**
- **[Google Colab (GPU gratuito)](https://colab.research.google.com/)**
- **[Datasets library](https://huggingface.co/docs/datasets)**
- **[PyTorch tutorials](https://pytorch.org/tutorials/)**

### **Para Ambos:**
- **[Awesome Fine-tuning](https://github.com/huggingface/awesome-papers)** - Papers y recursos
- **[Reddit r/MachineLearning](https://reddit.com/r/MachineLearning)** - Comunidad
- **[Stack Overflow](https://stackoverflow.com/questions/tagged/fine-tuning)** - Problemas técnicos

---

## ⚠️ Errores Comunes ACTUALIZADOS

### **Error #1: Subestimar el Trabajo de Datos**
- **Síntoma:** "Pensé que 10 ejemplos serían suficientes"
- **Realidad:** Necesitas 30+ ejemplos diversos mínimo
- **Solución:** Planifica 70% del tiempo para datos, 30% para modelo

### **Error #2: Datos Sintéticos Sin Validación**
- **Síntoma:** "Generé 1000 ejemplos con ChatGPT"
- **Realidad:** Datos sintéticos sin validación humana son problemáticos
- **Solución:** Genera sintético, pero valida manualmente una muestra

### **Error #3: No Probar Casos Edge**
- **Síntoma:** "Funciona perfectamente con mis ejemplos"
- **Realidad:** Los usuarios harán preguntas que no esperabas
- **Solución:** Prueba deliberadamente con casos raros y difíciles

### **Error #4: Optimizar Métricas Técnicas vs Negocio**
- **Síntoma:** "Tengo 95% de accuracy"
- **Realidad:** La accuracy técnica no siempre significa utilidad real
- **Solución:** Define métricas de negocio desde el inicio

---

## 💡 Consejos de Supervivencia ACTUALIZADOS

### **Para Principiantes (OpenAI):**
1. **Empieza con 5 casos reales perfectos** antes que 50 mediocres
2. **Usa ChatGPT para expandir**, pero revisa cada ejemplo manualmente
3. **Prueba el modelo cada 10 ejemplos** para ver progreso
4. **Documenta qué funciona** - vas a necesitar iterar

### **Para Técnicos (Código):**
1. **Empieza con un modelo pequeño** (DialoGPT-small, DistilBERT)
2. **Usa Google Colab** si no tienes GPU local
3. **Implementa logging desde el inicio** - vas a necesitar debuggear
4. **Guarda checkpoints frecuentemente** - el entrenamiento puede fallar

### **Para Ambos Caminos:**
1. **El dataset es el 80% del trabajo** - invierte tiempo ahí
2. **Calidad > Cantidad** - 30 ejemplos perfectos > 100 mediocres
3. **Mide lo que importa** - métricas de negocio, no solo técnicas
4. **Itera rápidamente** - mejor 3 modelos simples que 1 complejo

---

*¡Recuerda! El objetivo no es crear el modelo perfecto, sino aprender el proceso y entender los desafíos reales del fine-tuning. Tu primer modelo será tu peor modelo - ¡y eso está perfecto!*

