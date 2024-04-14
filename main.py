import os

from processes import DeejProcess

from ui import *

PROCNAME = "deej.exe"

if __name__ == '__main__':

    os.chdir("C:\\Users\\San\\PycharmProjects\\ClassTesting1\\deej")
    # test object
    #test = DeejProcess(PROCNAME, 0, False)
    
    # test functions
    #test.PrintSelf()
    
   # test.CheckRunName()

    #test.CheckRunPID()

    #test.GetState()

    #test.GetPid()

    #test.LaunchProcess()

    # call windows
    window_obj = Windows()
    window_obj.mainloop()

    """
    userin = ""

    while userin != 6:
        print("0: Check for running by pid\n1: Get self state\n2: Get self PID\n3: Launch\n4: Kill\n9: Exit")

        userin = input("choice:")

        match str(userin):
            case "0":
                test.UpdateState()
            case "1":
                test.GetState()
            case "2":
                test.GetPid()
            case "3":
                test.LaunchProcess()
            case "4":
                test.KillProcess()
            case "9":
                break
    """

