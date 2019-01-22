# (Loan Dataset Exploration)
## by Erfan Asnaashari


## Loan dataset

For this study, I have chosen "loan data from prosper" dataset which is available on the Udacity server.
The original loan dataset consists of 113,937 loans with 81 variables on each loan, including loan amount, borrower rate (or interest rate), current loan status, borrower income, and many others. After conducting the wrangling process, 97671 loans were remained and 12 variables were selected for this study.
The focus here is on two main features of any loan; loan amount and the interest rate as well as some other important features that can greatly affect the two main variables. Features explored in this study are:

__Main variables__
1. Loan amount
2. Interest rate (borrower rate)

__Supportive variables__
3. Income range
4. Employment status
5. Employment duration
6. Loan term (duration)
7. Loan status
8. Lower & upper credit score
9. Debt-to-income ratio
10. Listing category

## Summary of Findings

1. Findings from univariate visualizations:
  - Distribution of employment duration is highly skewed to the right. The majority of borrowers had been employed for less than 100 months (~ 8 years) at the time of listing.
  - The lowest and highest interest rates in the dataset are 0.00 and 0.36 respectively. Below 0.3, the data is roughly unimodal with the greatest peak at around 0.15. However, the highest peak of the distribution occurred between 0.30 and 0.35 which corresponds to almost 6000 borrowers.
  - There is almost a downward trend in the number of borrowers as the loan amount increases. The mode of loan amount is between $2500 and $5000.
  - The length of each credit core range is 20. The mode of lower credit score is 660 which means that the mode of upper credit score is 679.
  - The debt to income ratio for the majority of loan borrowers is less than 200%. However, there exists some outliers which are far away from the other points having maximum of 1010%.
  - Most loans were borrowed by the applicants in order to consolidate their other loans. This can be dangerous because many people will use it to pay off their credit cards and then run up even more debt within a few years.
  - The majority of applicants' salaries fall in the range of $25,000 to $75,000. Borrowers with less than $25,000 salary have the least count in the dataset.
  - Employed borrowers have the highest proportion followed by Other, self-employed and not employed.
  - Loans with the duration of 36 months are the most popular ones accounting for 74.9%. 60 months and 12 months loans comprised of 23.7% and 1.4% respectively.

2. Findings from bivariate visualizations:
  - Only employed applicants whose earnings are more than $100,000 have a chance to get more than $25,000 loan. Moreover, the median of loan amount increases with the increase in the income salary range. Employment status has also a significant impact on the amount one can borrow.
  - Employment duration does not have a significant effect on the loan amount and the interest rate.
  - Income also affects the interest rate of the loan. The median interest rate decreases as the income range increases.
  - Credit score affects the rate of interest of the borrower's loan. It is very unlikely to receive a loan with less than 15% interest rate if your lower credit score is less than 620. The majority of those applicants with the lower credit score of above 850 are entitled to low interest rate (5%-10%) loans.
  - More than 4000 applicants have a lower credit score of 660 to 680 and borrowed $2500 to $5000. The minimum lower credit score required to get loans of more than $27,500 is 720.
  - Applicants with more than $100,000 income have the best minimum and median credit scores.
  - Debt-to-income ratio has tangible influence on the amount of loan to borrow. It is impossible to get more than $27,500 loan if your debt-to-income ratio is above 50%.
  - The largest median interest rate belongs to loans with the duration of 60 months followed by 36 and 12 months. The 36-month loan term includes both the lowest and highest interest rates.
  - There is a high density of interest rates of more than 20% for defaulted, charged off and past due types of loan status. Their median interest rate is also higher than 20% while this density is considerably smaller for those completed or in final payment.

3. Findings from multivariate visualizations:
  - Average loan amount shows an upward trend as we move from retired to employed and from low-income to high-income applicants. It is interesting that retired applicants whose income is more than $100,000 borrowed less amount of loan on average compared to those of lower income ranges. Within all income ranges except $100,000+, self-employed applicants were offered larger amount of loan on average compared to employed ones.
  - The largest average interest rates belong to loans with the duration of 60 months followed by 36 and 12 months. This is because longer term economic conditions are much harder to predict thus lenders charge higher interest rates for longer term loans.

## Key Insights for Presentation

From the above findings, the following insights were chosen to be presented. Any changes in the design is also explained here.

1. Debt-to-income ratio vs. Loan amount:
  - The color map in the heatmap was reversed to show lowest values in light color and largest values in dark.
  - 'cmin' parameter was used not to display bins that have count less than 1.
  - Both axes and the color bar were labeled. A title was also specified above the heatmap.

2. Interest rate vs. Loan status:
  - The Loan status variable was ordered.
  - Both axes were labeled. A title was also specified for the violin plot.
  - x-ticks were all rotated by 15 degrees for clarity.


3. Mean of loan amount vs. Income range and Employment status:
  - Employment status was ordered.
  - Income range was ordered.
  - Both axes and the legend were labeled.
  - Colorblind mode was used for the color palette of employment status.

