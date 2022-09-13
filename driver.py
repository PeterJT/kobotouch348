#!/usr/bin/env python2
# vim:fileencoding=UTF-8:ts=4:sw=4:sta:et:sts=4:ai

__license__ = 'GPL v3'
__copyright__ = '2015, David Forrester <davidfor@internode.on.net>'
__docformat__ = 'markdown en'

import os

from calibre.devices.kobo.driver import KOBOTOUCH
from calibre.devices.usbms.driver import debug_print

class KOBOTOUCH348(KOBOTOUCH):
    '''
    Driver to enable new Kobo devices in calibre 3.48.

    NOTE: The only reason this driver exists is to allow use of the newer Kobo devices with calibre 3.48.
    And it will only be supported on platforms that later versions of calibre cannot run on. So, don't ask if about it 
    if you can install recent versions of calibre.
    '''

    name = 'KOBOTOUCH348'
    author = 'David Forrester'
    description = 'Communicate with the Kobo ereaders releases since calibre 4 was released. Currently supports the Kobo Elipsa, Kobo Libra 2, Kobo Nia and Kobo Sage. DO NOT use with anything other than calibre v3.48'

    minimum_calibre_version = (3, 48, 0)
    version = (1, 0, 2)

    supported_dbversion             = 166
    max_supported_fwversion         = (4, 31, 19075)
    min_elipsa_fwversion            = (4, 28, 17820)
    min_libra2_fwversion            = (4, 29, 18730)
    min_sage_fwversion              = (4, 29, 18730)

    ELIPSA_PRODUCT_ID   = [0x4233]
    LIBRA2_PRODUCT_ID   = [0x4234]
    NIA_PRODUCT_ID      = [0x4230]
    SAGE_PRODUCT_ID     = [0x4231]
    PRODUCT_ID          = ELIPSA_PRODUCT_ID + LIBRA2_PRODUCT_ID + NIA_PRODUCT_ID + SAGE_PRODUCT_ID + KOBOTOUCH.PRODUCT_ID
    debug_print("KOBOTOUCH348: PRODUCT_ID= [%s]" % (", ".join(hex(n) for n in PRODUCT_ID)))

    def isElipsa(self):
        return self.detected_device.idProduct in self.ELIPSA_PRODUCT_ID

    def isLibra2(self):
        return self.detected_device.idProduct in self.LIBRA2_PRODUCT_ID

    def isNia(self):
        return self.detected_device.idProduct in self.NIA_PRODUCT_ID

    def isSage(self):
        return self.detected_device.idProduct in self.SAGE_PRODUCT_ID

    def cover_file_endings(self):
        if self.isElipsa():
            _cover_file_endings = self.AURA_ONE_COVER_FILE_ENDINGS
        elif self.isLibra2():
            _cover_file_endings = self.LIBRA_H2O_COVER_FILE_ENDINGS
        elif self.isNia():
            _cover_file_endings = self.GLO_COVER_FILE_ENDINGS
        elif self.isSage():
            _cover_file_endings = self.FORMA_COVER_FILE_ENDINGS
        else:
            _cover_file_endings = super(KOBOTOUCH348, self).cover_file_endings()

        return _cover_file_endings
    
    def set_device_name(self):
        if self.isElipsa():
            device_name = 'Kobo Elipsa'
        elif self.isLibra2():
            device_name = 'Kobo Libra 2'
        elif self.isNia():
            device_name = 'Kobo Nia'
        elif self.isSage():
            device_name = 'Kobo Sage'
        else:
            device_name = super(KOBOTOUCH348, self).set_device_name()
        self.__class__.gui_name = device_name
        return device_name
