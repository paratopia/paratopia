exr = np.array([np.mean(rdol), np.mean(rbet), np.mean(rmom), np.mean(rdolbet), np.mean(rdolmom), np.mean(rbetmom), np.mean(rdolbetmom)]) 
vol = np.array([np.std(rdol), np.std(rbet), np.std(rmom), np.std(rdolbet), np.std(rdolmom), np.std(rbetmom), np.std(rdolbetmom)])
sr=exr/vol

print(sr)
[0.36083449, 0.30437091, 0.31644866, 0.3558714, 0.34802971, 0.32559516, 0.35667169]
