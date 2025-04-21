from preswald import text, plotly, connect, table, slider, checkbox
import pandas as pd
import plotly.express as px

# Connect to data source
connect()

# Load the CSV file once at the start
df = pd.read_csv('data/Global_Cybersecurity_Threats.csv')

# Dashboard header
text("# Global Cybersecurity Threats Dashboard")
text("## Interactive Analysis of Cybersecurity Incidents (2015-2024)")

# Add user controls
text("### Threshold Filters")
min_loss = slider("Minimum Financial Loss (Million $)", 
                 min_val=0, 
                 max_val=int(df['Financial Loss (in Million $)'].max()),
                 default=0)

min_users = slider("Minimum Affected Users",
                  min_val=0,
                  max_val=int(df['Number of Affected Users'].max()),
                  default=0)

# Display options
text("### Display Options")
show_table = checkbox("Show Data Table", default=True)
show_summary = checkbox("Show Summary Statistics", default=True)

# Filter data based on user inputs
filtered_df = df[
    (df['Financial Loss (in Million $)'] >= min_loss) &
    (df['Number of Affected Users'] >= min_users)
]

# Display filtered data counts
text(f"### Showing {len(filtered_df)} incidents matching the selected criteria")

# Aggregate filtered data by country and attack type
country_agg = filtered_df.groupby(['Country', 'Attack Type']).agg({
    'Financial Loss (in Million $)': 'sum',
    'Number of Affected Users': 'sum'
}).reset_index()

# Create a scatter plot with aggregated data
fig = px.scatter(
    country_agg,
    x='Financial Loss (in Million $)',
    y='Number of Affected Users',
    color='Attack Type',
    hover_name='Country',
    size='Financial Loss (in Million $)',
    size_max=25,
    title='Attack Impact by Country: Financial Loss vs. Affected Users',
    labels={
        'Financial Loss (in Million $)': 'Total Financial Loss (Million $)',
        'Number of Affected Users': 'Total Affected Users'
    }
)

# Improve the layout and marker size
fig.update_layout(
    template='plotly_white',
    legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="right",
        x=0.99
    ),
    hoverlabel=dict(
        bgcolor="white",
        font_size=12
    )
)

# Set minimum marker size
fig.update_traces(marker=dict(sizemin=7))

# Show the plot
plotly(fig)

# Create a bar chart of top 10 countries by financial loss
top_countries = filtered_df.groupby('Country')['Financial Loss (in Million $)'].sum().sort_values(ascending=False).head(10)

fig2 = px.bar(
    top_countries.reset_index(),
    x='Country',
    y='Financial Loss (in Million $)',
    title='Top 10 Countries by Total Financial Loss',
    labels={
        'Country': 'Country',
        'Financial Loss (in Million $)': 'Total Financial Loss (Million $)'
    }
)

# Style the plot
fig2.update_layout(template='plotly_white')

# Show the plot
plotly(fig2)

# Show summary statistics if enabled
if show_summary:
    text("### Summary Statistics by Attack Type")
    text("This table shows the total and average impact of each type of cyberattack:")
    
    # Prepare summary statistics
    summary_df = filtered_df.groupby('Attack Type').agg({
        'Financial Loss (in Million $)': ['sum', 'mean'],
        'Number of Affected Users': ['sum', 'mean']
    }).round(2)
    
    # Rename columns for clarity and reset index
    summary_df.columns = ['Total Financial Loss (M$)', 'Average Loss per Attack (M$)', 
                         'Total Users Affected', 'Average Users per Attack']
    summary_df = summary_df.reset_index()
    
    # Sort by total financial loss to show most impactful attacks first
    summary_df = summary_df.sort_values('Total Financial Loss (M$)', ascending=False)
    
    # Display the table
    table(summary_df)

# Show full data table if enabled
if show_table:
    text("### Full Data Table")
    table(filtered_df)

# Credits and information section
text("### About This Dashboard")
text("""
This dashboard analyzes global cybersecurity threats data from 2015-2024. 
The visualizations highlight patterns in attack frequency and financial impact.

Data source: Global Cybersecurity Threats Dataset (2015-2024)
""")