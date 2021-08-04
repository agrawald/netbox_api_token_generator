from extras.plugins import PluginConfig

class ApiTokenGeneratorConfig(PluginConfig):
    name = 'netbox_api_token_generator'
    verbose_name = 'Netbox API token generator'
    description = 'Plugin for generating API token for a user'
    version = '0.1'
    author = 'Dheeraj Agrawal'
    author_email = 'dheeraj.agrawal@cyber.gov.au'
    base_url = 'token'
    required_settings = []
    default_settings = {
        'loud': False
    }

config = ApiTokenGeneratorConfig
