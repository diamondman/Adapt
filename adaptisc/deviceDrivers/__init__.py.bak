import os
import pkgutil

from proteusisc.jtagDevice import JTAGDevice

device_driver_lookup = {}
driver_count = 0
base_dir = os.path.dirname(os.path.realpath(__file__))

for loader, module_name, is_pkg in\
    pkgutil.iter_modules([base_dir]):
    driver_count += 1
    module = loader.find_module(module_name).load_module(module_name)
    for cls_ in module.__dict__.values():
        if isinstance(cls_, type) and cls_ is not JTAGDevice and\
           issubclass(cls_, JTAGDevice):
            for devid in cls_.devices:
                device_driver_lookup[devid] = cls_
