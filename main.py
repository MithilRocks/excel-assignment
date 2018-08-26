import xlrd


def main():
    excel_file = xlrd.open_workbook('TechnicalAnalystTest.xls')
    
    # traverse over each tab in the excel
    for tab_name in excel_file.sheet_names():
        tab_file = tab_name + ".csv"

        # create a file for every tab in the excel
        fp = open(tab_file, "w")

        sheet = excel_file.sheet_by_name(tab_name)
        rows = sheet.nrows

        for i in range(0, rows):

            if i == 0:
                # for the first row which contains field names
                line = ",".join([ str(x) for x in sheet.row_values(i) ]) + ",Client"
            else:
                # other rows that contain data
                line = "Test," * (len(sheet.row_values(i)) + 1)

            fp.write(line + "\n")

        fp.close()

    
    
if __name__ == "__main__":
    main()