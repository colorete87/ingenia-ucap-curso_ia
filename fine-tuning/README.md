# Curso de Fine-Tuning - Material de Soporte

Este repositorio contiene el material de soporte completo para el curso de Fine-Tuning de modelos de lenguaje, incluyendo presentaciones, recursos y herramientas prácticas.

## 📁 Estructura del Proyecto

```
fine-tuning/
├── README.md                    # Este archivo
├── index.html                   # Página principal con navegación
├── css/
│   ├── presentations.css        # Estilos compartidos
│   └── README.md               # Documentación de estilos
├── html/
│   ├── presentacion_seccion_1.html  # Fundamentos del Fine-Tuning
│   ├── presentacion_seccion_2.html  # Demostraciones Prácticas
│   ├── presentacion_seccion_3.html  # Herramientas para Fine-Tuning
│   ├── presentacion_seccion_4.html  # Práctica y Aplicación
│   └── presentacion_seccion_5.html  # Casos de Uso Avanzados
├── images/                     # Imágenes y recursos visuales
│   ├── background.png          # Imagen de fondo
│   ├── logo_left.png          # Logo izquierdo
│   ├── logo_right.png         # Logo derecho
│   ├── ft_open_ai_*.png       # Capturas de pantalla de OpenAI
│   └── *.jpg                  # Otras imágenes
├── md/                         # Archivos Markdown fuente
│   ├── seccion_1_fundamentos.md
│   ├── seccion_2_demostraciones.md
│   ├── seccion_3_herramientas.md
│   └── seccion_4_practica.md
├── src_1/                      # Datasets de entrenamiento y validación
│   ├── training.jsonl          # Dataset de entrenamiento
│   ├── validation.jsonl        # Dataset de validación
│   ├── soccer_report_dataset.jsonl  # Dataset específico de fútbol
│   └── soccer_report_validation.jsonl
└── src_2/                      # Código de transfer learning
    ├── transfer_learning_demo.py     # Demo de transfer learning
    ├── requirements.txt              # Dependencias Python
    ├── README.md                     # Documentación del demo
    └── *.png                        # Gráficos de resultados
```

## 🎯 Contenido del Curso

### Sección 1: Fundamentos del Fine-Tuning
- **Archivo**: `html/presentacion_seccion_1.html`
- **Temas**: Modelos de lenguaje, tokens, embeddings, conceptos básicos
- **Duración**: ~45 minutos

### Sección 2: Demostraciones Prácticas
- **Archivo**: `html/presentacion_seccion_2.html`
- **Temas**: Exploración de tokens, modelos base vs instruidos
- **Duración**: ~40 minutos

### Sección 3: Herramientas para Fine-Tuning
- **Archivo**: `html/presentacion_seccion_3.html`
- **Temas**: OpenAI, Hugging Face, formatos de datos (JSON/JSONL)
- **Duración**: ~50 minutos

### Sección 4: Práctica y Aplicación
- **Archivo**: `html/presentacion_seccion_4.html`
- **Temas**: Casos de uso, implementación práctica, mejores prácticas
- **Duración**: ~60 minutos

### Sección 5: Casos de Uso Avanzados
- **Archivo**: `html/presentacion_seccion_5.html`
- **Temas**: Transfer learning, casos de uso específicos, optimización avanzada
- **Duración**: ~45 minutos

## 📊 Datasets y Material Práctico

### Datasets de Entrenamiento (`src_1/`)
Este directorio contiene datasets preparados para fine-tuning:

- **`training.jsonl`** y **`validation.jsonl`**: Datasets base para entrenamiento y validación
- **`soccer_report_dataset.jsonl`**: Dataset especializado en reportes de fútbol
- **`soccer_report_validation.jsonl`**: Dataset de validación para reportes de fútbol
- **`training_2.jsonl`** y **`validation_2.jsonl`**: Datasets alternativos

### Transfer Learning Demo (`src_2/`)
Incluye código práctico para transfer learning:

- **`transfer_learning_demo.py`**: Script principal de demostración
- **`requirements.txt`**: Dependencias Python necesarias
- **`README.md`**: Documentación específica del demo
- **`transfer_learning_*.png`**: Gráficos de resultados y métricas

## 🚀 Cómo Usar

1. **Abrir la página principal**:
   ```bash
   open index.html
   ```

2. **Navegar por las secciones**:
   - Usa la página `index.html` para acceder a todas las presentaciones
   - Cada presentación es independiente y se puede abrir directamente

3. **Presentar en pantalla completa**:
   - Presiona `F11` en tu navegador
   - Usa las flechas del teclado para navegar entre slides

4. **Ejecutar demos prácticos**:
   ```bash
   cd src_2
   pip install -r requirements.txt
   python transfer_learning_demo.py
   ```

## 🎨 Estilos Compartidos

Todas las presentaciones usan estilos CSS compartidos para mantener consistencia visual:

- **Archivo**: `css/presentations.css`
- **Beneficios**: Consistencia, mantenibilidad, fácil personalización
- **Características**: Responsive design, tipografía optimizada, componentes reutilizables

### Componentes Disponibles:
- `.code-block` - Bloques de código
- `.two-columns` - Layout de dos columnas
- `.demo-link` - Enlaces de demostración
- `.comparison-table` - Tablas de comparación
- `.warning` / `.success` - Cajas de alerta
- `.checklist` - Listas de verificación

## 🛠️ Tecnologías Utilizadas

- **Reveal.js**: Framework para presentaciones web
- **HTML5**: Estructura semántica
- **CSS3**: Estilos modernos y responsive
- **JavaScript**: Interactividad básica

## 📱 Compatibilidad

- ✅ Chrome, Firefox, Safari, Edge (últimas versiones)
- ✅ Dispositivos móviles y tablets
- ✅ Pantallas de diferentes resoluciones
- ✅ Modo de presentación y modo de edición

## 🔧 Personalización

### Modificar Estilos Globales:
Edita `css/presentations.css` para cambios que afecten todas las presentaciones.

### Agregar Estilos Específicos:
```html
<style>
/* Estilos específicos para esta presentación */
.mi-clase-personalizada {
    color: #ff6b6b;
}
</style>
```

### Crear Nuevas Presentaciones:
1. Copia una presentación existente como plantilla
2. Incluye el CSS compartido: `<link rel="stylesheet" href="css/presentations.css">`
3. Modifica el contenido manteniendo la estructura

## 📚 Recursos Adicionales

### Herramientas Mencionadas:
- **OpenAI Platform**: https://platform.openai.com
- **Hugging Face**: https://huggingface.co
- **Tiktokenizer**: https://tiktokenizer.vercel.app
- **Hyperbolic AI**: https://app.hyperbolic.ai

### Documentación:
- Archivos Markdown fuente en `md/`
- Imágenes y recursos en `images/`
- Datasets de entrenamiento en `src_1/`
- Código de demostración en `src_2/`

## 🤝 Contribuciones

Para contribuir al material:

1. Mantén la consistencia visual usando los estilos compartidos
2. Sigue la estructura de navegación existente
3. Documenta cambios importantes en este README
4. Prueba en diferentes navegadores antes de publicar

## 📝 Licencia

Material educativo desarrollado para el curso de Fine-Tuning.
Uso libre para fines educativos.

---

**Última actualización**: Enero 2025
**Versión**: 1.1
