

```python
#Import denpendencies
import pandas as pd
import os
```


```python
#get filepath and read csv file
filepath_students=os.path.join('raw_data','students_complete.csv')
filepath_school=os.path.join('raw_data','schools_complete.csv')
#read student data and school into a dataframe file
students_df=pd.read_csv(filepath_students)
school_df=pd.read_csv(filepath_school)

# print(students_df.head())
# print(school_df.head())
```


```python
#Code in this cell is for District Summary

#calculate the number of total schools
#and get the same result as the line below
num_schools=len(school_df)
#using len(students_df['school'].value_counts()) to calculate the number of schools

#calculate the number of total students
num_students=len(students_df)
#use school_df['size'].sum() gives the same number of students as well

#Total Budget
total_budget=school_df['budget'].sum()

#Average Math Score
ave_math=students_df['math_score'].mean()

#Average Reading Score
ave_reading=students_df['reading_score'].mean()

#% Passing Math
#I assume >=60 is passing 
math_passing_percentage=(students_df[(students_df['math_score']>=60)]['math_score'].count()/students_df['math_score'].count())*100
#using len(students_df.loc[students_df['math_score']>=60,:]) can also give number of students with math score>=60

#% Passing Reading
#I assume >=60 is passing 
reading_passing_percentage=(students_df[(students_df['reading_score']>=60)]['reading_score'].count()/students_df['reading_score'].count())*100
#using len(students_df.loc[students_df['reading_score']>=60,:]) can also give number of students with math score>=60

# Overall Passing Rate
overall_passing=(math_passing_percentage+reading_passing_percentage)/2

#creat the Disctric Summary dataframe
disc_sum=pd.DataFrame([[num_schools,num_students,total_budget,ave_math,ave_reading,\
                        math_passing_percentage,reading_passing_percentage,overall_passing]],\
                      columns=['Total Schools','Total Students','Total Budget','Average Math Score',\
                               'Average Reading Score','% Passing Math','% Passing Reading','% Overall Passing Rate'])

#Format the summary a little
disc_sum['Total Students']=disc_sum['Total Students'].map('{:,}'.format)
disc_sum['Total Budget']=disc_sum['Total Budget'].map('${:,}'.format)
disc_sum['Average Math Score']=disc_sum['Average Math Score'].map('{:.2f}'.format)
disc_sum['Average Reading Score']=disc_sum['Average Reading Score'].map('{:.2f}'.format)
disc_sum['% Passing Math']=disc_sum['% Passing Math'].map('{:.2f}%'.format)
disc_sum['% Passing Reading']=disc_sum['% Passing Reading'].map('{:.2f}%'.format)
disc_sum['% Overall Passing Rate']=disc_sum['% Overall Passing Rate'].map('{:.2f}%'.format)
disc_sum

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
      <th>Total Schools</th>
      <th>Total Students</th>
      <th>Total Budget</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>15</td>
      <td>39,170</td>
      <td>$24,649,428</td>
      <td>78.99</td>
      <td>81.88</td>
      <td>92.45%</td>
      <td>100.00%</td>
      <td>96.22%</td>
    </tr>
  </tbody>
</table>
</div>




```python
#code in this cell is to prepare school_df to make a School Summary
#set the index of school_df by school 'name' so it can be used for calculation
#and concation with other data series in the next cell
school_df=school_df.set_index('name')
```


```python
#code in this cell is to prepare school_df to make a School Summary
#drop the column of school ID since it is not required for the final summary
school_ID_drop_df=school_df.drop(columns=['School ID'])
```


```python
#code in this cell is to create School Summary

#School Name,School Type,Total Students,Total School Budget are all existing columns in school_ID_drop_df
#As I have figured out, the 'size' column in the school_ID_drop_df is actually the number of students in the school 
#because school_ID_drop_df['size'].sum() = len(students_df)
#to caluclate Per Student Budget and add per student budget as a column into school_ID_drop_df
school_ID_drop_df['Per Student Budget']=school_ID_drop_df['budget']/school_ID_drop_df['size']

#Now use data from students_df to calculate Average Math and reading score per school
#create a group object grouped by school
grouped_school=students_df.groupby(by='school')

#calculate the average math and reading score by school
ave_math_school=grouped_school['math_score'].mean()
ave_reading_school=grouped_school['reading_score'].mean()

#calculate the percentage of passing for math and reading for each school

