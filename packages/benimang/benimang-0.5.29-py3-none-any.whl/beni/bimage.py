from PIL import Image

from beni.btype import XPath


def convert(imgFile: XPath, maxSize: int | None = None, format: str | None = None):
    if set([maxSize, format]) == {None}:
        raise Exception('至少需要一个有效参数')
    img = Image.open(imgFile)
    with img:
        if maxSize:
            img.thumbnail((maxSize, maxSize))
        img.save(imgFile, format)
