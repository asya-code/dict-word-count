print("Day 1") # day of delivery
day_log = open("um-deliveries-day-1.txt")
for line in day_log:
    # fetch the data line by line
    line = line.rstrip() # get rid of whitespaces on the right end
    words = line.split('|') # separate the line by name of the product, count and amount
    print(words)
    melon = words[0]
    count = words[1]
    amount = words[2]

    #print(f"Delivered {count} {melon}s for total of ${amount}")
day_log.close()


print("Day 2")
day_log = open("um-deliveries-day-2.txt")
for line in day_log:
    line = line.rstrip()
    words = line.split('|')

    melon = words[0]
    count = words[0]
    amount = words[0]

    print(f"Delivered {count} {melon}s for total of ${amount}")
day_log.close()


print("Day 3")
day_log = open("um-deliveries-day-3.txt")
for line in the_file:
    line = line.rstrip()
    words = line.split('|')

    melon = words[0]
    count = words[0]
    amount = words[0]

    print(f"Delivered {count} {melon}s for total of ${amount}")
the_file.close()
