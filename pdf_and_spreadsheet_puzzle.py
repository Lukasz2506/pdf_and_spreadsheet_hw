# Task 1: Use Python to extract the Google Drive link from the .csv file.
# (Hint: Its along the diagonal from top left to bottom right).
import csv

f = open('files\\find_the_link.csv', encoding='utf-8')
csv_file = csv.reader(f)
# print(csv_file)


google_link = ''
n = 0
for lists in list(csv_file):
    # print(lists)
    for line in lists:
        list_line = line.split(',')
        # print(list_line)
        # print('\n')
        google_link += list_line[n]
        n += 1
print(google_link)




# Task2: Download the PDF from the Google Drive link
# (we already downloaded it for you just in case you can't download from Google Drive) and find the
# phone number that is in the document.
# Note: There are different ways of formatting a phone number!
import PyPDF2
import re


pdf = PyPDF2.PdfReader('Find_the_Phone_Number.pdf')
num_pages = len(pdf.pages)
pattern = r'\d{3}'
all_text = ''
for page in range(num_pages):
    # print(pdf.pages[page].extract_text())
    text = pdf.pages[page].extract_text()
    # print('\n')
    all_text += text

print(all_text)

for match in re.finditer(pattern, all_text):
    print(match)

phone = all_text[42905:42908] + '-' + all_text[42909:42912] + '-' + all_text[42913:42917]
print(f'phone: {phone}')