import pandas as pd
from sqlalchemy import create_engine, exc
from sqlalchemy.types import Integer, String, Float

def fetch_data_from_db():
    try:
        # SQLAlchemy connection string
        engine = create_engine('mysql+mysqlconnector://root:sagar123@localhost:3306/sagarsam')

        # SQL query to fetch data from the table
        query = 'SELECT * FROM Kaggle_Employee_DB'

        # Execute the query and fetch data
        df = pd.read_sql(query, engine)

        # Print success message
        print("Data fetched successfully!")

        return df

    except exc.SQLAlchemyError as err:
        print(f"Error: {err}")
        return None

def truncate_table(engine):
    try:
        # SQL query to truncate the table
        truncate_query = 'TRUNCATE TABLE Test_Attrition_Database'

        # Execute the query
        with engine.connect() as connection:
            connection.execute(truncate_query)

        # Print success message
        print("Test_Attrition_Database table truncated successfully!")

    except exc.SQLAlchemyError as err:
        print(f"Error: {err}")

def insert_data_to_new_table(data, engine):
    try:
        # Add the Attrition_Probability column with a hardcoded value of 50
        data['Attrition_Probability'] = 50.0

        # Define the table columns and their data types
        data_columns = [
            'Age', 'Attrition', 'BusinessTravel', 'DailyRate', 'Department', 'DistanceFromHome',
            'Education', 'EducationField', 'EmployeeCount', 'EmployeeNumber', 'EnvironmentSatisfaction',
            'Gender', 'HourlyRate', 'JobInvolvement', 'JobLevel', 'JobRole', 'JobSatisfaction',
            'MaritalStatus', 'MonthlyIncome', 'MonthlyRate', 'NumCompaniesWorked', 'Over18', 'OverTime',
            'PercentSalaryHike', 'PerformanceRating', 'RelationshipSatisfaction', 'StandardHours',
            'StockOptionLevel', 'TotalWorkingYears', 'TrainingTimesLastYear', 'WorkLifeBalance',
            'YearsAtCompany', 'YearsInCurrentRole', 'YearsSinceLastPromotion', 'YearsWithCurrManager',
            'Attrition_Probability'
        ]

        # Convert dataframe columns to match MySQL table
        data = data[data_columns]

        # Define column types for insertion
        column_types = {
            'Age': Integer(),
            'Attrition': String(3),
            'BusinessTravel': String(50),
            'DailyRate': Integer(),
            'Department': String(50),
            'DistanceFromHome': Integer(),
            'Education': Integer(),
            'EducationField': String(50),
            'EmployeeCount': Integer(),
            'EmployeeNumber': Integer(),
            'EnvironmentSatisfaction': Integer(),
            'Gender': String(10),
            'HourlyRate': Integer(),
            'JobInvolvement': Integer(),
            'JobLevel': Integer(),
            'JobRole': String(50),
            'JobSatisfaction': Integer(),
            'MaritalStatus': String(20),
            'MonthlyIncome': Integer(),
            'MonthlyRate': Integer(),
            'NumCompaniesWorked': Integer(),
            'Over18': String(3),
            'OverTime': String(3),
            'PercentSalaryHike': Integer(),
            'PerformanceRating': Integer(),
            'RelationshipSatisfaction': Integer(),
            'StandardHours': Integer(),
            'StockOptionLevel': Integer(),
            'TotalWorkingYears': Integer(),
            'TrainingTimesLastYear': Integer(),
            'WorkLifeBalance': Integer(),
            'YearsAtCompany': Integer(),
            'YearsInCurrentRole': Integer(),
            'YearsSinceLastPromotion': Integer(),
            'YearsWithCurrManager': Integer(),
            'Attrition_Probability': Float()
        }

        # Insert data into the Test_Attrition_Database table
        data.to_sql('Test_Attrition_Database', con=engine, if_exists='append', index=False, dtype=column_types)

        # Print success message
        print("Data inserted successfully into Test_Attrition_Database!")

    except exc.SQLAlchemyError as err:
        print(f"Error: {err}")

if __name__ == '__main__':
    engine = create_engine('mysql+mysqlconnector://root:sagar123@localhost:3306/sagarsam')
    data = fetch_data_from_db()
    if data is not None:
        truncate_table(engine)
        insert_data_to_new_table(data, engine)
