import csv
from collections.abc import Mapping, Sequence
from pathlib import Path


def save_csv(
    records: Sequence[Mapping[str, object]],
    filename: str | Path,
) -> Path:
    """Guarda registros con las mismas columnas en un archivo CSV."""
    if not records:
        raise ValueError("No hay registros para guardar.")

    filepath = Path(filename)
    filepath.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(records[0].keys())

    with filepath.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(
            csv_file,
            fieldnames=fieldnames,
            extrasaction="raise",
        )
        writer.writeheader()
        writer.writerows(records)

    return filepath
