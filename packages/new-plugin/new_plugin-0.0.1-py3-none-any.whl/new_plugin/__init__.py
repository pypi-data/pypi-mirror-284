from testy.plugins.hooks import TestyPluginConfig, hookimpl

class NewPluginConfig(TestyPluginConfig):
    package_name = 'new_plugin'
    verbose_name = 'New Plugin'
    description = 'LOL KEK CHEBUREK'
    version = '0.0.1'
    plugin_base_url = 'new_plugin'
    index_reverse_name = 'new_plugin'
    urls_module = 'new_plugin.urls'

@hookimpl
def config():
    return NewPluginConfig