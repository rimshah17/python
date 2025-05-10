# Unit Converter

This project is a simple unit converter application built using the Streamlit library. It allows users to convert between different units of length, time, and mass.

## Project Structure

```
unit-converter
├── src
│   ├── main.py              # Entry point of the Streamlit application
│   ├── length_converter.py   # Contains LengthConverter class for length conversions
│   ├── time_converter.py     # Contains TimeConverter class for time conversions
│   └── mass_converter.py     # Contains MassConverter class for mass conversions
├── requirements.txt          # Lists the dependencies required for the project
└── README.md                 # Documentation for the project
```

## Installation

To run this project, you need to have Python installed on your machine. You can install the required dependencies using pip. 

1. Clone the repository:
   ```
   git clone <repository-url>
   cd unit-converter
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

To start the Streamlit application, run the following command in your terminal:

```
streamlit run src/main.py
```

Once the application is running, you can use the interface to convert between different units of length, time, and mass.

## Features

- Convert between various length units (meters, kilometers, miles, etc.)
- Convert between different time units (seconds, minutes, hours, etc.)
- Convert between various mass units (grams, kilograms, pounds, etc.)

## Contributing

Feel free to submit issues or pull requests if you have suggestions for improvements or new features.