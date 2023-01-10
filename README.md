# Solus-Scraper

## Why This Was Made
This project was created for Owen Lem's successful campaign for the position of rector for Queen's Univerity. This rector election was the most contested election in 10 years with 6 total candidates. Within this campaign I was lead digital strategist and underwent the task of determining the most effective classes for Owen to directly campaign to. In order to determine the most effective classes to target the most effective strategy I determined was to determine the largest class sizes by enrollment and cross reference that with classes that are most commonly taken in conjunction with eachother. Determining which classes are commonly taken in conjunction was not hard to determine based on common interest, course level and class requirements by program. The issue came with determining which classes had the highest enrollment rates as this is not publicly available information published by the university. The only way to determine class enrollment is through Queen's online solus portal which shows current class enrollment, however aggregating the data of over 1500 total classes by hand would be extremely time consuming, hence why I decided to create this script to aggregate said data for Owen's campaign. 

## Design Choices
The solus site is constructed unlike most website and makes almost no use of path based routing and instead almost entirely uses header based routing, which made headless scraping considerably more complicated. Due to this and the fact that speed was not a constraint in creating this script and the fact that the data set being collected was relatively small I decided to use frontend scraping with selenium and a chrome webdriver in order to circumvent solus' antibot measures.

## How to run this
Sadly, Queens has entirely redesigned solus and therefore this script is now deprecated with the current solus release.
