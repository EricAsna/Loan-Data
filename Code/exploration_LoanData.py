#!/usr/bin/env python
# coding: utf-8

# # Loan Dataset Exploration
# ## by Erfan Asnaashari
# 
# ## Preliminary Wrangling
# 
# This data set contains 113,937 loans with 81 variables on each loan, including loan amount, borrower rate (or interest rate), current loan status, borrower income, and many others. Before starting the analysis the dataset, a wrangling process is done to prepare the dataset.

# In[1]:


# import all packages and set plots to be embedded inline
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

get_ipython().magic(u'matplotlib inline')


# In[2]:


df= pd.read_csv('loan_data.csv')
# Choosing 12 most important variables out of 81
col_list= ['ListingKey', 'Term', 'LoanStatus', 'BorrowerRate', 'ListingCategory (numeric)', 'EmploymentStatus', 'EmploymentStatusDuration', 'CreditScoreRangeLower', 'CreditScoreRangeUpper', 'IncomeRange', 'LoanOriginalAmount', 'DebtToIncomeRatio']
df= df[col_list]
df.head()


# In[3]:


df.info()


# In[4]:


df.isnull().sum()


# In[5]:


df['EmploymentStatus'].value_counts()


# In[6]:


df['IncomeRange'].value_counts()


# ## Data Assessment Summary
# 
# ### Quality Issues
# 
# - A number of columns have missing values.
# - The paranthesis in the name of ListingCategory column. 
# - ListingCategory values are numeric.
# - CreditScoreRangeLower & Upper values are floats.
# - EmploymentStatusDuration values are floats.
# - EmploymentStatus has part-time, full-time and not employed types.
# - 'Not Displayed' values in the IncomeRange column.
# - IncomeRange column has 'Not employed' values.

# In[7]:


df_clean= df.copy()


# ## Data Cleaning
# 
# ### Define
# Remove null values of the following columns:
#  1. EmploymentStatus 
#  2. EmploymentStatusDuration
#  3. CreditScoreRangeLower
#  4. CreditScoreRangeUpper
#  5. DebtToIncomeRatio

# ### Code

# In[8]:


col_null= ['EmploymentStatus', 'EmploymentStatusDuration', 'CreditScoreRangeLower', 'CreditScoreRangeUpper', 'DebtToIncomeRatio']
df_clean.dropna(axis= 0, inplace= True, subset= col_null)


# ### Test

# In[9]:


df_clean.isnull().sum()


# ### Define
# Change the name of "ListingCategory (numeric)" column to "ListingCategory".

# ### Code

# In[10]:


df_clean= df_clean.rename(columns= {'ListingCategory (numeric)': 'ListingCategory'})


# ### Test

# In[11]:


df_clean.head()


# ### Define
# Change the data types of ProsperScore, CreditScoreRangeLower & Upper and EmploymentStatusDuration columns from floats to integers. 

# ### Code

# In[12]:


col_dtype= ['CreditScoreRangeLower', 'CreditScoreRangeUpper', 'EmploymentStatusDuration']
df_clean[col_dtype]= df_clean[col_dtype].astype(int)


# ### Test

# In[13]:


df_clean.info()


# ### Define
# Changing Full-time and Part-time values in the EmploymentStatus column to Employed.

# ### Code

# In[14]:


df_clean['EmploymentStatus']= df_clean['EmploymentStatus'].replace({"Full-time" : "Employed",
                                                                    "Part-time" : "Employed"})


# ### Test

# In[15]:


df_clean.EmploymentStatus.value_counts()


# ### Define
# Assigning categories to the ListingCategory column.

# ### Code

# In[16]:


# Using data dictionary to interpret each number in the listingcategory column
cat_dic= {0 : 'Not_Available',
          1 : 'Debt_consolidation',
          2 : 'Home_improvement',
          3 : 'Business',
          4 : 'Personal_loan',
          5 : 'Student_use',
          6 : 'Auto',
          7 : 'Other',
          8 : 'Baby_and_adoption',
          9 : 'Boat',
          10 : 'Cosmetic_procedure',
          11 : 'Engagement_ring',
          12 : 'Green_loans',
          13 : 'Household_expenses',
          14 : 'Large_purchases',
          15 : 'Medical_Dental',
          16 : 'Motorcycle',
          17 : 'RV',
          18 : 'Taxes',
          19 : 'Vacation', 
          20 : 'Wedding_loans'}

