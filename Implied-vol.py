def __init__(libor_euro,libor_usd,spot, future, months, strike, call_price, euro, usd,p):
        volatility = 1*(10**-p)
        while True: #loops forever, owch.
            c = investment_level(spot,future,usd,volatility)
            f = downside(call_price,c,usd,euro,future,spot,volatility)
            if (f <= 0): #finds when downside is zero
                print (c,'Investment Level',f,'Downside')#prints solution
                #print ('The implied volatility would be: ',volatility)
                return volatility
                break #ends loop
            else:
                volatility = volatility+(1*(10**-p)) #adds volatility incrementally
volatility = 1*(10**-p)
def annual_to_month(months_to_expire, rate):
    a = (1+rate)**(months_to_expire/12)
    return a

def investment_level(spot,future,interest_us,volatility):
    d = (future/spot) #makes the next step a bit less messy
    b = ((spot*(d)+volatility)-spot)/((interest_us*((d)+volatility)-(d)-volatility))
    return b

def downside(price,investment_level,interest_us,interest_euro,future,spot,volatility):
    d = (future/spot)
    e = ((price-(investment_level))*interest_us)+(investment_level*(interest_euro*(d)-volatility))
    return e
