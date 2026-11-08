from datetime import datetime
from pathlib import Path


def capture_screenshot(driver, test_name):
    screenshots_dir = Path(__file__).resolve().parents[1] / "screenshots" / "failures"
    screenshots_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = screenshots_dir / f"{test_name}_{timestamp}.png"
    driver.save_screenshot(str(file_path))
    return str(file_path)
