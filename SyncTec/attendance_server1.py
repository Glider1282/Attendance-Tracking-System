from http.server import HTTPServer, BaseHTTPRequestHandler
from pymongo import MongoClient
from urllib.parse import parse_qs
from datetime import datetime
import json

# MongoDB configuration
client = MongoClient('localhost', 27017)
db = client['attendance_db']
collection = db['attendance_records']

class AttendanceRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
      if self.path == '/':
        self.send_response(301)
        self.send_header('Location', '/input_attendance.html')
        self.end_headers()
      elif self.path == '/input_attendance.html':
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        with open('input_attendance.html', 'rb') as file:
            self.wfile.write(file.read())
      elif self.path == '/attendance_records.html':
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        with open('attendance_records.html', 'rb') as file:
           self.wfile.write(file.read())
      elif self.path == '/attendance_records':
        self.send_response(200)
        self.send_header('Content-type', 'application/json')  # Changed content type to JSON
        self.end_headers()
        # Fetch attendance records from MongoDB
        records = collection.find({}, {"_id": 0})  # Exclude MongoDB ObjectIDs from response
        attendance_records = [record for record in records]

    # Send attendance records as JSON response
        self.wfile.write(json.dumps(attendance_records).encode())


    def do_POST(self):
       content_length = int(self.headers['Content-Length'])
       post_data = self.rfile.read(content_length)
       data = parse_qs(post_data.decode('utf-8'))
    
       employee_id = data['employee_id'][0]
       current_date = datetime.now().strftime('%Y-%m-%d')
       current_time = datetime.now().strftime('%H:%M:%S')
    
       attendance_record = {
        "date": current_date,
        "time": current_time,
        "employee_id": employee_id
        }
       collection.insert_one(attendance_record)

       # Redirect to http://localhost:8000/submit_attendance
       self.send_response(301)
       self.send_header('Location', 'http://localhost:8000/attendance_records.html')
       self.end_headers()
def run_server(server_class=HTTPServer, handler_class=AttendanceRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Server running on port {port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()
