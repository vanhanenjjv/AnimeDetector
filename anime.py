import cv2
import numpy

from fastapi import File


cascade_file = 'lbpcascade_animeface.xml'
cascade = cv2.CascadeClassifier(cascade_file)


class UnsupportedFormatError(Exception):
    pass


def is_image(file: File(...)) -> bool:
    content_types = list(map(lambda extension: 'image/' + extension, [
        'jpg',
        'jpeg',
        'png',
        'webp'
    ]))

    return file.content_type in content_types


async def detect_anime_from(file: File(...)) -> bool:
    if not is_image(file):
        raise UnsupportedFormatError()

    image_bytes = await file.read()
    image_string = numpy.fromstring(image_bytes, numpy.uint8)
    image = cv2.imdecode(image_string, cv2.IMREAD_COLOR)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)

    faces = cascade.detectMultiScale(gray,
                                     # detector options
                                     scaleFactor=1.1,
                                     minNeighbors=5,
                                     minSize=(24, 24))

    # numpy.ndarray when positive and tuple when negative
    return True if isinstance(faces, numpy.ndarray) else False
