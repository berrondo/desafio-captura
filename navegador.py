#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver


class Navegador:
    browser = None

    @classmethod
    def get_browser(cls):
        firefox_profile = webdriver.FirefoxProfile()

        firefox_profile.set_preference('permissions.default.stylesheet', 2)
        firefox_profile.set_preference('permissions.default.image', 2)
        firefox_profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')

        cls.browser = webdriver.Firefox(firefox_profile=firefox_profile)
        return cls.browser

    @classmethod
    def quit(cls):
        try:
            cls.browser.quit()
        except AttributeError:
            pass