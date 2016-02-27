#!/usr/bin/env python

import sys
from datetime import datetime

def yearNumber(yy):
   num = 29
   year = 2014

   diff = yy - 2014

   adj = diff / 19
   num += (diff * 11) - int(adj)

   return num % 30

def goldenNumber(mm, yy):
   if mm > 2:
      return yearNumber(yy)
   else:
      return yearNumber(yy - 1)

def lunarMonth(mm):
   ml = mm - 2
   if ml < 1:
      ml += 12

   return ml

def lunarDay(dd, mm, yy):
   return (dd + lunarMonth(mm) + goldenNumber(mm, yy)) % 30

def main():
   if len(sys.argv) > 1:
      dateText = sys.argv[1]
   else:
      dateText = raw_input("Insert the date using DD/MM/YYYY format: ")

   date = datetime.today()
   try:
      date = datetime.strptime(dateText, '%d/%m/%Y')
   except ValueError:
      raise ValueError("Incorrect data format, date is not in DD/MM/YYYY or it is not a valid date")

   ld = lunarDay(date.day, date.month, date.year)
   print('The Lunar Day for the date you chose is %d' % ld)

if __name__ == '__main__':
   main()
