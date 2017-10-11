from cx_Freeze import setup,Executable

includefiles = ['Atoms.csv','userinput.py']
includes = []
excludes = []
packages = ['numpy','pandas']

setup(
	name = 'Molar mass',
	version = '1.0',
	description = 'A calculator for the molar mass',
	author = 'Simon Moe Sørensen',
	options = {'build_exe': {'includes':includes,'excludes':excludes,'packages':packages,'include_files':includefiles}}, 
	executables = [Executable('Molarmass.py')]
)