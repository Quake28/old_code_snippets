# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 17:33:29 2021

@author: tahera
"""

import os
import pandas as pd

# Read data files with time series.

# Return data in a suitable data structure, like a Pandas data frame

# See the folders under Python_code_with_test_data\Code for an example


# FILE IS FORMATTED WITH BLACK, DEFAULT SETTINGS
def readFieldData(caseName):
    # merging all the files and their relvant datas
    file_list = []  # Creating an empty list for filenames+paths
    for datafile in os.listdir(caseName):
        if datafile[-4:] == ".csv":  # filtering to accept ".csv" only
            file_list.append(
                os.path.join(caseName, datafile)
            )  # appending values to the list

    fieldData_list = [
        pd.read_csv(file, skiprows=[1], index_col=[0]) for file in file_list
    ]  # creating dataframes from all files
    fieldData = pd.concat(fieldData_list)  # concatenating all dataframes into one
    fieldData.index = pd.to_datetime(
        fieldData.index
    )  # converting the indexes into panda's date time format
    fieldData.sort_index(
        inplace=True
    )  # sort according to index, in this case it will be timestamps
    # creating list of units/formats(datetime)
    df_list = [
        pd.read_csv(file, nrows=1) for file in file_list
    ]  # creating a list of dataframes, containing only the column headers and the units
    df = pd.concat(df_list)  # concatenating all dataframes into one
    df.reset_index(
        drop=True, inplace=True
    )  # resetting index to fix multiple 0 index issues
    # all of the lines extracted are from index 0 in every .csv file,
    # therefore we need to reset them to follow a sequence instead of letting them remain 0
    df = (
        df.transpose()
    )  # applying matrix transposition (flips columns to become rows and rows to become columns)

    df = df.fillna("")  # null types were problematic, and would be deleted anyways
    # therefore we change them into blank strings for easier coparison

    # traversing through every element in the matrix (our dataset is very small, just consisting of units across a few files)
    index_list = list(df.index.values)
    for rows in range(len(index_list)):
        for columns in range(1, len(df.columns)):
            if (
                df.iat[rows, columns] != ""
            ):  # checking above mentioned null entries (now blank string) entries to ignore
                df.iat[rows, 0] = df.iat[
                    rows, columns
                ]  # taking valid entried and putting them at the first column

    df.drop(
        df.columns[1:],
        axis=1,
        inplace=True,
    )  # deleting all other columns except for the first one
    # this is the simplest method as of now to push everything to the fist column (pos 0) and remove null entries
    index_list = [
        "Time",
        "Downhole temperature (near bit)",
        "Averaged topside torque on drill string",
        "In-slip signal (very low sampling rate)",
        "Averaged topside hook load",
        "Rate of Penetration (ROP)",
        "Drill string rotation (RPM)",
        "Depth of hole",
        "Depth of bit",
        "Annular pressure near bit",
        "Annular ECD near bit",
        "Mud temperature out of hole",
        "Mud temperature into hole",
        "Mud density out",
        "Mud density in",
        "Mud flow rate out",
        "Mud flow rate in",
        "ECD at ASM sensor 1",
        "Pressure at ASM sensor 3",
        "Depth at ASM sensor 3",
        "Pressure at ASM sensor 2",
        "Depth at ASM sensor 2",
        "Pressure at ASM sensor 1",
        "Depth at ASM sensor 1",
        "Pit gain/loss",
        "ECD at ASM sensor 2",
        "SPP",
    ]
    df.reset_index(inplace=True)
    df.columns = [
        "Variable Name",
        "Units",
    ]  # setting the name of the column to "Units", we don't have to worry about anything else because it's non-existant
    df["Description"] = [
        i for i in index_list
    ]  # adding blank description column for future use

    return fieldData, df


# Below are ways used to test above function

x, y = readFieldData(
    "C:\\Users\\shiha\\code\\python\\Others\\samira\\db"
)  # PLACE YOU PATH, REPLACE \ with \\
filex = open("testx.csv", "w")
x.to_csv(filex, line_terminator="\n")
filex.close()
filey = open("testy.csv", "w")
y.to_csv(filey, line_terminator="\n")  # index=False,
filey.close()
# (["data_bht.csv", "data_hookload_torque_slips.csv", "data_short.csv", "data_short_spp.csv"])
