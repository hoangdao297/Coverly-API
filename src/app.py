from coverletter_generator import CoverLetter
from flask import Flask, request, render_template, jsonify, make_response

app = Flask(__name__)

@app.route('/')
def mainpage():
    return render_template('form.html')

@app.route('/results',methods = ['POST', 'GET'])
def result():
    resume_link=request.args.get('resume_link')
    job_link=request.args.get('job_link')
    personalities=request.args.get('personalities')
    relatedhobbies=request.args.get('related_hobbies')
    awards=request.args.get('awards')
    if not resume_link or not job_link or not personalities:
        resp = make_response("Bad Request", 400)
        resp.headers['X-Something'] = 'A value'
        return resp
    generator=CoverLetter()
    prompt=generator.createPrompt(resume_link, job_link, personalities, relatedhobbies, awards)
    letter=generator.generateResult(prompt)
    return jsonify({'letter': letter}), 200

if __name__ == '__main__':
   app.run(debug=True)