#!/usr/bin/env python

import csv 
import argparse


def display_info(): 

   ''' 
    Search data by passing the username as command line argument.
    Specify the purchase date as command line argument if data of only particular date is required.

   '''
   parser = argparse.ArgumentParser()

   parser.add_argument('-us', '--user', help="specify username")
   parser.add_argument('-dop', '--purchaseDate', help="specify the date of purchase. Date Format(dd/mm/yyyy)")

   try:
        args = parser.parse_args()


        with open('purchase_data.csv', 'rb') as file1 :

             reader1 = csv.DictReader(file1)
                         
             print"USER:", args.user, "\n"

             if args.purchaseDate :
                  print"Date of Purchase:", args.purchaseDate
      	          for row1 in reader1:
                      if args.user in row1['user'] and args.purchaseDate in row1['date_of_purchase']:
                           item = row1['item']
                           cost_of_purchase = row1['cost_of_purchase']
                           print "Item:", item
                           print "Cost of Purchase:", cost_of_purchase, "\n"
                           break   
             else:
                  for row1 in reader1:
                      if args.user in row1['user']:
                          item = row1['item']
                          cost_of_purchase = row1['cost_of_purchase']
                          date_of_purchase = row1['date_of_purchase'] 

                          print "Date of Purchase:" , date_of_purchase
                          print "Item:", item
                          print "Cost of Purchase:", cost_of_purchase, "\n"
                         
                                           
   except argparse.ArgumentError, exc:
       print exc.message

   except IOError:  
       print "Cannot open input files."

   except Exception, e:
       print ("Error: %s" %e)

display_info() 
