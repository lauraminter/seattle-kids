# Seattle kids:changing demographics and the implications for public schools
# L. Minter December 2021

## Problem Statement
What role does density play in the distribution of children in Seattle's Urban Centers and Villages?  

What role do Urban Centers and Villages play in changing enrollments in Seattle Public Schools?

Can we model enrollment using population data alone?  Does density help us with modeling?

## Technical Requirements
Python with pandas, seaborn, numpy, matplotlib, sklearn

## Background
Welcome to Seattle, the tiniest big city you'll ever visit!  Though Seattle is by all acounts a major metropolitan area, the layout of the city lends itself to focus on the indivudal neighborhoods, resulting in a small town feel.  Across the city there are 32 'urban centers and villages' which act as miniature downtown areas.  These higher-density urban areas within the city are not accidental but rather the result of policies that focus development in specific areas of the city ([CityOfSeattle2021](http://www.seattle.gov/opcd/ongoing-initiatives/comprehensive-plan)).  The city-designated 'Urban Centers and Villages' (UCV) are subject to different zoning than the surrounding neighborhoods and are considered targets for dense development, including multi-family (e.g, high-rise apartments) as well as mixed-used residential/commercial. The areas targeted for development are typically along major corridors with transportation.  This approach allows for growth while avoiding rezoning significant portions of residential land currently slated for single-family housing ([Urbanist2019](https://www.theurbanist.org/2019/03/18/how-we-got-here-a-brief-history-of-mandatory-housing-affordability-in-seattle/)).  Today, most of the residential land in the city remains zoned exclusively for single-family homes and nearly all developable land in these residential areas has been used.  

