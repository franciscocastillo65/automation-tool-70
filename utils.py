import json
from dataclasses import dataclass
from typing import List
import cmath

@dataclass
class ClickData:
    position: complex
    delay: float

def load_click_data(path: str) -> List[ClickData]:
    with open(path, 'r') as f:
        raw_data = json.load(f)
    return [ClickData(complex(item.get('x', 0), item.get('y', 0)), item.get('delay', 0.1)) for item in raw_data]

def save_click_data(data: List[ClickData], path: str) -> None:
    serializable = [{'x': cd.position.real, 'y': cd.position.imag, 'delay': cd.delay} for cd in data]
    with open(path, 'w') as f:
        json.dump(serializable, f, indent=4)

def rotate_click_data(data: List[ClickData], angle_radians: float) -> List[ClickData]:
    rotation_factor = cmath.exp(1j * angle_radians)
    return [ClickData(cd.position * rotation_factor, cd.delay) for cd in data]

def scale_click_data(data: List[ClickData], scale_factor: float) -> List[ClickData]:
    return [ClickData(cd.position * scale_factor, cd.delay) for cd in data]

def calculate_total_time(data: List[ClickData]) -> float:
    return sum(cd.delay for cd in data)

def interleave_click_data(data1: List[ClickData], data2: List[ClickData]) -> List[ClickData]:
    result = []
    max_len = max(len(data1), len(data2))
    for i in range(max_len):
        if i < len(data1):
            result.append(data1[i])
        if i < len(data2):
            result.append(data2[i])
    return result

def filter_short_delays(data: List[ClickData], min_delay: float = 0.05) -> List[ClickData]:
    return [cd for cd in data if cd.delay >= min_delay]