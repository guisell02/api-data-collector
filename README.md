# API Data Collector: clima histórico de Pasto

Recolector de datos meteorológicos históricos de Pasto, Nariño. Consulta la API de Open-Meteo, organiza los datos diarios y genera archivos CSV para su análisis.

## Pregunta del proyecto

¿Cómo variaron la temperatura media y la precipitación acumulada por mes en Pasto entre 2016 y 2025?

## Estado

El proyecto recolecta datos meteorológicos históricos de Pasto, genera archivos CSV y presenta un análisis exploratorio en un notebook con visualizaciones e interpretación.

La suite actual contiene siete pruebas para el cliente HTTP, el servicio meteorológico y las funciones de agregación.

## Fuente y limitaciones

Los datos provienen de la [Historical Weather API de Open-Meteo](https://open-meteo.com/en/docs/historical-weather-api), con el modelo ERA5.
ERA5 es un reanálisis meteorológico: combina observaciones con modelos para estimar condiciones pasadas. Su resolución es de aproximadamente 0,25 grados (unos 25 km). Por eso, los datos describen la celda de grilla reportada por la API, no una medición directa de una estación meteorológica en el centro de Pasto.
La consulta solicita las coordenadas `1.214578, -77.278117`; Open-Meteo reportó la celda `1.25, -77.25`. La zona horaria solicitada es `America/Bogota`.
Los resultados sirven para describir el periodo analizado. No constituyen una normal climática oficial de 30 años ni demuestran por sí solos las causas de cambios climáticos.

## Datos recolectados

- Periodo: `2016-01-01` a `2025-12-31`.
- Variables diarias:
  - Temperatura media a 2 metros, en °C.
  - Precipitación acumulada diaria, en mm.
- Ubicación y periodo centralizados en `src/api_data_collector/collector/config/settings.py`.

## Instalación y ejecución

Requiere Python 3.13 o superior y `uv`.

```powershell
uv sync
uv run python -m api_data_collector.collector.main

```

La ejecución consulta Open-Meteo y genera estos archivos en `data/`:

- `pasto_daily_weather.csv`
- `pasto_monthly_weather_summary.csv`
- `pasto_monthly_climatology_2016_2025.csv`

La carpeta `data/` está excluida de Git; los archivos generados localmente no se suben al repositorio por defecto.

## Contenido de los CSV

### Datos diarios

| Columna | Descripción |
|---|---|
| `date` | Fecha local del registro |
| `temperature_2m_mean_c` | Temperatura media diaria en °C |
| `precipitation_sum_mm` | Precipitación diaria acumulada en mm |

### Resumen por año y mes

| Columna | Descripción |
|---|---|
| `year` | Año |
| `month` | Número del mes |
| `temperature_mean_c` | Promedio de las temperaturas diarias disponibles |
| `precipitation_sum_mm` | Suma de la precipitación diaria disponible |
| `temperature_days` | Días con dato de temperatura |
| `precipitation_days` | Días con dato de precipitación |

Los días sin datos se excluyen del cálculo y se reflejan en las columnas de cobertura.

### Climatología mensual 2016–2025

| Columna | Descripción |
|---|---|
| `month` | Número del mes |
| `temperature_climatology_mean_c` | Promedio de las temperaturas medias de ese mes entre los años disponibles |
| `precipitation_climatology_mean_mm` | Promedio de los totales de precipitación de ese mes entre los años disponibles |
| `temperature_years` | Cantidad de años incluidos en el promedio de temperatura |
| `precipitation_years` | Cantidad de años incluidos en el promedio de precipitación |

Cada fila representa un mes calendario. En este periodo, cada promedio incluye diez años.

## Análisis exploratorio

El notebook [`pasto_weather_analysis.ipynb`](notebooks/pasto_weather_analysis.ipynb) revisa la calidad de los datos, compara los promedios mensuales de temperatura y precipitación, y visualiza las diferencias entre años mediante mapas de calor.

Para reproducirlo, ejecuta primero el recolector para generar los CSV en `data/`. Después abre el notebook en VS Code, selecciona el kernel del entorno del proyecto y ejecuta todas las celdas.

## Pruebas

Ejecuta las pruebas con:

```powershell
uv run python -m pytest
```

## Estructura principal

```text
src/api_data_collector/collector/
├── clients/       # Comunicación HTTP con la API
├── config/        # Ubicación, periodo y parámetros
├── services/      # Consulta y agregación de datos
├── storage/       # Escritura de archivos CSV
└── main.py        # Orquestación de la ejecución
```

## Evidencia de ejecución
La ejecución generó 3.653 registros diarios, 120 resúmenes año-mes y 12 promedios mensuales. Cada promedio mensual cuenta con datos de los diez años. La respuesta reportó temperatura en °C y precipitación en mm.
