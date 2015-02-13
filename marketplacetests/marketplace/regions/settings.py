# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from marionette.by import By
from gaiatest.apps.base import Base


class Settings(Base):

    _email_locator = (By.CSS_SELECTOR, '.email.account-field > p')
    _save_locator = (By.CSS_SELECTOR, 'footer > p > button')
    _sign_in_button_on_my_apps_locator = (By.CSS_SELECTOR, '#account-settings a.button.persona:not(.register)')
    _sign_in_button_locator = (By.CSS_SELECTOR, 'a.button.login')
    _sign_out_button_locator = (By.CSS_SELECTOR, 'a.button.logout')
    _back_button_locator = (By.ID, 'nav-back')
    _save_changes_button_locator = (By.XPATH, "//section[@id='account-settings']//button[text()='Save Changes']")
    _my_apps_tab_locator = (By.CSS_SELECTOR, '.tab-link[href="/purchases"]')
    _login_required_message_locator = (By.CSS_SELECTOR, '.only-logged-out .notice')

    def __init__(self, marionette):
        Base.__init__(self, marionette)
        self.wait_for_element_displayed(*self._sign_in_button_locator)

    def tap_back(self):
        self.marionette.find_element(*self._back_button_locator).tap()
        from marketplacetests.marketplace.app import Marketplace
        return Marketplace(self.marionette)

    def wait_for_sign_in_displayed(self):
        self.wait_for_element_displayed(*self._sign_in_button_locator)

    def tap_sign_in(self):
        self.marionette.find_element(*self._sign_in_button_locator).tap()
        from marketplacetests.firefox_accounts.app import FirefoxAccounts
        return FirefoxAccounts(self.marionette)

    def tap_sign_in_from_my_apps(self):
        self.marionette.find_element(*self._sign_in_button_on_my_apps_locator).tap()
        from marketplacetests.firefox_accounts.app import FirefoxAccounts
        return FirefoxAccounts(self.marionette)

    def wait_for_sign_out_button(self):
        self.wait_for_element_displayed(*self._sign_out_button_locator)

    def tap_sign_out(self):
        self.wait_for_sign_out_button()
        self.marionette.find_element(*self._sign_out_button_locator).tap()

    def tap_save_changes(self):
        self.marionette.find_element(*self._save_changes_button_locator).tap()

    @property
    def email(self):
        return self.marionette.find_element(*self._email_locator).text

    def go_to_my_apps_page(self):
        self.marionette.find_element(*self._my_apps_tab_locator).tap()
        return MyApps(self.marionette)


class MyApps(Base):

    _login_required_message_locator = (By.CSS_SELECTOR, '#account-settings .main div p')
    _my_apps_list_locator = (By.CSS_SELECTOR, '.item.result')
    _settings_page_locator = (By.CSS_SELECTOR, '.tab-link[href="/settings"]')

    @property
    def login_required_message(self):
        return self.marionette.find_element(*self._login_required_message_locator).text

    @property
    def my_apps_list(self):
        return self.marionette.find_elements(*self._my_apps_list_locator)

    def go_to_settings_page(self):
        self.marionette.find_element(*self._settings_page_locator).tap()
