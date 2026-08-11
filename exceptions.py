class InputValidationError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def validate_input(data):
    if not isinstance(data, dict):
        raise InputValidationError('Input must be a dictionary')
    if 'name' not in data or not isinstance(data['name'], str):
        raise InputValidationError('Missing or invalid name')
    if 'age' not in data or not isinstance(data['age'], int) or data['age'] <= 0:
        raise InputValidationError('Missing or invalid age')


def process_data(data):
    try:
        validate_input(data)
        print('Processing:', data)
    except InputValidationError as e:
        print('Input validation error:', e.message)


if __name__ == '__main__':
    sample_data = {'name': 'Alice', 'age': 30}
    process_data(sample_data)
    invalid_data = {'name': 'Bob', 'age': -5}
    process_data(invalid_data)
    wrong_type_data = ['not', 'a', 'dict']
    process_data(wrong_type_data)