df_clean['ListingCategory'].replace(cat_dic, inplace= True)


# ### Test

# In[17]:


df_clean['ListingCategory'].value_counts()


# ### Define
# Replace 'Not Displayed' values in the IncomeRange column with Nan and then drop them.

# ### Code

# In[18]:


df_clean['IncomeRange'].replace('Not displayed', np.nan, inplace= True)
df_clean.dropna(axis= 0, inplace= True)


# ### Test

# In[19]:


df_clean.isnull().sum()


# ### Define
# 
# Remove "Not employed" values in the IncomeRange column.

# ### Code

# In[20]:


df_clean= df_clean[df_clean['IncomeRange'] != "Not employed"]


# ### Test

# In[21]:


df_clean['IncomeRange'].value_counts()


# In[22]:


df_clean


# # Structure of the dataset
# 
# The original loan dataset contains 113,937 loans with 81 variables as columns. 12 columns out of 81 are selected to be analyzed in this study. The final loan dataset after completing the wrangling process consists of 97671 rows and 12 columns. It has various data types including integers, floats and strings.  
# 
# ### Main and supportive features of the dataset
# 
# The main features of interest in this dataset are the loan amounts and the interest rates. The supportive features in the dataset are employment status, income range, Loan term, credit score, employment duration and debt-to-income ratio.

# ## Univariate Exploration
# 
# In this section, the distribution of all individual variables are investigated for possible unusual points or outliers.  

# In[23]:


bin_edges= np.arange(0, df_clean['EmploymentStatusDuration'].max()+24, 24)
plt.hist(data= df_clean, x= 'EmploymentStatusDuration', bins= bin_edges);
plt.xlabel('Employment Duration, month');
plt.ylabel('Count');


# Q1. What is the distribution of employment duration? How many years of employment do the most borrower have? 
# 
# Histogram should be used for employment duration since it is a numeric variable. The above histogram shows that the distribution of employment duration is highly skewed to the right. The majority of borrowers had been employed for less than 100 months (~ 8 years) at the time of listing. 

# In[24]:


bin_edges= np.arange(0, df_clean['BorrowerRate'].max()+0.01, 0.01)
plt.hist(data= df_clean, x= 'BorrowerRate', bins= bin_edges);
plt.xlabel('Interest Rate');
plt.ylabel('Count');


# Q2. How is the distribution of interest rate and what are the lowest and highest rates? 
# 
# Borrower's interest rate comment: BorrowerRate is also a numeric variable; therefore, histogram is the best choice to show its distribution. The lowest and highest interest rates in the dataset are 0.00 and 0.36 respectively. Below 0.3, the data is roughly unimodal with the greatest peak at around 0.15. However, the highest peak of the distribution occurred between 0.30 and 0.35 which corresponds to almost 6000 borrowers. 

# In[25]:


plt.figure(figsize= [10,6])
bin_edges= np.arange(0, df_clean['LoanOriginalAmount'].max()+ 2500, 2500)
plt.hist(data= df_clean, x= 'LoanOriginalAmount', bins= bin_edges);
plt.xlabel('Loan Amount');
plt.ylabel('Count');


# Q3. What is the highest count loan range offered to applicants? 
# 
# LoanAmount comment: There is almost a downward trend in the number of borrowers as the loan amount increases. It can also be observed that the mode happened between \\$2500 and \\$5000. 

# In[26]:


bin_edges= np.arange(500, df_clean['CreditScoreRangeLower'].max()+ 20, 20)
plt.hist(data= df_clean, x= 'CreditScoreRangeLower', bins= bin_edges);
plt.xlabel('Lower Credit Score');
plt.ylabel('Count');


# Q4. What is the distibution of lower credit score?
# 
# The length of each credit core range is 20. The distribution is unimodal and the mode of lower credit score in 660 which means that the mode of upper credit score is 679.

# In[27]:


bin_edges= np.arange(0, df_clean['DebtToIncomeRatio'].max()+ 0.1, 0.1)
plt.hist(data= df_clean, x= 'DebtToIncomeRatio', bins= bin_edges);
plt.xlabel('Debt_to_income_ratio');
plt.ylabel('Count');
plt.xlim(0,10.1);


