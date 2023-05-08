#David Hernandez
#05/07/2023
#CS 162 Week 3

#Enter queues as a list

#Input packets as a string, S=Stard, P=Priority, E=Economy
input_packets = ["S Mary", "P Dee", "P Dee", "P Dee", "E Eileen",
"E Mike", "E Joe", "P Dee", "E Vicky", "E George",
"P Dee", "P Joe", "E Sally", "P Joe", "S Pete",
"P Dee", "S Bill", "S Chase", "E Price", "P Dee",
"E Sue"]

#Make Priority/Standard/Economy Lists

Priority = []
Standard = []
Economy = []
Final_queue = []

#Make sorter and define the function
def SortPacket():
    #Confirms The first letter and sorts
    for x in input_packets:
        if x[0] == ("P"):
            Priority.append(x)
        elif x[0] == ("S"):
            Standard.append(x)
        elif x[0] == ("E"):
            Economy.append(x)
        else:
            print("Your packet doesn't have a priority level!, Try again please: ")

#Call the function SortPacket()
#Make packet reshuffle for final queue
def PacketReshuffle():
#Lets make loop
    totalPackets = len(Priority)+ len(Standard) + len(Economy)
    processedPackets = 0

    while processedPackets < totalPackets:
        #Process for figuring out priorities
        for i in range(3):
            if Priority.__len__()>0:
                Final_queue.append(Priority[0])
                Priority.pop(0)
                processedPackets += 1
        #Now the standard sort
        for i in range(2):
            if Standard.__len__() > 0:
                Final_queue.append(Standard[0])
                Standard.pop(0)
                processedPackets +=1
        #Now the economy sort
        if Economy.__len__() > 0:
            Final_queue.append(Economy[0])
            Economy.pop(0)
            processedPackets +=1
#Call main and print
def main():
    SortPacket()
    PacketReshuffle()

    print("                   ")
    print("Final queue is: ")
    print(Final_queue)
    print("                    ")

main()
