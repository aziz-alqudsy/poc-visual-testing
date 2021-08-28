from os import scandir
from PIL import Image, ImageDraw

class Analysis():
    def __init__(self, browser):
        self.browser = browser

    def grid(self, file_name):
        # open image
        ss_staging = Image.open("./screenshots/ss_staging.png")
        ss_production = Image.open("./screenshots/ss_production.png")

        # initiate column, row, and size
        columns = 60
        rows = 80
        screen_width, screen_height = ss_staging.size

        # creating block ceiling on image
        block_width = ((screen_width - 1) // columns) + 1
        block_height = ((screen_height - 1) // rows) + 1

        # creating grid
        for y in range(0, screen_height, block_height+1):
            for x in range(0, screen_width, block_width+1):
                region_staging = self.process_grid(ss_staging, x, y, block_width, block_height)
                region_prodcution = self.process_grid(ss_production, x, y, block_width, block_height)

                if region_staging is not None and region_prodcution is not None and region_prodcution != region_staging:
                    draw = ImageDraw.Draw(ss_staging)
                    draw.rectangle((x, y, x+block_width, y+block_height), outline="red")

        # save new image with grid
        ss_staging.save(f"./screenshots/{file_name}.png")

    def process_grid(self, image, x, y, width, height):
        # initiate region total
        region_total = 0

        # This is the sensitivity factor, the larger it is the less sensitive the comparison
        factor = 100

        # scanning coordinate
        for coordinateY in range(y, y+height):
            for coordinateX in range(x, x+width):
                try:
                    pixel = image.getpixel((coordinateX, coordinateY))
                    region_total += sum(pixel)/4
                except:
                    return "Sorry, can't get pixel coordinate!"

        return region_total/factor
