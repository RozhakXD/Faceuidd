from flask import Flask, render_template, redirect, jsonify, request
from application.facebook import Main

app = Flask(__name__)

@app.route('/facebook-id-retriever/', methods=["POST", "GET"])
async def Facebook():
    if request.method == "POST":
        json_data = request.json
        if json_data['link']:
            try:
                facebookID = await Main(json_data['link'])
                return (facebookID)
            except (Exception) as error:
                return jsonify({"Sukses": False, "Message": f"{error}"}), 500
        else:
            return jsonify({"Sukses": False, "Message": "Link cannot be empty"}), 400
    else:
        return render_template('index.html')

@app.route('/api/v1/facebook-id-retriever/', methods=["POST", "GET"])
async def FacebookApi():
    if request.method == "POST":
        json_data = request.json
        if 'link' in json_data:
            if json_data['link']:
                try:
                    facebookID = await Main(json_data['link'])
                    return (facebookID)
                except (Exception) as error:
                    return jsonify({"Sukses": False, "Message": f"{error}"}), 500
            else:
                return jsonify({"Sukses": False, "Message": "Link cannot be empty!"}), 400
        else:
            return jsonify({"Sukses": False, "Message": "`link` data is required in the request!"}), 400
    else:
        return jsonify({"Sukses": False, "Message": "Method not allowed!"}), 405

@app.route('/')
def HomePage():
    return redirect(
        '/facebook-id-retriever/'
    )

if __name__=='__main__':
    app.run(debug=True)