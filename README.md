# Global Cybersecurity Threats Dashboard

An interactive dashboard built with Preswald that visualizes global cybersecurity threats and their impacts from 2015 to 2024. The dashboard provides insights into financial losses and affected users across different countries and attack types.

## Features

- **Interactive Visualizations**:
  - Scatter plot showing the relationship between financial losses and affected users
  - Bar chart displaying top 10 countries by total financial loss
  - Summary statistics table breaking down impacts by attack type
  - Full data table with detailed incident information

- **Dynamic Filtering**:
  - Filter by minimum financial loss threshold
  - Filter by minimum affected users threshold
  - Toggle data table visibility
  - Toggle summary statistics visibility

## Prerequisites

- Python 3.7+
- Preswald library
- pandas
- plotly

## Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd [repository-name]
```

2. Install the required dependencies:
```bash
pip install preswald pandas plotly
```

3. Ensure your data file is in the correct location:
```
data/Global_Cybersecurity_Threats.csv
```

## Usage

1. Start the dashboard:
```bash
preswald run
```

2. Open your web browser and navigate to:
```
http://localhost:8502
```

## Data Structure

The dashboard expects a CSV file with the following columns:
- Year
- Country
- Attack Type
- Financial Loss (in Million $)
- Number of Affected Users

## Customization

You can customize the dashboard's appearance by:
1. Adding a custom logo at `/images/security.png`
2. Adding a custom favicon at `/images/shield.ico`
3. Modifying the `preswald.toml` file for branding configuration

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Data source: Global Cybersecurity Threats Dataset (2015-2024)
- Built with [Preswald](https://github.com/preswald)
- Visualization powered by [Plotly](https://plotly.com/) 
