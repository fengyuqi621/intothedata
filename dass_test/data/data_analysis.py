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

def geolocation(df):
    pd.set_option("display.max_rows", None, "display.max_columns", None)
    country_sl = df.groupby("country")["DScore", "AScore", "SScore"].mean()
    country_sl['Count'] = df.groupby("country").size()

    country_sl_sort = country_sl.sort_values(by= ['Count','DScore'], ascending=False)
    print(country_sl_sort)
    

def education(df):
    education_l = df.groupby("education")["DScore", "AScore", "SScore"].mean()
    education_l['Count'] = df.groupby("education").size()

    edl_sort = education_l.sort_values(by= ['Count','DScore'], ascending=False)
    print(edl_sort)

def religion(df): 
    relig_l = df.groupby("religion")["DScore", "AScore", "SScore"].mean()
    relig_l['Count'] = df.groupby("religion").size()

    relig_sort = relig_l.sort_values(by= ['Count','DScore'], ascending=False)
    print(relig_sort)

def hand(df):
    hand_l = df.groupby("hand")["DScore", "AScore", "SScore"].mean()
    print(hand_l)
    hand_l['Count'] = df.groupby('hand').size() 
    hand_sort = hand_l.sort_values(by= ['Count','DScore'], ascending=False)
    print(hand_sort)

def main():
    df = pd.read_csv('dass_test/data/cleaned_data.csv')
    
    geolocation(df)
    education(df)
    religion(df)
    hand(df)


if __name__ == '__main__':
    main()