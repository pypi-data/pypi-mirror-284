import numpy as np


def function_0():
	print('pypilib: print from function_0()')


def function_uses_numpy():
	print(f'numpy ver: {np.__version__}')
	a = np.sum(np.arange(4))
	print(f'pypilib: print from function_uses_numpy(): {a}')
