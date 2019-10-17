#
#
# Runs a process 
#
# python ways of reliable executing cli / command 
# stream output to queue 
# 
# Streaming 
# io.BytesIO or io.BufferedReader

import subprocess 

class ProcessRunner:

    def execute(self, command: str) -> bool:
        print("executing", command)
        self.streamedOutput = subprocess.Popen(['cat', 'r.csv'], stdout = subprocess.PIPE)
        self.sendOutput(self.streamedOutput)

    def sendOutput(self, streamedOutput):
        while True:
            executionResult = streamedOutput.stdout.readline()
            if executionResult:
             print(executionResult)
            else:
             break