from flask import Flask, jsonify
import psutil
app = Flask(__name__)
app.debug = True

@app.route("/cpu/current")
def get_currnet_cpu_pcent():
  res = {
    "cpu-pcent": psutil.cpu_percent()
  }
  return jsonify(res)


if __name__ == "__main__":
  app.run()
