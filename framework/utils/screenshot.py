import os
from datetime import datetime


def take_screenshot(driver, test_name):

    screenshot_dir = "screenshots"
    os.makedirs(screenshot_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = f"{test_name}_{timestamp}.png"

    file_path = os.path.join(screenshot_dir, filename)

    driver.save_screenshot(file_path)

    return file_path