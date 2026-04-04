import os
from pathlib import Path

SUPPORTED_EXTS = {".jpg", ".jpeg", ".png", ".webp"}

def list_catalog_images(catalog_dir: str) -> list[Path]:
    p = Path(catalog_dir)
    if not p.exists():
        return []

    files = []
    for fp in p.rglob("*"):
        if fp.is_file() and fp.suffix.lower() in SUPPORTED_EXTS:
            files.append(fp)

    files.sort(key=lambda x: str(x).lower())
    return files


def ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)
