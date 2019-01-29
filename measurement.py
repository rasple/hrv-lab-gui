
# switch all devices on

class Measurement():

    def on():
        time= datetime.datetime.now().isoformat() #current time
        print('on')
        urlget.get
        print (time)
        
    # switch all devices off

    def off():
        time= datetime.datetime.now().isoformat() #current time
        print('off')
        check_output('curl <192.168.0.15>:<31415>/?action=<off> HTTP/1.1')
        print (time)

    def mess():
        f=open('messungerst.txt', 'a')
        prewaitingtime= 60*0.25 #3 minutes waiting at the start of the measurement
        postwaitingtime= 60*0.25 #atleast 3 minutes waiting after 
        totaltime= 60* 1 # 15 minutes total time
        tut= 60* 0.25 # 5 minutes with 
        maxtimeshift=totaltime-prewaitingtime-postwaitingtime-tut
        start=random.randint(0,maxtimeshift)+prewaitingtime
        stop=start+tut
        print(start)
        #switch all the devices off
        time= datetime.datetime.now() #current time
        print (time)
        t = Timer(start, on)
        t.start()
        t2= Timer(stop, off)
        t2.start()
        t3= Timer(totaltime, end)
        t3.start()
        f.write('\nNeue Messung Beginn: ')
        f.write(time.isoformat())
        timestart= time + datetime.timedelta(seconds=start)
        timestop= time + datetime.timedelta(seconds=stop)
        timeend= time+datetime.timedelta(seconds=totaltime)
        f.write("\nStart: ")
        f.write(timestart.isoformat())
        f.write("\nStop: ")
        f.write(timestop.isoformat())
        f.write("\nEnd: ")
        f.write(timeend.isoformat())
        f.close()

    time2=datetime.datetime.now()
    time3=time2+ datetime.timedelta(seconds=24)
    print(time2)
    print(time3)
    f=open('test1.txt', 'w')
    f.write('Neue Messung Beginn: ')
    f.write(time2.isoformat())
    f.write("\nStart: ")
    f.write(time3.isoformat())
    f.close()