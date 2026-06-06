import numpy as np
import pandas as pd
import kagglehub as kgh
import os
import shutil
import matplotlib.pyplot as plt

dp_url = 'juhibhojani/house-price'

path = kgh.dataset_download(dp_url)
target_folder = './dataset'



if path:
    if not os.path.exists(target_folder):
        os.makedirs(target_folder, exist_ok=True)
        for file_name in os.listdir(path):
            source_file = os.path.join(path, file_name)
            target_file = os.path.join(target_folder, file_name)
            shutil.move(source_file, target_file)
            print(f"Moved {file_name} to {target_folder}")
    else:
        print(f"目標資料夾 {target_folder} 已存在！")
else:
    print("資料集下載失敗！")

train_set = pd.read_csv(os.path.join(target_folder, 'house_prices.csv'))
print(train_set.describe())

x_train = train_set.dropna(subset=['Amount(in rupees)', 
'Price (in rupees)', 'Carpet Area',]).to_numpy()

