from nautobot.apps import NautobotAppConfig

class DevicesConfig(NautobotAppConfig):
    name = 'nautobot_devices'
    verbose_name = 'Devices'
    description = 'An example app for development purposes'
    version = '0.1'
    author = 'Iran Alyf'
    author_email = 'iranalyf@gmail.com.com'
    base_url = 'sample-devices'
    required_settings = []
    default_settings = {
        'loud': False
    }

config = DevicesConfig