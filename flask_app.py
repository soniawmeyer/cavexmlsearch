from flask import Flask, request
import cavexmltosqlquery

app = Flask(__name__)

s = cavexmltosqlquery.CaveXMLtoSQLQuery()

#class variables
tag = "any" #lava tunnel
length = "20" #null default to 0
vertical_extent = "20"
altitude = "20"
length_gtlt = ">=" #must be >= or <=
vertical_extent_gtlt = ">="
altitude_gtlt = ">="

@app.route('/caves', methods=['GET'])
def caves():
    sql = s.sql_statement(tag, length, vertical_extent, altitude, length_gtlt, vertical_extent_gtlt, altitude_gtlt)
    return s.query(sql)

if __name__ == "__main__":
    app.run(debug=True)