The city of Seattle has seen immense population growth over the last twenty years.  While most residential land in the city has been zoned for single-family housing the explosive growth of the last two decades has resulted in more significant growth in the urban areas of the city.  With land for single-family homes depleted, housing growth in the city is necessarily be focused on areas zoned for larger developments ([SeattleTimes2018](https://www.seattletimes.com/business/real-estate/amid-seattles-rapid-growth-most-new-housing-restricted-to-a-few-areas/)).  

In July 2019, the city enacted legislation allowing the construction of accessory dwelling units (ADU) on single-family zoned property. ([CityOfSeattle2021-2](https://www.seattle.gov/sdci/permits/common-projects/accessory-dwelling-units)) This change was enacted to help with the severe housing affordability crisis the city was facing.  While ADUs were constructed in record numbers the housing crisis continues and the city is currently examining zoning restrictions in all areas of the city on a neighborhood-by-neighborhood basis.  This rezoning has focused on the UCVs, including the option to epand the boundaries of the zones and increase building height limits within the current boundaries.

During this immense growth in population, Seattle Public Schools (SPS) has seen an increase in enrollment ([SPS2021](https://www.seattleschools.org/enroll/)).  Despite temporary declines in the children per capita during the early 2000, the number of children in the city has been rising significantly over the last 10 years.  In 2019, in response to the rising student population, SPS reopened a high school on the north end that had been closed for 38 years([SeattleTimes2019](https://www.seattletimes.com/education-lab/how-seattles-lincoln-high-school-came-back-to-life/)).

With rapidly changing demographics, the city has been slow to respond to the growing need for schools in more urban parts of the city.  This includes the high density areas in South Seattle as well as the downtown core.  The issue has come up in relation to an urban plot of land offered to SPS by the City of Seattle ([KUOW2021](https://www.kuow.org/stories/can-downtown-seattle-attract-families-the-big-question-behind-the-debate-around-a-new-school)).  Moving forward, UCVs will play an increasing continue to play a major role in the population growth of the city for both adults and children.  

This project examines the growth in Seattle's child population growth in relation to the urban centers and vilages as well as enrollment in Seattle Public Schools.

## Data Collection

Looking at population and enrollment necessitated finding separated datasets that could be connected by geographic location.

Population data was available from several sources.  Data provided by the City of Seattle data was selected as it was already aggreggated into the city-designated Urban Centers and Villages.  This data was available in both pdf reports and csv files from the city's main data portal.  Population data was retrieved from the city of Seattle [population data website](https://www.seattle.gov/opcd/population-and-demographics/decennial-census) on December 5, 2021. These reports are based on early results from the 2020 census, aggregated by city-designated urban centers (subset of the city) as well as by larger neighborhood areas (covering entire city).  

Enrollment data is available directly from the Seattle Public School district via mandated enrollment reports.  The data is provided in pdfs covering individual years, along with comparison to overall enrollment in prior year.  Enrollment data was retrieved from [Seattle Public Schools](https://www.seattleschools.org/departments/enrollment-planning/enrollment-data/annual-enrollment-reports/) on December 5, 2021.  

In addition to enrollment reports, maps for the SPS attendance areas were used to construct a dataset connecting UCVs to the relevant schools.

## Data Cleaning

The population data was provided in easily readable csv files.  Data cleaning consisted of verifying the data was imported correctly, removing features that would not be used and renaming features to increase readability.  

The total enrollment data was provided in pdf reports, one for each school year 2011-2020.  With the exception of the 2016 report, the individual school enrollments were listed in tabular format and was copied from the reports.  The 2016 report did not contain the same breakdown but the data can be obtained from the 2017 which shows comparison with previous year.  Each table spans three pages of the pdf and several fixable formatting issues cropped up during transfer. The process was overall straightforward with only minor data manipulation required to fix merged cell data that was not transferred properly.  Data was spot checked for inconsistencies in both formatting and numerical values.  Computed column totals were compared to the totals given in the pdf.  

The total grade level enrollment, however, was provided only in graphical format, with each report covering the previous five years.  The data from school enrollment was used to produce K-5, 6-8, and 9-12 enrollment statistics.  If further breakdown is desired the data will need to be transferred by hand from the graphs in the individual enrollment reports.  


## Dashboards



## Key EDA Findings

Over the last 10 years the child population growth has been more concentrated in the highly urban, less dense UCV portions of the city.  In these areas the fractional growth in child population significantly outpaces the city-wide fractional growth.  UCVs will continue to play a major role in city growth with 14% of children currently living in UCVs and higher fractional growth in population than the rest of the city.  UCVs will continue to play an important role in driving school enrollments.  

South Lake Union, Downtown and Uptown saw significant fractional growth in child population.  While these neighborhoods are note generally thought of as family friendly, the number of children is rising and will continue to play a role in changing the face of the city.  

UCVs are subject to being broken up by school boundaries.  While this can help schools keep enrollments steady, it could very well break up the village feel of the neighborhood.  This is particularly true in Othello, with young children attending up to 6 different elementary schools, none of which lie within the boundaries of the UCV.  This is less prevalent on the north end where specific UCV carveouts appear in the attendance area boundary maps.

Enrollment at schools near dense UCVs did not see consistent rise or fall in enrollment.  Upon examination this may be the result of splitting of the UCV across multiple schools as well as adjustments to school attendance boundaries.  The overall impact of UCVs on schools remains difficult to quantify due to moving boundaries.  



## Modeling

Target model: linear regression relating enrollment data to the child population data.

In order to model annual enrollment, yearly population estimates were obtained by interpolating between census years.  While this is certainly not an exact value for the true population it provides a reasonable estimate for years in between the decennial census data.  Population lags will be considered to account for typical delays of 5, 10 and 15 years between birth and enrollment in elementary, middle, and high school, respectively.  Alternatively, data from the American Community Survey could be used but would require aggregating census tract data to arrive at UCV-level population.  

Models to evaluate:
- Simple linear regression on child population alone
- Multiple linear regression on child population and time lagged population
- NULL model assuming enrollment is average of years reported (training data only)

Averages for the null models are computed alongside each linear regression to ensure consist definitions of training and testing data.

#### Note on Null Model Comparisons
The null model consists of using the average enrollment from the training set to determine the predicted enrollment.  This is sensitive to the way the data is split but should give a reasonable comparison.  The R2 score is relative to this averaged model so this is expected to be 0.  The RMSE, on the other hand, gives a sense of overall how much error there is in the model.

### Model Evaluation
The time-lagged population data improved the linear models from around 69% explained variation to approximately 90% explained variation.  All of the models showed signficant improvement over the null model in terms of RMSE.  

The best model we were able to make used the population and 5-year lag of population to predict total enrollment.  This model had an R2 of 0.913 and an RMSE of 846 for unseen data.  This represents a factor of 5 decrease from the RMSE for the null model (average).  The model explains 91% of the variation in the enrollment using just two pieces of population data: current population and 5-year lagged population.


## Recommendations

Re-examine how we define school assignments in relation to urban centers and villages, particularly Othello and Lake City

Consider rising population of children in urban centers and villages when determining how to manage school assignments and plan for capital investments.  

## Next Steps

Improvements to the analysis could be made by:
- Adding housing and economic data from the American Community Survey.  This would require aggregating the census tract data to form UCV level data.
- Breaking down by child age.  Again, this data is not reported by the city but could be obtained from the federal government.
- Including distance information.  This would require domain area knowledge.  How far do students travel for school and what explains any differences across the city?  
