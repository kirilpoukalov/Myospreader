import os
import pandas as pd 
import numpy as np
inputdir='D:\\Science\\images\\stellarvision_processing\\output\\A871'
outputdir='D:\\Science\\images\\stellarvision_processing\\data\\A871'
inputfiles=os.listdir(inputdir)
Cy5Data=[]
DistanceData=[]
for x in inputfiles:
    famfile=x
    if famfile.startswith("FAM"):
        if famfile.endswith("nuclei.txt"):
            df = pd.read_csv(inputdir+ "\\" + famfile) 
            FAMnuclei= df.query("400<pixel_count<1500")['max']
            FAMnuclei=FAMnuclei.to_frame()
            NucleiID=list(FAMnuclei.index.values)
            cutoff= FAMnuclei['max'].mean() + 3*FAMnuclei['max'].std()
            Cas9Nuclei=FAMnuclei[(FAMnuclei["max"]>=cutoff)]
            Cas9NucleiID= list(Cas9Nuclei.index.values)
            Cas9NucleiID=list(map(str, Cas9NucleiID))
            for x in inputfiles:
                Cy5file=x
                if Cy5file.startswith("Cy5"):
                    if Cy5file.endswith(famfile[-24:]):
                        df = pd.read_csv(inputdir+ "\\" + Cy5file) 
                        Cy5nuclei= df.query('index in @NucleiID')
                        for x in inputfiles:
                            famdistancefile=x
                            if famdistancefile.startswith(famfile[0:23]):
                                if famdistancefile.endswith("Distances.txt"):
                                    df = pd.read_csv(inputdir+ "\\" + famdistancefile) 
                                    Famdistances= df.query('index in @NucleiID')
                                    DistancesfromCas9 = Famdistances.filter(Cas9NucleiID)
                                    if not DistancesfromCas9.empty:
                                        for column in DistancesfromCas9:
                                            Cy5nucleilist=list(Cy5nuclei["mean"])
                                            Cy5Data=Cy5Data+Cy5nucleilist
                                            DistancesfromCas9list=list(DistancesfromCas9[column])
                                            DistanceData=DistanceData+DistancesfromCas9list

data=pd.DataFrame(data=zip(Cy5Data,DistanceData),columns=['cy5data','disatnce'])
data.to_csv(outputdir+"\\"+"A871Data.txt")

