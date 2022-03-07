# Mohamed Mahmoud
# Patient Symptoms Program

# - Start of the Program -

def get_potential_cases(patient_to_symptoms, symptoms_of_interest, min_symptom_count):
    names=[]
    
    for i in patient_to_symptoms.items():
        patient=i[0]
        symptom=i[1]
        count=0
        for j in symptom:
            if j in symptoms_of_interest:
                count+=1
                if count>=min_symptom_count:
                    names.append(i[0])
                    break
                
    return names
 
# ------------------------ Testing ------------------------

# patient_to_symptoms={"Mary":["cough","tired","swollen lymph nodes"],
#                      "Abdoulaye":["headache"],
#                      "Amir":["tired","cough","fever"],
#                      "Maya":[],
#                      "Yana":["breast lump","swollen lymph nodes","cough"]
#                      }
 
# covid19=["cough","fever","tired"]
# covid_candidates_2 = get_potential_cases(patient_to_symptoms, covid19, 2)
# print(covid_candidates_2)
 
# covid_candidates_3=get_potential_cases(patient_to_symptoms, covid19, 3)
# print(covid_candidates_3)
 
# breast_cancer=["tired","swollen lymph nodes","breast lump"]
# breast_cancer_candidates_2=get_potential_cases(patient_to_symptoms, breast_cancer, 2)
# print(breast_cancer_candidates_2)
 
# # # example=["cough","tired","swollen lymph nodes"]
# # # tired_example=get_potential_cases(patient_to_symptoms,example,1)
# # # print(tired_example)
 
# # # example=["headache"]
# # # tired_example=get_potential_cases(patient_to_symptoms,example,1)
# # # print(tired_example)
 
# # # example=["tired","cough","fever"]
# # # tired_example=get_potential_cases(patient_to_symptoms,example,1)
# # # print(tired_example)
 
# # # example=[]
# # # tired_example=get_potential_cases(patient_to_symptoms,example,1)
# # # print(tired_example)
 
# # # example=["breast lump","swollen lymph nodes","cough"]
# # # tired_example=get_potential_cases(patient_to_symptoms,example,1)
# # # print(tired_example)

# - End of the Program -