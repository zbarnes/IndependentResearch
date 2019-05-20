from ahk import ActionChain
import os

'''
When run this script uses autohotkeys with a python wrapper to 
export .cev files, containing voltage and current fault data from
distribution systems, to csv format in order to do analysis
'''


ac = ActionChain()


directory = "D:\\File Path\\"


for filename in os.listdir(directory): 
    if (filename.endswith('CEV') or filename.endswith('cev')):
        filepath = directory + filename
	#open .cev file
        os.startfile(filepath)
        ac.sleep(3)
        base = os.path.basename(filename)
        split_name = os.path.splitext(base)[0]
        #get rid of file names that end with 
        if(split_name[len(split_name)-1] == ","):
           split_name = split_name[:len(split_name)-1]	
        #end if	
        #move mouse to export button
        ac.mouse_move(x=3626, y=25, speed=10, relative = False)
        ac.sleep(1)
        ac.click()
        ac.sleep(1)
        #navigate to save menu
        ac.key_down('Down')
        ac.sleep(1)
        ac.key_press('Enter')
        ac.sleep(1)
        #enter name of file to save
        ac.type(split_name)
        ac.sleep(1)
        ac.key_press('Enter')
        ac.sleep(1)
        #close out of current window
        ac.mouse_move(x=3820, y=20, speed=10, relative = False)
        ac.sleep(1)
        ac.click()
        ac.sleep(1)
        ac.perform()
    #end if
    print(filename)
