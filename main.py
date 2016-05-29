# -*- coding: utf-8 -*-
import parse_txt
import convert_df
import matplotlib.pyplot as plt
import matplotlib
import random

plt.style.use('ggplot') 
font = {'family' : 'meiryo'}
matplotlib.rc('font', **font)

def generate_random_color():
    return "#{0:X}{1:X}{2:X}".format(*[random.randint(0,255) for _ in range(3)])

if __name__ == '__main__':
    fname = "./sram_snmV1.txt"
    header = parse_txt.get_header(fname)
    datalist = parse_txt.get_parsedata(fname) 
    parse_txt.convert_float(datalist)
    list_df = convert_df.convert_df(header, datalist)
    
    colorlist = []

    for num in range(len(list_df)):
        colorlist.append(generate_random_color())

    for df,color in zip(list_df, colorlist):
        # df.plot(x=["V(n002)"], y=["V(n003)"])
        print(color)
        df_inv = df.copy()
        df_inv.index = df["V(n003)"]
        df_inv["V2"] = df.index
        df["V(n003)"].plot()
        df_inv["V2"].plot()

    plt.title("Static Noise Margin", size=16)
    plt.xlabel("V1 [V]")
    plt.ylabel("V2 [V]")
    # plt.show()
    plt.savefig("snm.png")
