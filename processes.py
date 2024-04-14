import psutil
import os

class DeejProcess:
    # class for process
    # 3 attributes, name, PID, state
    def __init__(self, process_name, process_id, process_state):
        # initialize process name
        self.process_name = process_name
        self.process_id = process_id
        self.process_state = process_state

        # check for running process and set id attribute when initializing

        PID = 0

        for proc in psutil.process_iter():
            # print(proc)
            if self.process_name in proc.name():
                # print(f"{proc.name()}, pid: {proc.pid}")
                PID = proc.pid
                # update object state
                self.process_state = True
                # update object id
                self.process_id = PID

                return

            self.process_state = False

    def PrintSelf(self):
        print("Target:", self.process_name)

    # for updating PID after launch internally
    def UpdatePid(self):

        PID = 0

        for proc in psutil.process_iter():
            # print(proc)
            if self.process_name in proc.name():
                # print(f"{proc.name()}, pid: {proc.pid}")
                PID = proc.pid

                # update object state
                self.process_state = True
                # update object id
                self.process_id = PID
                #print(f"#: {self.process_id}")

                return PID

        self.process_state = False
        return PID

    # after initial check, look for deej by PID
    def UpdateState(self):

        if self.process_id != 0 and psutil.pid_exists(self.process_id):
            #print(f"{process_id} already running")
            self.process_state = True
            print("Check by pid: ", self.process_id)
        else:
            #print(f"{process_id} not running")
            self.process_state = False

    # return process state
    def GetState(self):
        if self.process_state == True:
            print("Get state: running")
            return self.process_state
        else:
            print("Get state: not running")
            return self.process_state
    # return pid
    def GetPid(self):
        if self.process_state == True:
            print("Get Pid: ", self.process_id)

            return self.process_id

            # call check by name to update PID
            #self.CheckRunName()

        else:
            print("Get Pid: not running")
            return self.process_id
    # launch, kill process
    def LaunchProcess(self):
        if self.process_state == False:
            try:
                os.startfile("deej.exe")
                self.process_state = True

                # update pid attribute
                self.UpdatePid()

                print("Launch succesful")

                return "Launch Success"

            except:
                print("Error starting, exiting")
                return "Failure to launch"
        else:
            print("Launch: Process already running")
            return "Process already running"

    def KillProcess(self):
        if self.process_state == True and psutil.pid_exists(self.process_id):
            proc = psutil.Process(self.process_id)
            try:
                proc.kill()
                self.process_id = 0
                self.process_state = False

            except:
                print("error killing process, exiting")