#Two steps 
#Step1.count the number of students passing math or reading respectively for each school by doing the following:
#1a.from students_df select students with score>=60 for math and reading respectively and convert each into a dataframe
#1b.in the new dataframe groupby 'school' and use count to get the number of students passing math or reading
num_math_pass_school=pd.DataFrame(students_df.loc[students_df['math_score']>=60,:]).groupby(by='school')['math_score'].count()
num_reading_pass_school=pd.DataFrame(students_df.loc[students_df['reading_score']>=60,:]).groupby(by='school')['reading_score'].count()

#Step2.calculate the passing rate for math and reading for each school
#by dividing the num_math_pass_school by total students in the school 
#note I use two data series from two dataframe for this division
#I can do the calculation becaues the two data series have the same index(school names)
math_pass_rate_school=(num_math_pass_school/school_ID_drop_df['size'])*100
reading_pass_rate_school=(num_reading_pass_school/school_ID_drop_df['size'])*100

#Concate the data series of'% Passing Math'and'% Passing Reading' with school_ID_drop_df
#name this df as school_sum
school_sum=pd.concat([school_ID_drop_df,ave_math_school,ave_reading_school,math_pass_rate_school,reading_pass_rate_school],axis=1)

#change the column names in the school_sum
school_sum.columns=['Type','Size','Budget','Per Student Budget','Average Math Score',\
                    'Average Reading Score','% Passing Math','% Passing Reading']
#add a column of Overall Passing Rate
school_sum['% Overall Passing Rate']=(school_sum['% Passing Math']+school_sum['% Passing Reading'])/2

#format columns of 'Budget' and 'Per Student Budget' since I am not going to do further calculation on it
school_sum['Budget']=school_sum['Budget'].map('${:,}'.format)
school_sum['Per Student Budget']=school_sum['Per Student Budget'].map('${:.2f}'.format)

school_sum

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
      <th>Type</th>
      <th>Size</th>
      <th>Budget</th>
      <th>Per Student Budget</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Bailey High School</th>
      <td>District</td>
      <td>4976</td>
      <td>$3,124,928</td>
      <td>$628.00</td>
      <td>77.048432</td>
      <td>81.033963</td>
      <td>89.529743</td>
      <td>100.0</td>
      <td>94.764871</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>Charter</td>
      <td>1858</td>
      <td>$1,081,356</td>
      <td>$582.00</td>
      <td>83.061895</td>
      <td>83.975780</td>
      <td>100.000000</td>
      <td>100.0</td>
      <td>100.000000</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>District</td>
      <td>2949</td>
      <td>$1,884,411</td>
      <td>$639.00</td>
      <td>76.711767</td>
      <td>81.158020</td>
      <td>88.436758</td>
      <td>100.0</td>
      <td>94.218379</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>District</td>
      <td>2739</td>
      <td>$1,763,916</td>
      <td>$644.00</td>
      <td>77.102592</td>
      <td>80.746258</td>
      <td>89.302665</td>
      <td>100.0</td>
      <td>94.651333</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>Charter</td>
      <td>1468</td>
      <td>$917,500</td>
      <td>$625.00</td>
      <td>83.351499</td>
      <td>83.816757</td>
      <td>100.000000</td>
      <td>100.0</td>
      <td>100.000000</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>District</td>
      <td>4635</td>
      <td>$3,022,020</td>
      <td>$652.00</td>
      <td>77.289752</td>
      <td>80.934412</td>
      <td>89.083064</td>
      <td>100.0</td>
      <td>94.541532</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>Charter</td>
      <td>427</td>
      <td>$248,087</td>
      <td>$581.00</td>
      <td>83.803279</td>
      <td>83.814988</td>
      <td>100.000000</td>
      <td>100.0</td>
      <td>100.000000</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>District</td>
      <td>2917</td>
      <td>$1,910,635</td>
      <td>$655.00</td>
      <td>76.629414</td>
      <td>81.182722</td>
      <td>88.858416</td>
      <td>100.0</td>
      <td>94.429208</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>District</td>
      <td>4761</td>
      <td>$3,094,650</td>
      <td>$650.00</td>
      <td>77.072464</td>
      <td>80.966394</td>
      <td>89.182945</td>
      <td>100.0</td>
      <td>94.591472</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>Charter</td>
      <td>962</td>
      <td>$585,858</td>
      <td>$609.00</td>
      <td>83.839917</td>
      <td>84.044699</td>
      <td>100.000000</td>
      <td>100.0</td>
      <td>100.000000</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>District</td>
      <td>3999</td>
      <td>$2,547,363</td>
      <td>$637.00</td>
      <td>76.842711</td>
      <td>80.744686</td>
      <td>88.547137</td>
      <td>100.0</td>
      <td>94.273568</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>Charter</td>
      <td>1761</td>
      <td>$1,056,600</td>
      <td>$600.00</td>
      <td>83.359455</td>
      <td>83.725724</td>
      <td>100.000000</td>
      <td>100.0</td>
      <td>100.000000</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>Charter</td>
      <td>1635</td>
      <td>$1,043,130</td>
      <td>$638.00</td>
      <td>83.418349</td>
      <td>83.848930</td>
      <td>100.000000</td>
      <td>100.0</td>
      <td>100.000000</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>Charter</td>
      <td>2283</td>
      <td>$1,319,574</td>
      <td>$578.00</td>
      <td>83.274201</td>
      <td>83.989488</td>
      <td>100.000000</td>
      <td>100.0</td>
      <td>100.000000</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>Charter</td>
      <td>1800</td>
      <td>$1,049,400</td>
      <td>$583.00</td>
      <td>83.682222</td>
      <td>83.955000</td>
      <td>100.000000</td>
      <td>100.0</td>
      <td>100.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Code in the cell is to create Top Performing Schools (By Overall Passing Rate)
