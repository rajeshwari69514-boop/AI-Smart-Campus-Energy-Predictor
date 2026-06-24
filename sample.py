import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


np.random.seed(42)
records_count = 200

historical_data = {
    'Temperature_C': np.random.randint(22, 42, size=records_count),
    'Student_Count': np.random.randint(0, 180, size=records_count),
    'Hour_of_Day': np.random.randint(8, 20, size=records_count),
}


df = pd.DataFrame(historical_data)
df['Energy_Consumed_kWh'] = (df['Temperature_C'] * 1.5) + (df['Student_Count'] * 0.25) + (df['Hour_of_Day'] * 0.8) + np.random.normal(0, 3, records_count)


X = df[['Temperature_C', 'Student_Count', 'Hour_of_Day']]
y = df['Energy_Consumed_kWh']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


ai_predictor_model = LinearRegression()
ai_predictor_model.fit(X_train, y_train)

print("="*60)
print("🎯 PROTOTYPE STATUS: AI CORE PREDICTIVE ENGINE ONLINE")
print("="*60)


def get_live_campus_prediction(temp, students, hour):
    input_features = pd.DataFrame([[temp, students, hour]], columns=['Temperature_C', 'Student_Count', 'Hour_of_Day'])
    predicted_load = ai_predictor_model.predict(input_features)[0]
    
    print(f"\n🔮 LIVE CAMPUS MATRIX INPUTS:")
    print(f"   ↳ Ambient Temperature : {temp}°C")
    print(f"   ↳ Classroom Occupancy : {students} Students registered")
    print(f"   ↳ Planned Time Slot   : {hour}:00 Hours")
    print(f"📊 ML ENGINE OUTPUT PREDICTION:")
    print(f"   ↳ Estimated Grid Demand: {predicted_load:.2f} kWh")
    
    
    if students == 0 and predicted_load > 15:
        print("⚠️ SUSTAINABILITY WARNING: Zero occupancy but energy spike detected. Suggesting manual HVAC cutoff overrides.")
    else:
        print("✅ GRID STATUS: Balanced footprint efficiency optimized.")
    print("="*60)


get_live_campus_prediction(temp=34, students=120, hour=14) 
get_live_campus_prediction(temp=26, students=0, hour=18)  
