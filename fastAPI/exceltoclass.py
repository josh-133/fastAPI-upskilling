import pandas

from structures import *

def build_ETypes(df):
    entries = df['PType'].tolist()
    ptypes = []
    for e in entries:
        for _e in e.split(','):
            ptypes.append(PType(_e))
    return


def build_array1(filename:str,sheetname:str):
    df=pandas.read_excel(filename,sheetname)
    return

def build_presets(filename:str,sheetname:str):
    df=pandas.read_excel(filename,sheetname)
    return_array = []
    for entry in range(0, df.shape[0]):
        return_array.append(array2(df.iloc[entry]['String'],df.iloc[entry]['CType'],df.iloc[entry]['Str']))
    
    return return_array

def build_options(filename:str,sheetname:str):
    df=pandas.read_excel(filename,sheetname)
    return_array = []
    for entry in range(0, df.shape[0]):
        return_array.append(array1(df.iloc[entry]['CType'],df.iloc[entry]['PType']))
    
    return return_array



if __name__ == '__main__':
    array_container = build_presets('array1.xlsx','A2')
    pass