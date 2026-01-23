# MAIN IDEA:

    want to see ideal times of year/days to go skiing on east coast resorts -> best conidtions -> terrain availability, snow quality, weather
    
        Terrain availability:
            % of trails open
            % of lifts open
            % of acres open (optional)
        
        Snow Quality:
            base depth (in)
            24-72 hour snowfall (in)
            season total snowfall (in)
            snowmaking (in)
        
        Weather 
            temp
            rain (flag)
            freeze/thaw cycles?

    Raw Resort Data
        - resort id
        - resort name
        - date
        - trails open
        - lifts open
        - base depth (in)
        - snowfall 24hr
        - snowfall 72hr
        - season snowfall total
        - scraped timestamp
        - source url
    Raw Weather Data
        - resort id
        - resort name
        - date
        - temp high
        - temp low
        - precipitation type
        - precipitation (in)

    Derived Resort data
        - ski_score
        - trails_open_pct
        - lifts_open_pct
        - days since last snow
        - optimal temp (flag)
        - powder day score (weighted score of fresh snow + temp/weather)
    
    Resort Metadata
        - resort id
        - name
        - latitude
        - longitude
        - state
        - elevation base
        - elevation summit
        - trails total
        - lifts total
        - acres
        - avg annual snow (in)
    
**RESOURCES:**

    resort data: OnTheSnow.com, SkiResort.com, https://www.snow-forecast.com/resorts/Killington/6day/mid
    https://www.onthesnow.com/vermont/killington-resort/skireport
    weather data: NOAA, NWS, VisualCrossing Weather API


## PLAN 

**STEP 1: initial set up**

    - set up postgreSQL database in docker
    - get environment variable for visual crossing api and postgreSQL
    - figure out web scraping for resort data; will be different for each site maybe look into website with historical resort data

**STEP 2: EXTRACT**

    - raw data folder for resort conditions and weather
    - logic for resort scraping
    - logic for weather api
    - remember: just extracting raw data nothing more

**STEP 3: LOAD**

    - load raw data into postgreSQL
    - psycopg2 to connect to db in docker
    - initialize schemas for raw, core, mart

**STEP 4: TRANSFORM**

    - set up dbt for transform 
    - need to do some research for this STEP
    - dbt models in SQL for core (facts) and mart (opinions)
    - dbt test and dbt docs generate

**STEP 5: VISUALIZE**

    - decide on tableau or power BI
    - show best ski days for each resort
    - comparative base layers

**STEP 6: ORCHESTRATION**

    - apache airflow DAG for extracting new data every (day ? week?)


