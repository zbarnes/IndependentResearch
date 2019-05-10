from ahk import AHK
from ahk import ActionChain
import os

#os.startfile("C:\Program Files\SEL\SEL SynchroWAVe Event\SynchroWAVeEvent.exe")
#open file "D:\Exported_From Zack\3 LAKES CKT 12 - 1819 S #   
111347026301_13_201816_09_58_743_from_cev.Comtrade.Session"
#open file "D:\Exported_From Zack\FileName.Comtrade.Session"

directory = "D:\TwoSevenThree_LEFT_Pending"

for filename in os.listdir(directory):
    if filename.endswith(".cev"):
	    base = os.path.basename(filename)
	    split_name = os.path.splitext(base)[0]
	    if(split_name[len(split_name)-1] == ","):
		    split_name = split_name[:len(split_name)-1]
	    print(split_name)
	    #print(filename)


ahk = AHK()
ac = ActionChain()
ahk.mouse_move(x=3626, y=25, speed=10, relative = False)
ahk.click()
ahk.key_down('Down')
ac.sleep(1)
ahk.key_press('Enter')
ac.sleep(1)
ahk.type('Norton smells like poo')
ac.sleep(1)
ahk.key_press('Enter')
#ac.preform()




#write the name of file as the file name
