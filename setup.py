from setuptools import setup

setup(
	name = 'pyflakes-ext',
	version = '1.0.4',
	author = 'Quantlane',
	author_email = 'code@quantlane.com',
	packages = ['pyflakes_ext',],
	url = 'https://github.com/qntln/pyflakes-ext',
	license = 'MIT',
	description = 'A few extra additions to pyflakes.',
	install_requires = [
		'pyflakes>=1.2.3,<2.0.0',
	],
	entry_points = {
		'console_scripts': [
			'pyflakes-ext = pyflakes_ext.pyflakes_ext:main',
		]
	}
)
