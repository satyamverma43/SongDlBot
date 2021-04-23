import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "1747114944:AAF8Du-Rxl-C1nyDnFLGa4QwZs78GfwcRMw")

    APP_ID = int(os.environ.get("APP_ID", 5056902)

    API_HASH = os.environ.get("API_HASH", "c8cb10848ef55d24db42ae075fd54ffb")
