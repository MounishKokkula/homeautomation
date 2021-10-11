import logging
import time
from argparse import ArgumentParser
import configparser
import json

# todo: save json file after edit
# todo: add logging

class homeAutomation:
    def __init__(self):
        pass

    def edit_json(self):
        pass

    def display(self, module_data, room):
        # todo: extend code to support multiple lights in a room
        if room == "all":
            for i in module_data["home"]:
                print ("""
                Room: {}
                Light: {}
                Thermostat: {}
                """.format(i["room"], i["light"], i["thermostat"]))
        else:
            for i in module_data["home"]:
                if room == i["room"]:
                    print ("""
                    Room: {}
                    Light: {}
                    Thermostat: {}
                    """.format(i["room"], i["light"], i["thermostat"]))

    def toggle_light(self, module_data, room, toggle_option):
        if room == "all":
            for i in module_data["home"]:
                i["light"] = toggle_option
        else:
            for i in module_data["home"]:
                if room == i["room"]:
                    i["light"] = toggle_option


    def set_thermostat(self,  module_data, room, set_temp):
        if room == "all":
            for i in module_data["home"]:
                i["thermostat"] = set_temp
        else:
            for i in module_data["home"]:
                if room == i["room"]:
                    i["thermostat"] = set_temp

    def add_room(self, room):
        # todo: add room to json
        pass

    def add_light(self):
        # todo: add light to json
        pass

    def add_thermostat(self):
        # todo: add thermostat to json
        pass

    def home_page(self):
        return input("""
        Welcome to HomeApp: \n
        Make your selection from below
        1. Home \n
        2. Toggle Lights \n
        3. Set Thermostat \n
        --> """)

    def room_page(self):
        room_option = input("""
        Room selection
        1. all [Input 1]\n
        2. room [Input <room-name>] \n
        --> """)
        room = "all"
        if room_option == str(2):
            # todo: show all room options
            room = room_option
        return room

    def main(self, home_auto_module):
        input_option = self.home_page()
        if input_option == str(1):
            room_option = self.room_page()
            home_auto.display(home_auto_module, room=room_option)
            self.main(home_auto_module)

        elif input_option == str(2):
            room = self.room_page()
            light_option = input("""
            Toggle Light
            1. ON \n
            2. OFF \n
            --> """)

            # todo: move below to reusable function
            lights = "OFF"
            if light_option == str(1):
                lights = "ON"
            home_auto.toggle_light(home_auto_module, room=room, toggle_option=lights)
            self.main(home_auto_module)

        elif input_option == str(3):
            room = self.room_page()
            thermostat_option = input("""
                    Set Thermostat
                    1. ON \n
                    2. OFF \n
                    --> """)
            home_auto.toggle_light(home_auto_module, room=room, toggle_option=thermostat_option)
            self.main(home_auto_module)

if __name__ == "__main__":
    t = time.localtime()
    current_time = time.strftime("%Y-%m-%d-%H-%M-%S", t)
    argparser = ArgumentParser()
    argparser.add_argument('status', type=str)
    argparser.add_argument('props', type=str)

    parser = configparser.ConfigParser()
    parser.read('properties.ini')

    with open(parser.get('home', 'path')) as f:
        home_auto_module = json.load(f)

    home_auto = homeAutomation()
    home_auto.main(home_auto_module)
