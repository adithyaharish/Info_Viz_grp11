import pandas as pd
import plotly.graph_objects as go

# Read the agriculture data
agriculture_data = pd.read_csv('data.csv')

# Filter out the data for the desired year
agriculture_data = agriculture_data[(agriculture_data['Year'] == 2016)]

# Group the data by state and commodity, and calculate the total production
state_commodity_production = agriculture_data.groupby(['State', 'Commodity']).agg({' PRODUCTION, MEASURED IN $': 'sum'}).reset_index()

# Create a Sankey diagram
fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=state_commodity_production['State'].unique().tolist() + state_commodity_production['Commodity'].unique().tolist(),
        color="blue"
    ),
    link=dict(
        source=state_commodity_production['State'].apply(lambda x: state_commodity_production['State'].unique().tolist().index(x)),
        target=state_commodity_production['Commodity'].apply(lambda x: len(state_commodity_production['State'].unique().tolist()) + state_commodity_production['Commodity'].unique().tolist().index(x)),
        value=state_commodity_production[' PRODUCTION, MEASURED IN $'],
        color="rgba(255, 165, 0, 0.5)"  # Set custom color
    )
)])

# Update layout
fig.update_layout(title='Production Flow of Different Crops Across States (Year 2016)')

# Show the plot
fig.show()