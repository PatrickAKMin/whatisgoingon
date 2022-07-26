from flask import Flask,render_template,request
#from flask import request 

import pandas as pd 

app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def myform():
	return 'Hello, welcome! You can calcualte your salary raise by inputing /output?data=## where ## will be (%) number.'

@app.route('/output',methods=['GET','POST'])
def output():
	#data = request.form.get("x")
	args = request.args
	data = args.get("data")
	
	if data is not None:
		dataset = pd.read_excel('/home/PatrickMin/CODE/Employee_sal.xlsx')
		Name = dataset['Name'] 
		dataset['Salary'] = dataset['Salary'] + dataset['Salary']*int(data)/100
		filename1 = "Out_file.xlsx"
		dataset.to_excel(filename1)
		resp = "Your Data has been Updated to Out_file.xsl. Check it out!"
	else:
		resp = 'data parameter not defined'

	return resp

def main():
	return app.run()

if __name__ == '__main__':
	main()

	app.run(port=1235,debug=True) 


 