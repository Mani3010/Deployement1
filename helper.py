#35:14
import numpy as np
def fetch_medal_tally(df, year, country):
   medal_df = df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'])
   flag = 0
   if year == 'Overall' and country == 'Overall':
      temp_df = medal_df
   if year == 'Overall' and country != 'Overall':
      flag = 1
      temp_df = medal_df[medal_df['region'] == country]
   if year != 'Overall' and country == 'Overall':
      temp_df = medal_df[medal_df['Year'] == int(year)]
   if year != 'Overall' and country != 'Overall':
      temp_df = medal_df[(medal_df['Year'] == int(year)) & (medal_df['region'] == country)]
   if flag == 1:
      x = temp_df.groupby('Year').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Year').reset_index()
   else:
      x = temp_df.groupby('region').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Gold',
                                                                                    ascending=False).reset_index()
   x['total'] = x['Gold'] + x['Silver'] + x['Bronze']
   x['Gold'] = x['Gold'].astype('int')
   x['Silver'] = x['Silver'].astype('int')
   x['Bronze'] = x['Bronze'].astype('int')
   x['total'] = x['total'].astype('int')
   return x
def medal_tally(df):
   medal_tally=df.drop_duplicates(subset=['Team','NOC','Games','Year','City','Sport','Event','Medal'])
   medal_tally=medal_tally.groupby('region').sum()[['Gold','Silver','Bronze']].sort_values('Gold',ascending=False).reset_index()
   medal_tally['total']=medal_tally['Gold']+medal_tally['Silver']+medal_tally['Bronze']
   medal_tally['Gold']=medal_tally['Gold'].astype('int')
   medal_tally['Silver']=medal_tally['Silver'].astype('int')
   medal_tally['Bronze']=medal_tally['Bronze'].astype('int')
   medal_tally['total']=medal_tally['total'].astype('int')
   return medal_tally
def country_year_list(df):
   years=df['Year'].unique().tolist()
   years.sort()
   years.insert(0,'Overall')
   country=np.unique(df['region'].dropna().values).tolist()
   country.sort()
   country.insert(0,'Overall')
   return years,country
#1:09:43
def data_over_time(df,col):
   nations_over_time = df.drop_duplicates(['Year', col])['Year'].value_counts().reset_index().sort_values('Year')
   nations_over_time.rename(columns={'Year': 'Edition', 'count': 'col'}, inplace=True)
   return nations_over_time
#1:23:17
#12558
#14051
def most_successful(df,sport):
   temp_df = df.dropna(subset=['Medal'])
   if sport != 'Overall':
      temp_df = temp_df[temp_df['Sport'] == sport]
   # return temp_df['Name'].value_counts()
   # print(temp_df['Name'].value_counts().reset_index().head(15))
   # return temp_df['Name'].value_counts().reset_index().head(15).merge(df,left_on='index',right_on='Name',how='left')
   counts_df = temp_df['Name'].value_counts().reset_index()
   counts_df.columns = ['Name', 'count']
   x = counts_df.head(15).merge(df.drop_duplicates(subset=['Name']), on='Name', how='left')[['Name', 'count', 'Sport', 'region']]
   x.rename(columns={'count': 'Medal Count'}, inplace=True)
   return x
#14351
def year_wise_medal_tally(df,country):
   temp_df=df.dropna(subset=['Medal'])
   temp_df = temp_df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'])
   new_df = temp_df[temp_df['region'] == country]
   final_df = new_df.groupby('Year').count()['Medal'].reset_index()
   return final_df
def country_event_heatmap(df, country):
   temp_df = df.dropna(subset=['Medal'])
   temp_df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'], inplace=True)
   new_df = temp_df[temp_df['region'] == country]
   pt = new_df.pivot_table(index='Sport', columns='Year', values='Medal', aggfunc='count').fillna(0)
   return pt


def most_successful_countrywise(df, country):
   temp_df = df.dropna(subset=['Medal'])
   temp_df = temp_df[temp_df['region'] == country]
   # x = temp_df['Name'].value_counts().reset_index().head(10).merge(df, left_on='Name', right_on='count', how='left')[['Name', 'count', 'Sport']].drop_duplicates('Name')
   # x = temp_df['Name'].value_counts().reset_index().head(10)
   # x.rename( {'count': 'Medals Count'}, inplace=True)
   x = temp_df['Name'].value_counts().reset_index().head(20)
   # top_athletes = temp_df['Name'].value_counts().head(10)
   x.columns = ['Name', 'Medals Count']  # Rename columns for clarity
   # Merge with the original DataFrame to get additional details like 'Sport'
   x = x.merge(temp_df, on='Name', how='left')[['Name', 'Medals Count', 'Sport']].drop_duplicates('Name')
   return x
#20422
#21256
def weight_v_height(df, sport):
   athlete_df = df.drop_duplicates(subset=['Name', 'region'])
   athlete_df['Medal'].fillna('No Medal', inplace=True)
   if sport != 'Overall':
      temp_df = athlete_df[athlete_df['Sport'] == sport]
      return temp_df
   else:
      return athlete_df
   # 22614
def men_vs_women(df):
   athlete_df = df.drop_duplicates(subset=['Name', 'region'])
   men = athlete_df[athlete_df['Sex'] == 'M'].groupby('Year').count()['Name'].reset_index()
   women = athlete_df[athlete_df['Sex'] == 'F'].groupby('Year').count()['Name'].reset_index()
   final = men.merge(women, on='Year', how='left')
   final.rename(columns={'Name_x': 'Male', 'Name_y': 'Female'}, inplace=True)
   final.fillna(0, inplace=True)
   return final
# 22956