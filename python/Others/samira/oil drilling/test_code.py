# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 13:46:45 2021

@author: tahera
"""
import os
import pandas as pd
import copy
import numpy as np
import matplotlib.pyplot as plt
import random
import matplotlib.dates as mdates
plt.rcParams.update({'font.size': 6})


def readCaseInfo(caseName):

    # Read needed information about the case, including relevant meta data.

    # For example fluid properties, drill string and BHA diameters, well configuration, survey data.

    # Return a suitable data structure.

    caseInfo = []

    return caseInfo


def readFieldData(caseName):

    # Read data files with time series.

    # Return data in a suitable data structure, like a Pandas data frame

    # See the folders under Python_code_with_test_data\Code for an example

    # merging all the files and their relvant datas
    file_list = []
    # Creating an empty list for filenames+paths
    for datafile in os.listdir(caseName):
        if datafile[-4:] == ".csv":
            # filtering to accept ".csv" only
            file_list.append(os.path.join(caseName, datafile))
            # appending values to the list

    fieldData_list = [pd.read_csv(file, skiprows=[1], index_col=[0])
                      for file in file_list]  # creating dataframes from all files
    fieldData = pd.concat(fieldData_list)
    # concatenating all dataframes into one
    fieldData.index = pd.to_datetime(fieldData.index)
    # converting the indexes into panda's date time format
    fieldData.sort_index(inplace=True)
    # sort according to index, in this case it will be timestamps
    # creating list of units/formats(datetime)
    df_list = [pd.read_csv(file, nrows=1) for file in file_list]
    # creating a list of dataframes, containing only the column headers and the units
    df = pd.concat(df_list)
    # concatenating all dataframes into one
    df.reset_index(drop=True, inplace=True)
    # resetting index to fix multiple 0 index issues
    # all of the lines extracted are from index 0 in every .csv file,
    # therefore we need to reset them to follow a sequence instead of letting them remain 0
    df = (df.transpose())
    # applying matrix transposition (flips columns to become rows and rows to become columns)

    df = df.fillna("")
    # null types were problematic, and would be deleted anyways
    # therefore we change them into blank strings for easier comparison

    # traversing through every element in the matrix (our dataset is very small, just consisting of units across a few files)
    index_list = list(df.index.values)
    for rows in range(len(index_list)):
        for columns in range(1, len(df.columns)):
            if (df.iat[rows, columns] != ""):
                # checking above mentioned null entries (now blank string) entries to ignore
                df.iat[rows, 0] = df.iat[rows, columns]
                # taking valid entried and putting them at the first column

    df.drop(df.columns[1:], axis=1, inplace=True)
    # deleting all other columns except for the first one
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
    df.columns = ["Variable Name", "Units"]
    df["Description"] = [i for i in index_list]

    return fieldData, df

        

# Below are ways used to test above function

#x, y = readFieldData("C:\\Users\\taher\\Documents\\ENGI 001W\\Data")
# PLACE YOUR PATH, REPLACE \ with \\
#filex = open("raw_data.csv", "w")
#x.to_csv(filex, line_terminator="\n")
# filex.close()
#filey = open("test_y.csv", "w")
#y.to_csv(filey, line_terminator="\n")
# filey.close()
# (["data_bht.csv", "data_hookload_torque_slips.csv", "data_short.csv", "data_short_spp.csv"])


def processFieldData(fieldData, offBottomAsBinaryFlag=True):

    # Check and correct data.

    # Analysis and categorization.

    # Visualize data.

    # Plus other things required for next steps.

    # See the folders under Python_code_with_test_data\Code for an example

    raw_fieldData = fieldData.copy()

    # When the ROP is above this value, it is unphysical and should be removed
    ROPCutoff = 100
    fieldData.loc[fieldData.RT_ROPA_T > ROPCutoff, 'RT_ROPA_T'] = float('NaN')

    # Extreme ECD values are ignored
    # In the absence of a gas kick, a specific gravity of anything less than 0.8 is unbelievable & should be removed
    ECDMinimum = 0.8
    if "RT_ECD_T" in fieldData.columns:
        fieldData.loc[fieldData.RT_ECD_T <
                      ECDMinimum, 'RT_ECD_T'] = float('NaN')
    if "ASMECD1_T" in fieldData.columns:
        fieldData.loc[fieldData.ASMECD1_T <
                      ECDMinimum, 'ASMECD1_T'] = float('NaN')
    if "ASMECD2_T" in fieldData.columns:
        fieldData.loc[fieldData.ASMECD2_T <
                      ECDMinimum, 'ASMECD2_T'] = float('NaN')
    # The ECD should be ignored above a certain cutoff
    ECDCutOff = 10
    if "RT_ECD_T" in fieldData.columns:
        fieldData.loc[fieldData.RT_ECD_T >
                      ECDCutOff, 'RT_ECD_T'] = float('NaN')
    if "ASMECD1_T" in fieldData.columns:
        fieldData.loc[fieldData.ASMECD1_T >
                      ECDCutOff, 'ASMECD1_T'] = float('NaN')
    if "ASMECD2_T" in fieldData.columns:
        fieldData.loc[fieldData.ASMECD2_T >
                      ECDCutOff, 'ASMECD2_T'] = float('NaN')

    # Case dependent checks may be added

    # Temperature downhole  - remove some low (2-3 deg C) invalid values
    TemperatureMinimum = 5.0
    if "DHT001_TEMP_PCB_MEAN" in fieldData.columns:
        fieldData.loc[fieldData.DHT001_TEMP_PCB_MEAN <
                      TemperatureMinimum, 'DHT001_TEMP_PCB_MEAN'] = float('NaN')
    # NaN values are replaced with the last known value for that sensor reading
    fieldData.fillna(method='ffill', inplace=True)
    # When no prior readings exist, NaNs are replaced with the first non-NaN occurence
    fieldData.fillna(method='bfill', inplace=True)
    # Set RPM and torque to zero when hook load is small, indicating in slips
    # Note! The thresold 1400 depends on case, bit depth, and units (amongst others)
    if 'HKLDAV' in fieldData.columns:
        fieldData.loc[fieldData.loc[:, 'HKLDAV'] < 1400, 'RT_RPMS_T'] = 0
        fieldData.loc[fieldData.loc[:, 'HKLDAV'] < 1400, 'TQABAV'] = 0
        fieldData.loc[fieldData.loc[:, 'HKLDAV'] < 1400, 'RT_ROPA_T'] = 0
    # Pressure and ECD is ignored if negative
    if "ASMPAM1_T" in fieldData.columns:
        fieldData.loc[fieldData.ASMPAM1_T < 0, 'ASMPAM1_T'] = float('NaN')
    if "ASMPAM2_T" in fieldData.columns:
        fieldData.loc[fieldData.ASMPAM2_T < 0, 'ASMPAM2_T'] = float('NaN')
    if "ASMPAM3_T" in fieldData.columns:
        fieldData.loc[fieldData.ASMPAM3_T < 0, 'ASMPAM3_T'] = float('NaN')
    if "RT_ECD_T" in fieldData.columns:
        fieldData.loc[fieldData.RT_ECD_T < 0, 'RT_ECD_T'] = float('NaN')
    if "ASMECD1_T" in fieldData.columns:
        fieldData.loc[fieldData.ASMECD1_T < 0, 'ASMECD1_T'] = float('NaN')
    if "ASMECD2_T" in fieldData.columns:
        fieldData.loc[fieldData.ASMECD2_T < 0, 'ASMECD2_T'] = float('NaN')

# Pit volume may show instantaneous jumps, probably caused by switching tanks
# Jumps can be patched out by taking the time differential, where these jumps appear as spikes, remove these and integrate back
# This also takes care of spikes in the data set, which will appear as two spikes in opposite directions when differentiating

    # Limit for jumps in pit volume
    spikeLimit = 4
    # Take differential
    fieldData["pitDiff"] = fieldData.RT_PIT_GAIN_LOSS_T.diff()
    # Remove spikes
    fieldData.loc[abs(fieldData.pitDiff) > spikeLimit, 'pitDiff'] = 0
    # Integrate back by taking the cumulative sum
    fieldData["RT_PIT_GAIN_LOSS_T"] = fieldData.pitDiff.cumsum()
    # Delete helper variable
    del fieldData['pitDiff']
    # The differentiation and integration makes the first element of RT_PIT_GAIN_LOSS a NaN
    # We backfill to keep the cleansed data set NaN-free
    fieldData.RT_PIT_GAIN_LOSS_T[0] = fieldData.RT_PIT_GAIN_LOSS_T[1]

    # "OffBottom" signal defined as hole depth minus bit depth
    # Zero when drilling, positive otherwise
    fieldData['OffBottom'] = fieldData['RT_DEPTH_HOLE_T'] - \
        fieldData['RT_DEPTH_BIT_T']
    # Convert to a binary flag: Zero when drilling, otherwise 1
    if offBottomAsBinaryFlag:
        fieldData.loc[fieldData.OffBottom > 0, 'OffBottom'] = float('1')

    # Check for NaNs (which should be removed by now)
    if fieldData.isna().sum().sum() > 0:
        print("Warning: Dataset contains NaN values:\n", fieldData.isna().sum())

    modifiedFieldData = fieldData

    status = 0

    return status, modifiedFieldData



# Below are ways used to test above function
#c = processFieldData(readFieldData("C:\\Users\\taher\\Documents\\ENGI 001W\\Data")[0], offBottomAsBinaryFlag=True)
#filec = open("cleansed_data.csv", "w")
# c[1].to_csv(filec,line_terminator="\n")
# filec.close()


def skinFactor(caseInfo, drillingHistory, completionHistory,

               wellPressureHistory, reservoirPressureHistory,

               calibrationParameters):

    # Alternative name of skinFactor: formationDamage()

    # Ref.: SPE 179011, suggestions by Alexlandre Lavrov

    # Inputs to skinFactor():

    #    caseInfo: Static information on the case not covered by sub variables below

    #    drillingHistory: All information that may change during the drilling

    #       operation vs. time, including fluid type and properties, string geometry,

    #       pump rate, bit position, rotation rate, survey data, hole diameter

    #       vs. depth, etc.

    #    completionHistory: Similar as drillingHistory, but for completion

    #    wellPressureHistory: Calculated or measured pressure profile vs. time

    #    reservoirPressureHistory: Calculated or measured pressure profile vs. time

    #    calibrationParameters: Parameters that are updated on calibration

    status = 0

    return status


def calibrateSkinFactor(skinFactor, caseInfo,

                        wellPressureHistory, reservoirPressureHistory,

                        drillingHistory, completionHistory, calibrationParameters,

                        measuredSkinFactor

                        ):

    # measuredSkinFactor: Represents data on skin factor or a derived quantity,

    # e.g. early production profile.

    newCalibrationParameters = calibrationParameters

    status = 0

    return newCalibrationParameters, status

if __name__=="__main__":
    #"C:\\Users\\taher\\Documents\\ENGI 001W\\Data"
    df0, df2 = readFieldData("C:\\Users\\shiha\\codes\\python\\Others\\samira\\db")
    df3 = processFieldData(df0)
    filenameList = ["raw", "cleansed"]
    dataframeList = [df0, df3[1]]
    for dataframes in range(len(dataframeList)):
        df1 = dataframeList[dataframes]
        listdf = [df1[a] for a in df1.columns]
        description = list(df2["Description"])[1:]
        nrow, ncol = 6, 5
        fig, axes = plt.subplots(nrows = nrow, ncols=ncol)
        count = 0
        for r in range(nrow):
            for c in range(ncol):
                if count == len(listdf)-1:
                    break
                               
                listdf[count].plot(ax=axes[r, c],c=(random.random()*0.8,random.random()*0.8,random.random()*0.8), legend=description[count])
                graph = list(axes[r])[c]
                #graph.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
                graph.set_title("{} - {}".format(description[count], df2["Variable Name"][count+1]))
                count += 1
            if count == len(listdf):
                break 
        fig.set_size_inches((ncol+4)*2, (nrow+1)*2)
        for a in range(1,ncol-len(description)%ncol+1):
            axes[-1, -a].axis('off')
        plt.subplots_adjust(left=0.05, bottom=0.1, right=0.95, top=0.95, wspace=0.3, hspace=1)
        plt.savefig("{}_data_plot.png".format(filenameList[dataframes]), format='png',dpi=300)
        #plt.show()
    