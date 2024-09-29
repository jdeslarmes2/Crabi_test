# Análisis de Datos de Estado

Este proyecto tiene como objetivo cruzar datos de varios archivos en formato Excel relacionados con reclamos, personas y servicios con un archivo de estados, 
generando archivos finales que incluyen información relevante dichos archivos.


## Estructura del Proyecto

- `claim.xlsx`: Contiene datos de reclamos.
- `people.xlsx`: Contiene datos de personas relacionadas con las reclamos.
- `service.xlsx`: Contiene datos de servicios asociados a las reclamos.
- `status.xlsx`: Contiene datos de estados que describen las reclamos, peronas y servicios.

## Estructura recomendada: 

project/
├── data/
│   ├── claim.xlsx
│   ├── people.xlsx
│   ├── service.xlsx
│   └── status.xlsx
├── scripts/
│   └── data_analysis.py
└── README.md


## Descripción de Archivos Generados

- `final_claim.xlsx`: Resultado del cruce entre `claim.xlsx` y `status.xlsx`, añadiendo las columnas `claim_name` y `claim_description`.
- `final_people.xlsx`: Resultado del cruce entre `people.xlsx` y `status.xlsx`, añadiendo las columnas `people_name` y `people_description`.
- `final_service.xlsx`: Resultado del cruce entre `service.xlsx` y `status.xlsx`, añadiendo las columnas `service_name`, `service_description`, `coverage_name` y `coverage_description`.

## Requisitos

- Python 3.x
- pandas

## Instalación

1. Clona el repositorio:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd project

## Instalación de dependencias

pip install pandas

## Ejecución de script

python scripts/data_analysis.py


## Descripción del Código
### El script realiza los siguientes pasos:

## 1- Carga de Archivos: Carga los archivos Excel necesarios en DataFrames de Pandas.
## 2- Cruces de Datos: Realiza merges entre las tablas para obtener información combinada:
##    Cruce entre claim y status.
##    Cruce entre people y status.
##    Cruce entre service y status, incluyendo también información sobre la cobertura.
## 3- Renombrado de Columnas: Renombra columnas para mayor claridad.
## 4- Eliminación de Columnas Innecesarias: Se asegura de que las columnas innecesarias se eliminen de los DataFrames finales.
## 5- Guardado de Resultados: Guarda los resultados en archivos Excel en la misma ubicación.

## Contribuciones
## Si deseas contribuir al proyecto, por favor abre un issue o envía un pull request.

## Licencia
## Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más información.