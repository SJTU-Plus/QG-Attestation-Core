from io  import BytesIO
import qrcode
from base64 import b64encode


def to_qrcode(data:str):
    qr = qrcode.make(data)
    buf = BytesIO()
    qr.save(buf, 'png')
    buf.seek(0)
    encoded_img = b64encode(buf.read()).decode()
    return f"data:image/png;base64,{encoded_img}"
