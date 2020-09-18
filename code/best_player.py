import pandas as pd
import best_batsman
import best_bowler
import best_fielder
delivery=pd.read_csv('deliveries.csv')
while(1):
    print('''Choose what you want to know:
            1)Best Batsman
            2)Best Bowler
            3)Best Fielder
            4)Exit''')
    inp=int(input("Enter Choice:"))
    if(inp==1):
          best_batsman.bat()
    elif(inp==2):
          best_bowler.ball()
    elif(inp==3):
          best_fielder.field()
    elif(inp==4):
          exit()
    else:
          print('Please Enter Correct Input')
