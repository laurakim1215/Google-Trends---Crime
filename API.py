from pytrends.request import TrendReq
import pandas as pd
import time

#pd.set_option("max_r",108)


#include your google credentials
google_username1 = "lktao@g.gmail.com"
google_password1 = "kw^NGh3ee"
google_username2 = "laura.k.tao@g.gmail.com"
google_password2 = "IL0veC^ts"
google_username3 = "laura.gtrends"
google_password3 = "gtrendssuck"


path = "states_take2"





crimeKeyWords = ['guns,attacks, rape, homicide,crime',
            'guns, jail, theft, violence, hate',
            'guns, police, murder, killings, assault',
            'guns, fraud, felony, break in, abuse']


stateList1 = ["US-AL","US-AK","US-AZ","US-AR","US-CA",
            "US-CO","US-CT","US-DE","US-FL","US-GA",
            "US-HI","US-ID","US-IL"]
stateList = ["US-IL"]
stateList3 = ["US-IN","US-IA",
            "US-KS","US-KY","US-LA","US-ME","US-MD",
            "US-MA","US-MI","US-MN","US-MS","US-MO",
            "US-MT","US-NE","US-NV","US-NH","US-NJ",
            "US-NM","US-NY","US-NC","US-ND", "US-OH",
            "US-OK", "US-OR", "US-PA", "US-RI",
            "US-SC", "US-SD", "US-TN", "US-TX", "US-UT",
            "US-VT", "US-VA", "US-WA", "US-WV", "US-WI",
            "US-WY"
            ]

stateList2 = ["US-OK","US-OR","US-PA","US-RI",
             "US-SC","US-SD","US-TN","US-TX","US-UT",
             "US-VT","US-VA","US-WA","US-WV","US-WI",
             "US-WY"]


df = []
done = 0


def main():
    global stateList
    global df
    global done
    while (len(stateList) >0):
        state = stateList[0]
        print (state + " start")
        for i in range(len(crimeKeyWords)):
            ##adjust time frame as needed, this script using 108months inclusive starting from January 2007
            trend_payload = {'q': crimeKeyWords[i],'geo': state,'date': '1/2004 108m'}
            df.insert(-1,pytrend.trend(trend_payload, return_type='dataframe'))
            time.sleep(30)#i've had to wait 30 seconds between calls to prevent rate limit, sometimes failed, if failed, repeat function would wait 5 minutes


        c=0
        for i in df:
            #print(i)
            i.to_csv(path + state + str(c) +".csv",sep=",")
            c+=1


        print('starting concat')
        #add additional line to join additional dataframe sets of 5 keywords
        dfall = pd.concat([df[0],df[1]],axis=1,join_axes=[df[0].index])
        dfall = pd.concat([dfall,df[2]],axis=1,join_axes=[dfall.index])
        dfall = pd.concat([dfall,df[3]],axis=1,join_axes=[dfall.index])
        dfall = dfall.T.drop_duplicates().T
        print(dfall)

        dfall.to_csv(path + state + "_merged.csv",sep=",")
        print(state + " end")

        del df[:]
        print ("Done state: " + str(done))
        stateList.remove(state)
        for s in stateList:
            print (s)
    done = 1
    print ("Done state: " + str(done))

    
def repeat():
    while done == 0:
        print("start")
        while True:
            try:
                print ("try main")
                main()
                if done ==1: break
            except:
                print( "waiting")
                time.sleep(300)
                


# connect to Google
pytrend = TrendReq(google_username3, google_password3, custom_useragent='My Pytrends Script')

repeat()
