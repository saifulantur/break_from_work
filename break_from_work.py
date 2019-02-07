import webbrowser
import time

total_break=3
break_count=0
print("This program strated on"+time.ctime())
while (break_count <total_break):
    time.sleep(5)
    webbrowser.open("https://www.youtube.com/watch?v=CBfqi_nrif8&start_radio=1&list=RDCBfqi_nrif8")
    break_count=break_count+1
