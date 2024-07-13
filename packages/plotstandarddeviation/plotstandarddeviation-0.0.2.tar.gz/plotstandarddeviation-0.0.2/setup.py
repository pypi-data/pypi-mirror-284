from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Science/Research',
  'Operating System :: Microsoft :: Windows :: Windows 11',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3',
  'Natural Language :: English'
]
 
setup(
  name='plotstandarddeviation',
  version='0.0.2',
  description="Calculates all standard deviations from the mean within a dataset's range.",
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Alexander Levon Schulze',
  author_email='alexanderlevonschulze@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords=['standard_deviation','calculator'],
  packages=find_packages(),
  install_requires=['numpy', 'pandas'] 
)
