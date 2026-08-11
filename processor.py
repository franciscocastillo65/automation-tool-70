import json
import logging

logger = logging.getLogger(__name__)

class DataProcessor:
    def __init__(self, data):
        self.data = data

    def clean(self):
        logger.debug("Starting data cleaning")
        self.data = [item for item in self.data if self.is_valid(item)]
        logger.debug("Data cleaning completed")

    def is_valid(self, item):
        return isinstance(item, dict) and 'value' in item

    def process(self):
        logger.debug("Processing data")
        processed_data = [self.transform(item) for item in self.data]
        logger.info("Data processing completed")
        return processed_data

    def transform(self, item):
        logger.debug(f"Transforming item: {item}")
        return json.dumps(item)

if __name__ == '__main__':
    sample_data = [
        {'value': 1},
        {'value': 2},
        {'wrong_key': 3},
        {'value': 4},
    ]
    processor = DataProcessor(sample_data)
    processor.clean()
    result = processor.process()
    print(result)