# Online-Store
Python Program for Online Store

Program consists of two python scripts:

 - purchaseFinder.py
   Used to Search and Display all the previous purchases done by the user with the timestamp and the cost of purchase.

 - compute-order.py
   Used to implement an Online Shopping Cart for a user. Provides an interface for the user to place order and view the placed order.  

All the data is stored and retrieved from CSV files. CSV files used here are:
 
 - stock_data.csv 
   Stores the list of items along with their cost price and stock units available. 

 - purchase_data.csv
   Store the purchase data of the users. Purchase data includes username, user's order, date of purchase and total cost of purchase.

purchaseFinder.py is a command line utility tool.

 It accepts username and date of purchase as an optional parameter.
 Example: 
    python purchaseFinder.py -us <username> -dop <dd/mm/yyyy>

 Sample: 
 To display all the purchases made by a user.

    python purchaseFinder.py -us <username>

 To display purchases made by user on a particular day.
  
    python purchaseFinder.py -us <username> -dop <dd/mm/yyyy>

