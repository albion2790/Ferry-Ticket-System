from datetime import datetime
import time
now = datetime.now()
time1 = [10,11,12,13,14,15,16,17]
fid = [1,2,3,4,5,6,7,8]
vipkeepl2 = [[],[],[],[],[],[],[],[]]
vipkeepp2 = [[],[],[],[],[],[],[],[]]
ecokeepl2 = [[],[],[],[],[],[],[],[]]
ecokeepp2 = [[],[],[],[],[],[],[],[]]
megavipl = [[],[],[],[],[],[],[],[]]
megavipp = [[],[],[],[],[],[],[],[]]
megaecol = [[],[],[],[],[],[],[],[]]
megaecop = [[],[],[],[],[],[],[],[]]
listlimit = 0
while listlimit < 8:
    while len(megavipl[listlimit]) < 10:
        megavipl[listlimit].append (0)
    while len(megaecol[listlimit]) < 40:
        megaecol[listlimit].append (0)
    while len(megavipp[listlimit]) < 10:
        megavipp[listlimit].append (0)
    while len(megaecop[listlimit]) < 40:
        megaecop[listlimit].append (0)
    listlimit = listlimit + 1
def ferryid(tim,ferry,vipl2,vipp2,ecol2,ecop2,vipkeepl1,vipkeepp1,ecokeepl1,ecokeepp1):
    vipkeepl = vipkeepl1
    vipkeepp = vipkeepp1
    ecokeepl = ecokeepl1
    ecokeepp = ecokeepp1
    vipl = vipl2
    vipp = vipp2
    ecol = ecol2
    ecop = ecop2
    while True:
        print ("P - To Purchase Ticket \nV - To View Seating Arrangement \nQ - To Quit Menu")
        time.sleep(1)
        x = input ("Enter: ")
        if x == "P" or x == "p":
            print ("B - To purchase ticket for Business class\nE - To purchase ticket for Economy class\nM - To return to Main Menu")
            time.sleep(1)
            x = input ("Enter: ")
            if x == "M" or x == "m":
                True
            elif x == "B" or x == "b":
                dest = input("Choose the destination L(from langkawi) or P(from Penang): ")
                if dest == "L" or dest == "l":
                    if len(vipkeepl) > 9:
                        print ("Sorry the Business class is full would you like to book a seat in Economy class?")
                        time.sleep(1)
                        x = input ("Please enter Y(yes) or N(no): ")
                        if x == "Y" or x == "y":
                            x = "E"
                        elif x == "N" or x == "n":
                            print ("Next Ferry leaves in 1 hour, if you would still like to book a ticket please choose a different Departure time\n*Thank You!*")
                            time.sleep(1)                            
                            break
                        else:
                            print ("\n*Sorry you pressed a wrong key try again*\n")
                            time.sleep(1)
                    elif len(vipkeepl) < 10:
                        name = input("Enter your name please: ")
                        vipl.pop (len(vipkeepl))
                        vipl.insert (len(vipkeepl), 1)
                        vipkeepl.append(0)
                        print ('''
                          *****************************************
                          *BOARDING TICKET*           Ferry ID: ''',ferry,'''
                          *****************************************
                          From: Langkawi | To: Penang
                          *****************************************
                          Name:''',name,'''| Seat:''',len(vipkeepl),'''| Class: Business
                          *****************************************
                          Date: ''',now.day,'''/''',now.month,'''/''',now.year,''' | Time: ''',tim,'''
                          *****************************************''')
                        foo = open("Langkawi Tickets.txt", "a+")
                        foo.write("%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s\n" % (('''
                          *****************************************
                          *BOARDING TICKET*           Ferry ID: '''),(ferry),('''
                          *****************************************
                          From: Langkawi | To: Penang
                          *****************************************
                          Name:'''),(name),('''| Seat:'''),(len(vipkeepl)),('''| Class: Business
                          *****************************************
                          Date: '''),(now.day),('''/'''),(now.month),('''/'''),(now.year),(''' | Time: '''),(tim),('''
                          *****************************************''')))
                        foo.close()
                        time.sleep(1)
                        print("*Your seat has been booked, Thank You, Enjoy your Trip!*")
                        print ('Q - To Quit system\nM - To return to Main Menu')
                        time.sleep(1)
                        x = input ("Enter: ")
                        if x == "Q" or x == "q":
                            break
                        elif x == "M" or x == "m":
                            True
                        else:
                            print ("\n*Your seat has already been booked, Thank You!*\n")
                            time.sleep(1)
                elif dest == "P" or dest == "p":
                    if len(vipkeepp) > 9:
                        print ("Sorry the Business class is full would you like to book a seat in Economy class?")
                        time.sleep(1)
                        x = input ("Please enter Y(yes) or N(no): ")
                        if x == "Y" or x == "y":
                            x = "E"
                        elif x == "N" or x == "n":
                            print ("Next Ferry leaves in 1 hour, if you would still like to book a ticket please choose a different Departure time\n*Thank You!*")
                            time.sleep(1)
                            break
                        else:
                            print ("\n*Sorry you pressed a wrong key try again*\n")
                            time.sleep(1)
                    elif len(vipkeepp) < 10:
                        name = input("Enter your name please: ")
                        vipp.pop (len(vipkeepp))
                        vipp.insert (len(vipkeepp), 1)
                        vipkeepp.append(0)
                        print ('''
                          *****************************************
                          *BOARDING TICKET*           Ferry ID: ''',ferry,'''
                          *****************************************
                          From: Penang | To: Langkawi
                          *****************************************
                          Name:''',name,'''| Seat:''',len(vipkeepp),'''| Class: Business
                          *****************************************
                          Date: ''',now.day,'''/''',now.month,'''/''',now.year,''' | Time: ''',tim,'''
                          *****************************************''')
                        foo = open("Penang Tickets.txt", "a+")
                        foo.write("%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s\n" % (('''
                          *****************************************
                          *BOARDING TICKET*           Ferry ID: '''),(ferry),('''
                          *****************************************
                          From: Penang | To: Langkawi
                          *****************************************
                          Name:'''),(name),('''| Seat:'''),(len(vipkeepp)),('''| Class: Business
                          *****************************************
                          Date: '''),(now.day),('''/'''),(now.month),('''/'''),(now.year),(''' | Time: '''),(tim),('''
                          *****************************************''')))
                        foo.close()
                        time.sleep(1)
                        print("*Your seat has been booked, Thank You, Enjoy your Trip!*")
                        print ('Q - To Quit system\nM - To return to Main Menu')
                        time.sleep(1)
                        x = input ("Enter: ")
                        if x == "Q" or x == "q":
                            break
                        elif x == "M" or x == "m":
                            True
                        else:
                            print ("\n*Your seat has already been booked, Thank You!*\n")
                            time.sleep(1)
                else:
                        print ("\n*Sorry you pressed a wrong key try again*\n")
                        time.sleep(1)
            elif x == "E" or x == "e":
                dest = input("Choose the destination L(from langkawi) or P(from Penang): ")
                if dest == "L" or dest == "l":
                    if len(ecokeepl) > 39:
                        print ("Sorry the Economy class is full would you like to book a seat in Business class?")
                        time.sleep(1)
                        x = input ("Please enter Y(yes) or N(no): ")
                        if x == "Y" or x == "y":
                            x = "B"
                        elif x == "N" or x == "n":
                            print ("Next Ferry leaves in 1 hour, if you would still like to book a ticket please choose a different Departure time\n*Thank You!*")
                            time.sleep(1)
                            break
                        else:
                           print ("\n*Sorry you pressed a wrong key try again*\n")
                           time.sleep(1)
                    elif len(ecokeepl) < 40:
                        name = input("Enter your name please: ")
                        ecol.pop (len(ecokeepl))
                        ecol.insert (len(ecokeepl), 1)
                        ecokeepl.append(0)
                        print ('''
                          *****************************************
                          *BOARDING TICKET*           Ferry ID: ''',ferry,'''
                          *****************************************
                          From: Langkawi | To: Penang
                          *****************************************
                          Name:''',name,'''| Seat:''',len(ecokeepl),'''| Class: Economy
                          *****************************************
                          Date: ''',now.day,'''/''',now.month,'''/''',now.year,''' | Time: ''',tim,'''
                          *****************************************''')
                        foo = open("Langkawi Tickets.txt", "a+")
                        foo.write("%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s\n" % (('''
                          *****************************************
                          *BOARDING TICKET*           Ferry ID: '''),(ferry),('''
                          *****************************************
                          From: Langkawi | To: Penang
                          *****************************************
                          Name:'''),(name),('''| Seat:'''),(len(ecokeepl)),('''| Class: Economy
                          *****************************************
                          Date: '''),(now.day),('''/'''),(now.month),('''/'''),(now.year),(''' | Time: '''),(tim),('''
                          *****************************************''')))
                        foo.close()
                        time.sleep(1)
                        print("*Your seat has been booked, Thank You, Enjoy your Trip!*")
                        print ('Q - To Quit system\nM - To return to Main Menu')
                        time.sleep(1)
                        x = input ("Enter: ")
                        if x == "Q" or x == "q":
                            break
                        elif x == "M" or x == "m":
                            True
                        else:
                            print ("\n*Your seat has already been booked, Thank You!*\n")
                            time.sleep(1)
                elif dest == "P" or dest == "p":
                    if len(ecokeepp) > 39:
                        print ("Sorry the Economy class is full would you like to book a seat in Business class?")
                        time.sleep(1)
                        x = input ("Please enter Y(yes) or N(no): ")
                        if x == "Y" or x == "y":
                            x = "B"
                        elif x == "N" or x == "n":
                            print ("Next Ferry leaves in 1 hour, if you would still like to book a ticket please choose a different Departure time\n*Thank You!*")
                            time.sleep(1)
                            break
                        else:
                           print ("\n*Sorry you pressed a wrong key try again*\n")
                           time.sleep(1)
                    elif len(ecokeepp) < 40:
                        name = input("Enter your name please: ")
                        ecop.pop (len(ecokeepp))
                        ecop.insert (len(ecokeepp), 1)
                        ecokeepp.append(0)
                        print ('''
                          *****************************************
                          *BOARDING TICKET*           Ferry ID: ''',ferry,'''
                          *****************************************
                          From: Penang | To: Langkawi
                          *****************************************
                          Name:''',name,'''| Seat:''',len(ecokeepp),'''| Class: Economy
                          *****************************************
                          Date: ''',now.day,'''/''',now.month,'''/''',now.year,''' | Time: ''',tim,'''
                          *****************************************''')
                        foo = open("Penang Tickets.txt", "a+")
                        foo.write("%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s\n" % (('''
                          *****************************************
                          *BOARDING TICKET*           Ferry ID: '''),(ferry),('''
                          *****************************************
                          From: Penang | To: Langkawi
                          *****************************************
                          Name:'''),(name),('''| Seat:'''),(len(ecokeepp)),('''| Class: Economy
                          *****************************************
                          Date: '''),(now.day),('''/'''),(now.month),('''/'''),(now.year),(''' | Time: '''),(tim),('''
                          *****************************************''')))
                        foo.close()
                        time.sleep(1)
                        print("*Your seat has been booked, Thank You, Enjoy your Trip!*")
                        print ('Q - To Quit system\nM - To return to Main Menu')
                        time.sleep(1)
                        x = input ("Enter: ")
                        if x == "Q" or x == "q":
                            break
                        elif x == "M" or x == "m":
                            True
                        else:
                            print ("\n*Your seat has already been booked, Thank You!*\n")
                            time.sleep(1)
                else:
                    print ("\n*Sorry you pressed a wrong key try again*\n")
                    time.sleep(1)
            else:
                print ("\n*Sorry you pressed a wrong key try again*\n")
                time.sleep(1)
        elif x == "V" or x == "v":
            dest = input("Choose the destination L(from langkawi) or P(from Penang): ")
            if dest == "L" or dest == "l":
                print('''
                 *************************************************************
                 * Ferry ID : ''',ferry,'''                     Date: ''',now.day,'''/''',now.month,'''/''',now.year,''' *
                 *************************************************************
                 *                     BUSINESS CLASS                        *
                 *************************************************************
                 *    ''',vipl[0],'''     *   ''',vipl[1],'''     *   ''',vipl[2],'''     *   ''',vipl[3],'''     *   ''',vipl[4],'''    *
                 *************************************************************
                 *    ''',vipl[5],'''     *   ''',vipl[6],'''     *   ''',vipl[7],'''     *   ''',vipl[8],'''     *   ''',vipl[9],'''    *
                 *************************************************************
                 *                      ECONOMY CLASS                        *
                 *************************************************************
                 *    ''',ecol[0],'''     *   ''',ecol[1],'''     *   ''',ecol[2],'''     *   ''',ecol[3],'''     *   ''',ecol[4],'''    *
                 *************************************************************
                 *    ''',ecol[5],'''     *   ''',ecol[6],'''     *   ''',ecol[7],'''     *   ''',ecol[8],'''     *   ''',ecol[9],'''    *
                 *************************************************************
                 *    ''',ecol[10],'''     *   ''',ecol[11],'''     *   ''',ecol[12],'''     *   ''',ecol[13],'''     *   ''',ecol[14],'''    *
                 *************************************************************
                 *    ''',ecol[15],'''     *   ''',ecol[16],'''     *   ''',ecol[17],'''     *   ''',ecol[18],'''     *   ''',ecol[19],'''    *
                 *************************************************************
                 *    ''',ecol[20],'''     *   ''',ecol[21],'''     *   ''',ecol[22],'''     *   ''',ecol[23],'''     *   ''',ecol[24],'''    *
                 *************************************************************
                 *    ''',ecol[25],'''     *   ''',ecol[26],'''     *   ''',ecol[27],'''     *   ''',ecol[28],'''     *   ''',ecol[29],'''    *
                 *************************************************************
                 *    ''',ecol[30],'''     *   ''',ecol[31],'''     *   ''',ecol[32],'''     *   ''',ecol[33],'''     *   ''',ecol[34],'''    *
                 *************************************************************
                 *    ''',ecol[35],'''     *   ''',ecol[36],'''     *   ''',ecol[37],'''     *   ''',ecol[38],'''     *   ''',ecol[39],'''    *
                 *************************************************************''')
                foo = open("Seat Langkawi.txt", "a+")
                foo.write("%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s \n" % (('''
                 *************************************************************
                 * Ferry ID : '''),(ferry),('''                     Date: '''),(now.day),('''/'''),(now.month),('''/'''),(now.year),(''' *
                 *************************************************************
                 *                     BUSINESS CLASS                        *
                 *************************************************************
                 *    '''),(vipl[0]),('''     *   '''),(vipl[1]),('''     *   '''),(vipl[2]),('''     *   '''),(vipl[3]),('''     *   '''),(vipl[4]),('''    *
                 *************************************************************
                 *    '''),(vipl[5]),('''     *   '''),(vipl[6]),('''     *   '''),(vipl[7]),('''     *   '''),(vipl[8]),('''     *   '''),(vipl[9]),('''    *
                 *************************************************************
                 *                      ECONOMY CLASS                        *
                 *************************************************************
                 *    '''),(ecol[0]),('''     *   '''),(ecol[1]),('''     *   '''),(ecol[2]),('''     *   '''),(ecol[3]),('''     *   '''),(ecol[4]),('''    *
                 *************************************************************
                 *    '''),(ecol[5]),('''     *   '''),(ecol[6]),('''     *   '''),(ecol[7]),('''     *   '''),(ecol[8]),('''     *   '''),(ecol[9]),('''    *
                 *************************************************************
                 *    '''),(ecol[10]),('''     *   '''),(ecol[11]),('''     *   '''),(ecol[12]),('''     *   '''),(ecol[13]),('''     *   '''),(ecol[14]),('''    *
                 *************************************************************
                 *    '''),(ecol[15]),('''     *   '''),(ecol[16]),('''     *   '''),(ecol[17]),('''     *   '''),(ecol[18]),('''     *   '''),(ecol[19]),('''    *
                 *************************************************************
                 *    '''),(ecol[20]),('''     *   '''),(ecol[21]),('''     *   '''),(ecol[22]),('''     *   '''),(ecol[23]),('''     *   '''),(ecol[24]),('''    *
                 *************************************************************
                 *    '''),(ecol[25]),('''     *   '''),(ecol[26]),('''     *   '''),(ecol[27]),('''     *   '''),(ecol[28]),('''     *   '''),(ecol[29]),('''    *
                 *************************************************************
                 *    '''),(ecol[30]),('''     *   '''),(ecol[31]),('''     *   '''),(ecol[32]),('''     *   '''),(ecol[33]),('''     *   '''),(ecol[34]),('''    *
                 *************************************************************
                 *    '''),(ecol[35]),('''     *   '''),(ecol[36]),('''     *   '''),(ecol[37]),('''     *   '''),(ecol[38]),('''     *   '''),(ecol[39]),('''    *
                 *************************************************************''')))
                foo.close()
                time.sleep(1)
            elif dest == "P" or dest == "p":
                print('''
                 *************************************************************
                 * Ferry ID : ''',ferry,'''                     Date: ''',now.day,'''/''',now.month,'''/''',now.year,''' *
                 *************************************************************
                 *                     BUSINESS CLASS                        *
                 *************************************************************
                 *    ''',vipp[0],'''     *   ''',vipp[1],'''     *   ''',vipp[2],'''     *   ''',vipp[3],'''     *   ''',vipp[4],'''    *
                 *************************************************************
                 *    ''',vipp[5],'''     *   ''',vipp[6],'''     *   ''',vipp[7],'''     *   ''',vipp[8],'''     *   ''',vipp[9],'''    *
                 *************************************************************
                 *                      ECONOMY CLASS                        *
                 *************************************************************
                 *    ''',ecop[0],'''     *   ''',ecop[1],'''     *   ''',ecop[2],'''     *   ''',ecop[3],'''     *   ''',ecop[4],'''    *
                 *************************************************************
                 *    ''',ecop[5],'''     *   ''',ecop[6],'''     *   ''',ecop[7],'''     *   ''',ecop[8],'''     *   ''',ecop[9],'''    *
                 *************************************************************
                 *    ''',ecop[10],'''     *   ''',ecop[11],'''     *   ''',ecop[12],'''     *   ''',ecop[13],'''     *   ''',ecop[14],'''    *
                 *************************************************************
                 *    ''',ecop[15],'''     *   ''',ecop[16],'''     *   ''',ecop[17],'''     *   ''',ecop[18],'''     *   ''',ecop[19],'''    *
                 *************************************************************
                 *    ''',ecop[20],'''     *   ''',ecop[21],'''     *   ''',ecop[22],'''     *   ''',ecop[23],'''     *   ''',ecop[24],'''    *
                 *************************************************************
                 *    ''',ecop[25],'''     *   ''',ecop[26],'''     *   ''',ecop[27],'''     *   ''',ecop[28],'''     *   ''',ecop[29],'''    *
                 *************************************************************
                 *    ''',ecop[30],'''     *   ''',ecop[31],'''     *   ''',ecop[32],'''     *   ''',ecop[33],'''     *   ''',ecop[34],'''    *
                 *************************************************************
                 *    ''',ecop[35],'''     *   ''',ecop[36],'''     *   ''',ecop[37],'''     *   ''',ecop[38],'''     *   ''',ecop[39],'''    *
                 *************************************************************''')
                foo = open("Seat Penang.txt", "a+")
                foo.write("%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s \n" % (('''
                 *************************************************************
                 * Ferry ID : '''),(ferry),('''                     Date: '''),(now.day),('''/'''),(now.month),('''/'''),(now.year),(''' *
                 *************************************************************
                 *                     BUSINESS CLASS                        *
                 *************************************************************
                 *    '''),(vipp[0]),('''     *   '''),(vipp[1]),('''     *   '''),(vipp[2]),('''     *   '''),(vipp[3]),('''     *   '''),(vipp[4]),('''    *
                 *************************************************************
                 *    '''),(vipp[5]),('''     *   '''),(vipp[6]),('''     *   '''),(vipp[7]),('''     *   '''),(vipp[8]),('''     *   '''),(vipp[9]),('''    *
                 *************************************************************
                 *                      ECONOMY CLASS                        *
                 *************************************************************
                 *    '''),(ecop[0]),('''     *   '''),(ecop[1]),('''     *   '''),(ecop[2]),('''     *   '''),(ecop[3]),('''     *   '''),(ecop[4]),('''    *
                 *************************************************************
                 *    '''),(ecop[5]),('''     *   '''),(ecop[6]),('''     *   '''),(ecop[7]),('''     *   '''),(ecop[8]),('''     *   '''),(ecop[9]),('''    *
                 *************************************************************
                 *    '''),(ecop[10]),('''     *   '''),(ecop[11]),('''     *   '''),(ecop[12]),('''     *   '''),(ecop[13]),('''     *   '''),(ecop[14]),('''    *
                 *************************************************************
                 *    '''),(ecop[15]),('''     *   '''),(ecop[16]),('''     *   '''),(ecop[17]),('''     *   '''),(ecop[18]),('''     *   '''),(ecop[19]),('''    *
                 *************************************************************
                 *    '''),(ecop[20]),('''     *   '''),(ecop[21]),('''     *   '''),(ecop[22]),('''     *   '''),(ecop[23]),('''     *   '''),(ecop[24]),('''    *
                 *************************************************************
                 *    '''),(ecop[25]),('''     *   '''),(ecop[26]),('''     *   '''),(ecop[27]),('''     *   '''),(ecop[28]),('''     *   '''),(ecop[29]),('''    *
                 *************************************************************
                 *    '''),(ecop[30]),('''     *   '''),(ecop[31]),('''     *   '''),(ecop[32]),('''     *   '''),(ecop[33]),('''     *   '''),(ecop[34]),('''    *
                 *************************************************************
                 *    '''),(ecop[35]),('''     *   '''),(ecop[36]),('''     *   '''),(ecop[37]),('''     *   '''),(ecop[38]),('''     *   '''),(ecop[39]),('''    *
                 *************************************************************''')))
                foo.close()
                time.sleep(1)
            else:
                print ("\n*Sorry you pressed a wrong key try again*\n")
                time.sleep(1)
        elif x == "Q" or x == "q":
            break
        else:
            print ("\n*Sorry you pressed a wrong key try again*\n")
            time.sleep(1)
