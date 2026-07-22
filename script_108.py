def reliable_call(fn, *args, timeout_s=20, retries=2, fallback=None):
    for attempt in range(retries + 1):
        try:
            return call_with_timeout(fn, *args, timeout_s=timeout_s)  # bounded wait
        except TransientError:
            if attempt < retries:
                continue                                  # retry transient failures
        except Exception:
            break
    return fallback                                       # degrade gracefully
