# Estilos CSS Compartidos

Documentación técnica de los estilos CSS compartidos entre todas las presentaciones.

## 📄 Archivos

- `presentations.css` - Estilos principales compartidos

## 🎨 Componentes Disponibles

### Layout
- `.two-columns` - Sistema de dos columnas flexibles
- `.column` - Columna individual dentro del sistema

### Contenido
- `.code-block` - Bloques de código con sintaxis destacada
- `.demo-link` - Enlaces de demostración estilizados
- `.comparison-table` - Tablas de comparación con bordes

### Alertas y Notificaciones
- `.warning` - Cajas de advertencia (fondo amarillo)
- `.success` - Cajas de éxito (fondo verde)
- `.checklist` - Listas de verificación con checkboxes

### Tipografía
- `.emoji` - Estilo para emojis
- `.highlight` - Texto resaltado
- `.pros` / `.cons` - Colores para pros y contras

## 📱 Responsive Design

```css
@media (max-width: 768px) {
    .two-columns {
        flex-direction: column;
    }
}
```

## 🔧 Variables CSS Principales

```css
:root {
    --primary-color: #2c3e50;
    --secondary-color: #3498db;
    --warning-color: #f39c12;
    --success-color: #27ae60;
    --danger-color: #e74c3c;
}
```

## 📐 Tamaños de Fuente

- **Base**: 32px (reducido de 42px para mejor legibilidad)
- **H1**: 2em
- **H2**: 1.4em  
- **H3**: 1.1em
- **H4**: 0.9em
- **Código**: 0.8em

## 🎯 Uso en Presentaciones

```html
<!-- Incluir en todas las presentaciones -->
<link rel="stylesheet" href="css/presentations.css">
```

## 🔄 Mantenimiento

- Cambios globales: Modificar `presentations.css`
- Cambios específicos: Agregar estilos inline o archivo CSS adicional
- Testing: Verificar en múltiples navegadores y dispositivos
