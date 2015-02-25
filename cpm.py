#!/usr/bin/env python

import sys
import os
import shutil
try:
    sys.path.append(os.path.dirname(os.readlink(__file__)) + '/simplejson/')
except OSError:
    sys.path.append(os.path.dirname(__file__) + '/simplejson/')

import simplejson as json

CPM_HOME = os.path.expanduser('~/.cpm')
CPM_GIT = 'https://github.com/castisdev'

def print_usage():
    print ''
    print 'Usage: cpm <command>'
    print 'where <command> is one of:'
    print '    help, info, init, install, list, remove, update'


def print_init():
    print '[Error] cpm not initialized. please run `cpm init` first.'
    print_usage()


def init():
    if initialized():
        return
    os.makedirs(CPM_HOME)
    print '[Success] cpm initialized.'


def initialized():
    return os.path.isdir(CPM_HOME)


def check_init():
    if not initialized():
        print_init()
        sys.exit(1)


def install(pkg):
    check_init()
    path = CPM_HOME + '/' + pkg
    try:
        install_from_git(path, pkg)
        if not os.path.exists(path + '/package.json'):
            print '[Error] package.json not exist.'
            raise IOError
        data = open(path + '/package.json')
        j = json.load(data)
        if 'bin' in j:
            install_bins(path, j['bin'])
        print 'installed %s at: %s' % (pkg, path)
    except IOError:
        print '[Error] IOError occured. install failed'
        shutil.rmtree(path)
    except OSError:
        print '[Error] OSError occured. install failed'
        shutil.rmtree(path)


def install_from_git(path, pkg):
    uri = '%s/%s.git' % (CPM_GIT, pkg)
    cmd = 'git clone --recursive %s %s' % (uri, path)
    print cmd
    r = os.system(cmd)
    if r != 0:
        print '[Error] command `%s` failed with code %d' % (cmd, r)
        raise IOError

def install_bins(path, bins):
    for k in bins.keys():
        cmd = 'ln -sf %s/%s /usr/local/bin/%s' % (path, bins[k], k)
        r = os.system(cmd)
        if r != 0:
            print '[Error] command `%s` failed with code %d' % (cmd, r)
            raise OSError


def list():
    check_init()
    for s in os.listdir(CPM_HOME):
        if os.path.isdir(CPM_HOME + '/' + s):
            data = open('%s/%s/package.json' % (CPM_HOME, s))
            j = json.load(data)
            print '%s@%s' % (j['name'], j['version'])


def info(pkg):
    check_init()
    info_path = '%s/%s/package.json' % (CPM_HOME, pkg)
    if os.path.exists(info_path):
        os.system('cat %s' % info_path)
    else:
        print '[Error] %s package not installed.' % pkg


def remove(pkg):
    check_init()
    path = CPM_HOME + '/' + pkg
    if not os.path.exists(path):
        print '[Error] %s not installed yet.'
        return
    try:
        data = open(path + '/package.json')
        j = json.load(data)
        if 'bin' in j:
            remove_bins(path, j['bin'])
        shutil.rmtree(path)
    except IOError:
        print '[Error] IOError occured. remove failed.'
        return
    except OSError:
        print '[Error] OSError occured. remove failed.'
        return
    print 'removed', pkg


def remove_bins(path, bins):
    for k in bins.keys():
        cmd = 'rm /usr/local/bin/%s' % k
        os.system(cmd)


def update(pkg):
    check_init()
    path = CPM_HOME + '/' + pkg
    try:
        cmd = 'cd %s && git pull --recurse-submodules' % path
        print cmd
        r = os.system(cmd)
        if r != 0:
            print '[Error] command `%s` failed with code %d' % (cmd, r)
    except OSError:
        print '[Error] OSError occured. update failed'


def main(argv):
    try:
        cmd = argv[1]
        if cmd == 'help':
            print_usage()
        elif cmd == 'init':
            init()
        elif cmd == 'install':
            install(argv[2])
        elif cmd == 'list':
            list()
        elif cmd == 'info':
            info(argv[2])
        elif cmd == 'remove':
            remove(argv[2])
        elif cmd == 'update':
            update(argv[2])
        else:
            print_usage()
    except IndexError:
        if len(argv) != 1:
            print '[Error] invalid args'
        print_usage()


if __name__ == '__main__':
    main(sys.argv)
