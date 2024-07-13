"""FSQ console client for transfering data to FSQ server."""

import logging
import argparse
import glob
import os
from fsq.api import FSQ_PROTOCOL_VERSION
from fsq.api import Api as FsqApi
from fsq.api import FsqStorageDest

if __name__ == "__main__":
    dest_choices = {
        'null': FsqStorageDest.FSQ_STORAGE_NULL,
        'local': FsqStorageDest.FSQ_STORAGE_LOCAL,
        'lustre': FsqStorageDest.FSQ_STORAGE_LUSTRE,
        'tsm': FsqStorageDest.FSQ_STORAGE_TSM,
        'lustre_tsm': FsqStorageDest.FSQ_STORAGE_LUSTRE_TSM,
    }

    parser = argparse.ArgumentParser(description=f'FSQ client for sending files '
                                     f'via FSQ protocol version {FSQ_PROTOCOL_VERSION}')
    parser.add_argument('-f', '--fsname', type=str, required=True,
                        help='filespace name (e.g /lustre)')
    parser.add_argument('-a', '--fpath', type=str, required=True,
                        help='file path (e.g /lustre/experiment/data)')
    parser.add_argument('-o', '--storagedest', type=str, choices=dest_choices,
                        default='null', help='storage destination [default: null]')
    parser.add_argument('-n', '--node', type=str, required=True, help='TSM node name')
    parser.add_argument('-p', '--password', type=str, required=True, help='TSM password')
    parser.add_argument('-s', '--servername', type=str, required=True, help='FSQ hostname')
    parser.add_argument('-v', '--verbose', type=str, choices=['critical', 'error',
                                                              'warning', 'info', 'debug'],
                        default='info', help='verbose level [default: info]')
    parser.add_argument('files', nargs='+', help='files to send (use \'*\' to specify all files)')
    args = parser.parse_args()

    logging.basicConfig(level=getattr(logging, args.verbose.upper(), logging.INFO),
                        format='[%(asctime)s %(filename)s:%(lineno)d %(levelname)s] %(message)s')

    filenames = []
    for pattern in args.files:
        for filename in glob.glob(pattern):
            if os.path.isfile(filename):
                filenames.append(os.path.relpath(filename))

    if not filenames:
        logging.error('no files provided')

    fsq = FsqApi()
    fsq.connect(node=args.node, password=args.password, hostname=args.servername, port=7625)

    for filename in filenames:

        fpath = os.path.join(args.fpath, '', filename)
        fsq.open(fs=args.fsname,fpath=fpath,desc='',dest=dest_choices[args.storagedest])
        file_size = os.path.getsize(filename)

        with open(filename, 'rb') as f:
            file_data = f.read()
            fsq.write(file_data, file_size)
        fsq.close()

    fsq.disconnect()
