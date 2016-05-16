from setuptools import setup

setup(
	name = 'pyflakes-ext',
	version = '1.0.0',
	author = 'Vita Smid',
	author_email = 'me@ze.phyr.us',
	packages = ['pyflakes_ext',],
	url = 'https://github.com/ze-phyr-us/pyflakes-ext',
	license = 'MIT',
	description = 'A few extra additions to pyflakes.',
	install_requires = [
		'pyflakes',
	],
	entry_points = {
		'console_scripts': [
			'pyflakes-ext = pyflakes_ext.pyflakes_ext:main',
		]
	}
)
