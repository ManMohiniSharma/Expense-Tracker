import pandas as pd              # import panda library
import matplotlib.pyplot as plt  # import metplotlib for data visualization

# loading of data

df=pd.read_csv("expenses.csv", parse_dates=["date"])
print(df.head())
print("="*40)
print("\n")
while True:
   print("1. Add Expense")
   print("2. View Summary")
   print("3. Category Analysis")
   print("4. Show Graphs")
   print("5.Filter by Month")
   print("6. Exit")
   choice = input("Enter your Choice:")
   if choice == "6":
      print ("Exiting program...")
      break
   
   elif(choice=="5"):
      df["date"] = pd.to_datetime(df["date"], format="mixed")
      month = int(input("Enter month (1-12):"))
      filtered_df=df[df["date"].dt.month==month]
      if filtered_df.empty:
         print("No data for this month.")
      else:
         total = filtered_df["amount"].sum()
         print("\nTotal Expense for Month:", total)
         print("\nData:\n",filtered_df)
     
   elif choice == "1":
      while True:
        try: 
            date = pd.to_datetime (input ("Enter date (YYYY-MM-DD) : ").strip())
            break
        except:
            print("Invalid date format!")
        
   
      category =input("Enter category: ").strip().capitalize()
  
    # Amount input with retry
  
      while True:
        try:
            amount =float(input("Enter amount: "))
            break
        except ValueError:
            print("Invalid amount! ")
        
    # Create new entry

      new_data =pd.DataFrame([[date,category,amount]],columns =["date","category","amount"])
 
    # Append data

      df=pd.concat([df,new_data],ignore_index=True)
 
    # Save

      df.to_csv("expenses.csv",index=False)
      print("Expense added successfully!")
      df=pd.read_csv("expenses.csv",parse_dates=["date"])
      
   elif choice =="2": 
       
       
       
       total_expense=df["amount"].sum()
       mean_expense=df["amount"].mean()

       print("\nTotal Expense:", total_expense)
       print("Average Expense:", mean_expense)
   elif choice=="3":
      
      category_total = df.groupby("category")["amount"].sum()
      print("\n Expenses by Category:\n",category_total)
      
      print("\nHighest Spending Category:", category_total.idxmax())
      print("\nLowest Spending Category:", category_total.idxmin())
      
      category_count = df["category"].value_counts()
      print("\n Category Frequency:\n",category_count)
   
   elif choice=="4":
      
      category_total = df.groupby("category")["amount"].sum()
      daily_total=df.groupby("date")["amount"].sum()
      
      # Bar Chart
      plt.figure(figsize=(8,5))
      plt.bar(category_total.index , category_total.values)
      plt.xlabel("Category")
      plt.ylabel("Total Spending")
      plt.title("Category-wise Spending")
      plt.xticks(rotation=45)
      plt.tight_layout()
      plt.show()

      #Line Chart
      plt.figure(figsize=(8,5))
      plt.plot(daily_total.index,daily_total.values)
      plt.xlabel("Date")
      plt.ylabel("Total Spending")
      plt.title("Daily Spending Trend")
      plt.xticks(daily_total.index[::3],rotation=45)
      plt.tight_layout()
      plt.gcf().autofmt_xdate()
      plt.show()