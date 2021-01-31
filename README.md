# datathon-duke
COVID-19 pandemic has adversely affected cities worldwide and dramatically changed the way in which we conduct our lives. The pandemic has shown us that there are start disparity and differences in society as it has left behind a wreckage of human casualties and exposed weaknesses in healthcare infrastructure. While we have been able to counter some of the socio-economic impacts through the help of government aid, there are other economic effects that still affect millions globally, and will continue to do so in the foreseeable future unless innovative and effective policy measures are not put in place. Our team’s analysis aimed to address the question of how the COVID-19 pandemic affected US metropolitan cities through studying economic indicators and examining other parameters.

## Data
Raw data is in the `data` directory and the sanitised version is `sanitised` directory.

## Sanitisation Function
`main.py` is a python script that uses `pandas` to map city names to ids. Dates were converted to ISO using Google Sheets

## Visualisations 
- Employment : https://public.tableau.com/views/USMetroEmploymentLevel/Dashboard1?:language=en-GB&:display_count=y&:toolbar=n&:origin=viz_share_link
- Unemployment : https://public.tableau.com/views/USMetrosUnemploymentInsuranceClaimssinceCOVID-19onset/Dashboard1?:language=en-GB&:display_count=y&:toolbar=n&:origin=viz_share_link
- Job Posting : https://public.tableau.com/views/USMetrosAverageLevelofJobPostingssinceCOVID-19onset/Sheet1?:language=en-GB&:display_count=y&:origin=viz_share_link
- GPS Mobility Data : https://public.tableau.com/views/GPSMobilityData-USMetrosinceCOVID-19onset/Dashboard1?:language=en-GB&:display_count=y&:toolbar=n&:origin=viz_share_link
- Public Administration Indicators : https://public.tableau.com/views/USMetroCreditDebitcardspendinginallmerchantcategorycodes7daymovingaverage/Dashboard1?:language=en-GB&:display_count=y&:toolbar=n&:origin=viz_share_link
- Small Businesses :  
    - https://public.tableau.com/views/USMetrosPercentchangeinnetrevenueforsmallbusinessescalculatedasaseven-daymovingaverageseasonallyadjusted/Sheet1?:language=en-GB&:display_count=y&:toolbar=n&:origin=viz_share_link
    - https://public.tableau.com/views/USMetrosPercentchangeinnumberofsmallbusinessesopencalculatedasa7daymovingaverageseasonallyadjusted/Sheet1?:language=en-GB&:display_count=y&:toolbar=n&:origin=viz_share_link
- Education : https://public.tableau.com/views/USMetrosOnlinemathparticipationamogschoolsthatalreadyusedonlineplatformincourseinstructionpriortothepandemic/Sheet1?:language=en-GB&:display_count=y&:toolbar=n&:origin=viz_share_link

## Analysis 
While the combined employment level for all workers has declined due to COVID-19, it is very interesting to notice how the difference in recovery is so vast for workers in the top and bottom quartile of the income distribution. The top quartile is >$60,000 and bottom quartile is <$27,000 per year. Our visualizations suggest that the COVID-19 sparked recession has almost ended for high wage workers, but job losses persist for low wage workers. Although employment rates have rebounded to nearly pre-COVID-19 levels for high wage workers, they remain significantly lower for low wage workers. Combined with the unemployment data and job postings, this analysis indicates how COVID-19 has adversely affected cities where there is a significant population under low wage employment and we can expect it to have continued economic effects in the next 1, 2, to 5 years: San Francisco, New York City, New Orleans, Los Angeles, etc.

## Data Source
- Consumer spending - Affinity Solutions: www.affinity.solutions/dataforgood 
- Small Businesses - Womply: https://www.womply.com/ 
- Job Postings - Burning Glass Technologies: https://www.burning-glass.com/ 
- Employment - Paychex, Intuit, Earnin, Kronos
- Unemployment Claims - U.S. Department of Labor
- Online School Participation - Zearn
- GPS Mobility Data - https://www.google.com/covid19/mobility/ 

