import csv
csv.field_size_limit(10**9)


def process_rows_dict(merged_data, phone_reader, csv_writer):
    # Iterate over the rows in file_2
    for row in phone_reader:
        phone_id = row['id']
        if phone_id in merged_data:
            merged_data[phone_id]['phone'] = row['phone']

        for row in merged_data.values():
            csv_writer.writerow(row)
            # csv_writer.writerow(merged_data[phone_id])


with open('client.csv', 'r') as client_file, open('phone.csv', 'r') as phone_file, open('final.csv', 'w', newline='') as final_file:
    client_reader = csv.DictReader(client_file)
    phone_reader = csv.DictReader(phone_file)

    fieldnames = ['id', 'phone', 'name', 'email']
    csv_writer = csv.DictWriter(final_file, fieldnames=fieldnames)
    csv_writer.writeheader()

    merged_data = {}
    chunk_size = 10
    count = 0

    for i, row in enumerate(client_reader):
        client_id = row['id']
        merged_data[client_id] = {'id': client_id, 'name': row['name'], 'email': row['email']}
        count += 1

        if count % chunk_size == 0:
            process_rows_dict(merged_data, phone_reader, csv_writer)
            merged_data.clear()

    if merged_data:
        process_rows_dict(merged_data, phone_reader, csv_writer)
