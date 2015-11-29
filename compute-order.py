#!/bin/bash/env python

import csv
from datetime import datetime 

shopList = []
prices = {} 
stock  = {}

with open ('stock_data.csv','r') as file:
   reader = csv.DictReader(file)
   prices = {row["item"]:row["cost_price"] for row in reader}

with open ('stock_data.csv','r') as file:
   reader = csv.DictReader(file)
   stock = {row["item"]:row["stock"] for row in reader}


def display_stock():
   '''  
      Display stock available in inventory.  

   '''
   print "\n Welcome to Online Store"
   print "\nStock Available"
   print "\nItems  Cost"
   print "-------------"
   for key in stock:
      print key,"\t", prices[key]

def compute_bill(food):
    '''
       Compute Bill and update inventory data.
    
    '''
    total = 0
    for item in food:
        if stock[item] > 0 :
           total += int(prices[item])
           stock[item] = int(stock[item])-1
    return total

def update_data():
   '''
      Export Purchase Data to CSV. 
  
   '''
   purchase_Data = {}
   purchase_Data['user'] = raw_input('Enter your Name: ')
   purchase_Data['item'] = shopList
   now = datetime.now()
   purchase_Data['date_of_purchase'] = '%s/%s/%s' % (now.day, now.month, now.year)
   purchase_Data['cost_of_purchase'] = compute_bill(shopList)

   with open('purchase_Data.csv', 'ab') as file:
       writer = csv.DictWriter(file,purchase_Data.keys())
       writer.writerow(purchase_Data) 

def fill_cart():
   '''
      Get Items into Shopping-Cart. Press Enter to stop filling Cart.   
   
   '''      
   display_stock()
   
   i = 0
   while 1:
      i += 1 
      item = raw_input("Enter your Item to the List (Press enter to stop): ")
      if item not in stock and item !='':
         print "Item not in Stock"
         item = raw_input("Enter your Item to the List (Press enter to stop): ")
      if item=='':
         break
      shopList.append(item)
   #print shopList 
   update_data()

def display_order():
    '''
        Display user order.
    
    '''
    print "\nThank you for placing order. Your Order Details are:"
    print "Items Cost"
    print "----------"
    for item in shopList:
       print item,"\t", prices[item]
    
    bill_cost = compute_bill(shopList)
    print "Total Bill Cost: ", bill_cost


fill_cart()
display_order()
