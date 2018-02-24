#mark empty cell as np.nan then can use dropna
selected_dropna=selected_zip.replace({'Latitude':{'':np.nan},'Latitude':{'':np.nan}}).dropna()
