#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import yaml
import shutil
import glob
import datetime
import os
import pathlib

DEFAULT_CONF={'target_dir': ['~/Downloads', '~/Desktop'], 'outdir': '~/housekeep/', 'exts': {'iso': 'iso', 'csv': 'csv', 'dmg': 'dmg', 'doc': 'doc', 'docx': 'doc', 'drawio': 'drawio', 'jpg': 'jpg', 'jpeg': 'jpg', 'JPG': 'jpg', 'json': 'json', 'log': 'log', 'm4a': 'm4a', 'pdf': 'pdf', 'png': 'png', 'PNG': 'png', 'HEIC': 'png', 'ppt': 'ppt', 'pptx': 'ppt', 'py': 'py', 'txt': 'txt', 'xls': 'xls', 'xlsx': 'xls', 'yaml': 'yml', 'yml': 'yml', 'zip': 'zip', 'tar.gz': 'tar', 'tgz': 'tar', 'md': 'md', 'other': 'other'}}

def hk_argparse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', '-d', nargs="*", type=str, help='Target dir name')
    parser.add_argument('--conf', '-c', type=str, help='Configuration file name')
    return parser.parse_args()

def expand_target_dir(conf, dirs):
    if dirs:
        conf['target_dir'].extend(parser.parse_args().dir)

def init_config(conf):
    global DEFAULT_CONF
    with open(conf, mode='w') as f:
        yaml.dump(DEFAULT_CONF, f, default_flow_style=False, allow_unicode=True)

def load_config(conf):
    if conf:
        conf_path = conf
    else:
        conf_path = os.path.expanduser('~/.housekeep_conf.yml')
    if not os.path.exists(conf_path):
        init_config(conf_path)
    with open(conf_path) as f:
        conf = yaml.safe_load(f)
    return conf

def housekeep(dirname, conf):
    for ext in conf['exts'].keys():
        outdir = os.path.expanduser(f'{conf["outdir"]}/{conf["exts"][ext]}')
        os.makedirs(outdir, exist_ok=True)
        try:
          expand_path = os.path.expanduser(dirname)
          target_list = glob.glob(f'{expand_path}/*.{ext}')
          for target in target_list:
            try:
              shutil.move(target, outdir)
            except:
              fname=f'{target.rsplit("/")[-1]}_{str(datetime.date.today())}'
              newout = os.path.join(outdir,fname)
              shutil.move(target, newout)
        except FileNotFoundError:
          pass

def do_housekeep():
    args = hk_argparse()
    conf = load_config(args.conf)
    expand_target_dir(conf, args.dir)
    for dirname in conf['target_dir']:
        housekeep(dirname, conf)

if __name__ == '__main__':
    do_housekeep()