# Q5. Are there any unusual values in the dept-to-income-ratio variable?
# 
# The debt to income ratio for the majority of loan borrowers is less than 200% as depicted in the histogram. However, there exists some outliers which are far away from the other points having maximum of 1010%. 

# In[28]:


base_color= sb.color_palette()[0]
sb.countplot(data= df_clean, y= 'LoanStatus', color= base_color);
plt.xscale('log')


# Q6. What status has the highest count in the loan status variable?
# 
# LoanStatus is a categorical variable that can be well presented by a seaborn countplot. Current loans have the highest count followed by Completed and Chargedoff ones.

# In[29]:


sb.countplot(data= df_clean, y= 'ListingCategory', color= base_color);
plt.xscale('log')


# Q7. What are the main purposes of borrowing a loan by applicants?
# 
# There are many variables so a horizontal bar chart is a suitable visualization. Interestingly, most loans were borrowed in order to consolidate applicants' other loans. Other reasons, home improvement and business are respectively among the top purposes of getting loans. This can be dangerous because many people will use it to pay off their credit cards and then run up even more debt within a few years. 

# In[30]:


plt.figure(figsize= [8,6])
sb.countplot(data= df_clean, x= 'IncomeRange', color= base_color);


# Q8. How does the income range vary among the applicants in the dataset? 
# 
# A bar chart is used to show the distribution of IncomeRange column since it is a categorical variable. The majority of applicants' salaries fall in the range of \\$25,000 to \\$75,000. Borrowers with less than \\$25,000 salary have the least count in the dataset. 

# In[31]:


sb.countplot(data= df_clean, x= 'EmploymentStatus', color= base_color);
plt.yscale('log')


# Employed borrowers have the highest proportion followed by Other, self-employed and not employed. 

# In[32]:


sorted_counts= df_clean['Term'].value_counts()
plt.pie(sorted_counts, labels= ['36 months', '60 months', '12 months'], startangle= 90, counterclock= False, autopct='%1.1f%%');
plt.axis('square');
plt.title('Length of the loan in months');


# Q9. What is the proportion of loan duration terms in the dataset? 
# 
# A pie chart is used for the demonstration of the term of loans since there are only three types in this category. It can be observed that loans with the duration of 36 months are the most popular ones accounting for 74.9%. 60 months and 12 months loans comprised of 23.7% and 1.4% respectively.

# ### Discuss the distribution(s) of your variable(s) of interest. Were there any unusual points? Did you need to perform any transformations?
# 
# > The loan amount and borrower interest rate are my main variables of interest. The loan amount distribution is highly right skewed with the minimum of 1000 and maximum of 35000 dollars. The mode of the laon amounts is between 2500 and 5000 dollars.  Borrower's interest rate is the other main variable with the lowest and highest values of 0.00 and 0.36 respectively. Below 0.3, the data is roughly unimodal with the greatest peak at around 0.15. However, the highest peak of the distribution occurred between 0.30 and 0.35 corresponding to almost 6000 borrowers. The axis showing the count for loan status, listing category and employment status was transformed into logarithmic scale.
# 
# ### Of the features you investigated, were there any unusual distributions? Did you perform any operations on the data to tidy, adjust, or change the form of the data? If so, why did you do this?
# 
# > After assessing the data, a number of quality issues were identified and cleaned as expressed in the data assessment and data cleaning sections. This was performed to make the dataset ready for the final analysis.
# > The only unusual distribution relates to the debt-to-income ratio variable where 1000% values are present while the majority of points distributed below 200%.  

# ## Bivariate Exploration
# 
# In this section, the relationships between pairs of variables in the dataset are investigated. 

# In[33]:


plt.figure(figsize= [12, 5])
sb.boxplot(data= df_clean, x= 'IncomeRange', y= 'LoanOriginalAmount', color= base_color);


# In[34]:


plt.figure(figsize= [12, 5])
sb.boxplot(data= df_clean, x= 'EmploymentStatus', y= 'LoanOriginalAmount', color= base_color);


# Q10. Do employment status and income range affect the amount of loan to borrow?
# 
# From the above two visualizations, we observe that only employed applicants whose earnings are more than \\$100,000 have a chance to get more than \\$25,000 loan. Moreover, the median of loan amount increases with the increase in the income salary range. Employment status has also a significant impact on the amount one can borrow. 

# In[35]:


