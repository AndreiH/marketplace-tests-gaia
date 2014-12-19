# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from gaiatest.apps.base import Base
from marionette.by import By
from marionette.wait import Wait


class Payment(Base):

    _payment_frame_locator = (By.CSS_SELECTOR, "#trustedui-frame-container > iframe")

    # Create/confirm PIN
    _pin_container_locator = (By.CSS_SELECTOR, '.pinbox')
    _pin_digit_holder_locator = (By.CSS_SELECTOR, '.pinbox span')
    _pin_continue_button_locator = (By.CSS_SELECTOR, '.cta')
    _pin_heading_locator = (By.CSS_SELECTOR, 'section.content h1')

    # Final buy app panel
    _app_name_locator = (By.CSS_SELECTOR, '.product .title')
    _buy_button_locator = (By.XPATH, "//button[text()='Buy']")
    _cancel_button_locator = (By.XPATH, "//button[text()='Cancel']")

    def __init__(self, marionette):
        Base.__init__(self, marionette)
        self.switch_to_payment_frame()

    def switch_to_payment_frame(self):
        self.marionette.switch_to_frame()
        self.wait_for_element_present(*self._payment_frame_locator)
        payment_iframe = self.marionette.find_element(*self._payment_frame_locator)
        self.marionette.switch_to_frame(payment_iframe)

    @property
    def app_name(self):
        return self.marionette.find_element(*self._app_name_locator).text

    @property
    def pin_heading(self):
        return self.marionette.find_element(*self._pin_heading_locator).text

    def create_pin(self, pin):
        self.wait_for_element_displayed(*self._pin_container_locator)
        Wait(marionette=self.marionette).until(lambda m: 'Create' in self.pin_heading)
        self.marionette.find_element(*self._pin_container_locator).send_keys(pin)
        self.tap_pin_continue()
        self.wait_for_element_displayed(*self._pin_container_locator)
        Wait(marionette=self.marionette).until(lambda m: 'Confirm' in self.pin_heading)
        self.marionette.find_element(*self._pin_container_locator).send_keys(pin)
        self.tap_pin_continue()

    def tap_pin_continue(self):
        button = self.marionette.find_element(*self._pin_continue_button_locator)
        Wait(marionette=self.marionette).until(lambda m: button.is_enabled())
        button.tap()

    def wait_for_buy_app_section_displayed(self):
        self.wait_for_element_displayed(*self._buy_button_locator)

    def tap_buy_button(self):
        self.marionette.find_element(*self._buy_button_locator).tap()
        self.marionette.switch_to_frame()
        self.wait_for_element_not_present(*self._payment_frame_locator)
        self.marionette.switch_to_frame()
