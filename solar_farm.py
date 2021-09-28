'''
Ruairidh McNeil
CS 021
Assignment 4: Solar Farm
9/23/2021
'''

COST_PER_KILOWATT_HOUR = 0.19
running_total = 0

week_number = 0
restart = 'y'

while restart == 'y':
    panels_280w = int(input('Enter the number of 280 watt solar panels:'))
    panels_320w = int(input('Enter the number of 320 watt solar panels:'))
    hours_sunlight = float(input('Enter the number of hours of sunlight the panels receive per day:'))
    weeks = int(input('Enter the number of weeks to calculate the total power output:'))
    for n in range(weeks):
        while hours_sunlight < 0 or hours_sunlight > 24:
            print('Invalid input.')
            hours_sunlight = float(input('Enter the number of hours of sunlight the panels receive per day:'))
        while weeks <= 0:
            print('Invalid input.')
            weeks = int(input('Enter the number of weeks to calculate the total power output:'))

        KWHPD = ((panels_280w*280+panels_320w*320)*hours_sunlight)/1000
        week_number = week_number + 1
        running_total = running_total + KWHPD*7
        print(running_total)

    profit = running_total * COST_PER_KILOWATT_HOUR
    print(f"Total profit over {weeks} weeks: ${profit:,.2f}")
    print(f"${running_total:,.2f}")
    restart = print(input('Would you like to run another scenario? (y/n'))