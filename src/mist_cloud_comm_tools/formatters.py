"""
Common variable formatters.
"""

__copyright__ = 'Thinnect Inc. 2021'
__license__ = 'MIT'

def format_proto_timestamp(ts):
    return '{:d}.{:03d}'.format(ts.seconds, ts.nanos // 1000000)
