

```python
#Code in this cell is to import modules and read file
#if you want to test on purchase_data2.json just change the filename

#Import pandas and os
import pandas as pd
import os

#combine the filepath
filename='purchase_data.json'
filepath=os.path.join('HeroesOfPymoli',filename)

#read json file as pymoli_df 
pymoli_df=pd.read_json(filepath)
# print("debug let's take a look at the head of pymoli_df\n")
pymoli_df.head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>38</td>
      <td>Male</td>
      <td>165</td>
      <td>Bone Crushing Silver Skewer</td>
      <td>3.37</td>
      <td>Aelalis34</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21</td>
      <td>Male</td>
      <td>119</td>
      <td>Stormbringer, Dark Blade of Ending Misery</td>
      <td>2.32</td>
      <td>Eolo46</td>
    </tr>
    <tr>
      <th>2</th>
      <td>34</td>
      <td>Male</td>
      <td>174</td>
      <td>Primitive Blade</td>
      <td>2.46</td>
      <td>Assastnya25</td>
    </tr>
    <tr>
      <th>3</th>
      <td>21</td>
      <td>Male</td>
      <td>92</td>
      <td>Final Critic</td>
      <td>1.36</td>
      <td>Pheusrical25</td>
    </tr>
    <tr>
      <th>4</th>
      <td>23</td>
      <td>Male</td>
      <td>63</td>
      <td>Stormfury Mace</td>
      <td>1.27</td>
      <td>Aela59</td>
    </tr>
    <tr>
      <th>5</th>
      <td>20</td>
      <td>Male</td>
      <td>10</td>
      <td>Sleepwalker</td>
      <td>1.73</td>
      <td>Tanimnya91</td>
    </tr>
    <tr>
      <th>6</th>
      <td>20</td>
      <td>Male</td>
      <td>153</td>
      <td>Mercenary Sabre</td>
      <td>4.57</td>
      <td>Undjaskla97</td>
    </tr>
    <tr>
      <th>7</th>
      <td>29</td>
      <td>Female</td>
      <td>169</td>
      <td>Interrogator, Blood Blade of the Queen</td>
      <td>3.32</td>
      <td>Iathenudil29</td>
    </tr>
    <tr>
      <th>8</th>
      <td>25</td>
      <td>Male</td>
      <td>118</td>
      <td>Ghost Reaver, Longsword of Magic</td>
      <td>2.77</td>
      <td>Sondenasta63</td>
    </tr>
    <tr>
      <th>9</th>
      <td>31</td>
      <td>Male</td>
      <td>99</td>
      <td>Expiration, Warscythe Of Lost Worlds</td>
      <td>4.53</td>
      <td>Hilaerin92</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Code below is not required by the homework instruction
#but I feel obligated to check if there is any missing data by doing a count
# pymoli_df.count()
#Ok greate count for all column matches 
```




    Age          78
    Gender       78
    Item ID      78
    Item Name    78
    Price        78
    SN           78
    dtype: int64




