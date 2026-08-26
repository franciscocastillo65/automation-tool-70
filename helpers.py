import time
import random
import pyautogui
from typing import List, Tuple

def random_delay(min_seconds: float = 0.05, max_seconds: float = 0.3) -> None:
    delay = random.uniform(min_seconds, max_seconds)
    time.sleep(delay)

def get_random_offset(base_x: int, base_y: int, max_offset: int = 5) -> Tuple[int, int]:
    offset_x = random.randint(-max_offset, max_offset)
    offset_y = random.randint(-max_offset, max_offset)
    return base_x + offset_x, base_y + offset_y

def is_valid_position(x: int, y: int) -> bool:
    width, height = pyautogui.size()
    return 0 <= x < width and 0 <= y < height

def perform_click(x: int, y: int, clicks: int = 1, interval: float = 0.05, button: str = 'left') -> bool:
    if not is_valid_position(x, y):
        return False
    try:
        pos = get_random_offset(x, y, 3)
        random_delay(0.01, 0.04)
        pyautogui.click(pos[0], pos[1], clicks=clicks, interval=interval, button=button)
        random_delay(0.02, 0.08)
        return True
    except Exception:
        return False

def hold_click(x: int, y: int, duration: float = 0.8) -> bool:
    if not is_valid_position(x, y):
        return False
    try:
        pos = get_random_offset(x, y, 2)
        pyautogui.mouseDown(pos[0], pos[1])
        start_time = time.time()
        while time.time() - start_time < duration:
            jiggle_pos = get_random_offset(pos[0], pos[1], 4)
            pyautogui.moveTo(jiggle_pos[0], jiggle_pos[1], duration=0.02)
            random_delay(0.01, 0.05)
        pyautogui.mouseUp(pos[0], pos[1])
        return True
    except Exception:
        pyautogui.mouseUp()
        return False

def click_in_area(x1: int, y1: int, x2: int, y2: int, num_clicks: int = 3) -> int:
    successful = 0
    for _ in range(num_clicks):
        rand_x = random.randint(min(x1, x2), max(x1, x2))
        rand_y = random.randint(min(y1, y2), max(y1, y2))
        if perform_click(rand_x, rand_y):
            successful += 1
        random_delay(0.1, 0.25)
    return successful

def multi_point_sequence(points: List[Tuple[int, int]], cycles: int = 1) -> int:
    total_success = 0
    for _ in range(cycles):
        for px, py in points:
            if perform_click(px, py):
                total_success += 1
            random_delay(0.05, 0.15)
    return total_success