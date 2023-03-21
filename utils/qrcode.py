from datetime import datetime

from qrcode import QRCode
from qrcode.constants import ERROR_CORRECT_L
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask


def generate_qrcode(payload: str) -> None:

    qr = QRCode(error_correction=ERROR_CORRECT_L)
    qr.add_data(payload)

    img = qr.make_image(
        image_factory=StyledPilImage,
        module_drawer=RoundedModuleDrawer(),
        color_mask=RadialGradiantColorMask()
    )
    filename = f'{datetime.now().timestamp()}'.replace('.', '') + '.png'
    with open(filename, 'wb') as file:
        img.save(file)
