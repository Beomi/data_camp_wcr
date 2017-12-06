# https://docs.python.org/3/library/csv.html#csv.DictWriter

import csv

with open('names.csv', 'w', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name']
    csvfile.write('\ufeff')
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'first_name': '내이름은', 'last_name': 'Beans'})
    writer.writerow({'first_name': '댕댕이에요.', 'last_name': 'Spam'})
    writer.writerow({'first_name': '냥냥', 'last_name': 'Spam'})