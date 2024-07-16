import time

def waiter(seconds: int | float | None = None) -> None:
    """Waits for the provided time or infinite long."""
    if seconds is None:
        while True:
            time.sleep(100)
    else:
        time.sleep(seconds)