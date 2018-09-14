import argparse
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
import sys
from scipy.optimize import leastsq

def getParser():
    parser=argparse.ArgumentParser(description='Descripcion de la funcion de este programa.')
    parser.add_argument('-o',type=str,dest='formato',help="'png' si la imagen es guardada en formato .PNG, o 'pdf' para ser guardada en formato .PDF")
    parser.add_argument('-a',type=float,dest='a',help="Define el parametro inicial para la pendiente")
    parser.add_argument('-b',type=float,dest='b',help='Define el parametro inicial para el intercepto')
    if len(sys.argv)==1:
        print >> sys.stderr,parser.print_help()
        exit(0)
    return parser


def main():
	args=getParser().parse_args()
	formato=args.formato
	params=[args.a,args.b]

	#1
	m=2
	b=0.5
	t=np.linspace(0,10,200)
	funcion=m*t+b
	#2
	noise=np.random.normal(0,0.2,200)
	y=funcion+noise
	#3
	def res(params,x,y):
		m=params[0]
		b=params[1]
		sim=m*x+b
		return y-sim

	out=leastsq(res,params,args=(t,y))
	print out
	#4
	fit=out[0][0]*t+out[0][1]
	plt.plot(t,y,'ro')
	plt.plot(t,fit)
	
	if formato=="png":
		plt.savefig("ajuste.png")
	elif formato=="pdf":
		plt.savefig("ajuste.pdf")

if __name__=="__main__":
	main()
