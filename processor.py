from typing import List

class ClickProcessor:
    """
    A class to process click events for automation.
    """
    def __init__(self, interval: float, click_count: int) -> None:
        """
        Initializes the ClickProcessor with an interval and click count.
        
        :param interval: Time interval between clicks in seconds.
        :param click_count: Number of clicks to perform.
        """
        self.interval = interval
        self.click_count = click_count

    def perform_clicks(self) -> None:
        """
        Simulates the click actions based on the parameters set during initialization.
        """
        import time
        for _ in range(self.click_count):
            self.click()
            time.sleep(self.interval)

    @staticmethod
    def click() -> None:
        """
        Simulates a single click action.
        """
        print("Click!")

if __name__ == '__main__':
    click_processor = ClickProcessor(0.5, 10)
    click_processor.perform_clicks()