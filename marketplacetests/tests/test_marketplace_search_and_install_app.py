# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from gaiatest.apps.homescreen.app import Homescreen
from gaiatest.apps.homescreen.regions.confirm_install import ConfirmInstall
from marionette.by import By

from marketplacetests.marketplace_gaia_test import MarketplaceGaiaTestCase
from marketplacetests.marketplace.app import Marketplace


class TestSearchMarketplaceAndInstallApp(MarketplaceGaiaTestCase):

    APP_INSTALLED = False

    # System app confirmation button to confirm installing an app
    _yes_button_locator = (By.ID, 'app-install-install-button')

    # System app notification install message
    _notification_install_locator = (By.CSS_SELECTOR, '#system-banner > p')

    def test_search_and_install_app(self):
        marketplace = Marketplace(self.marionette, self.MARKETPLACE_DEV_NAME)
        marketplace.launch()

        self.app_name = marketplace.popular_apps[0].name

        # Remove the app if already installed
        if self.apps.is_app_installed(self.app_name):
            self.apps.kill(marketplace.app)
            self.apps.uninstall(self.app_name)
            marketplace.launch()
        marketplace.switch_to_marketplace_frame()

        app_author = marketplace.popular_apps[0].author
        results = marketplace.search(self.app_name)

        self.assertGreater(len(results.search_results), 0, 'No results found.')

        first_result = results.search_results[0]

        self.assertEquals(first_result.name, self.app_name, 'First app has the wrong name.')
        self.assertEquals(first_result.author, app_author, 'First app has the wrong author.')

        # Find and click the install button to the install the web app
        self.assertEquals(first_result.install_button_text, 'Free', 'Incorrect button label.')

        first_result.tap_install_button()
        self.wait_for_downloads_to_finish()

        # Confirm the installation and wait for the app icon to be present
        confirm_install = ConfirmInstall(self.marionette)
        confirm_install.tap_confirm()

        self.assertEqual('%s installed' % self.app_name, marketplace.install_notification_message)
        self.APP_INSTALLED = True

        # Press Home button
        self.device.touch_home_button()

        # Check that the icon of the app is on the homescreen
        homescreen = Homescreen(self.marionette)
        self.apps.switch_to_displayed_app()

        self.assertTrue(homescreen.is_app_installed(self.app_name))
