'''def UsingDataFrame():
    import pandas as pd
    df = pd.read_csv("hpc.csv", index_col=False, low_memory=False, delimiter=';')
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
    df5dot3 = pd.concat(((df5dot2[:middle])[::3], (df5dot2[middle:])[::4]), axis=0)
    print ("Starting dataframe, where time is more than 18:00:00 and power consumption per minute is more than 6 kW(DataFrame5):")
    print df5[:5]
    print ("Samples from DataFrame5, where sub_metering_2 is more than sub_metering_1 and sub_metering_3:")
    print df5dot2[:5]
    print ("Samples from DataFrame5 (every third from first half of DataFrame5 and every fourth from second half of DataFrame5):")
    print df5dot3[:5]


def UsingNumpyArray():
    names=['Date', 'Time', 'Global_active_power', 'Global_reactive_power', 'Voltage', 'Global_intensity', 'Sub_metering_1', 'Sub_metering_2', 'Sub_metering_3']
    from numpy import genfromtxt
    import numpy as np
    import random
    data = genfromtxt("hpc.csv", delimiter=";", dtype=None)
    data = data[data[:, 2] != '?']
    print ("Starting array:")
    print data[:5]

    data1 = data[data[:, 2] > "5"]
    print ("Samples from starting array, where Global_active_power > 5 kW:")
    print data1[:5]

    data2 = data[data[:, 4] > "235"]
    print ("Samples from starting array, where Voltage > 235 V:")
    print data2[:5]

    data3 = data[(data[:, 5] > "19") & (data[:, 5] < "20")]
    data3dot2 = data3[(data3[:, 7] > data3[:, 8])]
    print ("Samples from starting array, where Global_intensity is in range(19, 20) A (call it Array3):")
    print data3[:5]
    print ("Samples from Array3, where Sub_metering_2 > Sub_metering_3:")
    print data3dot2[:5]

    data4 = np.array(random.sample(data, 50))
    print ("500 000 random samples from starting array (Array4):")
    print data4[:5]
    avgOne = np.mean(data4[1:, 6].astype(np.float64))
    avgTwo = np.mean(data4[1:, 7].astype(np.float64))
    avgThree = np.mean(data4[1:, 8].astype(np.float64))
    print ("Average of all sub_metering_1 values from Array4:")
    print avgOne
    print ("Average of all sub_metering_2 values from Array4:")
    print avgTwo
    print ("Average of all sub_metering_3 values from Array4:")
    print avgThree

    data5 = data[data[1:, 1] > "18:00:00"]
    data5 = data5[data5[:, 2].astype(np.float64) + data5[:, 3].astype(np.float64) > np.float64('6')]
    data5dot2 = data5[data5[:, 7].astype(np.float64) > data5[:, 6].astype(np.float64) + data5[:, 8].astype(np.float64)]
    print data5dot2[:5]
    print len(data5dot2)
    middle = int(len(data5dot2) / 2)
    data5dot3 = np.concatenate(((data5dot2[:middle])[::3], (data5dot2[middle:])[::4]), axis=0)
    print ("Result:")
    print data5dot3[:5]'''


def UsingDataFrame():
    import pandas as pd
    df = pd.read_csv("hpc.csv", index_col=False, low_memory=False, delimiter=';')
    df = df[df['Global_active_power'] != '?']
    df = df.convert_objects(convert_numeric=True)

    df1 = df[df['Global_active_power'] > 5.0]

    df2 = df[df['Voltage'] > 235]

    df3 = df[(df['Global_intensity'] >= 19) & (df['Global_intensity'] <= 20)]
    df3dot2 = df3[df3['Sub_metering_2'] > df3['Sub_metering_3']]

    df4 = df.sample(500000)
    avgOneForDF4  = sum(df4['Sub_metering_1']) / 500000
    avgTwoForDF4  = sum(df4['Sub_metering_2']) / 500000
    avgThreeForDF4 = sum(df4['Sub_metering_3']) / 500000

    df5 = df[(df['Time'] > "18:00:00") & ((df['Global_active_power'] + df['Global_reactive_power']) >= 6)]
    df5dot2 = df5[(df5['Sub_metering_2'] > df5['Sub_metering_1']) & (df5['Sub_metering_2'] > df5['Sub_metering_3'])]
    middle = int(len(df5dot2) / 2)
    df5dot3 = pd.concat(((df5dot2[:middle])[::3], (df5dot2[middle:])[::4]), axis=0)


def UsingNumpyArray():
    names=['Date', 'Time', 'Global_active_power', 'Global_reactive_power', 'Voltage', 'Global_intensity', 'Sub_metering_1', 'Sub_metering_2', 'Sub_metering_3']
    from numpy import genfromtxt
    import numpy as np
    import random
    data = genfromtxt("hpc.csv", delimiter=";", dtype=None)
    data = data[data[:, 2] != '?']

    data1 = data[data[:, 2] > "5"]

    data2 = data[data[:, 4] > "235"]

    data3 = data[(data[:, 5] > "19") & (data[:, 5] < "20")]
    data3dot2 = data3[(data3[:, 7] > data3[:, 8])]

    data4 = np.array(random.sample(data, 50))
    avgOne = np.mean(data4[1:, 6].astype(np.float64))
    avgTwo = np.mean(data4[1:, 7].astype(np.float64))
    avgThree = np.mean(data4[1:, 8].astype(np.float64))

    data5 = data[data[1:, 1] > "18:00:00"]
    data5 = data5[data5[:, 2].astype(np.float64) + data5[:, 3].astype(np.float64) > np.float64('6')]
    data5dot2 = data5[data5[:, 7].astype(np.float64) > data5[:, 6].astype(np.float64) + data5[:, 8].astype(np.float64)]
    middle = int(len(data5dot2) / 2)
    data5dot3 = np.concatenate(((data5dot2[:middle])[::3], (data5dot2[middle:])[::4]), axis=0)

if __name__ == "__main__":
    import timeit
    print ("Time(array) = %s" % str(timeit.timeit("UsingNumpyArray()", number=5, setup="from __main__ import UsingNumpyArray") / 5))
    print ("Time(dataframe) = %s" % str(timeit.timeit("UsingDataFrame()", number=5, setup="from __main__ import UsingDataFrame") / 5))
