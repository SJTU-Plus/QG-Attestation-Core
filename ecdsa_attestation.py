from Crypto.Hash import SHA256
from Crypto.PublicKey import ECC
from Crypto.Signature import DSS

from base import AttestationBase


def load_key(path):
    from pathlib import Path
    return ECC.import_key(Path(path).read_text(encoding='utf-8'))


class EcdsaAttestation(AttestationBase):
    def __init__(self, key: ECC.EccKey, verify_only=False):
        self._key = key
        if not verify_only:
            assert key.has_private()

    def _common(self, data):
        h = SHA256.new(data)
        s = DSS.new(self._key, 'fips-186-3')
        return s, h

    def _generate(self, raw: bytes):
        s, h = self._common(raw)
        return s.sign(h)

    def _verify(self,  raw: bytes, quote: bytes):
        v, h = self._common(raw)
        v.verify(h, quote)


if __name__ == "__main__":
    from pathlib import Path

    private = ECC.generate(curve='P-256')
    Path('private.pem').write_text(
        private.export_key(format='PEM'), encoding='utf-8')

    public = private.public_key()
    Path('public.pem').write_text(
        public.export_key(format='PEM'), encoding='utf-8')

    a = EcdsaAttestation(private)
