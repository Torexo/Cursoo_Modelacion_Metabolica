"""
Created on Fri Nov 9 15:22:57 2018

@author: patri
"""
import cobra
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
#esta linea debe estar incluida para poder graficar en 3d, aunque no se utilize
from mpl_toolkits.mplot3d import Axes3D

def main():
    #Importamos el modelo
    model=cobra.io.read_sbml_model("iMM1415.xml")
    
    #Bounds de Oxigeno
    model.reactions.get_by_id('EX_o2_e').upper_bound=0
    model.reactions.get_by_id('EX_o2_e').lower_bound=-50
    
    #Bounds de Glucosa
    model.reactions.get_by_id('EX_glc__D_e').upper_bound=0
    model.reactions.get_by_id('EX_glc__D_e').lower_bound=-10
    
    #Guardamos la reaccion objetivo para generar el plano de fase
    obj=[model.reactions.get_by_id('BIOMASS_mm_1_no_glygln')]
    
    #generamos los datos del plano de fase
    phase=cobra.flux_analysis.phenotype_phase_plane.production_envelope(model,['EX_o2_e','EX_glc__D_e'],objective=obj)
    
    #guardamos los vectores del archivo pandas en un array
    o2=phase.iloc[:,7]
    glc=phase.iloc[:,8]
    
    #Transformar columna de biomasa en matriz
    x=phase.iloc[:,3]
    x1=np.matrix(x.tolist())
    M=np.reshape(x1,[20,20])
    
    #Extraer los datos de flux de Oxigeno
    a=np.zeros(20)
    for i in range(20):
        a[i]=o2[20*i]
    
    #Extraer los datos de flux de Glucosa
    b=np.zeros(20)
    for i in range(20):
        b[i]=glc[i]
    
    #Generar Planos de Fase, graficando en 3d
    fig=plt.figure()
    ax=fig.gca(projection="3d")
    surf=ax.plot_surface(a,b, M, cmap=cm.coolwarm,linewidth=0)
    fig.colorbar(surf, shrink=0.5, aspect=4)
    plt.xlabel('Oxigeno')
    plt.ylabel('Glucosa')
    plt.savefig('Plano de Fase1.png')
    plt.show()

if __name__=='__main__':
    main()