plt.figure(figsize= [12, 5])
plt.scatter(data= df_clean, x= 'EmploymentStatusDuration', y= 'LoanOriginalAmount', alpha= 1/5);
plt.xlabel('Employment duration (month)');
plt.ylabel('Loan amount');


# In[36]:


plt.figure(figsize= [12, 5])
plt.scatter(data= df_clean, x= 'EmploymentStatusDuration', y= 'BorrowerRate', alpha= 1/5);
plt.xlabel('Employment duration (month)');
plt.ylabel('Interest rate');


# Q11. How does employment duration affect the interest rate and loan amount?
# 
# Employment duration does not have a significant effect on the loan amount and the interest rate.

# In[37]:


plt.figure(figsize= [12, 5])
sb.boxplot(data= df_clean, x= 'IncomeRange', y= 'BorrowerRate', color= base_color);


# Comment: I used a boxplot to show the relationship between a categorical vs. a numeric variables. Income range also affects the interest rate of the loan. The median interest rate decreases as the income range increases. 

# In[38]:


plt.figure(figsize= [10, 8])
plt.scatter(data= df_clean, y= 'CreditScoreRangeLower', x= 'BorrowerRate', alpha= 1/5);
plt.xlabel('Interet Rate');
plt.ylabel('Lower Credit Score');


# Q12. Does low credit score increase the interest rate of a loan?
# 
# As expected, credit score affects the rate of interest of the borrower's loan. As depicted in the scatter plot above, it is very unlikely to receive a loan with less than 15% interest rate if your lower credit score is less than 620. The majority of those applicants with the lower credit score of above 850 are entitled to low interest rate (5%-10%) loans.

# In[39]:


plt.figure(figsize= [10, 8])
x_bins= np.arange(520, 880+ 20, 20)
y_bins= np.arange(0, 35000+ 2500, 2500)
plt.hist2d(data= df_clean, y= 'CreditScoreRangeLower', x= 'LoanOriginalAmount', cmin= 0.5, cmap= 'viridis_r', bins= [y_bins, x_bins]);
y_ticks= df_clean['CreditScoreRangeLower'].value_counts().index.sort_values()
plt.yticks(y_ticks, y_ticks)
plt.colorbar(label= 'Count');
plt.xlabel('Loan Amount');
plt.ylabel('Lower Credit Score');


# Q12. What is the best way of showing the distribution of loans based on lower credit score and loan amount?
# 
# Heatmap can be used for showing the distribution lower credit score and loan amount that both are numeric variables. According to the above heatmap, more than 4000 applicants have a lower credit score of 660 to 680 and borrowed 2500 to 5000 dollars. The heatmap also shows that the minimum lower credit score required to get loans of more than \\$27,500 is 720. 

# In[40]:


plt.figure(figsize= [12, 5])
sb.boxplot(data= df_clean, x= 'IncomeRange', y= 'CreditScoreRangeLower', color= base_color);


# Q13. Do applicants with higher salary have better credit scores?
# 
# It is interesting to know if people with higher salary also have better credit scores. The above boxplot confirms that applicant with more than \\$100,000 income have the best minimun and median credit scores. 

# In[41]:


plt.figure(figsize= [10, 8])
y_bins= np.arange(0, 10.01+ 0.5, 0.5)
x_bins= np.arange(1000, 35000+ 2500, 2500)
plt.hist2d(data= df_clean, x= 'LoanOriginalAmount', y= 'DebtToIncomeRatio', cmin= 0.5, cmap= 'viridis_r', bins= [x_bins, y_bins]);
plt.colorbar();
plt.xlabel('Loan Amount');
plt.ylabel('Debt to income ratio');


# Q14. How does high debt-to-income ratio affect the loan amount?
# 
# 
# It is clear from the above heatmap that debt-to-income ratio has tangible influence on the amount of loan to borrow. The figure shows that it is impossible to get more than \\$27,500 loan if your debt-to-income ratio is above 50%. 

# In[42]:


plt.figure(figsize= [10, 8])
y_bins= np.arange(0, 10.01+ 0.5, 0.5)
x_bins= np.arange(0, 0.36+ 0.02, 0.02)
plt.hist2d(data= df_clean, x= 'BorrowerRate', y= 'DebtToIncomeRatio', cmin= 0.5, cmap= 'viridis_r', bins= [x_bins, y_bins]);
plt.colorbar();
plt.xlabel('Interest Rate');
plt.ylabel('Debt to income ratio');


