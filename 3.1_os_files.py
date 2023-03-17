from http.client import parse_headers
import os
import urllib.request
 
#print(os.getcwd(), " is the current working directory")

#print(os.listdir('.'))  # it should return the contents of the directory, argument can also be a path

#os.makedirs('data', exist_ok=True)

url1 = 'https://hub.jovian.ml/wp-content/uploads/2020/08/loans1.txt'

#urllib.request.urlretrieve(url1, 'data/loans1.txt') # ---> it times out for some reason, I think its the link


# to open files manually
file1 = open('data/loans1.txt', mode='r')

file_contents = file1.read()

#print(file_contents)

file1.close()

# to do it automatically

with open('data/loans1.txt', 'r') as file2:
    file2_contents = file2.read()
    print(file2_contents)
    # no need to after that close it, as it happens automatically
    # to also do it line by line
    # file2_contents = file2.readlines()



# the following code will do these things
# 1. will take the loans file and will take the headers ; 2. after that for each record there will be a separate dictionary 
# where they headers will be the keys and values will be the actual values ; 3. file will be written to a new file in the new format

def parse_header(header_line):
    return header_line.strip().split(',')


def parse_values(data_line):
    values = []
    for item in data_line.strip().split(','):
        if item == '':
            values.append(0.0)
        else:
            values.append(float(item))
    return values


def create_item_dict(values, headers):
    result = {}
    for value, header in zip(values, headers):
        result[header] = value
    return result


def read_csv(path):
    result = []

    with open(path, 'r') as f:
        lines = f.readlines()

        headers = parse_header(lines[0])

        for data_line in lines[1:]:
            values = parse_values(data_line)

            item_dict = create_item_dict(values, headers)

            result.append(item_dict)

    return result

# and with those functions, having the file that is in the necessary format, by invoking the read_csv('data/loans1.txt) we have the 
# file that is the same but in the form of dictionaries, where the keys are the headers from the first file

# and then he refers back to the function that calculates the emi for loans and using that he adds another key:value pair by 
# calculating the emi for each loan in the record

# def compute_emis(loans):
# for loan in loans:
#     loan['emi'] = loan_emi(loan['amount'], loan['duration'], loan['rate'] / 12, loan['down_payment'])

# via this for loop, the loan_emi function calculates the emi and then the loan['emi'] attribute gets added for each record with 
# the corresponding values 

# and then to write to a file:

# with open('data/emis.txt', 'w') as f:
#     for loan in loans2:
#         f.write("{},{},{},{},{}\n".format(
#             loan['amount'],
#             loan['duration'],
#             loan['rate'],
#             loan['down_payment'],
#             loan['emi']))


# and then, ofcourse, he shows a function that does the same thing + something additional

def write_csv(items, path):
    with open(path, 'w') as f:
        if len(items) == 0:
            return
        headers = list(items[0].keys())
        f.write(','.join(headers) + '\n')

        for item in items:
            values = []
            for header in headers:
                values.append(str(item.get(header, "")))
            f.write(','.join(values) + '\n')

# this function writes to a file in csv-format

# and to then apply the functions to all the supposedly existing files with loans information:

# for i in range(1,4):
#     loans = read_csv(f'data/loans{i}.txt')
#     compute_emis(loans)
#     write_csv(loans, f"data/emis{i}.txt")

# and this is all for this lesson, onto number 4























































































