try:
    import pandas as pd
except ImportError:
    print('Pandas Library is not Installed in your system !! Please Install pandas first and try again')
def ball():
    delivery=pd.read_csv('deliveries.csv')
    x=delivery['bowler'].value_counts()>200
    y=x[x].index.tolist()
    mask=delivery['bowler'].isin(y)
    new_delivery=delivery[mask]
    mask=new_delivery['over']>15
    mew_delivery=new_delivery[mask]
    out=['hit wicket', 'caught and bowled', 'caught', 'lbw', 'stumped', 'bowled']
    print('''Choose according to what you want to select best Bowler:
            1)Best Bowler according to the Wicket Taker
            2)Best Bowler according to the Best Economy''')
    inp=int(input("Enter Your Choice:"))
    if(inp==1):
        mew_delivery=mew_delivery[mew_delivery['dismissal_kind'].isin(out)]
        a=mew_delivery.groupby('bowler')['dismissal_kind'].count()
        b=mew_delivery.groupby('bowler')['ball'].count()/6
        c=a/b
        print(c.sort_values(ascending=False).head())
    elif(inp==2):
        a=mew_delivery.groupby('bowler')['total_runs'].sum()
        b=mew_delivery.groupby('bowler')['ball'].count()/6
        c=a/b
        print(c.sort_values().head())
    else:
        print("Please Enter Correct Input")
