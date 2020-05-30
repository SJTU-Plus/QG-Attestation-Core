# QG-Attestation-Core

This is util for qgroup applicants attestation.

## Setup

Install dependencies with
``` console
pip3 install -r requirements.txt
```

## Usage

### Symmetric Style

to be filled

See `hash_attestation.py`

```
In [4]: qq
Out[4]: 19278604876

In [5]: run hash_attestation.py

In [6]: a.generate(qq)
Out[6]: 'qfTV6enU8EbW1WQyLdc1Woj83H8oQFLWZ2isN4swKySbjos3y'

In [7]: a.verify(qq, _)
Out[7]: datetime.datetime(2020, 5, 30, 23, 40, 30)
```

### Asymmetric Style

to be filled

See `ecdsa_attestation.py`

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
