# functions uses 2 arguments: the report file and day needed
def sales_reports(log_file, report_day):
    full_report = open(log_file)
    # fetch the data line by line
    for line in full_report:
        line = line.rstrip() # get rid of whitespaces on the right end
        day = line[0:3] # identify the day on the line
        if day == report_day: # choose only needed one, specified in function call
            print(line)

# call sales_reports() with log file and day needed
print(sales_reports("um-server-01.txt", "Wed"))
