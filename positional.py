'''
def display_result(roll,name,marks):
    print ("roll number=", roll)
    print ("name=",name)
    print ("parcent=",sum(marks)/len(marks))

    display_result(roll=52,name="noman",marks=[85,75,65,69,89])
'''


def electricity_bill(consumers):
    bills = []
    for units in consumers.value():

        if units<=200:
            amount=100+units*3
        elif units>201 and units<=300:
            amount=700+(units-200)*4
        elif units>301 and (units <=400):
            amount=1100+(units-300)*5
        elif units>400 and units<=500:
            amount=1600+(units-400)*6
        else:
            amount=2200+(units-500)*7
        consumers.append(amount)
    return consumers
list_of_consumers={"noman":340,"nawaz":500,"sawez":450,"ahemad":150,"nazim":240}
bill_amount=electricity_bill(list_of_consumers)
print("calculate bill amount",bill_amount)
