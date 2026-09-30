# Ejercicio: Sistema de Gestión de Personas

## Objetivo
Desarrollar un programa en Python que gestione una base de datos de personas utilizando SQLite3.

## Descripción de la Base de Datos
- **Tabla:** `Personas`
- **Columnas:**
  - `documento` (TEXT, PRIMARY KEY): Número de documento único
  - `nombre` (TEXT): Nombre de la persona
  - `apellido` (TEXT): Apellido de la persona
  - `edad` (INTEGER): Edad actual de la persona

## Requisitos del Programa

### Menú Principal
El programa debe mostrar un menú de consola con las siguientes opciones:

    === SISTEMA DE GESTIÓN DE PERSONAS ===
    1. Agregar nueva persona
    2. Registrar cumpleaños (incrementar edad)
    3. Modificar datos de una persona
    4. Eliminar persona
    5. Buscar persona por documento
    6. Reportes
    7. Salir

### Funcionalidades a Implementar

#### 1. Operaciones de Modificación de Datos

**a) Agregar nueva persona**
- Solicitar: documento, nombre, apellido y edad
- Validar que el documento no exista previamente
- Insertar el registro en la tabla

**b) Registrar cumpleaños**
- Solicitar el documento de la persona
- Incrementar la edad en 1
- Mostrar mensaje de confirmación con los datos actualizados

**c) Modificar datos de una persona**
- Permitir cambiar nombre, apellido o edad
- Buscar por documento
- Actualizar solo los campos indicados

**d) Eliminar persona**
- Solicitar documento
- Confirmar antes de eliminar
- Mostrar mensaje de éxito o error

**e) Buscar persona por documento**
- Mostrar todos los datos de la persona encontrada

#### 2. Menú de Reportes

    === REPORTES ===
    1. Listar todas las personas ordenadas por apellido
    2. Personas mayores de edad (≥18 años)
    3. Personas menores de edad (<18 años)
    4. Cantidad de personas por rango de edad
    5. Persona más joven y más longeva
    6. Estadísticas generales (promedio, mínimo, máximo de edad)
    7. Personas cuyo nombre empiece con una letra específica
    8. Apellidos con más de una persona (GROUP BY + HAVING)
    9. Volver al menú principal
