import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from math import sqrt
import statsmodels as sm
import statsmodels.formula.api as smf

def analyze_energy_data(csv_file):
    df = pd.read_csv(csv_file)
    df.rename(columns={'X1': 'Relative_Compactness', 
                       'X2': 'Surface_Area', 
                       'X3': 'Wall_Area', 
                       'X4': 'Roof_Area', 
                       'X5': 'Overall_Height', 
                       'X6': 'Orientation', 
                       'X7': 'Glazing_Area', 
                       'X8': 'Glazing_Area Distribution', 
                       'Y1': 'Heating_Load', 
                       'Y2': 'Cooling_Load'}, inplace=True)

    # fit models
    model_heating = smf.ols('Heating_Load ~ Roof_Area + Overall_Height + Surface_Area', data=df).fit()
    model_cooling = smf.ols('Cooling_Load ~ Roof_Area + Overall_Height + Surface_Area', data=df).fit()

    # print summaries
    print("\nHeating Summary\n")
    print(model_heating.summary())
    print("\nCooling Summary\n")
    print(model_cooling.summary())

    # extract coefficients
    heating_intercept = -28.8430
    heating_coefficient_ra = -0.0747  
    heating_coefficient_oh = 5.5208
    heating_coefficient_sa = 0.0527

    cooling_intercept = -27.7532
    cooling_coefficient_ra = -0.0380  
    cooling_coefficient_oh = 5.7617
    cooling_coefficient_sa = 0.0429

    # make predictions
    df['Predicted_Heating_Load'] = heating_intercept + (df['Roof_Area'] * heating_coefficient_ra) + (df['Overall_Height'] * heating_coefficient_oh) + (df['Surface_Area'] * heating_coefficient_sa)
    df['Predicted_Cooling_Load'] = cooling_intercept + (df['Roof_Area'] * cooling_coefficient_ra) + (df['Overall_Height'] * cooling_coefficient_oh) + (df['Surface_Area'] * cooling_coefficient_sa)

    # plot Heating Load predictions
    titleline_heating = f'Heating model predictions based off correlation \nR squared = {model_heating.rsquared:.3f} \nRMSE = {sqrt(model_heating.mse_total):.2f}'

    plt.figure(figsize=(8, 4))
    plt.plot(df['Heating_Load'], '.', color='red')
    plt.plot(df['Predicted_Heating_Load'], '.', color='blue')
    plt.xlabel('heating load (BTU)')
    plt.legend(['Observations','Model Prediction'])
    plt.title(titleline_heating)
    plt.show()

    titleline_cooling = f'Cooling model predictions based off correlation \nR squared = {model_cooling.rsquared:.3f} \nRMSE = {sqrt(model_cooling.mse_total):.2f}'

    plt.figure(figsize=(8, 4))
    plt.plot(df['Cooling_Load'], '.', color='red')
    plt.plot(df['Predicted_Cooling_Load'], '.', color='blue')
    plt.xlabel('cooling load (BTU)')
    plt.legend(['Observations','Model Prediction'])
    plt.title(titleline_cooling)
    plt.show()

    input1 = int(input("roof area: "))
    input2 = int(input("overall height: "))
    input3 = int(input("surface area: "))
    
    heating_user_prediction = heating_intercept + (heating_coefficient_ra * input1) + (heating_coefficient_oh * input2) + (heating_coefficient_sa * input3)
    print("heating load prediction: ", heating_user_prediction, "BTU")
    
    cooling_user_prediction = cooling_intercept + (cooling_coefficient_ra * input1) + (cooling_coefficient_oh * input2) + (cooling_coefficient_sa * input3)
    print("cooling load prediction: ", cooling_user_prediction, "BTU")

analyze_energy_data('ENB2012data.csv')
