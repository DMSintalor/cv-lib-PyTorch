from distutils.core import setup

setup(
    name='cv-lib',
    version='',
    packages=['cv_lib', 'cv_lib.flops', 'cv_lib.utils', 'cv_lib.logger', 'cv_lib.metrics',
              'cv_lib.metrics.precision_recall_meter', 'cv_lib.detection', 'cv_lib.detection.data',
              'cv_lib.detection.models', 'cv_lib.optimizers', 'cv_lib.schedulers', 'cv_lib.distributed',
              'cv_lib.augmentation', 'cv_lib.visualization', 'cv_lib.classification', 'cv_lib.classification.data',
              'cv_lib.classification.models'],
    url='',
    license='',
    author='zhfeing',
    author_email='',
    description=''
)
