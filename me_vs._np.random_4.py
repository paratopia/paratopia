daily1 =  yf.download(tiktok, start="2022-07-04", end ="2022-09-03")["Adj Close"].values
daily1 = ((daily1[1:,]/daily1[:-1])-1)

randomw1 = [randomjul4[i]/randomjul4[i].sum() for i in range(0, len(seed))]
randomret1 = [daily1*randomw1[i] for i in range(0, len(seed))]
mew1 = mejul4.values/mejul4.values.sum()
meret1 = daily1*mew1

daily2 = yf.download(tiktok, start="2022-08-08", end ="2022-09-03")["Adj Close"].values
daily2 = ((daily2[1:,]/daily2[:-1])-1)
zero = np.zeros((len(daily1)-len(daily2), len(daily1.T)))
daily2 = np.vstack([zero, daily2])

randomw2 = [randomaug8[i]/randomaug8[i].sum() for i in range(0, len(seed))]
randomret2 = [daily2*randomw2[i] for i in range(0, len(seed))]
mew2 = meaug8.values/meaug8.values.sum()
meret2 = daily2*mew2

randomret = np.array([np.sum([randomret1[i]+randomret2[i] for i in range(0, len(seed))][i], axis=1) for i in range(0, len(seed))]).T
meret = np.sum(meret1+meret2, axis=1)