# In[43]:


plt.figure(figsize= [12, 5])
sb.boxplot(data= df_clean, x= 'Term', y= 'BorrowerRate', color= base_color);


# Q15. Which loan term offers the lowest and highest interest rates?
# 
# As expected, the boxplot shows that the largest median interest rate belongs to loans with the duratio of 60 months followed by 36 and 12 months. The 36-month loan term includes both the lowest and highest interest rates.

# In[44]:


plt.figure(figsize= [15, 6])
sb.violinplot(data= df_clean, x= 'LoanStatus', y= 'BorrowerRate', color= base_color, inner= 'quartile');
plt.xticks(rotation= 20);


# Q16. What is an important characteristic of past due, charged off and defaulted loans? 
# 
# As depicted in the violin plot, for defaulted, chargedoff and past due types of loan status, there is a high density of interest rates more than 20% and the median interest rate is also higher than 20% while this density is considerably smaller for completed and final payment ones.

# ### Talk about some of the relationships you observed in this part of the investigation. How did the feature(s) of interest vary with other features in the dataset?
# 
# There is a positive correlation between the loan amount and income range, employment status and credit score and a negative correlation between the loan amount and dept-to-income ratio. 
# Income range and credit score also have negative correlation with the interest rate. On the other hand, there is a direct relationship between the duration term of the loan and its interest rate. It was also observed that only employed applicants whose earnings are more than \\$100,000 have a chance to get more than \\$25,000 loan.
# It was also found that receiving a loan with less than 15% interest is very unlikely if the borrower's lower credit score is less than 620. Also, the majority of those applicants with the lower credit score of above 850 are entitled to low interest rate (5%-10%) loans. The minimum lower credit score required to get more than \\$27,500 loans is 720.
# For all defaulted, chargedoff and past due types of loan status, the median interest rates are higher than 20% while completed and final payment ones have less than 20% median interest rate.
# 
# ### Did you observe any interesting relationships between the other features (not the main feature(s) of interest)?
# 
# Generally, applicants with higher salaries have better credit scores than low-income applicants. 

# ## Multivariate Exploration
# 
# In this section plots of three variables are created to investigate the data even further. 

# In[45]:


df_mod= df_clean.query('EmploymentStatus != "Not employed" and IncomeRange != "Not employed"')
plt.figure(figsize= [12,5])
ax= sb.barplot(data= df_mod, x= 'IncomeRange', y= 'LoanOriginalAmount', hue= 'EmploymentStatus')
plt.ylabel('Mean of loan amount');


# Q17. How do self-employed and employed applicant compare in terms of average amount of loan they can borrow based on their salaries?
# 
# It would be nice to understand how income range and employment status together can influence the average amount of loans lent to applicants. Average loan amount shows an upward trend as we move from retired to employed and from low-income to high-income applicants. It is interesting that retired applicants whose income is more than \\$100,000 on average borrowed less amount of loan compared to those of lower income ranges.The nature of 'Other' employment status is not clear. Within all income ranges except \\$100,000+, self-employed applicants were offered larger amount of loan on average compared to employed ones.

# In[46]:


df_mod= df_clean.query('EmploymentStatus != "Not employed" and IncomeRange != "Not employed"')
plt.figure(figsize= [12,5])
ax= sb.barplot(data= df_mod, x= 'IncomeRange', y= 'BorrowerRate', hue= 'Term')
plt.ylabel('Mean of Interest Rates');


# Q18. How do income and loan duration affect interest rate on average?
# 
# As expected, the barchat shows that the largest average interest rates belong to loans with the duration of 60 months followed by 36 and 12 months. This is because longer term economic conditions are much harder to predict thus lenders charge higher interest rates for longer term loans. It can be observed that low-income people have to pay more interest on their loans as higher risk is associated with their payment compared to high-income applicants.

# ### Talk about some of the relationships you observed in this part of the investigation. Were there features that strengthened each other in terms of looking at your feature(s) of interest?
# 
# When both the employment status and income range are considered against the loan amount in the above multivariate visualization, it becomes more clear these two variables are the main driver for the amount of loan one can borrow. In addition to income range, loan term is a key feature determining the interest rate.

# In[47]:


df_clean.to_csv('clean_loan_data.csv', index= False)

