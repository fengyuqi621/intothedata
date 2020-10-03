import pandas as pd

# calculates the avg score of DScore, AScore, and SScore based on different gender
def gender_average(df):
    das_mean = df[["DScore", "AScore", "SScore"]].mean()
    male_list = df[df['gender'] == 1]
    female_list = df[df['gender'] == 2]
    other_gender = df[df['gender'] == 3]
    # calculate 
    das_mean_male = male_list[["DScore", "AScore", "SScore"]].mean()
    das_mean_female = female_list[["DScore", "AScore", "SScore"]].mean()
    das_mean_other = other_gender[["DScore", "AScore", "SScore"]].mean()

    print(das_mean_male)
    print(das_mean_female)
    print(das_mean_other)

def severity(df):
    # normal depression
    df[df["DScore"] < 10]
    print()


def main():
    df = pd.read_csv('dass_test/data/cleaned_data.csv')
    
    gender_average(df)
    


if __name__ == '__main__':
    main()