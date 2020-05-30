from Crypto.Hash import HMAC, SHA256

from base import AttestationBase


def load_key(path):
    from pathlib import Path
    return Path(path).read_bytes()


class HashAttestation(AttestationBase):
    def __init__(self, secret: bytes):
        self._secret = secret

    def _common(self, raw: bytes):
        h = HMAC.new(self._secret, digestmod=SHA256)
        h.update(raw)
        return h

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
    Path('secret.bin').write_bytes(secret)

    a = HashAttestation(secret)
