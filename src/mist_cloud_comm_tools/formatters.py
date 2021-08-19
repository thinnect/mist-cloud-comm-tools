"""
Common variable formatters.
"""

def format_proto_timestamp(ts):
    return '{:d}.{:03d}'.format(ts.seconds, ts.nanos // 1000000)
