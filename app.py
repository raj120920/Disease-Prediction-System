from flask import Flask, render_template, url_for, request
import sqlite3
import pandas as pd
import numpy as np

app = Flask(__name__)

db_locale='patient.db'



@app.route('/')
@app.route('/home')
def home():
    return render_template('Tarp.html')



@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/symptoms', methods=['POST','GET'])
def symptoms():
    addpatient()
    return render_template('tarp123.html')



@app.route('/records', methods=['POST','GET'])
def records():
    adddisease()
    patient_data=query_patients()
    disease_data=query_disease()
    final_data=query_final()
    return render_template('records.html',patient_data=patient_data,disease_data=disease_data,final_data=final_data)



@app.route('/result',methods=['POST','GET'])
def result():
    symptom = pd.read_csv('data.csv')
    df = pd.DataFrame(symptom) 
    from sklearn.utils import shuffle
    df = shuffle(df)
    X = df.loc[: ,symptom.columns != ('prognosis')]
    y = df['prognosis']
    from sklearn.neighbors import KNeighborsClassifier
    knn = KNeighborsClassifier(n_neighbors=1)
    print(knn)
    knn.fit(X,y)
    if request.method == 'POST':
        Itching = request.form.get('Itching')
        Skin_Rash = request.form.get('Skin Rash')
        Nodal_Skin_Eruption = request.form.get('Nodal Skin Eruption')
        continuous_sneezing = request.form.get('continuous_sneezing')
        shivering = request.form.get('shivering')
        chills = request.form.get('chills')
        Joint_Pain = request.form.get('Joint Pain')
        Stomach_Pain = request.form.get('Stomach Pain')
        acidity = request.form.get('acidity')
        ulcers_on_tongue = request.form.get('ulcers_on_tongue')
        Muscle_Wasting = request.form.get('Muscle Wasting')
        Vomiting = request.form.get('Vomiting')
        Burining_Micturition = request.form.get('Burining Micturition')
        Spotting_Urination = request.form.get('Spotting Urination')
        fatigue = request.form.get('fatigue')
        weight_gain = request.form.get('weight_gain')
        anxiety = request.form.get('anxiety')
        cold_hands_and_feets = request.form.get('cold_hands_and_feets')
        mood_swings = request.form.get('mood_swings')
        weight_loss = request.form.get('weight_loss')
        restlessness = request.form.get('restlessness')
        lethargy = request.form.get('lethargy')
        Patchy_Throat = request.form.get('Patchy Throat')
        irregular_sugar_levels = request.form.get('irregular_sugar_levels')
        cough = request.form.get('cough')
        high_fever = request.form.get('high_fever')
        Sunken_Eyes = request.form.get('Sunken Eyes')
        breathlesness = request.form.get('breathlesness')
        sweating = request.form.get('sweating')
        dehydration = request.form.get('dehydration')
        Indigestion = request.form.get('Indigestion')
        headache = request.form.get('headache')
        Yellowish_Skin = request.form.get('Yellowish Skin')
        Dark_Urine = request.form.get('Dark Urine')
        Nausea = request.form.get('Nausea')
        loss_of_appetite = request.form.get('loss_of_appetite')
        Pain_behind_Eyes = request.form.get('Pain behind Eyes')
        Back_Pain = request.form.get('Back Pain')
        Constipation = request.form.get('Constipation')
        Abdominal_Pain = request.form.get('Abdominal Pain')
        Diarrhoea = request.form.get('Diarrhoea')
        mild_fever = request.form.get('mild_fever')
        Yellow_Urine = request.form.get('Yellow Urine')
        Yellowing_of_Eyes = request.form.get('Yellowing of Eyes')
        acute_liver_failure = request.form.get('acute_liver_failure')
        fluid_overload = request.form.get('fluid_overload')
        Swelling_Stomach = request.form.get('Swelling Stomach')
        Swelling_Lymph_node = request.form.get('Swelling Lymph node')
        malaise = request.form.get('malaise')
        blurred_and_distorted_vision = request.form.get('blurred_and_distorted vision')
        Phlegm = request.form.get('Phlegm')
        Throat_Irritation = request.form.get('Throat Irritation')
        Redness_of_Eyes = request.form.get('Redness-of Eyes')
        Sinus_Pressure = request.form.get('Sinus Pressure')
        Running_Nose = request.form.get('Running Nose')
        Congestion = request.form.get('Congestion')
        Chest_Pain = request.form.get('Chest Pain')
        Weak_Limbs = request.form.get('Weak Limbs')
        fast_heart_rate = request.form.get('fast_heart_rate')
        Pain_in_Bowel_Movem = request.form.get('Pain_in Bowel Movem')
        Pain_in_Anal_region = request.form.get('Pain_in Anal region')
        Bloody_Stool = request.form.get('Bloody Stool')
        Anus_Irritation = request.form.get('Anus Irritation')
        Neck_Pain = request.form.get('Neck Pain')
        dizziness = request.form.get('dizziness')
        Cramps = request.form.get('Cramps')
        Bruising = request.form.get('Bruising')
        obesity = request.form.get('obesity')
        Swollen_Legs = request.form.get('Swollen Legs')
        swollen_blood_vessel = request.form.get('swollen_blood_vessel')
        Puffy_Face_Eyes = request.form.get('Puffy(Face,Eyes)')
        Enlarged_Thyroid = request.form.get('Enlarged Thyroid')
        Brittle_Nails = request.form.get('Brittle Nails')
        Swollen_Extremities = request.form.get('Swollen Extremities')
        excessive_hunger = request.form.get('excessive_hunger')
        extra_marital_contacts = request.form.get('extra_marital_contacts')
        Drying_Tingling_Lips = request.form.get('Drying Tingling Lips')
        slurred_speech = request.form.get('slurred_speech')
        Knee_Pain = request.form.get('Knee Pain')
        Hip_Joint_Pain = request.form.get('Hip Joint Pain')
        Muscle_Weakness = request.form.get('Muscle Weakness')
        Stiff_Neck = request.form.get('Stiff Neck')
        Swelling_Joints = request.form.get('Swelling Joints')
        Stiff_Movement = request.form.get('Stiff Movement')
        spinning_movements = request.form.get('spinning_movements')
        loss_of_balance = request.form.get('loss_of_balance')
        unsteadiness = request.form.get('unsteadiness')
        Weakness_in_one_Body_Side = request.form.get('Weakness_in one Body Side')
        loss_of_smell = request.form.get('loss_of_smell')
        Bladder_Discomfort = request.form.get('Bladder Discomfort')
        Urine_Foul_Smell = request.form.get('Urine Foul Smell')
        Continous_feel_of_Urine = request.form.get('Continous feel of Urine')
        Passage_of_Gases = request.form.get('Passage of Gases')
        Internal_Itching = request.form.get('Internal Itching')
        toxic_look_typhos = request.form.get('toxic_look_(typhos)')
        depression = request.form.get('depression')
        irritability = request.form.get('irritability')
        Muscle_Pain = request.form.get('Muscle Pain')
        altered_sensorium = request.form.get('altered_sensorium')
        Red_Spots_over_Body = request.form.get('Red Spots over Body')
        Belly_Pain = request.form.get('Belly Pain')
        Abnormal_Menstruation = request.form.get('Abnormal Menstruation')
        Dischromatic_Patches = request.form.get('Dischromatic Patches')
        Watering_from_Eyes = request.form.get('Watering_from Eyes')
        increased_appetite = request.form.get('increased_appetite')
        Polyuria = request.form.get('Polyuria')
        family_history = request.form.get('family_history')
        Mucoid_Sputum = request.form.get('Mucoid Sputum')
        Rusty_Sputum = request.form.get('Rusty Sputum')
        lack_of_concentration = request.form.get('lack_of_concentration')
        visual_disturbances = request.form.get('visual_disturbances')
        receiving_blood_transfusion = request.form.get('receiving_blood_transfusion')
        receiving_unsterile_injections = request.form.get('receiving_unsterile_injections')
        coma = request.form.get('coma')
        Stomach_Bleeding = request.form.get('Stomach Bleeding')
        Abdomen_Distention = request.form.get('Abdomen Distention')
        history_of_alcohol_consumption = request.form.get('history_of_alcohol_consumption')
        fluid_overload1 = request.form.get('fluid_overload1')
        Blood_in_Sputum = request.form.get('Blood_in Sputum')
        Viens_on_Calf = request.form.get('Viens on Calf')
        palpitations = request.form.get('palpitations')
        Painful_Walking = request.form.get('Painful Walking')
        Puss_filled_Pimples = request.form.get('Puss filled Pimples')
        Blackheads = request.form.get('Blackheads')
        Scurring = request.form.get('Scurring')
        Skin_Peeling = request.form.get('Skin Peeling')
        Silver_like_Dusting = request.form.get('Silver like Dusting')
        Small_dents_in_Nails = request.form.get('Small dents_in Nails')
        Inflamatory_Nails = request.form.get('Inflamatory Nails')
        Blister = request.form.get('Blister')
        Red_Sore_around_Nose = request.form.get('Red Sore around Nose')
        Yellow_Crust_Ooze = request.form.get('Yellow Crust Ooze')


        data = ([Itching,Skin_Rash,Nodal_Skin_Eruption,continuous_sneezing,shivering,chills,Joint_Pain,Stomach_Pain,acidity,
         ulcers_on_tongue,Muscle_Wasting,Vomiting,Burining_Micturition,Spotting_Urination,fatigue,weight_gain,anxiety,
         cold_hands_and_feets,mood_swings,weight_loss,restlessness,lethargy,Patchy_Throat,irregular_sugar_levels,cough,
         high_fever,Sunken_Eyes,breathlesness,sweating,dehydration,Indigestion,headache,Yellowish_Skin,Dark_Urine,Nausea,
         loss_of_appetite,Pain_behind_Eyes,Back_Pain,Constipation,Abdominal_Pain,Diarrhoea,mild_fever,Yellow_Urine,
         Yellowing_of_Eyes,acute_liver_failure,fluid_overload,Swelling_Stomach,Swelling_Lymph_node,malaise,blurred_and_distorted_vision,
         Phlegm,Throat_Irritation,Redness_of_Eyes,Sinus_Pressure,Running_Nose,Congestion,Chest_Pain,Weak_Limbs,fast_heart_rate,
         Pain_in_Bowel_Movem,Pain_in_Anal_region,Bloody_Stool,Anus_Irritation,Neck_Pain,dizziness,Cramps,Bruising,obesity,
         Swollen_Legs,swollen_blood_vessel,Puffy_Face_Eyes,Enlarged_Thyroid,Brittle_Nails,Swollen_Extremities,excessive_hunger,
         extra_marital_contacts,Drying_Tingling_Lips,slurred_speech,Knee_Pain,Hip_Joint_Pain,Muscle_Weakness,Stiff_Neck,Swelling_Joints,
         Stiff_Movement,spinning_movements,loss_of_balance,unsteadiness,Weakness_in_one_Body_Side,loss_of_smell,Bladder_Discomfort,Urine_Foul_Smell,
         Continous_feel_of_Urine,Passage_of_Gases,Internal_Itching,toxic_look_typhos,depression,irritability,Muscle_Pain,
         altered_sensorium,Red_Spots_over_Body,Belly_Pain,Abnormal_Menstruation,Dischromatic_Patches,Watering_from_Eyes,
         increased_appetite,Polyuria,family_history,Mucoid_Sputum,Rusty_Sputum,lack_of_concentration,visual_disturbances,receiving_blood_transfusion,
         receiving_unsterile_injections,coma,Stomach_Bleeding,Abdomen_Distention,history_of_alcohol_consumption,fluid_overload1,
         Blood_in_Sputum,Viens_on_Calf,palpitations,Painful_Walking,Puss_filled_Pimples,Blackheads,Scurring,Skin_Peeling,
         Silver_like_Dusting,Small_dents_in_Nails,Inflamatory_Nails,Blister,Red_Sore_around_Nose,Yellow_Crust_Ooze])

        
        my_prediction = knn.predict([data])
        pred_val = my_prediction[0]
    pd.set_option('display.max_colwidth',-1)
    precaution=pd.read_csv('symptom_precaution.csv',encoding='latin1')
    precau=(precaution.loc[precaution['Disease']==pred_val])
    prec = precau.filter(like='Precaution').to_string(index=False,header=False)
    return render_template('result.html',prediction = pred_val, prec = prec)