```python
#Player Count

#get total number of players by len
total_players=len(pymoli_df)
# print('degbug: total number of players is {}'.format(total_players))

#based on the example given by homework instruction,it seems
#that we are ought to output the total player somehow... Make a dataframe
total_players_df=pd.DataFrame([[total_players]],columns=['Total Number of Players'])
total_players_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Number of Players</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>780</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Code in this cell for Purchase Analysis(total)

#Number of Unique Items
num_unique_items=len(pymoli_df['Item Name'].unique())
# print("debug: this is the number of unique items {}".format(num_unique_items))

#Average Purchase Price
ave_price=pymoli_df['Price'].mean()
# print("debug: this is the average price of total items {}".format(ave_price))

#Total Number of Purchases
total_purchases=pymoli_df['Item Name'].count()
# print("debug: this is the Total Number of Purchases {}".format(total_purchases))

#Total Revenue
total_revenue=pymoli_df['Price'].sum()
# print("debug: this is the Total Revenue {}".format(total_revenue))

#Make a dataframe to summarize the Purchase Analysis(total)
purchase_analysis_total=pd.DataFrame([[num_unique_items,ave_price,total_purchases,total_revenue]],
                                    columns=['Number of Unique Items','Average Price','Number of Purchases','Total Revenue'])
#format columns 'Average Price'and 'Total Revenue' to look prettier
purchase_analysis_total['Average Price']=purchase_analysis_total['Average Price'].map('${:.2f}'.format)
purchase_analysis_total['Total Revenue']=purchase_analysis_total['Total Revenue'].map('${:.2f}'.format)

purchase_analysis_total
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Number of Unique Items</th>
      <th>Average Price</th>
      <th>Number of Purchases</th>
      <th>Total Revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>179</td>
      <td>$2.93</td>
      <td>780</td>
      <td>$2286.33</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Code in this cell for Gender Demographics

# get the total counts of all genders
total_gender=pymoli_df['Gender'].count()

#get the counts of each gender
gender_counts=pymoli_df['Gender'].value_counts()

#calculate the percentage for each gender
percentage_each_gender=(gender_counts/total_gender)*100

#Make a dataframe to summarize Gender Demographics
Gender_Demographics=pd.DataFrame({'Percentage of Players':percentage_each_gender,'Total Count':gender_counts},
                                  index=['Male','Female','Other / Non-Disclosed'],
                                columns=['Percentage of Players','Total Count'])

#format columns 'Percentage of Players' to look prettier
Gender_Demographics['Percentage of Players']=Gender_Demographics['Percentage of Players'].map('{:.2f}%'.format)

Gender_Demographics
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Percentage of Players</th>
      <th>Total Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Male</th>
      <td>81.15%</td>
      <td>633</td>
    </tr>
    <tr>
      <th>Female</th>
      <td>17.44%</td>
      <td>136</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>1.41%</td>
      <td>11</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Purchasing Analysis (Gender)

#get Purchase Count by gender
gender_purchase_counts=pymoli_df.groupby(by='Gender')['Item Name'].count()

#Average Purchase Price by gender
gender_ave_purchase=pymoli_df.groupby(by='Gender')['Price'].mean()

#Total purchase values by gender
gender_total_purchaes=pymoli_df.groupby(by='Gender')['Price'].sum()

#Normalized totals by gender
#According to the Carlos the normalized total by gender is 
#the total purchase each gender divided by the player count per gender
#Note the number of players for each gender may not be the same as number of purchases each gender
#some people just play but not buy stuff 
gender_normalized_total=gender_total_purchaes/pymoli_df['Gender'].value_counts()

# print('debug the purchase count by gender is {}\n \
# the average purchase by gender is {}\n \
# the total purchase by gender is {}\n \
# the normalized total by gender is {}\n'.format(gender_purchase_counts,gender_ave_purchase,gender_total_purchaes,gender_normalized_total))

#Make a dataframe of Purchasing Analysis (Gender)
Purchase_Analysis_Gender=pd.DataFrame({'Purchase Count':gender_purchase_counts,'Average Purchase Price':gender_ave_purchase,
                                       'Total Purchase Value':gender_total_purchaes,'Normalized Totals':gender_normalized_total},
                                     index=['Male','Female','Other / Non-Disclosed'],
                                     columns=['Purchase Count','Average Purchase Price','Total Purchase Value','Normalized Totals'])

#format 'Average Purchase Price','Total Purchase Value','Normalized Totals'
Purchase_Analysis_Gender['Average Purchase Price']=Purchase_Analysis_Gender['Average Purchase Price'].map('${:.2f}'.format)
Purchase_Analysis_Gender['Total Purchase Value']=Purchase_Analysis_Gender['Total Purchase Value'].map('${:.2f}'.format)
Purchase_Analysis_Gender['Normalized Totals']=Purchase_Analysis_Gender['Normalized Totals'].map('${:.2f}'.format)


Purchase_Analysis_Gender
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
      <th>Normalized Totals</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Male</th>
      <td>633</td>
      <td>$2.95</td>
      <td>$1867.68</td>
      <td>$2.95</td>
    </tr>
    <tr>
      <th>Female</th>
      <td>136</td>
      <td>$2.82</td>
      <td>$382.91</td>
      <td>$2.82</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>11</td>
      <td>$3.25</td>
      <td>$35.74</td>
      <td>$3.25</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Code in this cell is for Age Demographics

#get the oldest player's age to set up the upper-bound of the bin
oldest=int(pymoli_df['Age'].max())

# set up bins
bins=[0,9,14,19,24,29,34,39,oldest]
bin_names=['<10','10-14','15-19','20-24','25-29','30-34','35-39','40+']
pymoli_df['Age Group']=pd.cut(pymoli_df['Age'],bins=bins,labels=bin_names)

#debug
# pymoli_df['Age Group'].count()
# pymoli_df['Age'].count()==pymoli_df['Age Group'].count()

#get number of players of each age group
age_group_player_count=pymoli_df['Age Group'].value_counts()

#calculate the percentage of players of each age group
age_group_player_percentage=(pymoli_df['Age Group'].value_counts()/total_players)*100

#make a dataframe for Age Demographics
Age_Demographics=pd.DataFrame({'Percentage of Players':age_group_player_percentage,'Total Count':age_group_player_count},
                             index=bin_names)
#format the 'Percentage of Players'
Age_Demographics['Percentage of Players']=Age_Demographics['Percentage of Players'].map('{:.2f}%'.format)


Age_Demographics
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Percentage of Players</th>
      <th>Total Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;10</th>
      <td>3.59%</td>
      <td>28</td>
    </tr>
    <tr>
      <th>10-14</th>
      <td>4.49%</td>
      <td>35</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>17.05%</td>
      <td>133</td>
    </tr>
    <tr>
      <th>20-24</th>
      <td>43.08%</td>
      <td>336</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>16.03%</td>
      <td>125</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>8.21%</td>
      <td>64</td>
    </tr>
    <tr>
      <th>35-39</th>
      <td>5.38%</td>
      <td>42</td>
    </tr>
    <tr>
      <th>40+</th>
      <td>2.18%</td>
      <td>17</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Code in this cell is for Purchasing Analysis (Age)

#get purchase_count by aged_group
age_group_purchase_count=pymoli_df.groupby(by='Age Group')['Item Name'].count()
#get Average Purchase Price by aged_group
age_group_ave_price=pymoli_df.groupby(by='Age Group')['Price'].mean()
#get Total Purchase Value by aged_group
age_group_total_purchase=pymoli_df.groupby(by='Age Group')['Price'].sum()

##Normalized totals by age_group, normalized totals by age_group is
#the total purchase each age_group divided by the player count per age_group
age_group_normalized_total=age_group_total_purchase/pymoli_df['Age Group'].value_counts()

# print('debug the purchase count by age_group is {}\n \
# the average purchase by age_group is {}\n \
# the total purchase by age_group is {}\n \
# the normalized total by age_group is {}\n'.format(age_group_purchase_count,age_group_ave_price,age_group_total_purchase,age_group_normalized_total))

#Make a dataframe of Purchasing Analysis (Age)
Purchase_Analysis_Age=pd.DataFrame({'Purchase Count':age_group_purchase_count,'Average Purchase Price':age_group_ave_price,
                                       'Total Purchase Value':age_group_total_purchase,'Normalized Totals':age_group_normalized_total},
                                   index=bin_names,columns=['Purchase Count','Average Purchase Price',\
                                                                 'Total Purchase Value','Normalized Totals'])

#format 'Average Purchase Price','Total Purchase Value','Normalized Totals'
Purchase_Analysis_Age['Average Purchase Price']=Purchase_Analysis_Age['Average Purchase Price'].map('${:.2f}'.format)
Purchase_Analysis_Age['Total Purchase Value']=Purchase_Analysis_Age['Total Purchase Value'].map('${:.2f}'.format)
Purchase_Analysis_Age['Normalized Totals']=Purchase_Analysis_Age['Normalized Totals'].map('${:.2f}'.format)


Purchase_Analysis_Age
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
      <th>Normalized Totals</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;10</th>
      <td>28</td>
      <td>$2.98</td>
      <td>$83.46</td>
      <td>$2.98</td>
    </tr>
    <tr>
      <th>10-14</th>
      <td>35</td>
      <td>$2.77</td>
      <td>$96.95</td>
      <td>$2.77</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>133</td>
      <td>$2.91</td>
      <td>$386.42</td>
      <td>$2.91</td>
    </tr>
    <tr>
      <th>20-24</th>
      <td>336</td>
      <td>$2.91</td>
      <td>$978.77</td>
      <td>$2.91</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>125</td>
      <td>$2.96</td>
      <td>$370.33</td>
      <td>$2.96</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>64</td>
      <td>$3.08</td>
      <td>$197.25</td>
      <td>$3.08</td>
    </tr>
    <tr>
      <th>35-39</th>
      <td>42</td>
      <td>$2.84</td>
      <td>$119.40</td>
      <td>$2.84</td>
    </tr>
    <tr>
      <th>40+</th>
      <td>17</td>
      <td>$3.16</td>
      <td>$53.75</td>
      <td>$3.16</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Code in this cell is for Top Spenders

#Get the total purchase value per spender
spender_total_purchase=pymoli_df.groupby(by='SN')['Price'].sum()

#Get the total Purchase Count per spender
spender_purchase_count=pymoli_df.groupby(by='SN')['Item Name'].count()

#Get the Average Purchase Price per spender
spender_ave_price=pymoli_df.groupby(by='SN')['Price'].mean()

# print('debug the purchase count by spender is {}\n \
# the average purchase by spender is {}\n \
# the total purchase by spender is {}\n '.format(spender_purchase_count,spender_total_purchase,spender_ave_price))

#Make a dataframe of purchase analysis by spender
Purchase_Analysis_Spender=pd.DataFrame({'Purchase Count':spender_purchase_count,'Average Purchase Price':spender_ave_price,
                                       'Total Purchase Value':spender_total_purchase},
                                       columns=['Purchase Count','Average Purchase Price','Total Purchase Value'])
#Sort dataframe Purchase_Analysis_Spender by Total Purchase Value starting from the largest
Sorted_Spender=Purchase_Analysis_Spender.sort_values(by='Total Purchase Value',ascending=False)

#top 5 spenders can be subset by using head of Sorted_Spender
top5_spender=Sorted_Spender.iloc[0:5,:]

#format the columns in the top5_spender dataframe
top5_spender['Average Purchase Price']=top5_spender['Average Purchase Price'].map('${:.2f}'.format)
top5_spender['Total Purchase Value']=top5_spender['Total Purchase Value'].map('${:.2f}'.format)

top5_spender
```

    /Users/yizhiyin/anaconda3/envs/PythonData/lib/python3.6/site-packages/ipykernel/__main__.py:27: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
    /Users/yizhiyin/anaconda3/envs/PythonData/lib/python3.6/site-packages/ipykernel/__main__.py:28: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>SN</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Undirrala66</th>
      <td>5</td>
      <td>$3.41</td>
      <td>$17.06</td>
    </tr>
    <tr>
      <th>Saedue76</th>
      <td>4</td>
      <td>$3.39</td>
      <td>$13.56</td>
    </tr>
    <tr>
      <th>Mindimnya67</th>
      <td>4</td>
      <td>$3.18</td>
      <td>$12.74</td>
    </tr>
    <tr>
      <th>Haellysu29</th>
      <td>3</td>
      <td>$4.24</td>
      <td>$12.73</td>
    </tr>
    <tr>
      <th>Eoda93</th>
      <td>3</td>
      <td>$3.86</td>
      <td>$11.58</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Code in this cell is for Most Popular Items

