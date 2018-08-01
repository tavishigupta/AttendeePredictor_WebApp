from flask import Flask, request, render_template

# create flask app
app = Flask(__name__)

# removes all new lines for correct input for model
def cleanAgenda(agenda):
    return agenda.replace('\n', ' ')

# builds array of items with same key values
# def arrayBuilder(result, key):
#     list = []
    
#     for key in result.values():
#         list.append[result[key]]

#     return list

# return homepage for user input
@app.route("/")
def main():
    return render_template('homepage.htm')

# return result page with prediction
@app.route('/getprediction', methods=['POST','GET'])
def get_delay():
    if request.method == 'POST':
        # extract all values from result
        result = request.form
        date = result['date']
        agenda = cleanAgenda(result['agenda'])
        length = result['length']
        venue = list(item['venue'] for item in result)
        #venue = arrayBuilder(result, 'venue')
        audience = result['audience']

        # validate correct format of each value
        print(result)
        print(date)
        print(agenda)
        print(length)
        print(venue)
        print(audience)

        # pkl_file = open('cat', 'rb')
        # index_dict = pickle.load(pkl_file)
        # cat_vector = np.zeros(len(index_dict))
        
        # pkl_file = open('logmodel.pkl', 'rb')
        # logmodel = pickle.load(pkl_file)
        # prediction = logmodel.predict(cat_vector)
        
        return render_template('result.htm', prediction = 5)

# check if the executed file is the main program and run the app
if __name__ == "__main__":
    app.debug = True # print tracebacks to console
    app.run()