import setuptools

setuptools.setup(
	name="Paolog_Pynecraft",
	version="0.1.1-1",
	include_package_data=True,
	package_data={"": ["*.*", "**/*.*"]},
	author="Paolog",
	description="A Minecraft recreation made with Ursina",
	packages=["Paolog_Pynecraft", "Paolog_Pynecraft.src.Games"],
	install_requires=['ursina', 'appdata', 'perlin_noise', 'screeninfo']
)