#group item by item ID 
#get item purchase count
item_purchase_count=pymoli_df.groupby(by='Item ID')['Item ID'].count()

#get the total purchase value for each Item
item_purchase=pymoli_df.groupby(by='Item ID')['Price'].sum()

#made a dataframe of purchase analysis by each item ID note so far it only has 'Purchase Count' and 'Total Purchase Value'
purchase_ana_item_ID=pd.DataFrame({'Purchase Count':item_purchase_count,'Total Purchase Value':item_purchase}) 


#create another data frame that has unique 'Item ID' and the name and price of each unique 'Item ID' 
unique_item_ID=pymoli_df[['Item ID','Item Name','Price']].drop_duplicates(['Item ID'])

# # #debug
# # len(unique_item_ID)==len(purchase_ana_item_ID)

# #Now merge the unique_item_ID and purchase_ana_item_ID on 'Item ID'
#do not forget to reset the index for the purchase_ana_item_ID
merge_purchase_ana_item=pd.merge(unique_item_ID,purchase_ana_item_ID.reset_index(),on='Item ID')

#rename the 'Price' column as 'Item Price
merge_purchase_ana_item=merge_purchase_ana_item.rename(columns={"Price":'Item Price'})
#Sorted the merge_purchase_ana_item by 'Purchase Count' and subset the top 5 most popular items
top5_popular_item=merge_purchase_ana_item.sort_values(by='Purchase Count',ascending=False).iloc[0:5,:].set_index('Item ID')

