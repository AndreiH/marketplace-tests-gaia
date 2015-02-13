# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from fxapom.fxapom import FxATestAccount

from marketplacetests.marketplace_gaia_test import MarketplaceGaiaTestCase
from marketplacetests.marketplace.app import Marketplace
from marketplacetests.payment.app import Payment


class TestMarketplaceCreateConfirmPin(MarketplaceGaiaTestCase):

    def test_create_confirm_pin(self):

        APP_NAME = 'Test Zippy With Me'
        PIN = '1234'
        acct = FxATestAccount(base_url=self.base_url).create_account()

        if self.apps.is_app_installed(APP_NAME):
            self.apps.uninstall(APP_NAME)

        marketplace = Marketplace(self.marionette, self.MARKETPLACE_DEV_NAME)
        marketplace.launch()

        marketplace.login(acct.email, acct.password)

        marketplace.set_region('United States')

        details_page = marketplace.navigate_to_app(APP_NAME)
        details_page.tap_install_button()

        payment = Payment(self.marionette)
        payment.create_pin(PIN)
        payment.wait_for_buy_app_section_displayed()
        self.assertIn(APP_NAME, payment.app_name)
