import pandas, sys
import numpy as np
import pandas as pd

# df1 = pd.read_csv("DB_OSSERVATORIO_1980_1984.csv")
# df2 = pd.read_csv("DB_OSSERVATORIO_1985_1989.csv")
#
# df1 = df1.append(df2)
# print(df1.head(), df1.tail())
#
# df1.to_csv("test.csv", index=False)


# df = pd.read_csv("test.csv")
#
# for i in range(1, 26306):
#     df.drop(df.index[i])
#
# df.to_csv("test2.csv", index=False)
#

# df = pd.read_csv("DB_OSSERVATORIO_1985_1989.csv").append(pd.read_csv("DB_OSSERVATORIO_1990_1994.csv").append(pd.read_csv("DB_OSSERVATORIO_1995_1999.csv").append(pd.read_csv("DB_OSSERVATORIO_2000_2004.csv"))))

# df.to_csv("test4.csv", index=False)


attributes = ["Date","H","Pressure","Temperature","WindDir","WindSpeed","Humidity","Precipitation","Insolation"]
df = pd.read_csv("test3_dataset.csv")

# Source Wiki - Levels cm and percentage of area submerged
levels = [90, 1.84, 100,	5.17,110,	14.04, 120 ,28.75, 130 ,43.15, 140 ,54.39, 150,62.98 ,160 ,69.43,170 ,74.20,180 ,78.11,190 ,82.39,200 ,86.4]

flood_levels = range(80, 200)

flood_levels_high = (140, 200)

dflist = df.values.tolist()

"""
Prominent Dates of Floods in Venice

194 cm on November 4, 1966
187 cm on November 12, 2019
166 cm on December 22, 1979
158 cm on February 1, 1986
156 cm on October 29, 2018
156 cm on December 1, 2008
154 cm on November 15, 2019
152 cm on November 17, 2019
151 cm on November 12, 1951
150 cm on November 18, 2019
149 cm on November 11, 2012
147 cm on April 16, 1936
147 cm on November 16, 2002
145 cm on December 25, 2009
145 cm on October 15, 1960
144 cm on November 13, 2019
144 cm on December 23, 2009
144 cm on November 3, 1968
144 cm on November 6, 2000
143 cm on February 12, 2013
143 cm on November 1, 2012
142 cm on December 8, 1992
140 cm on February 17, 1979

"""



print(type(dflist[0][7]))



for i in range(0, len(dflist)):
    temp = dflist[i]
    # remove all the blank values in precipitation and insolation, replace to 0
    if np.isnan(temp[7]):
        dflist[i][7] = 0
    if np.isnan(temp[8]):
        dflist[i][8] = 0

# print(dflist[0][7])

df2 = pd.read_csv("venezia.csv")

df2list = df2.values.tolist()


for i in range(0, len(df2list)):
    temp = df2list[i][1]

    if temp >= 30  and temp <= 60:
        df2list[i].append("High Tide")
        df2list[i].append(1)

    elif temp > 60 and temp < 90:
        df2list[i].append("Warning")
        df2list.append(2)

    elif temp < -15:
        df2list[i].append("Low Tide")
        df2list.append(3)

    elif temp >= 90:
        df2list[i].append("Flood")
        df2list[i].append(4)

    else:
        df2list[i].append("Normal")
        df2list[i].append(0)

labels = ["Normal", "High Tide", "Warning", "Low Tide", "Flood"]





