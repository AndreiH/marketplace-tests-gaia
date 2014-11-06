# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import os

from gaiatest.gaia_test import GaiaTestCase


class MarketplaceGaiaTestCase(GaiaTestCase):

    def setUp(self):
        GaiaTestCase.setUp(self)
        self.install_certs()
        self.connect_to_network()
        self.wait_for_element_not_displayed('id', 'os-logo')

        # Use this to override the Marketplace app version
        self.MARKETPLACE_DEV_NAME = 'Marketplace'

    def install_certs(self):
        """ Install the marketplace-dev certs and set the pref required """
        certs_folder = os.path.join('marketplacetests', 'certs')
        for file_name in self.device.manager.listFiles('/data/b2g/mozilla/'):
            if file_name.endswith('.default'):
                profile_folder = file_name
                break
        for file_name in os.listdir(certs_folder):
            self.device.file_manager.push_file(os.path.join(certs_folder, file_name),
                                  remote_path='data/b2g/mozilla/%s' % profile_folder)
        self.data_layer.set_char_pref('dom.mozApps.signed_apps_installable_from',
                                      'https://marketplace-dev.allizom.org,https://marketplace.firefox.com')
        self.data_layer.set_bool_pref('dom.mozApps.use_reviewer_certs', True)
