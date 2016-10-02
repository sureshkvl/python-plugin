from __future__ import print_function

import argparse

from stevedore import extension
from stevedore import driver


if __name__ == '__main__':
    extmgr = extension.ExtensionManager(
        namespace='jsonparser',
        invoke_on_load=True,
    )

    drv = driver.DriverManager(namespace='filedrivers',name='fileio')
    vale = drv.driver().readfile("/home/suresh/test.txt")
    print(vale)
    result = extmgr.__getitem__('simple').obj.format(vale)
    for chunk in result:
        print(chunk)
    print('')
    print(extmgr.names())
    print(drv.names())
