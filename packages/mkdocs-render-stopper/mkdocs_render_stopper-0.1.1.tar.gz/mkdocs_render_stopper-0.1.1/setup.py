from setuptools import setup, find_packages
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setup(
    name='mkdocs-render-stopper',
    version='0.1.1',
    author='Jean-François Cartier',
    author_email='jfcartier@cmontmorency.qc.ca',
    url='https://github.com/jfcmontmorency/mkdocs-render-stopper',
    description='A MkDocs plugin to stop rendering at a specific tag.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'mkdocs>=1.4.2', 
        'lxml>=4.7.0'
    ],
    include_package_data=True,
    python_requires='>=3.6',
    entry_points={
        'mkdocs.plugins': [
            'render-stopper = mkdocs_render_stopper.plugin:RenderStopperPlugin',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Framework :: MkDocs',
    ],
)