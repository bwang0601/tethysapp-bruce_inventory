from tethys_sdk.base import TethysAppBase, url_map_maker


class BruceInventory(TethysAppBase):
    """
    Tethys app class for Bruce Inventory.
    """

    name = 'Bruce Inventory'
    index = 'bruce_inventory:home'
    icon = 'bruce_inventory/images/icon.gif'
    package = 'bruce_inventory'
    root_url = 'bruce-inventory'
    color = '#2980b9'
    description = 'Place a brief description of your app here.'
    tags = ''
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='bruce-inventory',
                controller='bruce_inventory.controllers.home'
            ),
        )

        return url_maps
