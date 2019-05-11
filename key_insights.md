# Loan Dataset Exploration

## Key Insights for Presentation

The following insights were chosen to be presented. Any changes in the design is also explained here.

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
