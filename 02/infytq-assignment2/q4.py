#lex_auth_012693782475948032141

def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
    bill_amount=0
    dc=0
    #write your logic here
    if distance_in_kms <= 3:
        dc=0
    elif 3 < distance_in_kms <=6:
        dc=(distance_in_kms-3)*3
    else:
        dc=3*3 + (distance_in_kms-6)*6
        
    if(food_type == "V" or food_type == "N") and quantity_ordered > 0 and distance_in_kms > 0:
        if food_type == "V":
            bill_amount = 120 * quantity_ordered + dc
        else:
            bill_amount = 150 * quantity_ordered + dc
    else:
        bill_amount = -1
        
    return bill_amount

#Provide different values for food_type,quantity_ordered,distance_in_kms and test your program
bill_amount=calculate_bill_amount("N",2,7)
print(bill_amount)