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
    color = '#36992A'
    description = 'This app will help you to be aware of COVID 19'
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
            UrlMap(
                name='info',
                url='covid-info',
                controller='covid.controllers.info'
            ),
         
            UrlMap(
                name='help',
                url='covid-help',
                controller='covid.controllers.help'
            ),
            
        )

        return url_maps
