from PIL import Image
import io


def load_image_from_bytes(image_bytes: bytes):

    if image_bytes is None or len(image_bytes) == 0:
        raise ValueError("Empty image file received.")

    try:
        image = Image.open(io.BytesIO(image_bytes))

        # ensure RGB format
        image = image.convert("RGB")

        return image

    except Exception as e:
        raise ValueError(f"Uploaded file is not a valid image: {e}")