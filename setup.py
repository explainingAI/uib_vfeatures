from setuptools import setup

setup(name='uib_vfeatures',
      version='0.1',
      description='Vision features of generalistic use',
      url='https://gitlab.com/miquelca32/features',
      author='UIB-UGIVIA',
      author_email=['miquelca32@gmail.com', 'bernat_galmes@hotmail.com', 'gabriel_moya@uib.es'],
      license='MIT',
      packages=['uib_vfeatures'],
      install_requires=[
          'scikit-image',
          'opencv-python',
          'matplotlib',
          'scipy',
          'scikit-image',
          'numpy'
      ],
      zip_safe=False)
