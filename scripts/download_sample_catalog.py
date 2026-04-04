"""Downloads a small, free sample image set so the project runs immediately.

No paid APIs.

This downloads a few images from Wikimedia Commons (public domain / free licensed).
If your college requires offline datasets, skip this and use your own images.
"""

from pathlib import Path
import requests

SAMPLES = [
    (
        "shoe_1.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/3/3f/Shoe_%28AM_1960.022-8%29.jpg",
    ),
    (
        "shoe_2.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/3/3a/Running_shoes_asics.jpg",
    ),
    (
        "bag_1.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/2/2b/Backpack_%28Unsplash%29.jpg",
    ),
    (
        "tshirt_1.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/5/5a/Tshirtblue.jpg",
    ),
    (
        "watch_1.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/0/0b/Watch.jpg",
    ),
]

def main():
    out_dir = Path("catalog_images")
    out_dir.mkdir(parents=True, exist_ok=True)

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/115.0 Safari/537.36"
    }

    for name, url in SAMPLES:
        out_path = out_dir / name
        if out_path.exists():
            print(f"Exists: {out_path}")
            continue

        print(f"Downloading {name}...")
        try:
            resp = requests.get(url, headers=headers, timeout=30)
            resp.raise_for_status()
            with open(out_path, "wb") as f:
                f.write(resp.content)
        except Exception as e:
            print(f"Failed to download {url}: {e}")
            continue

    print("Done. Images saved to catalog_images/")


if __name__ == "__main__":
    main()
