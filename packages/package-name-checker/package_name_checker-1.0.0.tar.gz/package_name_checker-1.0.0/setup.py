from setuptools import setup, find_packages

# Load the README file
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='package_name_checker',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask',
        'requests',
        'beautifulsoup4',
    ],
    entry_points={
        'console_scripts': [
            'package_name_checker_start = package_name_checker.app:app.run',
        ],
    },
    author='Md. Shishir Ahmed',
    author_email='mdshishirahmed811@gmail.com',
    description='A Flask application to check app details from Google Play Store based on package names.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    keywords='flask google-play-store scraper',
    url='https://github.com/shishir1337/playstore_app_package_name_checker_package',
)
