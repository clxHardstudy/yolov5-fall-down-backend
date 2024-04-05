import configparser


config = configparser.ConfigParser()
config.read("../yolov5-Completed/development.ini")

print(config.get("db","port"))