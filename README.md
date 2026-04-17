# Tracking BINI in the Spotify Global Track Charts in the aftermath of their Coachella virality

![BINI in Coachella 2026 Week 1](images/bini.png)

## Context:

BINI made history last weekend by debuting as the first Filipino act to perform in the highly-anticipated and celebrated Coachella Valley Music Festival 2026. The P-Pop powerhouse group became an unexpected star of the season, with people from all around the world, both casuals and fans, unanimously amazed by their production, stage-presence, and talent. 

However, despite the group becoming the talk of social media, the big question that we now ask is whether their virality translated well to the charts. 

## Project Description
This project aims to determine the impact of BINI's virality following their unprecedented Filipino act performance in Coachella 2026 Week 1. Using the data scraped from SpotifyCharts website, we look into BINI's ranking throughout the months, placing emphasis on the difference before and after their Coachella set.

**Tags**: _time-series forecasting_, _web scraping_, _music analytics_, _data analysis_

### Data Source

-> [Spotify Global Charts](https://charts.spotify.com/charts/overview/global)

**Time Window:** Pre-Coachella vs. Post-Coachella Week 1 (January 1, 2026 - April 17, 2026)

### Key Questions
- How big of a jump did BINI make in the chart?
- Which songs benefitted the most?
- Are there observable trends before vs. after Coachella?

### Visualizations
- Daily Rank Trajectory per track
- Peak positions and chart duration
- Before vs. After Coachella Comparison


## Codebase
- /data: destination directory for the csvs collected 
- scraper.py: scrapes Spotify charts and saves data to csv
- main.ipynb: EDA and showcasing of results


### Future Additions
- NLP : Comparing articles that came before vs. after their Coachella Set
- Forecasting future performance chart

