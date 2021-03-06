# Election_Analysis

MODULE 3
______________


![image](https://user-images.githubusercontent.com/90135381/158719612-efa697c9-406f-49fe-bacb-01d663aaffca.png)



## Overview of Election Audit
______________________________
Completed the following tasks for election audit of a recent local congressional election via creation of lists and dictionaries; empty strings; variables; for loops; decision statements with logical operators; repitition statements with conversion to text files in order to assist Tom. Tom is an employee at the Colorado Board of Elections and this was completed a) to generate a report to certify this election and b) help Tom determine if Python is more efficient at automating the report in comparison to VBA, per the request of his manager, Seth. This report emphasized the following in order to complete the assessment:

1. Calculate total# votes
2. Formulate a complete list of candidates receiving votes
3. Calculate total #votes each candidate received
4. Calclate %votes each candidate won
5. Determine winner of election based on popular vote
6. Determine the voter turnout for each county
7. Calculate the percentage of votes from each county out of the total votes
8. Determine the county with the highest turnout

## Resources
____________
- Data source:election_results.csv
- Software: Python 3.7.6, 3.8.8, Visual Studio Code 1.62.2
- image obtained from: pixabay.com

## Election Audit Results
_________________________

    Election Results
    -------------------------
    Total Votes: 369,711
    -------------------------

    County Votes:
    38855
    Jefferson: 10.5% (38,855)
    306055
    Denver: 82.8% (306,055)
    24801
    Arapahoe: 6.7% (24,801)
    Denver-------------------------
    Winner: Denver
    Winning Vote Count: 306,055
    Winning Percentage: 82.8%
    -------------------------

    Charles Casper Stockham: 23.0% (85,213)

    Diana DeGette: 73.8% (272,892)

    Raymon Anthony Doane: 3.1% (11,606)

    -------------------------
    Winner: Diana DeGette
    Winning Vote Count: 272,892
    Winning Percentage: 73.8%
    -------------------------
The Analysis of the election disclosed the following in corresponding order:
  1. the total number of votes for this election were 369,711 votes
  2. The complete list  of candidates receiving votes is:
      a) Charles Casper Stockham
      b) Diana DeGette
      c) Raymon Anthony Doane
  3. The total #votes each received, respectively, were:
      a) 85,213
      b) 272,892
      c) 11,606
  4. The percent votes each candidate won, respectively, were:
      a) 23.0%
      b) 73.8%
      c) 3.1%
  5. The winner of the election based on popular vote was Diana DeGette
  6. The voter turnout for each county was: Jefferson 38,855; Denver 306,055; Arapahoe 24,801 voters
  7. The percentage of votes from each county out of the total votes were; Jefferson 10.5%; Denver 82.8%, Arapahoe 6.7%
  8. Therefore, the county with the greatest voter turnout was Denver
      
## Election Audit Summary
_________________________

In conclusion, the capability of Python to automate the code in order to tally the required information to determine the following was efficient:
        candidtates and counties with pecentages for both; 
        voter turnout; 
        county with the greatest turnout; 
        and elections winner 
        Additionally, the ability to convert the results to text (.txt) enables the reader to clearly determine the results, which Tom and Seth both appreciated.
    This can be translated to other congressional districts and local elections all over the US with a simple modification of the code by altering the lists and dictionaries to consider different:
        -candidate names 
        -county names
        -and results on a State and federal level.
        
