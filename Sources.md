# Investigating the Effectiveness of Non-pharmaceutical Interventions on COVID-19

This file serves as references of the invervention data used in the project I have co-authored with Angelina Wong, *"Investigating the Effectiveness of Non-pharmaceutical Interventions on COVID-19"*. This project worked on 14 European countries, namely:

1. Denmark
2. Italy
3. Germany
4. Spain
5. United Kingdom
6. France
7. Norway
8. Belgium
9. Austria
10. Sweden
11. Switzerland
12. Greece
13. The Netherlands
14. Portugal

## Infection & Fatality Data

Infection & fatality data was taken until 2nd December 2020, extracted with a [Javascript script](/Infection%20Fatality%20Data/read-worldometer.js). Extracted *.csv* file can be found [here](Infection%20Fatality%20Data/COVID-19-up-to-date-eu-02-12.csv)

- "Worldometer." https://www.worldometers.info/

## Interventions Included

Most intervention data were collected from [government sources](#government-sources), later verified with [credible news sources](#credible-news-sources). We extracted data manually into various *.csv* files, and with the help of a self-made [Python script](/Intervention%20Data/decode_interventions.py), transforming it into a sequence of floats between 0 and 1, found in [here](/Intervention%20Data/python-script-output/)

## Government Sources

- "Austria Interventions." https://www.bmbwf.gv.at/Ministerium/Presse.html
- "Belgium Interventions." https://www.info-coronavirus.be/en/
- "Denmark Interventions." https://coronasmitte.dk/
- "France Interventions." https://web.archive.org/web/*/https://www.gouvernement.fr/en/coronavirus-covid-19
- "Germany Government Interventions." https://www.bundesregierung.de/breg-de/themen/coronavirus/mpk-1730186
- "Germany Government Interventions Daily Updates." https://web.archive.org/web/20200720080246/https://www.rki.de/DE/Home/homepage_node.html
- "Greece Interventions." https://covid19.gov.gr/schedio-stadiakis-apoklimakosis-perioristikon-metron/
- "Italy Interventions." http://www.salute.gov.it/portale/nuovocoronavirus/archivioNotizieNuovoCoronavirus.jsp
- "Netherlands Interventions." https://www.government.nl/government/news
- "Norway Interventions." https://www.regjeringen.no/en/topics/koronavirus-covid-19/id2692388/
- "Portugal Interventions." https://www.visitportugal.com/en/node/421175
- "Spain Interventions." https://www.mscbs.gob.es/gabinete/notasPrensa.do
- "Sweden Government Interventions." https://www.folkhalsomyndigheten.se/nyheter-och-press/nyhetsarkiv/2020/
- "Switzerland Government Interventions." https://www.bag.admin.ch/bag/de/home/das-bag/aktuell/medienmitteilungen.html?dyn_startDate=01.01.2016
- "UK Government Interventions." https://www.gov.uk/coronavirus

## Credible News Sources

- "Euronews." https://www.euronews.com/
- "Reuters." https://www.reuters.com/
- "BBC News." http://www.bbc.com/news
