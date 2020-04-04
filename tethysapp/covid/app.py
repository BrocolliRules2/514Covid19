from tethys_sdk.base import TethysAppBase, url_map_maker


class Covid(TethysAppBase):
    """
    Tethys app class for Covid 514 Project.
    """

    name = 'Covid 514 Project'
    index = 'covid:home'
    icon = 'covid/images/icon.gif'
    package = 'covid'
    root_url = 'covid'
    color = '#16a085'
    description = 'This app will help you deter'
    tags = 'CE514, FinalProject, Covid'
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
                url='covid',
                controller='covid.controllers.home'
            ),
        )

        return url_maps