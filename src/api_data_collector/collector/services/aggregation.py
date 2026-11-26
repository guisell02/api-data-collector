from collections import defaultdict
from datetime import date
from typing import Any
from statistics import fmean


def build_monthly_summary(
    daily_records: list[dict[str, Any]],
) -> list[dict[str, int | float | None]]:
    """Agrupa los registros diarios por año y mes."""
    monthly_stats: dict[tuple[int, int], dict[str, int | float]] = defaultdict(
        lambda: {
            "temperature_sum": 0.0,
            "temperature_days": 0,
            "precipitation_sum": 0.0,
            "precipitation_days": 0,
        }
    )

    for record in daily_records:
        observed_date = date.fromisoformat(record["date"])
        month_key = (observed_date.year, observed_date.month)
        stats = monthly_stats[month_key]

        temperature = record["temperature_2m_mean_c"]
        precipitation = record["precipitation_sum_mm"]

        if temperature is not None:
            stats["temperature_sum"] += temperature
            stats["temperature_days"] += 1

        if precipitation is not None:
            stats["precipitation_sum"] += precipitation
            stats["precipitation_days"] += 1

    summary = []

    for (year, month), stats in sorted(monthly_stats.items()):
        temperature_days = int(stats["temperature_days"])
        precipitation_days = int(stats["precipitation_days"])

        temperature_mean = (
            round(stats["temperature_sum"] / temperature_days, 2)
            if temperature_days
            else None
        )
        precipitation_total = (
            round(stats["precipitation_sum"], 2) if precipitation_days else None
        )

        summary.append(
            {
                "year": year,
                "month": month,
                "temperature_mean_c": temperature_mean,
                "precipitation_sum_mm": precipitation_total,
                "temperature_days": temperature_days,
                "precipitation_days": precipitation_days,
            }
        )

    return summary


def build_monthly_climatology(
    monthly_records: list[dict[str, Any]],
) -> list[dict[str, int | float | None]]:
    """Promedia los resúmenes anuales para cada mes calendario."""
    values_by_month: dict[int, dict[str, list[float]]] = {
        month: {
            "temperature": [],
            "precipitation": [],
        }
        for month in range(1, 13)
    }

    for record in monthly_records:
        month = int(record["month"])

        if month not in values_by_month:
            raise ValueError(f"Número de mes inválido: {month}")

        temperature = record["temperature_mean_c"]
        precipitation = record["precipitation_sum_mm"]

        if temperature is not None:
            values_by_month[month]["temperature"].append(float(temperature))

        if precipitation is not None:
            values_by_month[month]["precipitation"].append(float(precipitation))

    climatology = []

    for month in range(1, 13):
        temperatures = values_by_month[month]["temperature"]
        precipitation_values = values_by_month[month]["precipitation"]

        climatology.append(
            {
                "month": month,
                "temperature_climatology_mean_c": (
                    round(fmean(temperatures), 2) if temperatures else None
                ),
                "precipitation_climatology_mean_mm": (
                    round(fmean(precipitation_values), 2)
                    if precipitation_values
                    else None
                ),
                "temperature_years": len(temperatures),
                "precipitation_years": len(precipitation_values),
            }
        )

    return climatology
