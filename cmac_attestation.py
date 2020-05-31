from Crypto.Hash import CMAC
from Crypto.Cipher import AES

from base import AttestationBase


def load_key(path):
    from pathlib import Path
    return Path(path).read_bytes()


class CmacAttestation(AttestationBase):
    def __init__(self, secret: bytes, ciphermod=AES):
        self._secret = secret
        self._mod = ciphermod

    def _common(self, raw: bytes):
        c = CMAC.new(self._secret, ciphermod=self._mod)
        c.update(raw)
        return c

    def _generate(self, raw: bytes) -> bytes:
        h = self._common(raw)
        return h.digest()

    def _verify(self, raw: bytes, quote: bytes):
        h = self._common(raw)
        h.verify(quote)


if __name__ == "__main__":
    from pathlib import Path
    from Crypto.Random import get_random_bytes

    secret = get_random_bytes(16)
    Path('csecret.bin').write_bytes(secret)

    a = CmacAttestation(secret)
