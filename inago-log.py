import time
from datetime import datetime
from model import LogModel
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--mute-audio")
driver = webdriver.Chrome(chrome_options=options)
driver.get("https://inagoflyer.appspot.com/btcmac")


def get_volumes():
    buy = sell = 0
    for _buy_vol in driver.find_elements_by_id("buyVolumePerMeasurementTime"):
        buy = float(_buy_vol.text)

    for _sell_vol in driver.find_elements_by_id("sellVolumePerMeasurementTime"):
        sell = float(_sell_vol.text)

    return sell, buy


while True:
    log = LogModel()
    _buy, _sell = get_volumes()
    log.add([datetime.now().strftime('%Y/%m/%d %H:%M:%S'), _buy, _sell])
    time.sleep(1)
