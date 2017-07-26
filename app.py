from flask import Flask, render_template
import csv



# Instantiate Flask class instance as "app"
app = Flask(__name__)  # Note the double underscores on each side!

def get_csv():
	csv_path = './static/la-riots-deaths.csv'
	csv_file = open(csv_path, 'rt')
	csv_obj = csv.DictReader(csv_file)
	csv_list = list(csv_obj)
	return csv_list


@app.route("/")
def index():
	template = 'index.html'
	object_list = get_csv()
	return render_template(template, object_list=object_list)


# unique detail for each record
@app.route('/<row_id>')
def detail(row_id):
	template = 'detail.html'
	object_list = get_csv()
	for row in object_list:
		if row['id'] == row_id:
			return render_template(template, object=row)




if __name__ == '__main__':
    # Fire up the Flask test server
    app.run(debug=True, use_reloader=True)