@app.route('/addpatient',methods=['GET','POST'])
def addpatient():
    if request.method=="GET":
        return render_template('Tarp.html')
    else:
        patient_details=(
            request.form['name'],
            request.form['phone'],
            request.form['age'],
            request.form['height'],
            request.form['weight']
        )
    insertdetails(patient_details)


def insertdetails(patient_details):
    connie=sqlite3.connect(db_locale)
    c=connie.cursor()
    sql_execute_string="INSERT INTO patients (name,phn,age,height,weight,date) VALUES (?,?,?,?,?,date('now'))"
    c.execute(sql_execute_string,patient_details)
    connie.commit()
    connie.close()
    print(patient_details)

def query_patients():
    connie=sqlite3.connect(db_locale)
    c=connie.cursor()
    c.execute("""
        SELECT * FROM patients
    """)
    patientdata = c.fetchall()
    return patientdata


def insertdisease(disease_details):
    connie=sqlite3.connect(db_locale)
    c1=connie.cursor()
    sql_execute_string='INSERT INTO disease (disease) VALUES (?)'
    c1.execute(sql_execute_string,disease_details)
    connie.commit()
    connie.close()
    print(disease_details)


@app.route('/adddisease',methods=['GET','POST'])
def adddisease():
    if request.method=="GET":
        return render_template('Tarp.html')
    else:

        disease_details=(
            request.form['dise'],
        )
    insertdisease(disease_details)

def query_disease():
    connie=sqlite3.connect(db_locale)
    c1=connie.cursor()
    c1.execute("""
        SELECT * FROM disease
    """)
    disease = c1.fetchall()
    return disease



def query_final():
    connie=sqlite3.connect(db_locale)
    c=connie.cursor()

    c.execute("""

    SELECT patients.id, patients.date, patients.name, patients.phn, patients.age, patients.height, patients.weight, disease.disease
    FROM patients
    INNER JOIN disease ON patients.id=disease.id WHERE patients.phn=8369420057;

    """)

    datafinal = c.fetchall()
    return datafinal

if __name__ == '__main__':
    app.run(debug=True)

