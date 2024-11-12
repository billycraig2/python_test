def highest_savings(data):
    highest_saving = 0
    highest_savers = []
    for person, details in data.items():
        salary = details['salary']
        expenditure = details['expenditure']
        savings = salary - (expenditure['rent'] + expenditure['medical'])

        if (savings > highest_saving):
            highest_saving = savings
            highest_savers = [person]
        elif savings == highest_saving:
            highest_savers.append(person)

    return highest_savers, highest_saving

data = {
    "sandy":{
        "salary":50000,
        "expenditure":{"rent":1000,"medical":4000}
        },
    "dheeraj":{
        "salary":500001,
        "expenditure":{"rent":6000,"medical":4000}
        },
    "Pratik":{
        "salary":500001,
        "expenditure":{"rent":6000,"medical":4000}
        }
        }

highest_savers, highest_saving = highest_savings(data)
print(str(highest_savers) + " has the most savings with " + str(highest_saving) + " saved")