# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from marionette.by import By
from gaiatest.apps.base import Base


class FirefoxAccounts(Base):

    # iframe
    _ff_accounts_frame_locator = (By.CSS_SELECTOR, "iframe[name='fxa']")

    # firefox accounts login
    _body_loading_locator = (By.CSS_SELECTOR, 'body.loading')
    _email_input_locator = (By.CSS_SELECTOR, '.email')
    _password_input_locator = (By.ID, 'password')
    _sign_in_button_locator = (By.ID, 'submit-btn')
    _firefox_logo_locator = (By.ID, 'fox-logo')

    def __init__(self, marionette):
        Base.__init__(self, marionette)
        self.marionette.switch_to_frame()
        self.wait_for_element_present(*self._ff_accounts_frame_locator)
        self.frame = self.marionette.find_element(*self._ff_accounts_frame_locator)
        self.marionette.switch_to_frame(self.frame)
        self.wait_for_element_not_present(*self._body_loading_locator)
        self.wait_for_element_displayed(*self._firefox_logo_locator)

    def login(self, email, password):
        self.wait_for_email_input()
        self.type_email(email)
        self.wait_for_email_input()
        self.type_password(password)
        self.tap_sign_in()

    def wait_for_email_input(self):
        self.wait_for_element_displayed(*self._email_input_locator)

    def type_email(self, value):
        email_field = self.marionette.find_element(*self._email_input_locator)
        email_field.send_keys(value)

    def wait_for_password_input(self):
        self.wait_for_element_displayed(*self._password_input_locator)

    def type_password(self, value):
        password_field = self.marionette.find_element(*self._password_input_locator)
        password_field.send_keys(value)

    def tap_sign_in(self):
        self.marionette.find_element(*self._sign_in_button_locator).tap()

