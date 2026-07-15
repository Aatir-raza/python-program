
# total food orderred for snacking
#electricity units spend 
# charge per unit
# person living in room/flat

# output
# total amount you've to pay is 

rent=int(input('enter your hostel/flat rent= '))
food=int(input('enter the amount of food ordered='))
electricity_spend=int(input('enter the total electicity spend ='))
charge_per_unit=int(input('enter the charge per unit ='))
persons=int(input('enter the number of persons living in room/flat='))

total_bill=electricity_spend*charge_per_unit
output=(food+rent+total_bill)//persons

print('each persons will pay =',output)# inputs we need from user
# total rent
