# stevedore/example/load_as_extension.py
from __future__ import print_function

import argparse

from stevedore import extension


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--width',
        default=60,
        type=int,
        help='maximum output width for text',
    )
    parsed_args = parser.parse_args()

    data = {
        'a': 'A',
        'b': 'B',
        'long': 'word ' * 80,
    }

    mgr = extension.ExtensionManager(
        namespace='myextensions',
        invoke_on_load=True,
        invoke_args=(parsed_args.width,),
    )

    mgr1 = extension.ExtensionManager(
        namespace='extensions',
        invoke_on_load=True,
        invoke_args=(parsed_args.width,),
    )
    print(mgr.names())
    print(mgr1.names())
