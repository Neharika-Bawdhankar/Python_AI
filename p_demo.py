import pandas as pd

df = pd.read_csv(r"D:\Protek\Workbook\Workbook\Pandas\emp.csv")
# print(df)
# print(df.shape)
# rows, columns = df.shape
# print("Number of rows:", rows)
# print("Number of columns:", columns)

# print(df.head(2))
# print(df.tail(2))

# print(df.columns)

# print(df['fname'])
# print(df.lname)

# print(df[['fname','lname','salary']])

# print(df['salary'].max())
# print(df[df.salary>15000])

# print(df.index)

# df = pd.read_csv("D:\Protek\Workbook\Workbook\Pandas\emp.csv", header=None, names=['id', 'fname', 'lname', 'dept', 'salary'])

# df = pd.read_csv("D:\Protek\Workbook\Workbook\Pandas\emp.csv", nrows=3)  # Read only the first 3 rows of the CSV file

# df = pd.read_csv("D:\Protek\Workbook\Workbook\Pandas\emp.csv", na_values=["not available","n.a."])

# df = pd.read_csv("D:\Protek\Workbook\Workbook\Pandas\emp.csv", na_values={
#     'phone': ['not available', 'n.a.'],
#     'email': ['not available', 'n.a.'],
#     'salary': ['not available', 'n.a.', '-1']    
# })
# print(df)

# df.to_csv("D:\Protek\Workbook\Workbook\Pandas\emp_output.csv", index=False , header=False)
#     # This will write the DataFrame to a CSV file without including the index and with the default header.

# df.to_csv("D:\Protek\Workbook\Workbook\Pandas\emp_output.csv", columns= ['fname','lname', 'salary'])
#     # This will write only the specified columns to the output CSV file, excluding the others.

# def convert_people_cell(cell):
#     if cell == 'not available' or cell == 'n.a.':
#         return 'Sam walton'
#     return cell

# def convert_eps_cell(cell):
#     if cell == 'not available' or cell == 'n.a.':
#         return None
#     return cell

# df = pd.read_csv("D:\Protek\Workbook\Workbook\Pandas\emp.csv", converters={
#     'people': convert_people_cell,
#     'eps': convert_eps_cell
#     })

df_stocks = pd.DataFrame({
    'tickers': ['AAPL', 'GOOGL', 'MSFT'],
    'prices': [150.25, 2800.50, 300.75],
    'pe': [30.5, 35.2, 28.7],
    'eps': [5.0, 8.0, 10.0]
})

df_weather = pd.DataFrame({
    'city': ['New York', 'Los Angeles', 'Chicago'],
    'temperature': [75, 85, 70],
    'humidity': [60, 50, 65]
})

with pd.ExcelWriter("stocks_weather.xlsx") as writer:
    df_stocks.to_excel(writer, sheet_name='Stocks')
    df_weather.to_excel(writer, sheet_name='Weather')