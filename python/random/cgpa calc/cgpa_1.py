from bracu_cgpa_calc import *
#import bracu_cgpa_calc as bcc #this is another alternative import

add("CSE110", 4, 3) #adding courses
add("CSE111", 3.7, 3) #adding courses
add("CSE220", 3.3, 3) #adding courses
add("MAT215", 0, 3) #adding courses
#bcc.add("MAT215", 0, 3) #adding courses using alternative import
#remove("CSE220") #removing courses
#check_attempted_course() #returns list of courses attempted.
#check_completed_course() #returns list of courses completed.
#check_retake_course() #returns list of courses needs retake.
#credits_attempted() #returns number of credits attempted.
#credits_completed() #returns number of credits completed.
#get_cgpa() #returns CGPA
#readme() #prints out readme
#docs() #prints out documentation
#save_to_pc() #self-explanatory
#read_from_pc("CGPA.xlsx") #reads "CGPA.xlsx" from device
#flush() #flushes all the data of course list and CGPA and everything from the code
save_to_pc()