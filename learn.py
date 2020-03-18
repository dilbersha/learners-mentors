import string
class tech:
    stack_count=0
    stack = []
    i=0
    def addStacks():
        a=raw_input("Enter your stack ")
        stack[i]=a
        i+=1
    def setMentorOrLearner():
        type=raw_input("Are you mentor or learner? ")
        type=type.lower()
        if (type=="mentor"):
            t=1
        elif (type=="learner"):
            t=2
        else:
            t=0
        return t
    def setAvailableTime():
        if (t==1):
            AvailableTimeF=raw_input("Enter your available time from ")
            AvailableTimeT=raw_input("Enter your available time to ")
            n=input("Enter no. of stacks ")
            j=0
            KnownStack=[]
            while (j<n):
                KnownStack[j]=raw_input("Enter your stack ")
    def getMentor(timeF,timeT,stac):
        if ((timeF < AvailableTimeF)|(timeT > AvailableTimeT)&(stac in KnownStack)):
            return 1

