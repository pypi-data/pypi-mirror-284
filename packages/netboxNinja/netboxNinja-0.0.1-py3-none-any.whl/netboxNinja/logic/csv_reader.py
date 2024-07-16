import csv


class CSVReader:
    @staticmethod
    def read_csv_as_dict(file_path):
        data: list = []
        try:
            with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
                csv_reader = csv.DictReader(csvfile)
                for row in csv_reader:
                    data.append(dict(row))
        except FileNotFoundError:
            print(f"Error: The file {file_path} was not found.")
        except PermissionError:
            print(f"Error: Permission denied to read the file {file_path}.")
        except csv.Error as e:
            print(f"Error: An error occurred while reading the CSV file {file_path}: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        return data

    @staticmethod
    def read_csv_as_dict_with_semicolon(file_path):
        data: list = []
        try:
            with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
                csv_reader = csv.reader(csvfile, delimiter=';')
                headers = next(csv_reader)
                for row in csv_reader:
                    data.append({headers[i]: row[i] for i in range(len(headers))})
        except FileNotFoundError:
            print(f"Error: The file {file_path} was not found.")
        except PermissionError:
            print(f"Error: Permission denied to read the file {file_path}.")
        except csv.Error as e:
            print(f"Error: An error occurred while reading the CSV file {file_path}: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        return data
