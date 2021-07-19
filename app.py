from flask import Flask,render_template,request
import pickle
import numpy as np
# import x

model = pickle.load(open('model.pkl', 'rb'))
app=Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/water_quality",methods=['GET','POST'])
def predict_quality():
    inputs=[]
    inputs2=[]
    potable=-1
    potability=-1
    if request.method=='POST':
        # print('NOt working')
        ph=float(request.form.get('ph'))
        # print(gust_dir)
        hardness=float(request.form.get('hardness'))
        tds=float(request.form.get('tds'))
        chloramines=float(request.form.get('chloramines'))
        sulfate=float(request.form.get('sulfate'))
        conductivity=float(request.form.get('conductivity'))
        organic_carbon=float(request.form.get('organic_carbon'))
        trihalomethanes=float(request.form.get('trihalomethanes'))
        turbidity=float(request.form.get('turbidity'))

        inputs=[ph,hardness,tds,chloramines,sulfate,conductivity,organic_carbon,trihalomethanes,turbidity]
        # print(inputs)
        inputs_np=np.array([inputs])
        # print(inputs_np.shape)
        # print(inputs_np)
        potable=model.predict(inputs_np)[0] 
        potability=model.predict_proba(inputs_np)[0][1]
        print(potability)
        potability=potability*100
    else:
        print('NOt working')
    return render_template('index.html',safe=potable,percent_of_safety=potability)

if __name__=='__main__':
    app.run(debug=True)