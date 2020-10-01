import pandas as pd


# Explanation for the parameters
# skiprows:  skip the number of rows at the start of the csv file. In this case, we want to skip the 1st row (the header)
#            since the headers aren't separated properly (it caused our data to be stored in 1 column). 
# engine: specify which engine we're using to parse the csv file. In this case, we're using python instead of c. 
# header: specify if the input csv contains a header (If so, which row). In this case, as we decide to skip the 1st row, 
#         we will need to set our header to None
# names: indicates all the column names we want to use 
# sep:  what delimiter separates the column.  in this case, we used the comma delimiter in our csv file
# more parameter info can be found here: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
# Yuqi
#file = pd.read_csv('/Users/fengyuqi/Desktop/intothedata/dass_test/data/dass_data.csv', sep=',', skiprows=1, header=None, engine='python', names=fields)

# Ian (use the following absolute path to read in the csv & comment the above line of code)


def drop_columns (df):
    # data cleaning
    # Step 1: Drop columns
    # Step 1.1: drop "engnat", "screensize", "uniquenetworklocation", "introelapse", "surveyelapse"
    cleaned_table = df.drop(columns=["engnat", "screensize", "uniquenetworklocation", "introelapse", "surveyelapse"])

    # Step 1.2: drop all the time and position columns
    for i in range(1, 43):
        positionColumn, timeColumn = "Q{i}I".format(i=i), "Q{i}E".format(i=i)
        cleaned_table = cleaned_table.drop(columns=[positionColumn, timeColumn])
    return cleaned_table

def drop_rows (df):
    # Step 2: Eliminate the rows that do not pass the validity check
    # Step 2.1: Select all the columns that contain the string "VCL"
    df['VCLT'] = df['VCL1'] + df['VCL2'] + df['VCL3'] + df['VCL4'] + df['VCL5'] + df['VCL6'] +df['VCL7'] + df['VCL8'] + df['VCL9'] + df['VCL10'] + df['VCL11'] + df['VCL12'] + df['VCL13'] + df['VCL14'] + df['VCL15'] + df['VCL16'] 
    df_filtered = df[df['VCLT'] >= 5]
    df = df_filtered.drop(df_filtered.filter(regex='VCL').columns, axis=1) 

    df['DScore'] = df['Q3A'] + df['Q24A'] + df['Q5A'] + df['Q26A'] + df['Q10A'] + df['Q31A'] + df['Q13A'] + df['Q34A'] + df['Q16A'] + df['Q17A'] + df['Q37A'] + df['Q38A'] + df['Q21A'] + df['Q42A'] - 14
    df['AScore'] = df['Q2A'] + df['Q23A'] + df['Q4A'] + df['Q25A'] + df['Q7A'] + df['Q28A'] + df['Q9A'] + df['Q30A'] + df['Q15A'] + df['Q36A'] + df['Q19A'] + df['Q40A'] + df['Q20A'] + df['Q41A'] - 14
    df['SScore'] = df['Q1A'] + df['Q22A'] + df['Q6A'] + df['Q27A'] + df['Q8A'] + df['Q29A'] + df['Q11A'] + df['Q32A'] + df['Q12A'] + df['Q33A'] + df['Q14A'] + df['Q35A'] + df['Q18A'] + df['Q39A'] - 14
    # score = df[df['DScore'] > 20]
    return df



def main():
    fields = ["Q1A","Q1I","Q1E","Q2A","Q2I","Q2E","Q3A","Q3I","Q3E","Q4A","Q4I","Q4E","Q5A","Q5I","Q5E","Q6A","Q6I","Q6E","Q7A","Q7I",
"Q7E","Q8A","Q8I","Q8E","Q9A","Q9I","Q9E","Q10A","Q10I","Q10E","Q11A","Q11I","Q11E","Q12A","Q12I","Q12E","Q13A","Q13I","Q13E","Q14A",
"Q14I","Q14E","Q15A","Q15I","Q15E","Q16A","Q16I","Q16E","Q17A","Q17I","Q17E","Q18A","Q18I","Q18E","Q19A","Q19I","Q19E","Q20A","Q20I",
"Q20E","Q21A","Q21I","Q21E","Q22A","Q22I","Q22E","Q23A","Q23I","Q23E","Q24A","Q24I","Q24E","Q25A","Q25I","Q25E","Q26A","Q26I","Q26E",
"Q27A","Q27I","Q27E","Q28A","Q28I","Q28E","Q29A","Q29I","Q29E","Q30A","Q30I","Q30E","Q31A","Q31I","Q31E","Q32A","Q32I","Q32E","Q33A",
"Q33I","Q33E","Q34A","Q34I","Q34E","Q35A","Q35I","Q35E","Q36A","Q36I","Q36E","Q37A","Q37I","Q37E","Q38A","Q38I","Q38E","Q39A","Q39I",
"Q39E","Q40A","Q40I","Q40E","Q41A","Q41I","Q41E","Q42A","Q42I","Q42E","country","source","introelapse","testelapse","surveyelapse",
"TIPI1","TIPI2","TIPI3","TIPI4","TIPI5","TIPI6","TIPI7","TIPI8","TIPI9","TIPI10","VCL1","VCL2","VCL3","VCL4","VCL5","VCL6","VCL7","VCL8",
"VCL9","VCL10","VCL11","VCL12","VCL13","VCL14","VCL15","VCL16","education","urban","gender","engnat","age","screensize",
"uniquenetworklocation","hand","religion","orientation","race","voted","married","familysize","major"]
    df = pd.read_csv('dass_test/data/dass_data.csv', sep=',', skiprows=1, header=None, engine='python', names=fields)

    cleaned_table = drop_columns(df)
   
    final = drop_rows(cleaned_table)
   
    print(final)
    final.to_csv('dass_test/data/cleaned_data.csv', index=False)

if __name__ == '__main__':
    main()