top_schools=school_sum.sort_values(by=['% Overall Passing Rate'],ascending=False).head()
top_schools
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
      <th>Type</th>
      <th>Size</th>
      <th>Budget</th>
      <th>Per Student Budget</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Cabrera High School</th>
      <td>Charter</td>
      <td>1858</td>
      <td>$1,081,356</td>
      <td>$582.00</td>
      <td>83.061895</td>
      <td>83.975780</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>Charter</td>
      <td>1468</td>
      <td>$917,500</td>
      <td>$625.00</td>
      <td>83.351499</td>
      <td>83.816757</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>Charter</td>
      <td>427</td>
      <td>$248,087</td>
      <td>$581.00</td>
      <td>83.803279</td>
      <td>83.814988</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>Charter</td>
      <td>962</td>
      <td>$585,858</td>
      <td>$609.00</td>
      <td>83.839917</td>
      <td>84.044699</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>Charter</td>
      <td>1761</td>
      <td>$1,056,600</td>
      <td>$600.00</td>
      <td>83.359455</td>
      <td>83.725724</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>100.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Code in the cell is to create bottome performing schools(By overall Passing Rate)
bottom_schools=school_sum.sort_values(by='% Overall Passing Rate',ascending=True).head()
bottom_schools
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
      <th>Type</th>
      <th>Size</th>
      <th>Budget</th>
      <th>Per Student Budget</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Figueroa High School</th>
      <td>District</td>
      <td>2949</td>
      <td>$1,884,411</td>
      <td>$639.00</td>
      <td>76.711767</td>
      <td>81.158020</td>
      <td>88.436758</td>
      <td>100.0</td>
      <td>94.218379</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>District</td>
      <td>3999</td>
      <td>$2,547,363</td>
      <td>$637.00</td>
      <td>76.842711</td>
      <td>80.744686</td>
      <td>88.547137</td>
      <td>100.0</td>
      <td>94.273568</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>District</td>
      <td>2917</td>
      <td>$1,910,635</td>
      <td>$655.00</td>
      <td>76.629414</td>
      <td>81.182722</td>
      <td>88.858416</td>
      <td>100.0</td>
      <td>94.429208</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>District</td>
      <td>4635</td>
      <td>$3,022,020</td>
      <td>$652.00</td>
      <td>77.289752</td>
      <td>80.934412</td>
      <td>89.083064</td>
      <td>100.0</td>
      <td>94.541532</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>District</td>
      <td>4761</td>
      <td>$3,094,650</td>
      <td>$650.00</td>
      <td>77.072464</td>
      <td>80.966394</td>
      <td>89.182945</td>
      <td>100.0</td>
      <td>94.591472</td>
    </tr>
  </tbody>
</table>
</div>




