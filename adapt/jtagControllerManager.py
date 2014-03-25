import pkgutil
import usb1

usbcontext = usb1.USBContext()

_controllerfilter = {}
_modules = []

for loader, module_name, is_pkg in pkgutil.iter_modules(['drivers']):
    module = loader.find_module(module_name).load_module(module_name)
    _modules.append(module)
    for reg in module.__filter__:
        fltr, cls = reg
        vid_dict = _controllerfilter.setdefault(fltr[0], {})
        vid_dict[fltr[1]] = cls

def getAttachedControllers():
    controllers = []
    for device in usbcontext.getDeviceList(skip_on_error=True):
        vid_dict = _controllerfilter.get(device.getVendorID())
        if vid_dict:
            driver_class = vid_dict.get(device.getProductID(), vid_dict.get(None))
            if driver_class:
                print "Found Driver for %04x:%04x: %s"%(device.getVendorID(), device.getProductID(), cls)
                controller = cls(device)
                controllers.append(controller)
            else:
                print "No Driver Found for %04x:%04x"%(device.getVendorID(), device.getProductID())
        else:
            pass
    return controllers

