# Boom Solutions - Extensión CRM

## 1. Descripción General
Este módulo extiende la funcionalidad estándar del módulo **CRM** de Odoo para la gestión de leads y oportunidades, añadiendo nuevos campos, botones y lógicas personalizadas que permiten un control más detallado del ciclo de aprobación, tiempos de entrega y categorización de clientes.

## 2. Dependencias
- **crm** (módulo estándar de Odoo)

## 3. Características Principales
- Inclusión de nuevos campos en el modelo `crm.lead`, tales como:
  - **Tipo de Cliente** (`x_lead_category`): clasificación en residencial, empresarial o gubernamental.
  - **Fecha Límite** (`x_delivery_deadline`): para seguimiento de entregas.
  - **Aprobado por** (`x_approved_by`): usuario que aprueba el lead.
  - **Fecha de Aprobación** (`x_approved_date`): momento exacto de aprobación.
  - **Tiempo desde Aprobación** (`x_duration_since_approved`): campo calculado que indica cuánto tiempo ha transcurrido desde la aprobación.
  - **Requiere instalación** (`x_installation_required`) y **Fecha de instalación o entrega** (`x_installation_date`).
  - **Referencia de contrato** (`x_contract_reference`).
  - **Solicitó soporte postventa** (`x_support_required`).

- Botón en vista formulario para:
  - Registrar la aprobación del lead.
  - Asignar automáticamente fecha y usuario aprobador.
  - Definir la fecha límite de entrega.

- Cálculo automático y legible del tiempo transcurrido desde la aprobación.


## 4. Instalación
1. Copiar la carpeta `boom__solutions` en el directorio de **addons** de Odoo.
2. Reiniciar el servidor Odoo.
3. Activar el modo desarrollador.
4. Instalar el módulo desde **Aplicaciones**.

## 5. Datos de Ejemplo
El módulo incluye datos de demostración en `data/demo_data.xml` con leads de ejemplo que muestran los nuevos campos llenos y el flujo de aprobación en funcionamiento.

## 6. Mejoras de Seguridad (Recomendaciones)
Aunque actualmente no se incluye un archivo `security/ir.model.access.csv`, se recomienda:
- Definir reglas de acceso para limitar la edición de campos como `x_approved_by` y `x_approved_date` solo a usuarios autorizados.
- Proteger el botón de aprobación mediante grupos de usuarios (`groups="module.group_name"` en la vista XML).

