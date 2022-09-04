import yfinance as yf
tiktok = "ABB.ST ALFA.ST ALIV-SDB.ST ASSA-B.ST ATCO-A.ST ATCO-B.ST AZN.ST BOL.ST ELUX-B.ST ERIC-B.ST ESSITY-B.ST EVO.ST GETI-B.ST HEXA-B.ST HM-B.ST INVE-B.ST KINV-B.ST NDA-SE.ST SAND.ST SCA-B.ST SEB-A.ST SHB-A.ST SINCH.ST SKA-B.ST SKF-B.ST SWED-A.ST SWMA.ST TEL2-B.ST TELIA.ST VOLV-B.ST"

jul4open = yf.download(tiktok, start="2022-07-04", end ="2022-07-05")["Open"]
randomjul4 = [randomin4jul[i]*jul4open.values for i in range(0, len(seed))]
mejul4 = jul4open*mein4jul

aug8open = yf.download(tiktok, start="2022-08-08", end ="2022-08-09")["Open"]
randomaug8 = [randomin8aug[i]*aug8open.values for i in range(0, len(seed))]
meaug8 = aug8open*mein8aug
