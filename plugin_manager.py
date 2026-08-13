import os
import importlib
from base import BasePlugin
def discover_plugins(plugins_dir="plugins"):
    loaded_plugins = []
    if not os.path.exists(plugins_dir):
        os.makedirs(plugins_dir)
    for filename in os.listdir(plugins_dir):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = f"plugins.{filename[:-3]}"
            module = importlib.import_module(module_name)
            if hasattr(module, 'Plugin'):
                loaded_plugins.append(module.Plugin(BasePlugin))
    return loaded_plugins