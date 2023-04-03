from flask import Flask,request,jsonify,render_template
import pickle

app=Flask(__name__)

model=pickle.load(open("model.pkl","rb"))

@app.route("/")
def home():
    return render_template("front.html")

@app.route("/predict",methods=['POST','GET'])
def predict():
        hei=float(request.form['number'])
        wei=float(request.form['wei'])
        prediction=int(model.predict([[hei]]))
        if(wei>=prediction-5 and wei<=prediction+5):
            return render_template('front.html',pred='Your Weight is Normal for your Height {}'.format(prediction))
        if(wei<prediction-5):
            return render_template('front.html',pred='Your Weight is underweight for your Height {}'.format(prediction))
        if(wei>prediction+5):
            return render_template('front.html',pred='Your Weight is Overweight for your Height {}'.format(prediction))

if __name__=="__main__":
    app.run(debug=True)