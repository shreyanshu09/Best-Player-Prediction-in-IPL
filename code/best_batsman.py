try:
    import pandas as pd
except ImportError:
    print('Pandas Library is not Installed in your system !! Please Install pandas first and try again')
def bat():
    delivery=pd.read_csv('deliveries.csv')
    delivery['batsman'].nunique() 
    x=delivery['batsman'].value_counts()>200 
    y=x[x].index.tolist()
    mask=delivery['batsman'].isin(y) 
    new_delivery=delivery[mask]
    mask=new_delivery['over']>15
    mew_delivery=new_delivery[mask]
    print(''' Choose according to what you want to select best batsman:
            1)Best Batsman according to the Best Strike Rate
            2)Best Batsman according to the Best Average Runs
            3)Best Batsman according to the Longest Survival ''')
    inp=int(input("Enter Your Choice:"))
    if(inp==1):
        q=mew_delivery.groupby('batsman')['batsman_runs'].sum()
        w=mew_delivery.groupby('batsman')['batsman_runs'].count()/6
        e=q/w
        print(e.sort_values(ascending=False).head(5))
    elif(inp==2):
        q=mew_delivery.groupby('batsman')['batsman_runs'].sum()
        w=mew_delivery.groupby('batsman')['match_id'].nunique()
        e=q/w
        print(e.sort_values(ascending=False).head(5))
    elif(inp==3):
        q=mew_delivery.groupby('batsman')['batsman_runs'].count()/6
        w=mew_delivery.groupby('batsman')['match_id'].nunique()
        e=q/w
        print(e.sort_values(ascending=False).head(5))
    else:
        print("Please Enter Correct Input")
            
