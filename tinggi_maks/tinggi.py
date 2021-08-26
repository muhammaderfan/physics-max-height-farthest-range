import math

def tinggi (v, theta):
	sudut_radian = math.radians(theta)
	return ((v * v) * ((math.sin(sudut_radian))**2)) / (2 * 9.8)