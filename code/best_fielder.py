try:
    import pandas as pd
except ImportError:
    print('Pandas Library is not Installed in your system !! Please Install pandas first and try again')
def field():
    delivery=pd.read_csv('deliveries.csv')
    print('''Choose according to what you want to select best Fielder:
            1)Best Fielder according to the Catches per Match
            2)Best Fielder according to the Catches per Over''')
    inp=int(input("Enter Your Choice:"))
    if(inp==1):
        a=delivery.groupby('fielder')['fielder'].count()
        b=delivery.groupby('fielder')['match_id'].nunique()
        c=a/b
        print(c.sort_values(ascending=False).head(5))
    elif(inp==2):
        a=delivery.groupby('fielder')['fielder'].count()
        b=delivery.groupby('fielder')['ball'].count()/6
        c=a/b
        print(c.sort_values(ascending=False).head(5))
    else:
        print("Please Enter Correct Input")

