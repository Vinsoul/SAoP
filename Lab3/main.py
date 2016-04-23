'''def main():
    import random
    import pandas as pd
    df = pd.read_csv("hpc.csv", index_col=False, low_memory=False)
    df = df[df['Global_active_power'] != '?']
    df = df.convert_objects(convert_numeric=True)
    print ("Starting DataFrame:")
    print df[:5]

    df1 = df[df['Global_active_power'] > 5.0]
    print ("Samples from starting dataframe, where global_active_power is more than 5 kW:")
    print df1[:5]

    df2 = df[df['Voltage'] > 235]
    print ("Samples from starting dataframe, where voltage is more than 235 V:")
    print df2[:5]

    df3 = df[(df['Global_intensity'] >= 19) & (df['Global_intensity'] <= 20)]
    df3dot2 = df3[df3['Sub_metering_2'] > df3['Sub_metering_3']]
    print ("Samples from starting dataframe, where global_intensity is in range 19-20 A (DataFrame3):")
    print df3[:5]
    print ("Samples from DataFrame3, where sub_metering_2 is more than sub_metering_3:")
    print df3dot2[:5]

    df4 = df.sample(500000)
    avgOneForDF4  = sum(df4['Sub_metering_1']) / 500000
    avgTwoForDF4  = sum(df4['Sub_metering_2']) / 500000
    avgThreeForDF4 = sum(df4['Sub_metering_3']) / 500000
    print ("500 000 random samples from starting dataframe (DataFrame4):")
    print df4[:5]
    print ("Average of all sub_metering_1 values from DataFrame4:")
    print avgOneForDF4
    print ("Average of all sub_metering_2 values from DataFrame4:")
    print avgTwoForDF4
    print ("Average of all sub_metering_3 values from DataFrame4:")
    print avgThreeForDF4

    df5 = df[(df['Time'] > "18:00:00") & ((df['Global_active_power'] + df['Global_reactive_power']) >= 6)]
    df5dot2 = df5[(df5['Sub_metering_2'] > df5['Sub_metering_1']) & (df5['Sub_metering_2'] > df5['Sub_metering_3'])]
    middle = int(len(df5dot2) / 2)
    df5dot3 = pd.DataFrame(columns=df.columns.values)
    for i in range(0, middle):
        if i % 3 == 0:
            df5dot3 = df5dot3.append(df5dot2[i:i+1])
    for i in range(middle, len(df5dot2)):
        if i % 4 == 0:
            df5dot3 = df5dot3.append(df5dot2[i:i+1])
    print ("Starting dataframe, where time is more than 18:00:00 and power consumption per minute is more than 6 kW(DataFrame5):")
    print df5[:5]
    print ("Samples from DataFrame5, where sub_metering_2 is more than sub_metering_1 and sub_metering_3:")
    print df5dot2[:5]
    print ("Samples from DataFrame5 (every third from first half of DataFrame5 and every fourth from second half of DataFrame5):")
    print df5dot3[:5]

if __name__ == '__main__':
    import timeit
    print ("Starting...")
    print ("Time = %s" % str(timeit.timeit("main()", number=3, setup="from __main__ import main") / 3))'''

def UsingNumpyArray():
    converters = {
        0: 'str'
    }
    names=['Date', 'Time', 'Global_active_power', 'Global_reactive_power', 'Voltage', 'Global_intensity', 'Sub_metering_1', 'Sub_metering_2', 'Sub_metering_3']
    from numpy import genfromtxt
    import numpy as np
    data = genfromtxt("hpc.csv", delimiter=",", names=names, dtype=None)
    data = data[data['Global_active_power'] != '?']
    print np.shape(data)
    print data[:5]

'''if __name__ == "__main__":
    import timeit
    print (timeit.timeit("UsingNumpyArra()", number=1, setup="from __ main__ import UsingNumpyArray"))'''

UsingNumpyArray()