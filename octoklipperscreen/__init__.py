from __future__ import absolute_import, unicode_literals
import octoklipperscreen.main as main
import octoprint.plugin

class HelloWorldPlugin(octoprint.plugin.StartupPlugin, octoprint.plugin.TemplatePlugin):
    def on_after_startup(self):
        self._logger.info("OctoKlipperScreen starting...")
        main.main()
        

__plugin_name__ = "Octo Klipper Screen"
__plugin_pythoncompat__ = ">=3.5,<=0"
__plugin_implementation__ = HelloWorldPlugin()