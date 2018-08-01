from flask import Flask, request, render_template

# create flask app
app = Flask(__name__)

# removes all new lines for correct input to trained model
def cleanAgenda(agenda):
    return agenda.replace('\n', ' ')

# return homepage for user input
@app.route("/")
def main():
    return render_template('homepage.htm')

# return result page with prediction
@app.route('/getprediction', methods=['POST','GET'])
def get_prediction():
    if request.method == 'POST':
        # instantiate all venue and audience inputs
        offices = stores = schools = premises = otherv = 0
        under5 = six = twelve = eighteen = over23 = industry = educators = government = othera = 0

        # extract all values from result
        result = request.form
        date = result['date']
        agenda = cleanAgenda(result['agenda'])
        length = result['length']

        # extract list of all venues and audiences
        venue = request.form.getlist('venue')
        audience = request.form.getlist('audience')

        # validate correct format of each value
        print(result)
        print(date)
        print(agenda)
        print(length)
        print(venue)
        print(audience)

        # 
        if 'offices' in venue:
            offices = 1
        if 'stores' in venue:
            stores = 1
        if 'schools' in venue:
            schools = 1
        if 'premises' in venue:
            premises = 1
        if 'other' in venue:
            otherv = 1

        if 'under5' in audience:
            under5 = 1
        if '6to11' in audience:
            six = 1
        if '12to17' in audience:
            twelve = 1
        if '18to22' in audience:
            eighteen = 1
        if '23Over' in audience:
            over23 = 1
        if 'industry' in audience:
            industry = 1
        if 'educators' in audience:
            educators = 1
        if 'government' in audience:
            government = 1
        if 'other' in audience:
            othera = 1

        # validate correct value for venue and audience input
        print(offices)
        print(stores)
        print(schools)
        print(premises)
        print(otherv)
        print(under5)
        print(six)
        print(twelve)
        print(eighteen)
        print(over23)
        print(industry)
        print(educators)
        print(government)
        print(othera)

        # pkl_file = open('cat', 'rb')
        # index_dict = pickle.load(pkl_file)
        # cat_vector = np.zeros(len(index_dict))
        
        # pkl_file = open('logmodel.pkl', 'rb')
        # logmodel = pickle.load(pkl_file)
        # prediction = logmodel.predict(cat_vector)
        
        return render_template('result.htm', prediction = 5)

# check if the executed file is the main program and run the app
if __name__ == "__main__":
    app.debug = True # print traceback to console
    app.run()