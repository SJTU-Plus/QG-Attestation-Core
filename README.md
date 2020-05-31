# QG-Attestation-Core

This is util for qgroup applicants attestation.

## Setup

Install dependencies with
``` console
pip3 install -r requirements.txt
```

## Usage

### Symmetric Style (HMAC)

```
In [13]: run hash_attestation.py

In [14]: qq
Out[14]: 42925309569021849

In [15]: a.generate(qq)
Out[15]: '2dLuxY8Pvqut3k9FJB3r8316JitsDxsLPMTB1ivxaCX1eMNuoT'

In [16]: x = _

In [17]: a.verify(qq, x)
Out[17]: datetime.datetime(2020, 5, 31, 12, 51, 34)
```

### Symmetric Style (CMAC)

```
In [22]: qq
Out[22]: 42925309569021849

In [23]: run cmac_attestation.py

In [24]: a.generate(qq)
Out[24]: '2K8pmFXQVuWT4k8s5WPnZU9EYDGZ'

In [25]: a.verify(qq, _)
Out[25]: datetime.datetime(2020, 5, 31, 12, 53, 50)

In [26]: len('2K8pmFXQVuWT4k8s5WPnZU9EYDGZ')
Out[26]: 28
```

### Asymmetric Style (ECDSA)

```
In [8]: qq
Out[8]: 19278604876

In [9]: run ecdsa_attestation.py

In [10]: a.generate(qq)
Out[10]: 'MDKW9oLUDfL3K4AbFUMFq99QFjWJ9wwt5Z9zvDP3MPKzh5JktDYKovyRrwJ3cvEAc9KDNJvKEQH8kGnLUEkakC1oberBE'

In [11]: a.verify(qq, _)
Out[11]: datetime.datetime(2020, 5, 30, 23, 41, 14)
```

## Contribution

Issuses and Pull Requests are welcome.

Please `autopep8 -i *.py` before giving a pull request.
