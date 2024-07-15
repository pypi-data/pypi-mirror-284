from datetime import timedelta


def format_duration(duration: timedelta) -> str:
    seconds = duration.total_seconds()
    if seconds > 1:
        return f"{seconds:.2f}s"

    ms = seconds * 1000
    if ms > 1:
        return f"{ms:.1f}ms"

    us = ms * 1000
    return f"{us:.1f}us"
