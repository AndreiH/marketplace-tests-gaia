# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from marketplacetests.marketplace_gaia_test import MarketplaceGaiaTestCase
from marketplacetests.marketplace.app import Marketplace


class TestMarketplaceWithoutConnectivity(MarketplaceGaiaTestCase):

    MARKETPLACE_DEV_NAME = 'Marketplace Dev'

    expected_error_title = u'Network connection unavailable'
    expected_error_message = u'Marketplace Dev requires a network connection. Try connecting to a Wi-Fi or mobile data network.'

    def setUp(self):
        MarketplaceGaiaTestCase.setUp(self)

        # disable all potential data connections
        if self.device.has_mobile_connection:
            self.data_layer.disable_cell_data()

        if self.device.has_wifi:
            self.data_layer.forget_all_networks()
            self.data_layer.disable_wifi()

    def test_marketplace_without_connectivity(self):
        marketplace = Marketplace(self.marionette, self.MARKETPLACE_DEV_NAME)
        marketplace.launch()

        self.apps.switch_to_displayed_app()

        self.assertEqual(marketplace.error_title_text, self.expected_error_title)
        self.assertEqual(marketplace.error_message_text, self.expected_error_message)
