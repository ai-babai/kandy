from setuptools import setup, find_packages

setup(
    name='kandy',
    version='0.2.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'requests',
        'Pillow',
    ],
    author='Maksim Popkov',
    author_email='maxim.popkov.91@gmail.com',
    description='Пакет для работы с API Kandinsky для генерации изображений',
    keywords='api image generation kandinsky',
)
