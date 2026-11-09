# Sistema de Gestión de Inventario (Python & SQLite)

Proyecto académico final desarrollado para estructurar el backend de un inventario de productos utilizando bases de datos relacionales y una interfaz de terminal.

## Tecnologías Utilizadas
*   **Lenguaje:** Python (implementación de módulos, tuplas y docstrings).
*   **Base de Datos:** SQLite3.
*   **Integración de IA:** Se utilizaron asistentes de código (LLMs) como apoyo de pair-programming. Se delegó la generación de la estructura base (boilerplate) y se auditó el resultado para asegurar la modularización del código y la implementación de consultas parametrizadas (`?`) para prevenir vulnerabilidades de Inyección SQL.

## Características
*   Arquitectura modular (`main.py` para la lógica de presentación y `database.py` para la interacción con la base de datos).
*   Operaciones CRUD completas (Crear, Leer, Actualizar, Eliminar).
*   Validación robusta de inputs de usuario.
*   Persistencia de datos en disco mediante generación automática de esquema `IF NOT EXISTS`.

## Cómo ejecutarlo
1. Clonar el repositorio.
2. Ejecutar `python main.py` en la terminal. El archivo `.db` se creará automáticamente en la primera ejecución.