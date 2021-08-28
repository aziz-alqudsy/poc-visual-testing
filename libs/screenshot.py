class Screenshot():
    def __init__(self, browser):
        self.browser = browser

    def open(self, url, file_name):
        # save screenshot from web
        self.browser.get(url)
        self.browser.maximize_window()
        print(f"Capturing {url} screenshot as {file_name}..")
        self.browser.save_screenshot(f"./screenshots/{file_name}.png")
        print("Screenshot is saved!")
