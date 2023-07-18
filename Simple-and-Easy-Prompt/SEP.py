# Simple and Easy Prompt (SEP)
try:
    # importing required modules
    from cmd import Cmd
    import cv2
    import pyqrcode
    from captcha.image import ImageCaptcha
    import time
    from plyer import notification
    import os
    import art
    import tkinter as tk
    import requests
    import emoji
    import pyjokes
    import sys
    import wikipedia as wk
    import wget
    from faker import Faker
    from PIL import Image

    # class is created
    class CMD(Cmd):
        prompt = "[*]-->"
        intro = """
                **** Simple and Easy Prompt (SEP) ****
                    ____________________________

Type help for seeing all the documented commands.

Type help <documented variable> for seeing help of a particular documented
commands.

                *** This Program is MIT Licensed ***
                    
================================================================================
                """

        # creating function section for keyword
        # function for creating qrcode
        def do_qrcode(self, link):
            if link == "":
                print("Enter the text to be in qrcode and try again!!!")
            else:
                try:
                    img = pyqrcode.create(f"{link}")
                    os.makedirs("C:\Simple and Easy Prompt (SEP)\Qrcode", exist_ok=True)
                    img.png(f"C:\Simple and Easy Prompt (SEP)\Qrcode\{link}.png", scale = 8)
                    im = Image.open(f"C:\Simple and Easy Prompt (SEP)\Qrcode\{link}.png")
                    im.show()
                    print("Successfully created qrcode and saved in C:\Simple and Easy Prompt (SEP)\Qrcode\ ")
                except:
                    print("Failed to create qrcode\nAn unknown error occurred")

        # function for creating captcha
        def do_captcha(self, x):
            if x == " ":
                print("Enter the text to be in captcha and try again!!!")
            else:
                try:
                    image = ImageCaptcha(width=280, height=90)
                    data = image.generate_image(x)
                    os.makedirs("C:\Simple and Easy Prompt (SEP)\Captcha", exist_ok=True)
                    image.write(x, f"C:\Simple and Easy Prompt (SEP)\Captcha\{x}.png")
                    im = Image.open(f"C:\Simple and Easy Prompt (SEP)\Captcha\{x}.png")
                    im.show()
                    print("Successfully created captcha and saved in C:\Simple and Easy Prompt (SEP)\Captcha\ ")
                except:
                    print("Failed to create a captcha\nText to be in captcha is not given")

        # function for notification
        def do_popup(self, abc):
            try:
                if __name__ == "__main__":
                    notification.notify(
                        title=input("Enter the title: "),
                        app_name="Simple and Easy Prompt (SAP)",
                        message=input("Enter the description: "),
                        timeout=int(input("Enter timeout: ")))
                    return False
            except:
                print("Failed to popup\nAn unknown error occurred")

        # function for taking screenshots
        def do_screenshot(self, strain):
            if strain == "":
                print("Enter the name of the screenshot and try again!!!")
            else:
                try:
                    import pyautogui
                    time.sleep(5.0)
                    img = pyautogui.screenshot()
                    os.makedirs("C:\Simple and Easy Prompt (SEP)\Screenshot", exist_ok=True)
                    img.save(f"C:\Simple and Easy Prompt (SEP)\Screenshot\{strain}.png")
                    im = Image.open(f"C:\Simple and Easy Prompt (SEP)\Screenshot\{strain}.png")
                    im.show()
                    print("Successfully screenshot has been taken and saved in "
                          "C:\Simple and Easy Prompt (SEP)\Screenshot\ ")
                except:
                    print("Failed to take screenshot\nAn unknown error occurred")

        # function for taking photo
        def do_capture(self, abcd):
            if abcd == "":
                print("Enter the name of the image and try again!!!")
            else:
                try:
                    vid = cv2.VideoCapture(0)
                    while True:
                        time.sleep(0)
                        ret, frame = vid.read()
                        os.makedirs("C:\Simple and Easy Prompt (SEP)\Capture", exist_ok=True)
                        cv2.imwrite(f"C:\Simple and Easy Prompt (SEP)\Capture\{abcd}.png", frame)
                        vid.release()
                        break
                    cv2.destroyAllWindows()
                    im = Image.open(f"C:\Simple and Easy Prompt (SEP)\Capture\{abcd}.png")
                    im.show()
                    print("Successfully photo has been taken and saved in C:\Simple and Easy Prompt (SEP)\Capture\ ")
                except:
                    print("Failed to take photo\nAn unknown error occurred")

        # function for date, time, day
        def do_today(self, a):
            print(time.ctime())

        # function for installing python modules using pip
        def do_pip(self, b):
            if b == "":
                print("Enter install / uninstall and try again!!!")
            else:
                c = input("Enter the correct module name: ")
                if b == "install":
                    try:
                        os.system("pip install " + str(c))
                        return False
                    except:
                        print("Failed\nAn unknown error occurred")
                elif b == "uninstall":
                    try:
                        os.system("pip uninstall " + str(c))
                        print(f"{str(c)} uninstalled.")
                    except:
                        print("Failed\nAn unknown error occurred")

        # function for art
        def do_art(self, d):
            if d == "":
                print("Enter the text to make art and try again!!!")
            else:
                art.tprint(str(d))

        # function for videos in youtube
        def do_youtube(self, e):
            if e == "":
                print("Enter the topic of video to be played and try again!!!")
            else:
                try:
                    import pywhatkit
                    pywhatkit.playonyt(str(e))
                    print("Playing...")
                except:
                    print("Failed to play\nAn unknown error occurred")

        # function to perform search in google
        def do_search(self, f):
            try:
                import pywhatkit
                pywhatkit.search(str(f))
                print("Searching...")
            except:
                print("Failed to search\nAn unknown error occurred")

        # function for handwritten copy the text entered
        def do_handwritten(self, h):
            if h == "":
                print("Enter the text to be in handwritten")
            else:
                try:
                    import pywhatkit
                    index = h[1]
                    pywhatkit.text_to_handwriting(str(h), rgb=(0, 0, 0), save_to=f"{index}.png")
                    im = Image.open(f"{index}.png")
                    im.show()
                    print("Successfully created and saved in same directory of SEP")
                except:
                    print("Failed!!!.An unknown error occurred")

        # function for ascii art
        def do_asciiart(self, i):
            if i == "":
                print("Enter the path of the image and try again!!!")
            else:
                try:
                    import pywhatkit
                    pywhatkit.image_to_ascii_art(str(i), output_file=str(i)+".txt")
                    print("Successfully created")
                    print("Text file is created and saved in same directory of the image given")
                except:
                    print("Failed\nCheck the path of the image")

        # function for weather
        def do_weather(self, j):
            def getWeather(canvas):
                city = textField.get()
                api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=06c921750b9a82d8f5d1294e1586276f"
                json_data = requests.get(api).json()
                condition = json_data['weather'][0]['main']
                temp = int(json_data['main']['temp'] - 273.15)
                min_temp = int(json_data['main']['temp_min'] - 273.15)
                max_temp = int(json_data['main']['temp_max'] - 273.15)
                pressure = json_data['main']['pressure']
                humidity = json_data['main']['humidity']
                wind = json_data['wind']['speed']
                sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
                sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))
                final_info = condition + "\n" + str(temp) + "°C"
                final_data = "\n" + "Min Temp: " + str(min_temp) + "°C" + "\n" + "Max Temp: " + str(
                max_temp) + "°C" + "\n" + "Pressure: " + str(pressure) + "\n" + "Humidity: " + str(
                humidity) + "\n" + "Wind Speed: " + str(
                wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
                label1.config(text=final_info)
                label2.config(text=final_data)

            try:
                canvas = tk.Tk()
                canvas.geometry("600x500")
                canvas.title("Weather App")
                f = ("poppins", 15, "bold")
                t = ("poppins", 35, "bold")
                textField = tk.Entry(canvas, justify='center', width=20, font=t)
                textField.pack(pady=20)
                textField.focus()
                textField.bind('<Return>', getWeather)
                label1 = tk.Label(canvas, font=t)
                label1.pack()
                label2 = tk.Label(canvas, font=f)
                label2.pack()
                canvas.mainloop()
            except:
                print("Failed\nAn unknown error occurred")

        # function for emoji
        def do_emoji(self, l):
            if l == "":
                print("Enter the name of the emoji and try again!!!")
            else:
                print(emoji.emojize(f":{l}:"))

        # function for jokes
        def do_joke(self, m):
            print(pyjokes.get_joke("en", "all"))

        # function for search in wikipedia
        def do_information(self, n):
            if n == "":
                print("Enter the topic name to be searched in wikipedia and try again!!!")
            else:
                try:
                    see = wk.summary(n)
                    print(see)
                except:
                    print("Failed!!!.An unknown error occurred")

        # function to create fake details
        def do_fake(self, q):
            if q == "":
                print("Enter the type of information to be fake and try again!!!")
            else:
                q = str(q)
                q.lower()
                fake = Faker()
                if q == "name":
                    print(fake.name())
                elif q == "email":
                    print(fake.email())
                elif q == "address":
                    print(fake.address())
                elif q == "text":
                    print(fake.text())
                elif q == "url":
                    print(fake.url())
                elif q == "country":
                    print(fake.country())
                elif q == "profile":
                    print(fake.profile())

        # function to shut down the pc
        def do_shutdown(self, r):
            try:
                os.system("shutdown /s /t 10")
                print("System will shutdown in 10 seconds")
            except:
                print("Failed!!!\nAn unknown error occurred")

        # function to restart the pc
        def do_restart(self, s):
            try:
                os.system("shutdown /r /t 10")
                print("System will restart after 10 seconds")
            except:
                print("Failed!!!\nAn unknown error occurred")

        # function to make pc to sleeep
        def do_sleep(self, t):
            try:
                os.system("shutdown /h")
            except:
                print("Failed!!!\nAn unknown error occurred")

        # function to exit from the program
        def do_exit(self, person):
            return sys.exit()

        # creating help section for the keyword

        def help_qrcode(self):
            print("Syntax: qrcode <Type string to be in qrcode>")
            print("A qrcode will be created with the string given")

        def help_captcha(self):
            print("Syntax: captcha <Type string to be in captcha>")
            print("A captcha will be created in for the string given")

        def help_screenshot(self):
            print("Syntax: screenshot <screenshot name>")
            print("It will take picture of your screen")

        def help_capture(self):
            print("Syntax: takepic <image name (compulsory)>")
            print("After some second a picture will be taken through your default camera")

        def help_today(self):
            print("syntax: today")
            print("It shows day,month,date,time,year")

        def help_pip(self):
            print("Syntax: pip <install or uninstall>")
            print("It will install or uninstall module through pip")

        def help_art(self):
            print("Syntax: art <Letters to be in the art>")
            print("It will print a image of the given letters made of line")

        def help_youtube(self):
            print("Syntax: youtube <Topic of the video>")
            print("It wil display most video in the entered topic in your default broswer")

        def help_search(self):
            print("Syntax: search <Topic to be searched in google>")
            print("It will show search result in your default browser")


        def help_handwritten(self):
            print("Syntax: handwritten <words to be written>")
            print("It returns a image that will contain the handwritten words given")

        def help_asciiart(self):
            print("Syntax: asciiart <path of the image>")
            print("It will create a text file with ascii keys for the image and "
              "will be stored in the same directory of the image given")

        def help_weather(self):
            print("Syntax: weather")
            print("It will open an application and weather of the city will be displayed")

        def help_emoji(self):
            print("Syntax: emoji <short name of the emoji>")
            print("It returns the emoji if the given short name "
              "is correct or it returns the short name")
            print("For short name of emoji, see this link --> https://unicode.org/emoji/charts/emoji-list.html")

        def help_joke(self):
            print("Syntax: joke")
            print("It will return a joke or a tongue twister")

        def help_information(self):
            print("Syntax: information <Topic to searched>")
            print("It returns the information from wikipedia")
            print("If the topic is not found it returns a failed notification and an error")

        def help_fake(self):
            print("Syntax: fake <keyword>")
            print("It support keyword like: name,address,email,url,text,country,profile")
            print("It return a fake detail of the keyword")

        def help_shutdown(self):
            print("Syntax: shutdown ")
            print("It will shutdown your system in 10 seconds")

        def help_restart(self):
            print("Syntax: restart ")
            print("It will restart your system in 10 seconds")

        def help_sleep(self):
            print("Syntax: sleep")
            print("It will may your system to sleep")

        def help_popup(self):
            print("Syntax: popup")
            print("It shows a popup in a fraction of seconds")

        def help_exit(self):
            print("syntax: exit")
            print("It stops the program")

    if __name__ == "__main__":
        CMD().cmdloop()

except ModuleNotFoundError:
    print("Requirement of SEP is not satisfied!!!")
