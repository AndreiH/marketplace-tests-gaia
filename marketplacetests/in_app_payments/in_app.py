# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from marionette.by import By
from gaiatest.apps.base import Base


class InAppPayment(Base):

    # Products
    _buy_product_button_locator = (By.CSS_SELECTOR, '.item > button')
    _bought_product_locator = (By.CSS_SELECTOR, '#bought .item > h4')

    def __init__(self, marionette):
        Base.__init__(self, marionette)
        self.apps.switch_to_displayed_app()

    def tap_buy_product(self):
        self.wait_for_element_displayed(*self._buy_product_button_locator)
        self.marionette.find_element(*self._buy_product_button_locator).tap()
        from marketplacetests.firefox_accounts.app import FirefoxAccounts
        return FirefoxAccounts(self.marionette)

    @property
    def bought_product_text(self):
        return self.marionette.find_element(*self._bought_product_locator).text

    def wait_for_bought_products_displayed(self):
        self.wait_for_element_displayed(*self._bought_product_locator)