#format the columns in the top5_popular_item dataframe
top5_popular_item['Item Price']=top5_popular_item['Item Price'].map('${:.2f}'.format)
top5_popular_item['Total Purchase Value']=top5_popular_item['Total Purchase Value'].map('${:.2f}'.format)

top5_popular_item
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Item Name</th>
      <th>Item Price</th>
      <th>Purchase Count</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>39</th>
      <td>Betrayal, Whisper of Grieving Widows</td>
      <td>$2.35</td>
      <td>11</td>
      <td>$25.85</td>
    </tr>
    <tr>
      <th>84</th>
      <td>Arcane Gem</td>
      <td>$2.23</td>
      <td>11</td>
      <td>$24.53</td>
    </tr>
    <tr>
      <th>175</th>
      <td>Woeful Adamantite Claymore</td>
      <td>$1.24</td>
      <td>9</td>
      <td>$11.16</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Serenity</td>
      <td>$1.49</td>
      <td>9</td>
      <td>$13.41</td>
    </tr>
    <tr>
      <th>31</th>
      <td>Trickster</td>
      <td>$2.07</td>
      <td>9</td>
      <td>$18.63</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Code in this cell is for Most Profitable items

#Sort the merge_purchase_ana_item by 'Total Purchase Value' and subset the top5 most profitable items
top5_profitable_item=merge_purchase_ana_item.sort_values(by='Total Purchase Value',ascending=False).iloc[0:5,:].set_index('Item ID')

