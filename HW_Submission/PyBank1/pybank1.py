# modules
import csv

# set path
csvpath = "Resources/budget_data.csv"

# variable
month_count = 0
total_profit = 0

# to calculate changes
last_month_profit = 0

changes = []
month_changes = []

# open CSV using the uTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    #Read each row of data after the header
    for row in csvreader:
        print(row)

        # count months
        month_count = month_count + 1

        # add profit
        total_profit = total_profit + int(row[1])

        # last month profit
        # subtract this month profit from last month profit
        # Append to changes list

        # IF first row, there is no change
        if (month_count == 1):  #this is the first row, so no change
            last_month_profit = int(row[1])
        else:
            change = int(row[1]) - last_month_profit
            changes.append(change)
            month_changes.append(row[0])

            #reset last month profit
            last_month_profit = int(row[1])

    print(month_count)
    print(total_profit)
    print(len(changes))

    avg_change = sum(changes) / len(changes)
    print(avg_change)

    max_change = max(changes)
    max_month_indx = changes.index(max_change)
    max_month = month_changes[max_month_indx]

    print(max_change)
    print(max_month)

    min_change = min(changes)
    min_month_indx = changes.index(min_change)
    min_month = month_changes[min_month_indx]

    print(min_change)
    print(min_month)

    output = f"""Financial Analysis
-------------------------------
Total Months: {month_count}
Total: ${total_profit}
Average Change: ${round(avg_change,  2)}
Greatest Increase in Profits: {max_month} (${max_change})
Greatest Decrease in Profit: {min_month} (${min_change})"""

    print(output)

    with(open("output_sarkis.txt", 'w') as f):
        f.write(output)












