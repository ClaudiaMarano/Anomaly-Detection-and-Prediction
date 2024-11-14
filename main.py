import pandas as pd

# Imposta l'opzione per una larghezza di visualizzazione elevata
pd.set_option('display.max_columns', None)  # Mostra tutte le colonne
pd.set_option('display.width', 1000)

"""
# Caricamento dei file del dataset fisico
file_path1 = '.\Src\dataset\Physical dataset\phy_att_1.csv'
file_path2 = '.\Src\dataset\Physical dataset\phy_att_2.csv'
file_path3 = '.\Src\dataset\Physical dataset\phy_att_3.csv'
file_path4 = '.\Src\dataset\Physical dataset\phy_att_4.csv'
file_path5 = '.\Src\dataset\Physical dataset\phy_norm.csv'

# Leggi i file CSV specificando una diversa codifica
phy_att_1 = pd.read_csv(file_path1, sep='\t', encoding='utf-16')
phy_att_2 = pd.read_csv(file_path2, sep='\t', encoding='utf-16')
phy_att_3 = pd.read_csv(file_path3, sep='\t', encoding='utf-16')
phy_att_4= pd.read_csv(file_path4, sep=',', encoding='utf-8-sig') # Utilizzo la virgola come delimitatore
phy_norm = pd.read_csv(file_path5, sep='\t', encoding='utf-16')
"""

# Caricamento dei file del dataset di rete
#file_path6 = '.\Src\dataset/Network datatset/csv/attack_1.csv'
#file_path7 = '.\Src\dataset/Network datatset/csv/attack_2.csv'
#file_path8 = '.\Src\dataset/Network datatset/csv/attack_3.csv'
#file_path9 = '.\Src\dataset/Network datatset/csv/attack_4.csv'
file_path10 = '.\Src\dataset/Network datatset/csv/normal.csv'

# Leggi i file CSV specificando una diversa codifica
#attack_1 = pd.read_csv(file_path6, sep=';',encoding='utf-8')
#attack_2 = pd.read_csv(file_path7, encoding='utf-8')
#attack_3 = pd.read_csv(file_path8, encoding='utf-8')
#attack_4= pd.read_csv(file_path9, encoding='utf-8')
normal = pd.read_csv(file_path10, encoding='utf-8')

# Visualizza il file
print(normal.head(100))

"""
## INFO FILE DATI FISICI

phy_att_1.csv:
[2420 rows x 43 columns]

phy_att_2.csv:
[2104 rows x 43 columns]

phy_att_3.csv:
[1254 rows x 43 columns]

phy_att_4.csv:
[1717 rows x 43 columns]

phy_norm.csv:
[3428 rows x 43 columns]

## INFO FILE DATI DI RETE

attack_1.csv:
[1048575 rows x 16 columns]

attack_2.csv:
[5159469 rows x 16 columns]

attack_3.csv:
[5862547 rows x 16 columns]

attack_4.csv:
[5522490 rows x 16 columns]

normal.csv:
[7757289 rows x 16 columns]

"""

