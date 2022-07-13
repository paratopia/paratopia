import yfinance as yf
import pandas as pd
tiktok = "HEXA-B.ST AZN.ST INVE-B.ST KINV-B.ST SKF-B.ST"
df = yf.download(tiktok, start="2000-07-01", end="2022-07-01", interval="1mo").dropna()
