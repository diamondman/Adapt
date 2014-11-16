import pkgutil
import usb1
from os import environ
from os.path import join

usbcontext = usb1.USBContext()

_controllerfilter = {}
_modules = []

driver_count = 0
base_dir = environ.get('ADAPT_HOME', '/home/diamondman/Adapt')
for loader, module_name, is_pkg in pkgutil.iter_modules([join(base_dir,'adapt/drivers'),
                                                         join(base_dir, 'drivers')]):
    driver_count += 1
    module = loader.find_module(module_name).load_module(module_name)
    _modules.append(module)
    for reg in module.__filter__:
        fltr, cls = reg
        vid_dict = _controllerfilter.setdefault(fltr[0], {})
        vid_dict[fltr[1]] = cls

if not driver_count:
    print('\033[91m'+'Found 0 drivers.'+'\033[0m')
    if not base_dir:
        print('\033[93m'+'Your ADAPT_HOME env variable was not set. '\
            'This is likely why the drivers could not be loaded.'+'\033[0m')

def getAttachedControllers(cname=None):
    controllers = []
    for device in usbcontext.getDeviceList(skip_on_error=True):
        vid_dict = _controllerfilter.get(device.getVendorID())
        if vid_dict:
            driver_class = vid_dict.get(device.getProductID(), vid_dict.get(None))
            if driver_class:
                controller = driver_class(device)
                controllers.append(controller)
            else:
                print("No Driver Found for %04x:%04x"%(device.getVendorID(), device.getProductID()))

    if not cname:
        return controllers

    filteredcontrollers = []
    for controller in controllers:
        if controller.name == cname:
            filteredcontrollers.append(controller)
    return filteredcontrollers


