from api_data_collector.collector.services.aggregation import (
    build_monthly_summary,
    build_monthly_climatology,
)


def test_build_monthly_summary_aggregates_values_and_missing_data():
    records = [
        {
            "date": "2020-01-01",
            "temperature_2m_mean_c": 10.0,
            "precipitation_sum_mm": 2.0,
        },
        {
            "date": "2020-01-02",
            "temperature_2m_mean_c": None,
            "precipitation_sum_mm": 0.0,
        },
        {
            "date": "2020-02-01",
            "temperature_2m_mean_c": 20.0,
            "precipitation_sum_mm": None,
        },
    ]

    result = build_monthly_summary(records)

    assert result == [
        {
            "year": 2020,
            "month": 1,
            "temperature_mean_c": 10.0,
            "precipitation_sum_mm": 2.0,
            "temperature_days": 1,
            "precipitation_days": 2,
        },
        {
            "year": 2020,
            "month": 2,
            "temperature_mean_c": 20.0,
            "precipitation_sum_mm": None,
            "temperature_days": 1,
            "precipitation_days": 0,
        },
    ]


def test_build_monthly_climatology_averages_yearly_monthly_values():
    records = [
        {
            "year": 2020,
            "month": 1,
            "temperature_mean_c": 10.0,
            "precipitation_sum_mm": 100.0,
        },
        {
            "year": 2021,
            "month": 1,
            "temperature_mean_c": 12.0,
            "precipitation_sum_mm": 80.0,
        },
        {
            "year": 2020,
            "month": 2,
            "temperature_mean_c": 20.0,
            "precipitation_sum_mm": None,
        },
    ]

    result = build_monthly_climatology(records)

    assert len(result) == 12
    assert result[0] == {
        "month": 1,
        "temperature_climatology_mean_c": 11.0,
        "precipitation_climatology_mean_mm": 90.0,
        "temperature_years": 2,
        "precipitation_years": 2,
    }
    assert result[1] == {
        "month": 2,
        "temperature_climatology_mean_c": 20.0,
        "precipitation_climatology_mean_mm": None,
        "temperature_years": 1,
        "precipitation_years": 0,
    }
