@echo off
cd "C:\Users\Roshni\OneDrive\Desktop\SS and Pics\nosql\SyncTec" 
start cmd /k "mongod --dbpath \"C:\Users\Roshni\OneDrive\Desktop\SS and Pics\nosql\""
start cmd /k "python attendance_server1.py"
