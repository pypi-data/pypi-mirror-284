# openai_assistant/utils.py
import base64
import io

_openai = None


def init(openai_client):
    global _openai
    _openai = openai_client


def get_openai_client():
    if _openai is None:
        raise ValueError("OpenAI client is not initialized. Call `init(openai_client)` first.")
    return _openai


def covert_base64_image(base64_image):
    if base64_image.startswith('data:image/png;base64,'):
        base64_image_cleaned = base64_image[len('data:image/png;base64,'):]
        mimetype = 'image/png'
    elif base64_image.startswith('data:image/jpeg;base64,') or base64_image.startswith('data:image/jpg;base64,'):
        base64_image_cleaned = base64_image.split('base64,')[1]
        mimetype = 'image/jpeg'
    elif base64_image.startswith('data:image/webp;base64,'):
        base64_image_cleaned = base64_image[len('data:image/webp;base64,'):]
        mimetype = 'image/webp'
    elif base64_image.startswith('data:image/gif;base64,'):
        base64_image_cleaned = base64_image[len('data:image/gif;base64,'):]
        mimetype = 'image/gif'
    else:
        raise ValueError("Unsupported image type")

    missing_padding = len(base64_image_cleaned) % 4
    if missing_padding:
        print("Missing padding")
        base64_image_cleaned += '=' * (4 - missing_padding)

    image_data = base64.b64decode(base64_image_cleaned)
    image_io = io.BytesIO(image_data)
    return image_io, mimetype
