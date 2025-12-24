import pandas as pd
import sys
import os

def convert_file(file_path, sheet=None):
    # get the name & extension of the file
    file_name , extension = os.path.splitext(file_path)

    # lowecase the extesion
    extention = extension.lower()

    if extension == ".xlsx":
        # read the excel file
        df = pd.read_excel(file_path, sheet_name=sheet)
        #  prepare the result file name
        result_file = file_name + ".csv"
        # convert to csv
        df.to_csv(result_file, index=False)

        print(f"Successfully created : {result_file}")
    elif extension == ".csv":
        # read csv file
        df = pd.read_csv(file_path)
        #  prepare the result file name
        result_file = file_name + ".xlsx"
        # convert to excel
        df.to_excel(result_file, index=False)

        print(f"Successfully created : {result_file}")
    else:
        print("Unsupported file format. Please provide a .xlsx or .csv file.")
        exit(1)

if __name__ == "__main__":
    if len(sys.argv) >1:
        convert_file(sys.argv[1], sys.argv[2])
    else:
        print("No file path provided.")
        exit(1)
