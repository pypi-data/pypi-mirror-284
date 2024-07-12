from setuptools import setup, find_packages

setup(
    name='whoisbuild',
    version='1.0.2',
    packages=find_packages(),
    install_requires=['discord.py'],
    author='Taylor Kalos',
    author_email='talosfk@example.com',
    description='A module to facilitate the creation of Embeds Discord',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/votrecompte/discord_embed_helper',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
