"""
Common variable formatters.
"""

__copyright__ = 'Thinnect Inc. 2021'
__license__ = 'MIT'

def format_proto_timestamp(ts):
    return f'{ts.seconds:d}.{ts.nanos // 1000000:03d}'
