import pandas as pd

# calculates the avg score of DScore, AScore, and SScore based on different gender
def gender_average(df):
    gender_avg = df.groupby("gender")["DScore", "AScore", "SScore"].mean()
    gender_avg['Count'] = df.groupby("gender").size()
    print(gender_avg)

def age_average(df):
    teen_list = df[(df['age'] <= 17) & (df['age'] >=12)]
    young_adult_list = df[(df['age'] <=25) & (df['age'] >=18)]
    adult_list = df[(df['age'] <= 64) & (df['age'] >= 26)]
    elderly_list = df[(df['age'] >=65) & (df['age'] < 100)]

    # calculate 
    teen_list_mean = teen_list[["DScore", "AScore", "SScore"]].mean()
    young_adult_list_mean = young_adult_list[["DScore", "AScore", "SScore"]].mean()
    adult_list_mean = adult_list[["DScore", "AScore", "SScore"]].mean()
    elderly_list_mean = elderly_list[["DScore", "AScore", "SScore"]].mean()
    
    print("Number of teen: " + str(teen_list.count()))
    print(teen_list_mean)
    print("Number of yount adult: " + str(young_adult_list.count()))
    print(young_adult_list_mean)
    print("Number of adult: " + str(adult_list.count()))
    print(adult_list_mean)
    print("Number of elderly: " + str(elderly_list.count()))
    print(elderly_list_mean)
 #   pd.set_option("display.max_rows", None, "display.max_columns", None)


def depression_severity(df):
    # normal depression
    normal_d = df[df["DScore"] < 10]
    # mild depression
    mild_d = df[(df["DScore"] <= 13) & (df["DScore"] >=10)]
    # moderate depression
    moderate_d = df[(df["DScore"] <= 20) & (df["DScore"] >=14)]
    # severe depression
    severe_d = df[(df["DScore"] <= 27) & (df["DScore"] >=21)]
    # extreme severe
    ex_severe_d = df[df["DScore"] >=28]
    print("Percentage of normal depression: " + str(normal_d.size / df.size * 100) + "%")
    print("Percentage of mild depression: " + str(mild_d.size / df.size * 100) + "%")
    print("Percentage of moderate depression: " + str(moderate_d.size / df.size * 100) + "%")
    print("Percentage of severe depression: " + str(severe_d.size / df.size * 100) + "%")
    print("Percentage of extreme severe depression: " + str(ex_severe_d.size / df.size * 100) + "%")

def anxiety_severity(df):
    # normal anxiety
    normal_a = df[df["AScore"] < 8]
    # mild anxiety
    mild_a = df[(df["AScore"] <= 9) & (df["AScore"] >=8)]
    # moderate anxiety
    moderate_a = df[(df["AScore"] <= 14) & (df["AScore"] >=10)]
    # severe anxiety
    severe_a = df[(df["AScore"] <= 19) & (df["AScore"] >=15)]
    # extreme severe anxiety
    ex_severe_a = df[df["AScore"] >=20]
    print("Percentage of normal anxiety: " + str(normal_a.size / df.size * 100) + "%")
    print("Percentage of mild anxiety: " + str(mild_a.size / df.size * 100) + "%")
    print("Percentage of moderate anxiety: " + str(moderate_a.size / df.size * 100) + "%")
    print("Percentage of severe anxiety: " + str(severe_a.size / df.size * 100) + "%")
    print("Percentage of extreme severe anxiety: " + str(ex_severe_a.size / df.size * 100) + "%")
    
def geolocation(df):
   # pd.set_option("display.max_rows", None, "display.max_columns", None)
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
    hand_l['Count'] = df.groupby('hand').size() 
    hand_sort = hand_l.sort_values(by= ['Count','DScore'], ascending=False)
    print(hand_sort)

def stress_severity(df):
    # normal stress
    normal_s = df[df["SScore"] < 15]
    # mild stress
    mild_s = df[(df["SScore"] <= 18) & (df["SScore"] >=15)]
    # moderate stress
    moderate_s = df[(df["SScore"] <= 25) & (df["SScore"] >=19)]
    # severe stress
    severe_s = df[(df["SScore"] <= 33) & (df["SScore"] >=26)]
    # extreme severe stress
    ex_severe_s = df[df["SScore"] >=34]
    print("Percentage of normal stress: " + str(normal_s.size / df.size * 100) + "%")
    print("Percentage of mild stress: " + str(mild_s.size / df.size * 100) + "%")
    print("Percentage of moderate stress: " + str(moderate_s.size / df.size * 100) + "%")
    print("Percentage of severe stress: " + str(severe_s.size / df.size * 100) + "%")
    print("Percentage of extreme severe stress: " + str(ex_severe_s.size / df.size * 100) + "%")
    

def main():
    df = pd.read_csv('dass_test/data/cleaned_data.csv')
    
    gender_average(df)
    age_average(df)

    depression_severity(df)
    anxiety_severity(df)
    stress_severity(df)

    geolocation(df)
    education(df)
    religion(df)
    hand(df)


if __name__ == '__main__':
    main()