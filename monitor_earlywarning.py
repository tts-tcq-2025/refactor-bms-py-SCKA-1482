from typing import Callable, List, Optional

def get_warning_ranges():
    return {
        "temperature": {"low": 36.0, "high": 38.0},
        "pulse": {"low": 60, "high": 100},
        "spo2": {"low": 90},
    }

def check_temperature(temp: float) -> Optional[str]:
    ranges = get_warning_ranges()["temperature"]
    if temp < ranges["low"]:
        return "Temperature low warning"
    elif temp > ranges["high"]:
        return "Temperature high warning"
    return None

def check_pulse(pulse: int) -> Optional[str]:
    ranges = get_warning_ranges()["pulse"]
    if pulse < ranges["low"]:
        return "Pulse rate low warning"
    elif pulse > ranges["high"]:
        return "Pulse rate high warning"
    return None

def check_spo2(spo2: int) -> Optional[str]:
    ranges = get_warning_ranges()["spo2"]
    if spo2 < ranges["low"]:
        return "SpO2 low warning"
    return None

def check_vitals(
    temperature: float,
    pulse: int,
    spo2: int,
    alert_handler: Optional[Callable[[str], None]] = None,
) -> List[str]:
    """
    Check vital signs and return list of warnings.
    If alert_handler is provided, call it for each warning.
    """
    checks = [
        check_temperature,
        check_pulse,
        check_spo2,
    ]
    warnings = []
    for check in checks:
        warning = check(temperature if check == check_temperature else pulse if check == check_pulse else spo2)
        if warning:
            warnings.append(warning)
            if alert_handler:
                alert_handler(warning)
    return warnings

def vitals_ok(temperature: float, pulse: int, spo2: int) -> bool:
    """
    Returns True if all vitals are in normal range (no warnings).
    """
    return not bool(check_vitals(temperature, pulse, spo2))

def alert_vitals_with_warning(
    temperature: float,
    pulse: int,
    spo2: int,
    alert_handler: Callable[[str], None],
) -> None:
    """
    Alert for all warnings using alert_handler.
    """
    warnings = check_vitals(temperature, pulse, spo2)
    for warning in warnings:
        alert_handler(warning)
