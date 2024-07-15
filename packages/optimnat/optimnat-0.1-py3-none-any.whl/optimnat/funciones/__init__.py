import importlib
import pkgutil

# Descubrir e importar todos los submódulos
for _, module_name, _ in pkgutil.iter_modules(__path__):
    module = importlib.import_module(f".{module_name}", package=__name__)
    for attr_name in dir(module):
        if not attr_name.startswith("_"):
            globals()[attr_name] = getattr(module, attr_name)

# Crear __all__ dinámicamente
__all__ = [name for name in globals() if not name.startswith("_")]
