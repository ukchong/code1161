"""All about IO."""


import json
import os
import requests
import inspect
import sys

# Handy constants
LOCAL = os.path.dirname(os.path.realpath(__file__))  # the context of this file
CWD = os.getcwd()  # The curent working directory
if LOCAL != CWD:
    print("Be careful that your relative paths are")
    print("relative to where you think they are")
    print("LOCAL", LOCAL)
    print("CWD", CWD)



def get_some_details():
    """Parse some JSON.

    In lazyduck.json is a description of a person from https://randomuser.me/
    Read it in and use the json library to convert it to a dictionary.
    Return a new dictionary that just has the last name, password, and the
    number you get when you add the postcode to the id-value.
    TIP: Make sure that you add the numbers, not concatinate the strings.
         E.g. 2000 + 3000 = 5000 not 20003000
    TIP: Keep a close eye on the format you get back. JSON is nested, so you
         might need to go deep. E.g to get the name title you would need to:
         data["results"][0]["name"]["title"]
         Look out for the type of brackets. [] means list and {} means
         dictionary, you'll need integer indeces for lists, and named keys for
         dictionaries.
    """
    json_data = open(LOCAL + "/lazyduck.json").read()       #json_data 명찰, (/Users/ewan/Desktop/Ewan/uni/code1161/lazyduck.json).read()
                                                            #이게 IOExample보다 쉬운 파일 열어서 읽는 법인듯
    data = json.loads(json_data)                            #data 명찰에 lazyduck.json을 로드
    result = data["results"][0]                             #lazyduck확인결과 male mr romain hoogmoed임.
    return {"lastName":       result["name"]["last"],
            "password":       result["login"]["password"],
            "postcodePlusID": result["location"]["postcode"] +
            int(result["id"]["value"])
            }



def wordy_pyramid():
    """Make a pyramid out of real words.

    There is a random word generator here:
    http://api.wordnik.com/v4/words.json/randomWords?api_key=a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5&minLength=10&maxLength=10&limit=1
    The arguments that the generator takes is the minLength and maxLength of the word
    as well as the limit, which is the the number of words. 
    Visit the above link as an example.
    
    Use this and the json and requests library to make a word pyramid. The shortest
    words they have are 3 letters long and the longest are 20. The pyramid
    should step up by 2 letters at a time.
    Return the pyramid as a list of strings.
    I.e. ["cep", "dwine", "tenoner", ...]
    [
    "cep",
    "dwine",
    "tenoner",
    "ectomeric",
    "archmonarch",
    "phlebenterism",
    "autonephrotoxin",
    "redifferentiation",
    "phytosociologically",
    "theologicohistorical",
    "supersesquitertial",
    "phosphomolybdate",
    "spermatophoral",
    "storiologist",
    "concretion",
    "geoblast",
    "Nereis",
    "Leto",
    ]
    TIP: to add an argument to a URL, use: ?argName=argVal e.g. &minLength=
    TIP II: Requests has a json method. It may make your life easier.
    """

    pyramid1 = []
    pyramid2 = []
    url = "http://api.wordnik.com/v4/words.json/randomWords?api_key=a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5&minLength={}&maxLength={}&limit=1"
    for length in range(3, 21):
        if length % 2 == 1:
            pyramid1.append(requests.get(url.format(length, length)).json()[0]['word'])
        else:
            pyramid2 = [requests.get(url.format(length, length)).json()[0]['word']] + pyramid2

    return pyramid1 + pyramid2


def wunderground():
    """Find the weather station for Sydney.

    Get some json from a request parse it and extract values.
    Sign up to https://www.wunderground.com/weather/api/ and get an API key
    TIP: reading json can someimes be a bit confusing. Use a tool like
         http://www.jsoneditoronline.org/ to help you see what's going on.
    TIP: these long json accessors base["thing"]["otherThing"] and so on, can
         get very long. If you are accessing a thing often, assign it to a
         variable and then future access will be easier.
    """
    base = "http://api.wunderground.com/api"
    api_key = "2a7730bdd6f6ff60"
    country = "AU"
    city = "Sydney"
    template = "{base}/{key}/conditions/q/{country}/{city}.json"
    url = template.format(base=base, key=api_key, country=country, city=city)
    r = requests.get(url)
    the_json = json.loads(r.text)
    obs = the_json['current_observation']

    dict1 = {"state":           obs["display_location"]["state"],
             "latitude":        obs["display_location"]["latitude"],
             "longitude":       obs["display_location"]["longitude"],
             "local_tz_offset": obs["local_tz_offset"]}
    print(str(dict1))
    return dict1



def diarist():
    """Read gcode and find facts about it.

    Read in Trispokedovetiles(laser).gcode and count the number of times the
    laser is turned on and off. That's the command "M10 P1".
    Write the answer (a number) to a file called 'lasers.pew' in the week4 directory.
    TIP: you need to write a string, so you'll need to cast your number
    TIP: Trispokedovetiles(laser).gcode uses windows style line endings. CRLF
         not just LF like unix does now. If your comparison is failing this
         might be why. Try in rather than == and that might help.
    TIP: remember to commit 'lasers.pew' and push it to your repo, otherwise
         the test will have nothing to look at.  ok.
    """
    count = 0
    laser_file = 'Trispokedovetiles(laser).gcode'
    with open(laser_file, 'r') as laser:    #with open(파일, 모드) as laser: 
        commands = laser.read().split('\n') #리스트를 만듬 - 한줄 띄어진것마다 리스트가 된다
        for command in commands:            #commands list안의 command들에대해 - 여기서 command는 그냥 요소들
            if "M10 P1" in command:         #M10 P1이 있을떄마다
                count += 1                  #count에 1씩 더한다.

    pew_file = 'lasers.pew'                 #pew_file이라는 명함 파주고
    with open(pew_file, 'w') as pew:        #with open(파일, 모드) as pew:
        pew.write(str(count))               #pew에 카운트(넘버)를 스트링으로 적는다
    return count                            #카운트를 리턴. 연 파일은 안닫아도 되나? IOExample에서는 닫았음..


if __name__ == "__main__":
    functions = [obj for name,obj in inspect.getmembers(sys.modules[__name__]) if (inspect.isfunction(obj))]
    for function in functions:
        try:
            print(function())
        except Exception as e:
            print(e)
    if not os.path.isfile("lasers.pew"):
        print('diarist did not create lasers.pew')
