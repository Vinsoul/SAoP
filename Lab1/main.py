import urllib2
import pandas as pd
import numpy as np
import time

changing_index = {
	1: 22,
	2: 24,
	3: 23,
	4: 25,
	5: 3,
	6: 4,
	7: 8,
	8: 19,
	9: 20,
	10: 21,
	11: 9,
	12: 0,
	13: 10,
	14: 11,
	15: 12,
	16: 13,
	17: 14,
	18: 15,
	19: 16,
	20: 0,
	21: 17,
	22: 18,
	23: 6,
	24: 1,
	25: 2,
	26: 7,
	27: 5
}

rename_columns = {
	"VCI": "Vegetation Condition Index",
	"VHI": "Vegetation Health Index",
	"TCI": "Temperature Condition Index",
	"%Area_VHI_LESS_15": "Percentage of an area, where VHI less than 15%",
	"%Area_VHI_LESS_35": "Percentage of an area, where VHI less than 35%"

}

def DownloadFile(index):
	#changing index in accordance with task
	index = changing_index[index]
	"""
		filename - number of the file on website
		because files are numerating like (01, 02, ..., 09, 10, ...)
	"""
	filename = ""
	if index <= 0 or index > 27:
		return False
	elif index < 10:
		filename += "0" + str(index)
	else:
		filename += str(index)
	#opening url
	url = "http://www.star.nesdis.noaa.gov/smcd/emb/vci/gvix/G04/ts_L1/ByProvince/Mean/L1_Mean_UKR.R%s.txt" % filename
	url_file = urllib2.urlopen(url)
	current_time = str(time.strftime("%d.%m.%Y_%H-%M-%S"))
	out = open("Files/vhi_id_%s_%s.csv" % (filename, current_time), "w")
	print ("Downloading file vhi_id_%s" % filename)
	out.write(url_file.read())
	out.close()
	return "Files/vhi_id_%s_%s.csv" % (filename, current_time)

#Load file in dataFrame
def LoadInDataFrame(path):
	df = pd.read_csv(path, index_col=False, header=1)
	return df

#print VHI of some region by year
def PrintByYear(df):
	print ("Printing by year: ")
	year = int(raw_input("Enter year: "))
	while (year < 1981 or year > 2016):
		year = int(raw_input("Enter proper year(>1981 and <2017): "))
	print (pd.DataFrame(df[df['year'] == year], columns=['year', 'week', rename_columns['VHI']]))

def PrintMax(df):
	print ("Maximum VHI: %s" % str(max(df[rename_columns["VHI"]])))

def PrintMin(df):
	print ("Minimum VHI: %s" % str(min(df[rename_columns["VHI"]])))

def FindYearVHIExtremelyLow(df, lim):
	df = df[df[rename_columns["%Area_VHI_LESS_35"]] >= lim]
	years = np.unique(df['year'])
	print ("Years: %s" % years)
	return True

def FindYearVHILow(df, lim):
	df = df[df[rename_columns["%Area_VHI_LESS_15"]] >= lim]
	years = np.unique(df['year'])
	print ("Years: %s" % years)
	return True

#Additional function
def ReversedChangeIndex(index):
	index = int(index)
	if index < 1 or index > 25:
		return 0
	for i in range(1, len(changing_index)):
		if int(changing_index[i]) == index:
			return int(i)
	return 0

#main function
def main():
	files = [] #list of path all files that was downloaded
	for i in range(1, 27):
		if i == 12 or i == 20:
			files.append("")
			continue
		path = DownloadFile(i)
		if path == False:
			print ("Failed to download file!")
			return
		else:
			files.append(path)
	print ("Files successfully downloaded!")
	dframe = []
	count = 0
	for path in files:
		if path != "":
			dframe.append(LoadInDataFrame(path))
			dframe[count].rename(columns=rename_columns, inplace=True)
		else:
			dframe.append(pd.DataFrame(columns=[]))
		count += 1
	print (len(dframe))
	if len(dframe) == 0:
		print ("Error with loading files in dataframe! Program will now close")
		return
	print ("Files was successfully loaded in dataframes")
	while True:
		print ("1-print all info of the region by year;")
		print ("2-print info for the region when VHI is maximum;")
		print ("3-print info for the region when VHI is minimum;")
		print ("4-find years when percentage of an area, where VHI less than 35%, is higher than a some number;")
		print ("5-find years when percentage of an area, where VHI less than 15%, is higher than a some number;")
		print ("0-exit the program")
		userInput = int(raw_input("Enter command: "))
		if userInput == 0:
			return
		elif userInput == 1:
			userInput = raw_input("Enter index of a region: ")
			userInput = int(ReversedChangeIndex(userInput))
			if userInput != 0:
				PrintByYear(dframe[userInput-1])
			else:
				print ("Error! Ircorrect index")
		elif userInput == 2:
			userInput = raw_input("Enter index of a region: ")
			userInput = int(ReversedChangeIndex(userInput))
			if userInput != 0:
				PrintMax(dframe[userInput-1])
			else:
				print ("Error! Ircorrect index")

		elif userInput == 3:
			userInput = raw_input("Enter index of a region: ")
			userInput = int(ReversedChangeIndex(userInput))
			if userInput != 0:
				PrintMin(dframe[userInput-1])
			else:
				print ("Error! Ircorrect index")
		elif userInput == 4:
			userInput = raw_input("Enter index of a region: ")
			userInput = int(ReversedChangeIndex(userInput))
			if userInput != 0:
				FindYearVHIExtremelyLow(dframe[userInput-1], int(raw_input("Enter % limit: ")))
			else:
				print ("Error! Ircorrect index")

		elif userInput == 5:
			userInput = raw_input("Enter index of a region: ")
			userInput = int(ReversedChangeIndex(userInput))
			if userInput != 0:
				FindYearVHILow(dframe[userInput-1], int(raw_input("Enter % limit: ")))
			else:
				print ("Error! Ircorrect index")

	else:
			print ("Unknown command. try again")


main();