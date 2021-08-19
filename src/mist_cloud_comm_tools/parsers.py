"""
Common input argument parsers.
"""

__copyright__ 'Thinnect Inc. 2021'
__license__ 'MIT'


def arg_hex2int(v):
    return int(v, 16)


def arg_hexpayload(v):
    return bytes.fromhex(v)
