import pandas as pd
import plotly.express as px

EthnicFilePath = "data/race_and_ethnicity.csv"
EmploymentFilePath = "data/employment_by_occupations.csv"
GlobalDiversityPath = "data/global_diversity.csv"

# 1st question: largest ethnic group in New York, NY
# sorted by year (ascending) and share (descending)
def df_largest_ethnic_nyc():
    # Read the csv file with pandas
    df = pd.read_csv(EthnicFilePath)
    df_gb = df.groupby(by=['year', 'race_and_ethnic']).agg( # group by then agg to be sure
    # sometimes you got data with more dimensions, not the case here, but it avoid errors in case you forgot)
        {'share':'sum', 'population': 'sum'}).sort_values(# sort values
        by=['year', 'share'], ascending=[True, False])
        
    return df_gb

   
# 2nd question: create a treemap with plotly-express with 1st question dataframe
def treemap_ethnic_nyc():
    # get the data from the fonction of the 1st question and make a reset_index
    # to have a plain dataframeotherwise ploty-express is not going to be happy
    df = df_largest_ethnic_nyc().reset_index()
    # do the magic with ploty-express with a tree map
    tm = px.treemap(df, path=['year', 'race_and_ethnic'], values='share',
                    hover_data = ['year', 'race_and_ethnic', 'share', 'population'],
                    color='race_and_ethnic')
    # saving the treemap into an html page so we can visual it
    tm.write_html('tm_ethnic.html')


# 3rd question: Employment by occupations
def df_employment_by_occupations():
    # Read the csv file with pandas
    df = pd.read_csv(EmploymentFilePath)
    df_gb = df.groupby(by=['year', 'occupation']).agg( # group by then agg to be sure
    # sometimes you got data with more dimensions, not the case here, but it avoid errors in case you forgot)
        {'workforce':'sum'}).sort_values(# sort values
        by=['year', 'workforce'], ascending=[True, False])
    df_workforce = df_gb.groupby(level=['year'])['workforce'].sum()
    df_gb['share'] = df_gb.apply(lambda x: x.workforce / df_workforce.loc[x.name[0]], axis=1)
    return df_gb


def histogram_share_employment_by_occupations():
    df = df_employment_by_occupations().reset_index()
    histo = px.histogram(df, x='year', y='share', color='occupation')
    histo.write_html('hist_occupation.html')


# 4th question: line chart of Computer & Mathematical Occupations
def line_chart_computer_math_occupation():
    df = pd.read_csv(EmploymentFilePath)
    df_filter = df.loc[df.occupation == "Computer & Mathematical Occupations"]
    line = px.line(df_filter, x='year', y='workforce')
    line.write_html('line_computer_math.html')


# Bonus question: world map of immigration people
def world_map_global_diversity():
    df = pd.read_csv(GlobalDiversityPath).sort_values('year')
    fig = px.choropleth(
        df,
        locations='country_code',
        animation_frame='year',
        color="total_population",)
    fig.write_html('world_map.html')

