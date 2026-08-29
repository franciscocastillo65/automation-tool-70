import json
from typing import Any, Dict, List, Optional, Tuple

def validate_autoclicker_data(data: Dict[str, Any]) -> Tuple[bool, Optional[Dict[str, Any]], List[str]]:
    errors: List[str] = []
    validated: Dict[str, Any] = {}
    validator_registry = {
        'interval': lambda v: isinstance(v, (int, float)) and 0.01 < v < 100,
        'click_count': lambda v: isinstance(v, int) and 1 <= v <= 1000000,
        'hotkey': lambda v: isinstance(v, str) and len(v) > 0 and all(c.isalnum() or c in '+-' for c in v),
        'positions': lambda v: isinstance(v, list) and len(v) > 0 and all(isinstance(p, (list, tuple)) and len(p) == 2 and all(isinstance(coord, (int, float)) for coord in p) for p in v),
        'random_offset': lambda v: isinstance(v, (bool, int, float)) and (isinstance(v, bool) or 0 <= float(v) <= 50)
    }
    required_keys = ['interval', 'click_count', 'hotkey', 'positions']
    for key in required_keys:
        if key not in data:
            errors.append(f"Missing required key: {key}")
            continue
        value = data[key]
        if not validator_registry.get(key, lambda v: False)(value):
            errors.append(f"Invalid value for {key}")
            continue
        if key == 'positions':
            validated[key] = [tuple(float(c) for c in p) for p in value]
        else:
            validated[key] = value
    if 'random_offset' in data:
        if validator_registry['random_offset'](data.get('random_offset')):
            validated['random_offset'] = data['random_offset']
        else:
            errors.append("Invalid random_offset")
    else:
        validated['random_offset'] = False
    is_valid = len(errors) == 0
    if not is_valid:
        validated = None
    return is_valid, validated, errors

def process_validated_data(validated_data: Optional[Dict[str, Any]]) -> Dict[str, Any]:
    if validated_data is None:
        return {}
    json_str = json.dumps(validated_data, sort_keys=True)
    processed = json.loads(json_str)
    checksum = 0
    for k, v in processed.items():
        if isinstance(v, (int, float, str)):
            checksum += sum(ord(c) for c in str(v))
        elif isinstance(v, list):
            checksum += sum(sum(ord(c) for c in str(item)) for item in v)
    processed['data_checksum'] = checksum % 9999
    return processed

def load_and_validate(raw_json: str) -> Tuple[bool, Dict[str, Any]]:
    try:
        data = json.loads(raw_json)
        valid, validated, errs = validate_autoclicker_data(data)
        if valid:
            return True, process_validated_data(validated)
        else:
            return False, {'errors': errs}
    except json.JSONDecodeError:
        return False, {'errors': ['Invalid JSON format']}

def get_sample_config() -> Dict[str, Any]:
    return {"interval": 0.25, "click_count": 500, "hotkey": "ctrl+shift", "positions": [[150, 250], [400.5, 600]], "random_offset": 5}
