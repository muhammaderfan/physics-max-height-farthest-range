import math

def jarak (v, theta):
	sudut_radian = math.radians(theta)
	t = (2 * v * math.sin(sudut_radian)) / 9.8
	v_x = v * math.cos(sudut_radian)
	return  v_x * t