```python
#code in this cell is to create a table for Math Scores by Grade for each school
#Group students_df by school and grade and get the average math score for each school
ave_math_school_grade=students_df.groupby(['grade','school'])['math_score'].mean()

#subset the average score of math of all schools for each grade 
#and concate them into one dataframe
math_scores_grade_sum=pd.concat([ave_math_school_grade.xs('9th',level='grade'),\
                                 ave_math_school_grade.xs('10th',level='grade'),\
                                ave_math_school_grade.xs('11th',level='grade'),\
                                 ave_math_school_grade.xs('12th',level='grade')],axis=1)
#change the column names
math_scores_grade_sum.columns=['Math 9th','Math 10th','Math 11th','Math 12th']
math_scores_grade_sum
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
      <th>Math 9th</th>
      <th>Math 10th</th>
      <th>Math 11th</th>
      <th>Math 12th</th>
    </tr>
    <tr>
      <th>school</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Bailey High School</th>
      <td>77.083676</td>
      <td>76.996772</td>
      <td>77.515588</td>
      <td>76.492218</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>83.094697</td>
      <td>83.154506</td>
      <td>82.765560</td>
      <td>83.277487</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>76.403037</td>
      <td>76.539974</td>
      <td>76.884344</td>
      <td>77.151369</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>77.361345</td>
      <td>77.672316</td>
      <td>76.918058</td>
      <td>76.179963</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>82.044010</td>
      <td>84.229064</td>
      <td>83.842105</td>
      <td>83.356164</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>77.438495</td>
      <td>77.337408</td>
      <td>77.136029</td>
      <td>77.186567</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>83.787402</td>
      <td>83.429825</td>
      <td>85.000000</td>
      <td>82.855422</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>77.027251</td>
      <td>75.908735</td>
      <td>76.446602</td>
      <td>77.225641</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>77.187857</td>
      <td>76.691117</td>
      <td>77.491653</td>
      <td>76.863248</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>83.625455</td>
      <td>83.372000</td>
      <td>84.328125</td>
      <td>84.121547</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>76.859966</td>
      <td>76.612500</td>
      <td>76.395626</td>
      <td>77.690748</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>83.420755</td>
      <td>82.917411</td>
      <td>83.383495</td>
      <td>83.778976</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>83.590022</td>
      <td>83.087886</td>
      <td>83.498795</td>
      <td>83.497041</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>83.085578</td>
      <td>83.724422</td>
      <td>83.195326</td>
      <td>83.035794</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>83.264706</td>
      <td>84.010288</td>
      <td>83.836782</td>
      <td>83.644986</td>
    </tr>
  </tbody>
</table>
</div>




```python
#code in this cell is to create a table for Math Scores by Grade for each school
#Group students_df by school and grade and get the average math score for each school
ave_reading_school_grade=students_df.groupby(['grade','school'])['reading_score'].mean()

#subset the average score of math of all schools for each grade 
#and concate them into one dataframe
reading_scores_grade_sum=pd.concat([ave_reading_school_grade.xs('9th',level='grade'),\
                                 ave_reading_school_grade.xs('10th',level='grade'),\
                                ave_reading_school_grade.xs('11th',level='grade'),\
                                 ave_reading_school_grade.xs('12th',level='grade')],axis=1)
#change the column names
reading_scores_grade_sum.columns=['Reading 9th','Reading 10th','Reading 11th','Reading 12th']
reading_scores_grade_sum
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
      <th>Reading 9th</th>
      <th>Reading 10th</th>
      <th>Reading 11th</th>
      <th>Reading 12th</th>
    </tr>
    <tr>
      <th>school</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Bailey High School</th>
      <td>81.303155</td>
      <td>80.907183</td>
      <td>80.945643</td>
      <td>80.912451</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>83.676136</td>
      <td>84.253219</td>
      <td>83.788382</td>
      <td>84.287958</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>81.198598</td>
      <td>81.408912</td>
      <td>80.640339</td>
      <td>81.384863</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>80.632653</td>
      <td>81.262712</td>
      <td>80.403642</td>
      <td>80.662338</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>83.369193</td>
      <td>83.706897</td>
      <td>84.288089</td>
      <td>84.013699</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>80.866860</td>
      <td>80.660147</td>
      <td>81.396140</td>
      <td>80.857143</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>83.677165</td>
      <td>83.324561</td>
      <td>83.815534</td>
      <td>84.698795</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>81.290284</td>
      <td>81.512386</td>
      <td>81.417476</td>
      <td>80.305983</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>81.260714</td>
      <td>80.773431</td>
      <td>80.616027</td>
      <td>81.227564</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>83.807273</td>
      <td>83.612000</td>
      <td>84.335938</td>
      <td>84.591160</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>80.993127</td>
      <td>80.629808</td>
      <td>80.864811</td>
      <td>80.376426</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>84.122642</td>
      <td>83.441964</td>
      <td>84.373786</td>
      <td>82.781671</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>83.728850</td>
      <td>84.254157</td>
      <td>83.585542</td>
      <td>83.831361</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>83.939778</td>
      <td>84.021452</td>
      <td>83.764608</td>
      <td>84.317673</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>83.833333</td>
      <td>83.812757</td>
      <td>84.156322</td>
      <td>84.073171</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Code below is to create a table for Scores by School Spending

