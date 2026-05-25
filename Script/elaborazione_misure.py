import csv
import numpy as np
path = "Dati/misure_laboratorio.csv"


with open(path, mode='r', encoding='utf-8') as f:
    reader = csv.reader(f)
    
    # 1. Saltiamo e salviamo l'intestazione
    header = next(reader)
    
    # Se vuoi saltare la prima colonna (Misurazione) anche nell'header:
    labels = header[1:]
    
    # Creiamo una struttura per i dati (es. una lista di liste per ogni colonna)
    # Inizializziamo una lista vuota per ogni colonna di interesse
    colonne_dati = [[] for _ in labels]

    # 2. Iteriamo sulle righe dei dati
    for riga in reader:
        # riga[0] è l'indice (1, 2, 3...), lo ignoriamo
        # riga[1:] sono i valori delle misure
        misure = riga[1:]
        
        for i, valore in enumerate(misure):
            colonne_dati[i].append(float(valore))

tau_medi = []
varianze = []
# 3. Ora puoi iterare sui tuoi set di misure per i calcoli
for i, nome_set in enumerate(labels):
    dati = colonne_dati[i]
    tau_medio = np.mean(dati)
    tau_medi.append(round(float(tau_medio), 3))

    varianza = np.var(dati,ddof=1)
    varianze.append(varianza)

varianza_media = []
for varianza in varianze:
    varianza_media.append(varianza/10)

errore_tau = []
for i in varianza_media:
    errore_tau.append(round(float(np.sqrt(i)),3))

masse = [25.07, 30.4, 40.1, 50.13, 70.09, 20.1]

for i,k in zip(tau_medi,errore_tau):
    print(f"{i/5} +- {np.round(k/5, 3)}")

#print(len(tau_medi), len(errore_tau))
"""
print(tau_medi)
print(varianze)
print(varianza_media)
print(errore_tau)
"""