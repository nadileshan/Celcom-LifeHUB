import os
import datetime

# Replace "test_name" with the actual name of your test
test_name = "test_name"
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Create a new directory for the test screenshots
directory = f"{test_name}_{timestamp}"
parent_dir = "screenshots"
path = os.path.join(parent_dir, directory)
os.makedirs(path, exist_ok=True)

# Use the path variable to specify the location for saving the screenshot
# driver.save_screenshot(f"{path}/screenshot.png")
