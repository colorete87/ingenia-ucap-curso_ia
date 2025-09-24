# Sección 2: Demostraciones Prácticas

## Material de Soporte para el Curso de Fine-Tuning

---

# 2.1 Conceptos Fundamentales en Acción

## 🎯 Objetivos de esta Sección

Al finalizar esta sección, los participantes podrán:
- Comprender qué es un token de forma práctica
- Repasar la estructura de prompts y respuestas
- Diferenciar entre modelos base e instruidos
- Observar el comportamiento de diferentes tipos de modelos

---

## 🔍 Explorando Tokens

### **¿Qué es un Token? (Demostración Práctica)**

**Nota importante:**
- No es estrictamente fine-tuning, pero está bueno que lo vean
- Es fundamental entender estos conceptos básicos

### **Vamos a ver qué es un token**

**¿Qué es un token?**
- Es la **unidad básica** que entiende el modelo
- Puede ser una palabra completa, parte de una palabra, o símbolos
- Los modelos "piensan" en tokens, no en letras o palabras

**Ejemplos prácticos:**
```
Texto: "¡Hola mundo!"
¿Cuántos tokens crees que son?
```

**Herramienta de demostración:**
🔗 **https://tiktokenizer.vercel.app/**

----

### **Actividad Práctica: Explorando Tokens**

**Vamos a probar diferentes textos:**

1. **Texto simple en español:**
   ```
   "Hola, ¿cómo estás?"
   ```

2. **Texto con números:**
   ```
   "El año 2024 tiene 366 días"
   ```

3. **Texto con emojis:**
   ```
   "Me gusta la pizza 🍕 y el café ☕"
   ```

4. **Código de programación:**
   ```python
   def saludar(nombre):
       return f"Hola, {nombre}!"
   ```

----

**¿Qué observamos?**
- Palabras comunes = menos tokens
- Palabras raras = más tokens
- Números = comportamiento especial
- Emojis = múltiples tokens
- Código = muchos tokens

---

## 💬 Estructura de Conversación con IA

### **Vamos a repasar un prompt y respuesta**

**Estructura básica de una conversación:**

#### **1. System (Sistema)**
```
Rol: Define el comportamiento del asistente
Ejemplo: "Eres un profesor experto en inteligencia artificial"
```

#### **2. User (Usuario)**
```
Rol: La pregunta o instrucción del usuario
Ejemplo: "Explícame qué es el fine-tuning"
```

#### **3. Assistant (Asistente)**
```
Rol: La respuesta del modelo
Ejemplo: "El fine-tuning es un proceso donde..."
```

---

## 🧠 Modelos Base vs Modelos Instruidos

### **Recordemos cómo funcionan los LLMs**

**Los LLMs se entrenan con datos de texto:**
- **Fuente principal:** Internet (páginas web, libros, artículos)
- **Objetivo original:** Predecir el siguiente token
- **Resultado:** Saben hablar mucho y muy largo, pero no como un chat

### **El Problema de los Modelos Base**

**¿Qué hacen naturalmente?**
- Completan texto
- Continúan historias
- Siguen patrones
- **NO conversan como humanos**

**Ejemplo de comportamiento:**
```
Input: "El clima hoy está"
Modelo Base: "El clima hoy está nublado. Según el pronóstico 
meteorológico, se esperan lluvias durante la tarde. La temperatura 
máxima será de 22°C y la mínima de 15°C. Los vientos serán del 
sureste con velocidades de 15 km/h..."
```

----

### **La Solución: Fine-Tuning para Instrucciones**

**Para llegar a un modelo que se parezca a un chat hay que hacer algo:**
- **Ese algo es fine-tuning**
- Específicamente: **Instruction Fine-Tuning**
- Entrenar al modelo para seguir instrucciones
- Enseñarle a conversar como humano

---

## 🔬 Demostración Práctica: Base vs Instruido

### **Modelo Base - Llama 3.1 405B Base**

🔗 **https://app.hyperbolic.ai/models/llama31-405b-base-bf-16**

**Características:**
- **Modelo original** sin fine-tuning de instrucciones
- **Completa texto** en lugar de responder
- **Comportamiento "crudo"** del modelo

**Vamos a probar:**
```
Prompt: "El capital de Francia es"
¿Qué esperamos que responda?
```

----

### **Modelo Instruido - Llama 3.1 405B Instruct**

🔗 **https://app.hyperbolic.ai/models/llama31-405b**

**Características:**
- **Mismo modelo base** pero con fine-tuning
- **Responde preguntas** como un asistente
- **Comportamiento conversacional**

**Vamos a probar:**
```
Prompt: "¿Cuál es la capital de Francia?"
¿Qué diferencia esperamos ver?
```

----

### **Actividad de Comparación**

**Prompts para probar en ambos modelos:**

1. **Completar texto:**
   ```
   "La inteligencia artificial es"
   ```

2. **Pregunta directa:**
   ```
   "¿Qué es la inteligencia artificial?"
   ```

3. **Instrucción específica:**
   ```
   "Explica en 3 puntos qué es el machine learning"
   ```

4. **Conversación:**
   ```
   "Hola, ¿puedes ayudarme?"
   ```

### **¿Qué diferencias observamos?**

**Modelo Base:**
- ✅ Excelente para completar texto
- ✅ Muy creativo y fluido
- ❌ No sigue instrucciones específicas
- ❌ No conversa como humano
- ❌ Puede generar texto irrelevante

**Modelo Instruido:**
- ✅ Sigue instrucciones precisas
- ✅ Conversa naturalmente
- ✅ Respuestas estructuradas
- ✅ Se comporta como asistente
- ❌ Menos creativo en algunos casos

---

## 🎯 Conclusiones de las Demostraciones

### **Lo que aprendimos:**

1. **Tokens son fundamentales**
   - Todo texto se convierte en tokens
   - Diferentes idiomas = diferentes patrones
   - Importante para entender costos y límites

2. **Estructura de conversación**
   - System, User, Assistant tienen roles específicos
   - El formato es crucial para el comportamiento
   - La calidad del prompt afecta la respuesta

3. **Fine-tuning transforma modelos**
   - Mismo modelo base → comportamientos diferentes
   - Instruction tuning crea asistentes conversacionales
   - Es la diferencia entre "completar" y "responder"

----

### **Próximos pasos:**
- En las siguientes secciones veremos cómo hacer nuestro propio fine-tuning
- Aprenderemos a preparar datos de entrenamiento
- Usaremos herramientas prácticas para el proceso

---

## 🤔 Preguntas para Reflexionar

1. **¿Por qué crees que es importante entender los tokens?**
2. **¿En qué situaciones usarías un modelo base vs uno instruido?**
3. **¿Qué ventajas y desventajas ves en cada tipo de modelo?**
4. **¿Cómo crees que el fine-tuning puede mejorar un modelo para tu caso específico?**

---

## 📚 Recursos Adicionales

### **Herramientas mencionadas:**
- **Tiktokenizer:** https://tiktokenizer.vercel.app/
- **Llama 3.1 405B Base:** https://app.hyperbolic.ai/models/llama31-405b-base-bf-16
- **Llama 3.1 405B Instruct:** https://app.hyperbolic.ai/models/llama31-405b

### **Para explorar más:**
- Prueba diferentes tipos de texto en el tokenizador
- Experimenta con ambos modelos usando diferentes prompts
- Observa cómo cambia el comportamiento según el tipo de entrada

---

*Esta sección prepara el terreno para entender por qué el fine-tuning es necesario y cómo transforma el comportamiento de los modelos.*
