# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import re

from marionette.by import By
from gaiatest.apps.base import Base
from gaiatest.apps.base import PageRegion


class SearchResults(Base):

    _search_results_area_locator = (By.ID, 'search-results')
    _search_results_loading_locator = (By.CSS_SELECTOR, 'div.loading')
    _search_result_locator = (By.CSS_SELECTOR, '#search-results li.item')

    def __init__(self, marionette):
        Base.__init__(self, marionette)
        self.wait_for_element_not_present(*self._search_results_loading_locator)

    @property
    def search_results(self):
        self.wait_for_element_displayed(*self._search_result_locator)
        search_results = self.marionette.find_elements(*self._search_result_locator)
        return [Result(self.marionette, result) for result in search_results]


class Result(PageRegion):

    _name_locator = (By.CSS_SELECTOR, '.info > h3')
    _author_locator = (By.CSS_SELECTOR, '.info .author')
    _install_button_locator = (By.CSS_SELECTOR, '.button.product.install')

    @property
    def name(self):
        return self.root_element.find_element(*self._name_locator).text

    @property
    def author(self):
        return self.root_element.find_element(*self._author_locator).text

    @property
    def install_button_text(self):
        return self.root_element.find_element(*self._install_button_locator).text

    def tap_install_button(self):
        self.root_element.find_element(*self._install_button_locator).tap()
        self.marionette.switch_to_frame()

    def tap_app(self):
        app_name = self.root_element.find_element(*self._name_locator)
        app_name.tap()
        from marketplacetests.marketplace.regions.app_details import Details
        return Details(self.marionette)
