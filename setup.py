from setuptools import setup, find_packages
setup(
    name='sora-scheduler',
    version='1.0',
    description='sora.scheduler',
    author='MaBing',
    author_email='cumt_ttr@163.com',
    platforms=['Any'],
    scripts=[],
   # provides=['sora.scheduler',
   #           ],
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'sora.scheduler': [
            'memorybase = scheduler.memory:memoryscheduler',
            'randombase = scheduler.simple:simplescheduler',
        ],
    },
    zip_safe=False,
)
