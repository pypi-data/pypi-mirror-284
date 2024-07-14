from setuptools import setup, find_packages

setup(
    name='django-cron-command',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django>=3.0',
    ],
    entry_points={
        'console_scripts': [
            # Define any command line scripts here if needed
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Framework :: Django',
    ],
    python_requires='>=3.6',
    description='A Django app to manage cron jobs.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Faruk-Hossain-1101/django-cron-command',
    author='Faruk Hossain',
    author_email='hossainf114@gmail.com',
    license='MIT',
)
