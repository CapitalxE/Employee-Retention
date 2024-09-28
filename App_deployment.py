import streamlit as st
import pandas as pd
import joblib

# Load your trained machine learning model
model = joblib.load("my_model.pkl")

# Define mappings according to your preprocessing
gender_mapping = {'Male': 0, 'Female': 1, 'Other': 2}
experience_mapping = {'Has relevent experience': 1, 'No relevent experience': 0}
enrolment_mapping = {'no_enrollment': 0, 'Part time course': 1, 'Full time course': 2}
education_mapping = {'Primary School': 0, 'High School': 1, 'Graduate': 2, 'Masters': 3, 'Phd': 4}
major_mapping = {'No Major': 0, 'STEM': 1, 'Humanities': 2, 'Business Degree': 3, 'Arts': 4, 'Other': 5}
company_size_mapping = {'Microenterprise': 0, 'Small enterprise': 1, 'Medium-sized enterprise': 2, 'Large enterprise': 3, 'MNC': 4}
company_type_mapping = {'Pvt Ltd': 5, 'Public Sector': 4, 'Funded Startup': 1, 'NGO': 2, 'Early Stage Startup': 0, 'Other': 3}
last_new_job_mapping = {'never': 0, '1': 1, '2': 2, '3': 3, '4': 4, '4+': 5}
experience_years_mapping = {'Fresher': 1, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 
                            '10': 10, '11': 11, '12': 12, '13': 13, '14': 14, '15': 15, '16': 16, '17': 17, '18': 18, 
                            '19': 19, '20+': 20}

# Define a function to make predictions
def predict_employee_retention(data):
    # Convert the list to a DataFrame
    input_df = pd.DataFrame(data, columns=['city_development_index', 'gender', 'relevent_experience', 'enrolled_university',
                                           'education_level', 'major_discipline', 'experience', 'company_size', 
                                           'company_type', 'last_new_job', 'training_hours'])
    
    # Make prediction
    prediction = model.predict(input_df)
    return prediction

# Streamlit app
st.title('🚀 Employee Retention Prediction')

# Input fields for the user to provide data for prediction
st.header('🔍 Input Employee Details')

def user_input_features():
    # Add a slider for City Development Index using precision up to 3 decimal places
    city_development_index = st.slider('🏙️ City Development Index', min_value=0.400, max_value=1.000, step=0.001, value=0.898)

    gender = st.selectbox("👤 Gender", list(gender_mapping.keys()))
    relevent_experience = st.selectbox("💼 Relevant Experience", list(experience_mapping.keys()))
    enrolled_university = st.selectbox("🎓 Enrolled University", list(enrolment_mapping.keys()))
    education_level = st.selectbox("📚 Education Level", list(education_mapping.keys()))
    major_discipline = st.selectbox("🏫 Major Discipline", list(major_mapping.keys()))
    experience = st.selectbox("🗓️ Experience (Years)", list(experience_years_mapping.keys()))
    company_size = st.selectbox("🏢 Company Size", list(company_size_mapping.keys()))
    company_type = st.selectbox("🏭 Company Type", list(company_type_mapping.keys()))
    last_new_job = st.selectbox("📅 Last New Job (Years)", list(last_new_job_mapping.keys()))
    training_hours = st.slider("📈 Training Hours", min_value=1, max_value=340, value=36)

    # Apply the mapping to the input values
    gender_mapped = gender_mapping[gender]
    relevent_experience_mapped = experience_mapping[relevent_experience]
    enrolled_university_mapped = enrolment_mapping[enrolled_university]
    education_level_mapped = education_mapping[education_level]
    major_discipline_mapped = major_mapping[major_discipline]
    company_size_mapped = company_size_mapping[company_size]
    company_type_mapped = company_type_mapping[company_type]
    last_new_job_mapped = last_new_job_mapping[last_new_job]
    experience_mapped = experience_years_mapping[experience]

    # Create a list with the mapped inputs
    data = [[city_development_index, gender_mapped, relevent_experience_mapped, enrolled_university_mapped,
             education_level_mapped, major_discipline_mapped, experience_mapped, company_size_mapped, company_type_mapped,
             last_new_job_mapped, training_hours]]

    return data

# Predict and display result
input_data = user_input_features()

if st.button('🔮 Predict'):
    prediction = predict_employee_retention(input_data)
    
    if prediction == 1:
        st.success('🚶 The employee is likely to **leave**.')
    else:
        st.success('🎉 The employee is likely to **stay**.')
