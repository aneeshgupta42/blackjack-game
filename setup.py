from setuptools import setup

setup(name='blackjack-game',
	version='1.0',
	packages=['game'],
	install_requires=[	],
	package_dir={'':'gamemodules'},
	entry_points={
		'console_scripts': [
			'game = game.__main__:main',
		]
	},
)
