# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 13:46:45 2021

@author: tahera
"""
import os
import pandas as pd
import tabula
import lasio
import copy
import numpy as np
import matplotlib.pyplot as plt
import random
plt.rcParams.update({'font.size': 6})


def readCaseInfo(caseName):

    # Read needed information about the case, including relevant meta data.

    # For example fluid properties, drill string and BHA diameters, well configuration, survey data.

    # Return a suitable data structure.

    file_list = [os.path.join(caseName, datafile) for datafile in os.listdir(caseName)]
    caseInfo_list = []
    for datafile in file_list:
        if datafile[-4:] == ".pdf":
            caseInfo_list.append(pd.concat(tabula.read_pdf(datafile, pages="all", stream=True)))
        elif datafile[-5:] == ".xlsx":
            caseInfo_list.append(pd.read_excel(datafile))
        elif datafile[-4:] == ".las":
            lasfile = lasio.read(datafile)
            caseInfo_list.append(lasfile.df())
        elif datafile[-4:] == ".prn":
            caseInfo_list.append(pd.read_csv(datafile, sep=" "))
    
    caseInfo = pd.concat(caseInfo_list)
    
    return caseInfo

# Below are ways used to test above function
#x = readCaseInfo("C:\\Users\\taher\\Documents\\ENGI 001W\\Alaska Well Data")
#PLACE YOUR PATH, REPLACE \ with \\
#filex = open("caseInfo.csv", "w")
#x.to_csv(filex, line_terminator="\n")


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


def processFieldData(raw_fieldData, offBottomAsBinaryFlag=True):

    # Check and correct data.

    # Analysis and categorization.

    # Visualize data.

    # Plus other things required for next steps.

    # See the folders under Python_code_with_test_data\Code for an example

    fieldData = copy.deepcopy(raw_fieldData)

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

    
    status = 0

    return status, fieldData


# Below are ways used to test above function
# c = processFieldData(readFieldData("C:\\Users\\taher\\Documents\\ENGI 001W\\Data")[0], offBottomAsBinaryFlag=True)
# filec = open("cleansed_data.csv", "w")
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

#Visualization of data
def plotting(df0, df1, df2, df3, df5, df6, nrow, ncol, num): #df4, 
    fig, axes = plt.subplots(nrows = nrow, ncols=ncol)
    count = 0
    for r in range(nrow):
        for c in range(ncol):
            if count == len(df0):
                break

            if ncol > 1:
                graph = list(axes[r])[c]
                df0[count].plot(ax=axes[r,c],c=(0,0,0), marker="x", linestyle="", markersize=2, markeredgewidth=0.5)
                df3[count].plot(ax=axes[r,c],c=(random.random()*0.8,random.random()*0.8,random.random()*0.8), linewidth=0.5) 
            else:
                graph = list(axes)[r]
                df0[count].plot(ax=axes[r],c=(0,0,0), marker="x", linestyle="", markersize=2, markeredgewidth=0.5)
                df3[count].plot(ax=axes[r],c=(random.random()*0.8,random.random()*0.8,random.random()*0.8), linewidth=0.5)
                
            graph.legend(["raw data", "cleansed data"], loc="best")
            graph.set_ylabel("{} ({})".format(df5[count],df6[count])) #Temperature(°C)
            graph.set_title("{} - {}".format(df1[count], df2[count]))
            count += 1
        if count == len(df0):
            break 
    fig.set_size_inches((ncol+6)*2, (nrow+2)*2)
    if ncol > 1:
        for a in range(-1,-(count%ncol+1), -1):
            axes[-1, a].axis('off')
    plt.subplots_adjust(left=0.05, bottom=0.1, right=0.95, top=0.95, wspace=0.1, hspace=0.7)
    plt.savefig("data_plot_{}.png".format(num), format='png',dpi=300)
    plt.show()

def plotting_2(df0, df1, df3, df5, df6, num): # df2, df4, 
    graph=plt.figure()
    legends=[]
    color=[(random.random()*0.7/len(df3))+0.1 for a in range(3)]
    for count in range(len(df3)):
        cleansed_color=[(count+1)*a for a in color]
        raw_color=[a-0.1 for a in cleansed_color]
        #print(count,df1[count])
        if df0[count]!=None:
            graph=df0[count].plot(c=raw_color, marker="x", linestyle="", markersize=2, markeredgewidth=0.5)
            legends.append("{} (raw)".format(df1[count]))
            legends.append("{} (cleansed)".format(df1[count]))
        graph=df3[count].plot(c=cleansed_color, linewidth=0.5)
    if df0[count]!=None:
        graph.legend(legends, loc="best")
    graph.set_title("{}".format(df1[0][:-3]))
    
    graph.set_ylabel("{} ({})".format(df5[0],df6[0])) #Temperature(°C)
    
    #print()
    # fig.set_size_inches((ncol+6)*2, (nrow+2)*2)
    # plt.subplots_adjust(left=0.05, bottom=0.1, right=0.95, top=0.95, wspace=0.1, hspace=0.7)
    plt.savefig("mud_data_plot_{}.png".format(num), format='png',dpi=300)
    plt.show()
    
if __name__=="__main__":
    # PLACE YOUR PATH, REPLACE \ with \\
    df0, df1 = readFieldData("C:\\Users\\shiha\\codes\\python\\others\\samir\\db")
    df2, df3 = processFieldData(df0)
    #filenameList = ["raw", "cleansed"]
    #dataframeList = [df0, df3[1]]
    #for dataframes in range(len(dataframeList)):
    #df1 = dataframeList[dataframes]
    df0 = [df0[a] for a in df0.columns]
    df2 = list(df1["Variable Name"])[1:]
    df4 = list(df1["Units"])[1:]
    df3 = [df3[a] for a in df3.columns]
    df1 = list(df1["Description"])[1:]
    df5 = ["Temperature", "Torque", "In-slip Signal", "Hook Load", "Rate", "Rotation", "Depth", "Depth", "Pressure", "ECD", "Temperature", "Temperature", 
           "Density", "Density", "Flow Rate", "Flow Rate", "ECD","Pressure","Depth", "Pressure", "Depth", "Pressure","Depth", "Pit Gain/Loss",   
          "ECD","Pressure"]

    df6 = df4[:]
    for a in range(len(df6)):
        if df6[a] == "degC":
            df6[a] = "°C"
        elif df6[a] == "g/cm3":
            df6[a] = "$\mathregular{g/cm^{3}}$"
        elif df6[a] == "kg/m3":
            df6[a] = "$\mathregular{kg/m^{3}}$"
        elif df6[a] == "m3":
            df6[a] = "$\mathregular{m^{3}}$"


    nrow, ncol = [3,2,2,3,3,3,3], [1,2,1,2,2,1,1]
    df10=(df0[0:3], df0[3:6]+[df0[23]], df0[6:8], (df0[8],df0[17],df0[19],df0[21],df0[25]), df0[10:16], (df0[9],df0[16],df0[24]), (df0[18],df0[20],df0[22]))
    df11=(df1[0:3], df1[3:6]+[df1[23]], df1[6:8], (df1[8],df1[17],df1[19],df1[21],df1[25]), df1[10:16], (df1[9],df1[16],df1[24]), (df1[18],df1[20],df1[22]))
    df12=(df2[0:3], df2[3:6]+[df2[23]], df2[6:8], (df2[8],df2[17],df2[19],df2[21],df2[25]), df2[10:16], (df2[9],df2[16],df2[24]), (df2[18],df2[20],df2[22]))
    df13=(df3[0:3], df3[3:6]+[df3[23]], df3[6:8], (df3[8],df3[17],df3[19],df3[21],df3[25]), df3[10:16], (df3[9],df3[16],df3[24]), (df3[18],df3[20],df3[22]))
    #df14=(df4[0:3], df4[3:6]+[df4[23]], df4[6:8], (df4[8],df4[17],df4[19],df4[21],df4[25]), df4[10:16], (df4[9],df4[16],df4[24]), (df4[18],df4[20],df4[22]))
    df15=(df5[0:3], df5[3:6]+[df5[23]], df5[6:8], (df5[8],df5[17],df5[19],df5[21],df5[25]), df5[10:16], (df5[9],df5[16],df5[24]), (df5[18],df5[20],df5[22]))
    df16=(df6[0:3], df6[3:6]+[df6[23]], df6[6:8], (df6[8],df6[17],df6[19],df6[21],df6[25]), df6[10:16], (df6[9],df6[16],df6[24]), (df6[18],df6[20],df6[22]))
    for num in range(len(df10)):
        #pass
        #nrow, ncol = len(df10[num]), 1
        plotting(df10[num], df11[num], df12[num], df13[num], df15[num], df16[num], nrow[num], ncol[num], num) # df14[num],
    

    df20=(df0[12:14][::-1],df0[14:16][::-1],[None],[None])#[df0[12].subtract(df0[13])],)
    df21=(df1[12:14][::-1],df1[14:16][::-1],["Mud density difference (In - Out)   "],["Mud flow rate difference (In - Out)   "])
    #df22=(df2[12:14][::-1],df2[14:16][::-1])
    df23=(df3[12:14][::-1],df3[14:16][::-1],[df3[12].subtract(df3[13])],[df3[14].subtract(df3[15])])
    #df24=(df4[12:14][::-1],df4[14:16][::-1])
    df25=(df5[12:14][::-1],df5[14:16][::-1],[df5[12]],[df5[14]])
    df26=(df6[12:14][::-1],df6[14:16][::-1],[df6[12]],[df6[14]])
    #print(df1[12:14],"\n",df1[12:14][::-1])
    for num in range(len(df20)):
        #pass
        plotting_2(df20[num], df21[num], df23[num],df25[num], df26[num], num) # df22[num],  df24[num], 
