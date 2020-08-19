# QG-Attestation-Core

This is a util for qgroup applicants attestation.

## Setup

Install dependencies with
``` console
pip3 install -r requirements.txt
```

> For faster public key operations in Unix, you should install GMP in your system.

## Usage


### Symmetric Style (Blake2b)

```
In [9]: qq
Out[9]: '123456789012'

In [10]: run blake2_attestation.py

In [11]: att = Blake2Attestation.load('hsecret.bin')

In [12]: x = att.generate(qq)

In [13]: len(x), x
Out[13]: (38, '9ZBm3iZtt2Cm3hXuwboP2dxagCAqTnw9kaGugx')

In [14]: att.verify(qq, x)
Out[14]: datetime.datetime(2020, 8, 20, 0, 45, 2)

In [15]: att.verify(qq, x+'1') == None
Out[15]: True
```

### Symmetric Style (HMAC)

```
In [13]: qq
Out[13]: '123456789012'

In [14]: run hash_attestation.py

In [15]: att = HashAttestation.load('hsecret.bin')

In [16]: x = att.generate(qq)

In [17]: len(x), x
Out[17]: (49, 'u5Du366vSiUZsPEMf5ti79vozf53f8aD1kiGjs73QicckFbtS')

In [18]: att.verify(qq, x)
Out[18]: datetime.datetime(2020, 6, 3, 14, 0, 22)

In [19]: att.verify(qq, x+'1') == None
Out[19]: True
```

### Symmetric Style (CMAC)

```
In [20]: qq
Out[20]: '123456789012'

In [21]: run cmac_attestation.py

In [22]: att = CmacAttestation.load('csecret.bin')

In [23]: x = att.generate(qq)

In [24]: len(x), x
Out[24]: (28, '3QyzDFQLVXADo3RFySGPaucMjBv4')

In [25]: att.verify(qq, x)
Out[25]: datetime.datetime(2020, 6, 3, 14, 1, 17)

In [26]: att.verify(qq, x+'1') == None
Out[26]: True
```

### Asymmetric Style (ECDSA)

```
In [27]: qq
Out[27]: '123456789012'

In [28]: run ecdsa_attestation.py

In [29]: att = EcdsaAttestation.load('private.pem')

In [30]: x = att.generate(qq)

In [31]: len(x), x
Out[31]:
(93,
 'VAEbcjxJZqAwXkh2fFG4edd5jEtCnsGkV7AEmBi14K4EWfZ2cptkAiSez3PGLSfzf3GP5JYSLnpckHsSEdpmewGtWV1C4')

In [32]: att.verify(qq, x)
Out[32]: datetime.datetime(2020, 6, 3, 14, 1, 59)

In [33]: att.verify(qq, x+'1') == None
Out[33]: True
```


Verify Only
```
In [36]: qq
Out[36]: '123456789012'

In [37]: x
Out[37]: 'VAEbcjxJZqAwXkh2fFG4edd5jEtCnsGkV7AEmBi14K4EWfZ2cptkAiSez3PGLSfzf3GP5JYSLnpckHsSEdpmewGtWV1C4'

In [38]: att = EcdsaAttestation.load('public.pem', verify_only=True)

In [39]: att.verify(qq, x)
Out[39]: datetime.datetime(2020, 6, 3, 14, 1, 59)

In [40]: att.verify(qq, x+'1') == None
Out[40]: True
```

## Contribution

Issues and Pull Requests are welcome.

Please `autopep8 -i *.py` before giving a pull request.
