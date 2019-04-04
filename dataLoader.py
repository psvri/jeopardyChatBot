import numpy as np
import pandas as pd

data = pd.read_csv('JEOPARDY_CSV.csv')

qa = data.iloc[:,-2:].values

ids_toremove = []
for x in range(len(qa)):
    if 'href' in qa[x][0]:
        ids_toremove.append(x)
#print(ids_toremove)
qa = np.delete(qa,ids_toremove,axis=0)

#print(len(qa))

np.save('clean_data',qa)
