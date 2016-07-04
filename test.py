#!/usr/bin/python
#encoding: utf-8
"""
    直接运行该文件，python test.py test_manual
    或者 python test.py test_auto
"""
import argparse
from stevedore import driver

def test_manual():
    from scheduler.memory import memoryscheduler
    dt = {13:'id1',324:'id2',434:'id3','memory':[13,324,434]}
    driver = memoryscheduler()
    print 'test_manual: %s' % driver.scheduler(dt)
 
def test_DriverManager():
    """
        测试stevedore.driver.DriverManager,每次只取出指定的
    """
    from stevedore import driver
    dt = {13:'id1',324:'id2',434:'id3','memory':[13,324,434]}
    mgr = driver.DriverManager(
          namespace='sora.scheduler',
          name='randombase',
          invoke_on_load=True,         #设置为true，即载入后自动实例化插件类，如果是函数，则调用
    )
    for item in range(5):
        print 'test_auto: %s' % mgr.driver.scheduler(dt)

def test_ExtensionManager():
    """
        测试stevedore.extension.ExtensionManager,每次都会把所有的插件都取出来
    """
    from stevedore.extension import ExtensionManager
    dt = {13:'id1',324:'id2',434:'id3','memory':[13,324,434]}
    dex = ExtensionManager(namespace='sora.scheduler')
    count = len(dex.extensions)
    for item in range(count):
        print dex.extensions[item].plugin().scheduler(dt)

def test_NamedExtensionManager():
    from stevedore.named import NamedExtensionManager
    dt = {13:'id1',324:'id2',434:'id3','memory':[13,324,434]}
    nem = NamedExtensionManager(namespace='sora.scheduler', names=['memorybase'])
    count = len(nem.extensions)
    for item in range(count):
        print nem.extensions[0].plugin().scheduler(dt)
    nem_multiple = NamedExtensionManager(namespace='sora.scheduler', names=['memorybase', 'randombase'])
    count = len(nem_multiple.extensions)
    for item in range(count):
        print nem_multiple.extensions[item].plugin().scheduler(dt)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'name',
        nargs='?',
        default='test_manual',
        help='指定要执行的函数名称'
    ) 
    parsed_args = parser.parse_args()
    globals()[parsed_args.name]() 
