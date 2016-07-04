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
 
def test_auto():
    from stevedore import driver
    dt = {13:'id1',324:'id2',434:'id3','memory':[13,324,434]}
    mgr = driver.DriverManager(
          namespace='sora.scheduler',
          name='randombase',
          invoke_on_load=True,         #设置为true，即载入后自动实例化插件类，如果是函数，则调用
    )
    for item in range(5):
        print 'test_auto: %s' % mgr.driver.scheduler(dt)

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
