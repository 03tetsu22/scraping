import csv
import pandas as pd
# import matplotlib.pyplot as plt

files = {
	'symphogear': 'symphogear.csv'
}

#csv読み込み
df = pd.read_csv(files['symphogear'])

# 響
hibiki = df[(df['名前'].str.contains('立花響')) & (df['初期レアリティ'] == '星5')]
hibiki_mean = hibiki.mean()
print('響のステータス')
print(hibiki_mean)
print(hibiki.shape)

#翼さん
tsubasa = df[(df['名前'].str.contains('風鳴翼')) & (df['初期レアリティ'] == '星5')]
tsubasa_mean = tsubasa.mean()
print(tsubasa_mean)
print(tsubasa.shape)

#クリス
chris = df[(df['名前'].str.contains('雪音クリス')) & (df['初期レアリティ'] == '星5')]
chris_mean = chris.mean()
print('クリスのステータス')
print(chris_mean)
print(chris.shape)

#マリア
maria = df[(df['名前'].str.contains('マリア')) & (df['初期レアリティ'] == '星5')]
maria_mean = maria.mean()
print('マリアのステータス')
print(maria_mean)
print(maria.shape)

#調
shirabe = df[(df['名前'].str.contains('月読調')) & (df['初期レアリティ'] == '星5')]
shirabe_mean = shirabe.mean()
print('調のステータス')
print(shirabe_mean)
print(shirabe.shape)

# 切歌
kirika = df[(df['名前'].str.contains('暁切歌')) & (df['初期レアリティ'] == '星5')]
kirika_mean = kirika.mean()
print('切歌のステータス')
print(kirika_mean)
print(kirika.shape)

# 奏
kanade = df[(df['名前'].str.contains('天羽奏')) & (df['初期レアリティ'] == '星5')]
kanade_mean = kanade.mean()
print('奏のステータス')
print(kanade_mean)
print(kanade.shape)

# 未来
miku = df[(df['名前'].str.contains('小日向未来')) & (df['初期レアリティ'] == '星5')]
miku_mean = miku.mean()
print('未来のステータス')
print(miku_mean)
print(miku.shape)

# # セレナ
selena = df[(df['名前'].str.contains('セレナ')) & (df['初期レアリティ'] == '星5')]
selena_mean = selena.mean()
print('セレナのステータス')
print(selena_mean)
print(selena.shape)

# 弦十郎
otona = df[df['名前'].str.contains('風鳴弦十郎')]
otona_mean = otona.mean()
print(otona_mean)

# フィーネ
fine = df[df['名前'].str.contains('フィーネ')]
fine_mean = fine.mean()
print(fine_mean)

# ウェル
au = df[df['名前'].str.contains('ウェル博士')]
au_mean = au.mean()
print(au_mean)

# サンジェルマン
san = df[df['名前'].str.contains('サンジェルマン')]
san_mean = san.mean()
print(san_mean)

# カリオストロ
kari = df[df['名前'].str.contains('カリオストロ')]
kari_mean = kari.mean()
print(kari_mean)

# プレラーティ
pre = df[df['名前'].str.contains('プレラーティ')]
pre_mean = pre.mean()
print(pre_mean)

# # 錬金術師

# # scores_std = scores.std(ddof=0)