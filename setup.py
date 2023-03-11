from setuptools import setup, find_namespace_packages

setup(
    name='rofi-notion',
    version='1.2.0',
    description='Quickly create new Notion pages for your databases with rofi as GUI',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/mathix420/rofi-notion',
    author='Arnaud Gissinger',
    author_email='agissing@student.42.fr',
    license='MIT',
    keywords=[
        'notion.so',
        'notion',
        'rofi',
        'dmenu',
        'x11',
        'i3',
    ],
    python_requires='>=3.7',
    classifiers=[
                'Intended Audience :: Developers',
                'Intended Audience :: End Users/Desktop',

                'Topic :: Utilities',
                'Topic :: Text Processing',
                'Topic :: Text Processing :: Markup :: Markdown',
                'Topic :: Office/Business',
                'Topic :: Office/Business :: Financial :: Spreadsheet',
                'Topic :: Office/Business :: Financial :: Spreadsheet',

                'License :: OSI Approved :: MIT License',

                'Operating System :: POSIX :: Linux',

                'Programming Language :: Python :: 3 :: Only',
                'Programming Language :: Python :: 3.7',
                'Programming Language :: Python :: 3.8',
                'Programming Language :: Python :: 3.9',
                'Programming Language :: Python :: 3.10',
                'Programming Language :: Python :: 3.11',
                'Programming Language :: Python :: 3.12',
    ],
    install_requires=[
        'notion-client==1.0.0',
        'python-rofi==1.0.1',
        'PyInquirer==1.0.3',
        'argparse==1.4.0',
        'PyYAML==6.0',
    ],
    packages=find_namespace_packages(include=["rofi_notion", "rofi_notion.*"]),
    entry_points={'console_scripts': ['rofi-notion=rofi_notion.__main__:main']},
)
