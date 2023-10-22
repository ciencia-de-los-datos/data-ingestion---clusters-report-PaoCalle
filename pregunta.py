"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd


def ingest_data():

    #
    # Inserte su código aquí
    #
    data=[]
    i=0
    current_line=0
    with open('clusters_report.txt',mode='r') as file:
        for line in file:
            
            element=line.replace('.','').strip().split('  ')
            element=line.replace('.','').strip().replace('-','').split('  ') if i==3 else element
            if i==0:
                current_line=i
                line_elements=[x for x in element if x!='' and len(x)>0]
                new_line=[line_elements[0],line_elements[1],line_elements[2],line_elements[3]]
                if len(new_line)>0:
                    data.append(new_line)
            
            elif i==1:
                line_elements=[]
                line_elements=[x for x in element if x!='' and len(x)>0]
                data[current_line][1]=data[current_line][1]+' '+(line_elements[0])
                data[current_line][2]=data[current_line][2]+' '+(line_elements[1])

            elif len(element[0])==1 or len(element[0])==2:
                current_line=current_line+1
                line_elements=[]
                line_elements=[x for x in element if x!='' and len(x)>0]
                new_line=[line_elements[0],line_elements[1],line_elements[2],' '.join(line_elements[3:])]
                if len(new_line)>0:
                    data.append(new_line)
          
            elif len(element[0])>2 and i>1:
                for val in element:
                    data[current_line][3]=data[current_line][3]+' '+val.strip()
 
            i=i+1

    df=pd.DataFrame(data[1:],columns=data[0])
    cols=df.columns.to_list()
    new_cols=[c.strip().replace(' ','_').lower() for c in cols]
    df.columns=new_cols
    for col in df.columns:
        df[col]=df[col].str.strip()

    df.cluster=df.cluster.astype(int)
    df.cantidad_de_palabras_clave=df.cantidad_de_palabras_clave.astype(int)
    df.porcentaje_de_palabras_clave=df.porcentaje_de_palabras_clave.str.replace('%','').str.replace(',','.').astype(float)
    df.principales_palabras_clave=df.principales_palabras_clave.str.replace('  ',' ')

    return df