#create a dataframe with the columns of personal budget,Average Math Score, Average Reading Score,
#% Passing Math,% Passing Reading,Overall Passing Rate ,with an index of school name
#I have set the school_df index as school name already so I just need to concat all the columns
score_by_spending=pd.concat([school_ID_drop_df['Per Student Budget'],\
                             school_sum.iloc[:,[4,5,6,7,8]]],axis=1)

#bin and assign names since there is no specific way I am using qcut and break it by quaters
score_by_spending['Spending Range per Student']=pd.qcut(score_by_spending['Per Student Budget'],4,\
                                                        labels=['<$591.5','$591.5-628','$628-641.5','$641.5-655'])
#groupby the Spending Range per Student and make a dataframe 
spend_range_score_sum=pd.DataFrame(score_by_spending.groupby(['Spending Range per Student']).mean())

spend_range_score_sum



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
      <th>Per Student Budget</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing Rate</th>
    </tr>
    <tr>
      <th>Spending Range per Student</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;$591.5</th>
      <td>581.00</td>
      <td>83.455399</td>
      <td>83.933814</td>
      <td>100.000000</td>
      <td>100.0</td>
      <td>100.000000</td>
    </tr>
    <tr>
      <th>$591.5-628</th>
      <td>615.50</td>
      <td>81.899826</td>
      <td>83.155286</td>
      <td>97.382436</td>
      <td>100.0</td>
      <td>98.691218</td>
    </tr>
    <tr>
      <th>$628-641.5</th>
      <td>638.00</td>
      <td>78.990942</td>
      <td>81.917212</td>
      <td>92.327965</td>
      <td>100.0</td>
      <td>96.163983</td>
    </tr>
    <tr>
      <th>$641.5-655</th>
      <td>650.25</td>
      <td>77.023555</td>
      <td>80.957446</td>
      <td>89.106772</td>
      <td>100.0</td>
      <td>94.553386</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Code below is to create a table for Scores by School Size
#create a dataframe with the columns of school size,Average Math Score, Average Reading Score,
#% Passing Math,% Passing Reading,Overall Passing Rate ,with an index of school name
#I have set the school_df index as school name already so I just need to concat all the columns

score_by_size=pd.concat([school_ID_drop_df['size'],\
                             school_sum.iloc[:,[4,5,6,7,8]]],axis=1)

#bin and assign names since there is no specific way I am using qcut and break it by quaters
score_by_size['School Size']=pd.qcut(score_by_size['size'],3,labels=['Small (<1787)','Medium (1787-2927)','Big (2928-4976)'])

#drop 'size' column and groupby School Size and make it into a dataframe
score_by_size_sum=pd.DataFrame(score_by_size.drop(columns=['size']).groupby('School Size').mean())

score_by_size_sum
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
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing Rate</th>
    </tr>
    <tr>
      <th>School Size</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Small (&lt;1787)</th>
      <td>83.554500</td>
      <td>83.850220</td>
      <td>100.000000</td>
      <td>100.0</td>
      <td>100.000000</td>
    </tr>
    <tr>
      <th>Medium (1787-2927)</th>
      <td>80.750065</td>
      <td>82.769850</td>
      <td>95.632216</td>
      <td>100.0</td>
      <td>97.816108</td>
    </tr>
    <tr>
      <th>Big (2928-4976)</th>
      <td>76.993025</td>
      <td>80.967495</td>
      <td>88.955929</td>
      <td>100.0</td>
      <td>94.477965</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Code below is to create a table for Scores by school type
#create a dataframe with the columns of school type,Average Math Score, Average Reading Score,
#% Passing Math,% Passing Reading,Overall Passing Rate ,with an index of school name
#I have set the school_df index as school name already so I just need to concat all the columns
score_by_type=pd.concat([school_ID_drop_df['type'],\
                             school_sum.iloc[:,[4,5,6,7,8]]],axis=1)
#groupby the school type and make a dataframe 
score_by_type_sum=pd.DataFrame(score_by_type.groupby(['type']).mean())

score_by_type_sum
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
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing Rate</th>
    </tr>
    <tr>
      <th>type</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Charter</th>
      <td>83.473852</td>
      <td>83.896421</td>
      <td>100.000000</td>
      <td>100.0</td>
      <td>100.000000</td>
    </tr>
    <tr>
      <th>District</th>
      <td>76.956733</td>
      <td>80.966636</td>
      <td>88.991533</td>
      <td>100.0</td>
      <td>94.495766</td>
    </tr>
  </tbody>
</table>
</div>