#format the columns in the top5_profitable_item dataframe
top5_profitable_item['Item Price']=top5_profitable_item['Item Price'].map('${:.2f}'.format)
top5_profitable_item['Total Purchase Value']=top5_profitable_item['Total Purchase Value'].map('${:.2f}'.format)

top5_profitable_item
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Item Name</th>
      <th>Item Price</th>
      <th>Purchase Count</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>34</th>
      <td>Retribution Axe</td>
      <td>$4.14</td>
      <td>9</td>
      <td>$37.26</td>
    </tr>
    <tr>
      <th>115</th>
      <td>Spectral Diamond Doomblade</td>
      <td>$4.25</td>
      <td>7</td>
      <td>$29.75</td>
    </tr>
    <tr>
      <th>32</th>
      <td>Orenmir</td>
      <td>$4.95</td>
      <td>6</td>
      <td>$29.70</td>
    </tr>
    <tr>
      <th>103</th>
      <td>Singed Scalpel</td>
      <td>$4.87</td>
      <td>6</td>
      <td>$29.22</td>
    </tr>
    <tr>
      <th>107</th>
      <td>Splitter, Foe Of Subtlety</td>
      <td>$3.61</td>
      <td>8</td>
      <td>$28.88</td>
    </tr>
  </tbody>
</table>
</div>


