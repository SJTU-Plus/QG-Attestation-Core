from Crypto.Hash import HMAC, SHA256

from base import AttestationBase


def load_key(path):
    from pathlib import Path
    return Path(path).read_bytes()


class HashAttestation(AttestationBase):
    def __init__(self, secret: bytes, digestmod=SHA256):
        self._secret = secret
        self._mod = digestmod

    def _common(self, raw: bytes):
        h = HMAC.new(self._secret, digestmod=self._mod)
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
    Path('hsecret.bin').write_bytes(secret)

    a = HashAttestation(secret)