while True:
    print ("\t***Welcome to the Ferry Ticketing System***\n\n***Please follow the instructions bellow and book yourself a seat!***")
    time.sleep (2)
    print ("\nDeparture time slots: \n10:00\n11:00\n12:00\n13:00\n14:00\n15:00\n16:00\n17:00")
    time.sleep(1)
    timeselect = input ("\nPlease enter a time slot e.g '10' or Q(to quit system): ")
    if timeselect == "Q" or timeselect == "q":
        break
    else:
        True
    while True:
        if timeselect == "10" or timeselect == "11" or timeselect == "12" or timeselect == "13" or timeselect == "14" or timeselect == "15" or timeselect == "16" or timeselect == "17":
            timeselect = int (timeselect)
            if timeselect == 10 and timeselect > now.hour:
                ferryid(time1[0],fid[0],megavipl[0],megavipp[0],megaecol[0],megaecop[0],vipkeepl2[0],vipkeepp2[0],ecokeepl2[0],ecokeepp2[0])
                break
            if timeselect == 11 and timeselect > now.hour:
                ferryid(time1[1],fid[1],megavipl[1],megavipp[1],megaecol[1],megaecop[1],vipkeepl2[1],vipkeepp2[1],ecokeepl2[1],ecokeepp2[1])
                break
            elif timeselect == 12 and timeselect > now.hour:
                ferryid(time1[2],fid[2],megavipl[2],megavipp[2],megaecol[2],megaecop[2],vipkeepl2[2],vipkeepp2[2],ecokeepl2[2],ecokeepp2[2])
                break
            elif timeselect == 13 and timeselect > now.hour:
                ferryid(time1[3],fid[3],megavipl[3],megavipp[3],megaecol[3],megaecop[3],vipkeepl2[3],vipkeepp2[3],ecokeepl2[3],ecokeepp2[3])
                break
            elif timeselect == 14 and timeselect > now.hour:
                ferryid(time1[4],fid[4],megavipl[4],megavipp[4],megaecol[4],megaecop[4],vipkeepl2[4],vipkeepp2[4],ecokeepl2[4],ecokeepp2[4])
                break
            elif timeselect == 15 and timeselect > now.hour:
                ferryid(time1[5],fid[5],megavipl[5],megavipp[5],megaecol[5],megaecop[5],vipkeepl2[5],vipkeepp2[5],ecokeepl2[5],ecokeepp2[5])
                break
            elif timeselect == 16 and timeselect > now.hour:
                ferryid(time1[6],fid[6],megavipl[6],megavipp[6],megaecol[6],megaecop[6],vipkeepl2[6],vipkeepp2[6],ecokeepl2[6],ecokeepp2[6])
                break
            elif timeselect == 17 and timeselect > now.hour:
                ferryid(time1[7],fid[7],megavipl[7],megavipp[7],megaecol[7],megaecop[7],vipkeepl2[7],vipkeepp2[7],ecokeepl2[7],ecokeepp2[7])
                break
            elif timeselect == 17 and timeselect < now.hour:
                print ("\n*Sorry the last ferry is gone, but please come tomorrow!*")
                time.sleep(1)
                break
            elif timeselect <= now.hour:
                print ("\n*Sorry the ferry is already gone please choose a different Departure time*\n")
                time.sleep(1)
                break
            else:
                print ("\n*Sorry you pressed a wrong key try again*\n")
                time.sleep(1)
                break
        else:
            print ("\n*Sorry you pressed a wrong key try again*\n")
            time.sleep(1)
            break
