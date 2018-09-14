import argparse
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
import sys
from scipy.optimize import leastsq

def getParser():
	parser=argparse.ArgumentParser(description='Descripcion de la funcion de este programa.')
	parser.add_argument('-o',type=str,dest='formato',help="'png' si la imagen es guardada en formato .PNG, o 'pdf' para ser guardada en formato .PDF")
	parser.add_argument('-a',type=float,dest='params',help="Define los parametros iniciales para la regresion")
	if len(sys.argv)==1:
		print >> sys.stderr,parser.print_help()
		exit(0)
	return parser


def main():
	args=getParser().parse_args()
	formato=args.formato
	params=args.params

	#1
	alfa=4.3
	t=np.linspace(0,4*np.pi,200)
	funcion=alfa*np.sin(t)
	#2
	noise=np.random.normal(0,0.2,200)
	y=funcion+noise
	#3
	def res(alfa,x,y):
	    sim=alfa*np.sin(x)
	    return y-sim
	
	out=leastsq(res,params,args=(t,y))
	print out
	#4
	fit=out[0][0]*np.sin(t)
	plt.plot(t,y,'ro')
	plt.plot(t,fit)
	
	if formato=="png":
		plt.savefig("ajuste.png")
	elif formato=="pdf":
		plt.savefig("ajuste.pdf")

if __name__=="__main__":
	main()
