# -*- coding: utf-8 -*-
import parse_txt
import convert_df

if __name__ == '__main__':
    fname = "./sram_snmV1.txt"
    header = parse_txt.get_header(fname)
    datalist = parse_txt.get_parsedata(fname) 
    print(parse_txt.convert_float(datalist))
    convert_df.convert_df(header, datalist)
