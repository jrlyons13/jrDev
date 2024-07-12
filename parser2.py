import re
import csv
import collections

def log_file_reader(filename):
    # Get all IP addresses from the log file
    with open(filename) as f:
        log = f.read()
        regex = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
        ip_list = re.findall(regex, log)
        return ip_list
    
    """ To Read the log file line by line
        log_file = open(filename, "r+")
        for row in log_file:
            print(row)
            regex = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
            ip_list = re.findall(regex, row)
            print()
            return ip_list
        pass
    """

# Get total count of IPs
def count_ip(ip_list):
    return collections.Counter(ip_list)

def write_to_csv(counter):
    with open('output.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        header = ['IP', 'Count']
        writer.writerow(header)
        sorted_ips = sorted(counter.items(), key=lambda x: x[1], reverse=True)
        for item in sorted_ips:
            writer.writerow((item[0], item[1]))

def print_sorted_ips(counter):
    sorted_ips = sorted(counter.items(), key=lambda x: x[1], reverse=True)
    for ip, count in sorted_ips:
        print(f"{ip}: {count}")

if __name__ == "__main__":
    ip_list = log_file_reader('log')
    ip_counter = count_ip(ip_list)
    write_to_csv(ip_counter)
    print_sorted_ips(ip_counter)
