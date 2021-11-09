##
import matplotlib.pyplot as plt
import pandas as pd

# %%
# Posizione del file excel
xls_path = "aaa Manuali DEF.xlsx"

# Importiamo l'excel
df = pd.read_excel(xls_path)

# Rinominiamo le date
df.columns = ["date" if idx == 0 else col for idx, col in enumerate(df.columns)]

# mettiamo le date come indice delle righe
new_df = df.set_index("date")

# Eliminamo le colonne che non hanno un autore nel titolo
cols2remove = [col for col in new_df.columns if col.startswith("Unnamed")]

autori = new_df.drop(cols2remove, axis=1)

# Ora autori è la nostra tabella ripulita

# %% Stampiamo qualcosa


ax = autori.plot.line(legend=False)
plt.savefig("autori_line.png")

# %%
ax = autori.plot.bar(legend=False, stacked=True)
plt.savefig("autori_bar")
