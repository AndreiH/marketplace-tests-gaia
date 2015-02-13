# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
from fxapom.fxapom import FxATestAccount

from marketplacetests.marketplace_gaia_test import MarketplaceGaiaTestCase
from marketplacetests.marketplace.app import Marketplace


class TestMarketplaceFeedback(MarketplaceGaiaTestCase):
    feedback_submitted_message = u'Feedback submitted. Thanks!'
    test_comment = 'This is a test comment.'

    def test_marketplace_feedback_user(self):
        acct = FxATestAccount(base_url=self.base_url).create_account()

        # launch marketplace dev and go to marketplace
        marketplace = Marketplace(self.marionette, self.MARKETPLACE_DEV_NAME)
        marketplace.launch()
        marketplace.login(acct.email, acct.password)

        # go to feedback tab
        marketplace.select_setting_feedback()

        # enter and submit your feedback
        marketplace.enter_feedback(self.test_comment)
        marketplace.submit_feedback()

        # catch the notification
        marketplace.wait_for_notification_message_displayed()
        message_content = marketplace.notification_message

        # verify if the notification is right
        self.assertEqual(message_content, self.feedback_submitted_message)
