from flask import Flask, request, Response, render_template
from executor import Executor
from agents.planner import planner_agent
import json


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")



@app.route("/run")
def run():

    task = request.args.get("task")


    tasks = planner_agent(task)


    executor = Executor()

    executor.load(tasks)



    def stream():

        for output in executor.run():

            # convert python dict to JSON
            yield json.dumps(output) + "\n"



    return Response(
        stream(),
        mimetype="application/json"
    )



if __name__ == "__main__":
    app.run(debug=True)
