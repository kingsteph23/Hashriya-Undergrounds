import time

print("_________________________________")
print("|    🔰 走り屋にわたって地下  🔰       |")
print("|                                 |"
      "\n|  🔰 Hashriya Undergrounds 🔰   |"
      "\n|       Phase 1(Tokyo)          |"
      "\n|_______________________________|")

start = input("Hello playa.  Do you wish to begin?"
              "\nstart"
              "\nquit"
              "\n>>")
if start == "quit":
    print("Understandable.  Have a wonderful day!")
    exit()
elif start == "start":
    print("Gotcha. but theres some things you should know.....")
# Warning
input("BEFORE WE GET STARTED")
input("\n Note, there are some things you should know before starting this game"
      "\n 1:Everytime you respond to a question, make sure you type it EXACTLY how you see")
print()
input("For example,if you are required to respond to a question,such as a yes or no question"
      "\nif you select yes, write yes EXACTLY how you see it. If you select no, write it exactly how you see it.")
input("Even if its a long response such as,Take the car to the tuning garage."
      "\nYou MUST type it exactly like this, or the computer will not read it."
      "\nSo be careful when writing your responses a and make sure you write it EXACTLY AS YOU SEE IT. ")
print()
input(" Don't type another answer that isn't there"
      "\n If you are given a response where you have a option of yes or no, but you put yeezus as a answer..."
      "\n It will be marked either as a invalid answer, or you can potentially get a answer that you don't want"
      "\n nor will it make sense.")
print()
input("There are times where I may use Japanese words,"
      "\nbut a majority of them i translated into English")
print()
input("To anyone that speaks Japanese(especially fluently), mind my crappy Japanese. "
      "\n 日本語を話す人（特に流暢に）には、私の嫌な日本語を心に入れてください")
print()
input("Feedback and constructive criticism is greatly appreciated.  If you experience any bugs or issues with my game."
      "\nOr just general feedback(pros/cons)"
      "\nPlease mark it as a new issue on my github.")

print()
input("Also, because I ended up realizing that not so much people may not know so much about the Japanese car scene..."
      "\nI made a reference table on the types of cars/courses in the game so people understand what i'm talking about ."
      "\nAlso the links to my Github and Instagram is there as well if you want to check it out.")
print()
input("Have fun ;)")

# Intro
choice = input("Welcome to the land of the rising sun,Do you wish to start?(yes/no)>>").lower().strip()
if choice.lower().strip() == "no":
    print("Understandable.  Have a wonderful day!")
    exit()
else:
    print("Welcome to Hayshriya Undergrounds;)")
    print()

playa = input("Quick question.... What is your name?"
              "\n>>")

# Selecting a Japanese car Manufactuer.  I'll add some European cars in a future update.  Time of Day(TOD)
market = input("Okay " + playa + " Please select a Japanese Car Manufactuer."
                                 "\nHonda"
                                 "\nMazda"
                                 "\nMitsubishi"
                                 "\nNissan"
                                 "\nSubaru"
                                 "\nToyota"
                                 "\n>>")

JDM = input("Okay " + playa + "! Please select a Japanese Car Manufactuer"
                              "\nJust add the Car manufacturer from the top you selected."
                              "\nHonda"
                              "\nMazda"
                              "\nMitsubishi"
                              "\nNissan"
                              "\nSubaru"
                              "\nToyota"
                              "\n>>")
print()
# Tech specs for Honda cars
if JDM == "Honda":
    JDM = input("Please select which Honda  model you wish to select. "
                "(\nS2000"
                "\nNsx(NC1)"
                "\nEK9"
                "\n>>")
if JDM == "S2000":
    print("Tech specs of " + market + " " + JDM + "."
                                                  "\nBody Style-2  door roadster"
                                                  "\nLayout-Front engine and Rear wheel drive"
                                                  "\nEngine type-  Naturally Aspirated inline 4"
                                                  "\nHorsepower-237 hp"
                                                  "\nTorque-162 lb per feet"
                                                  "\nTransmission-6 speed manual"
                                                  "\nWeight-1,250 kg(2,756 lb)"
                                                  "\nProduction- 1999-2009"
                                                  "\nTop speed:160 mph")
elif JDM == "Nsx(NC1)":
    print("Tech specs of " + market + " " + JDM + "."
                                                  "\nBody Style- 2 door coupe,2 door targa top"
                                                  "\nLayout- Transverse mid-engine,RWD"
                                                  "\nEngine type-  Honda C30A V6"
                                                  "\nHorsepower- 270 hp"
                                                  "\nTorque-210 lb-ft"
                                                  "\nTransmission-5 OR 6 SPEED MANUAL"
                                                  "\nWeight- 3,020 lb(1,370 kg)"
                                                  "\nProduction-  1990-2005"
                                                  "\nTop speed:191 MPH")
if JDM == "EK9":
    print("Tech specs of " + market + " " + JDM + "."
                                                  "\nBody Style- 2 door hatchback"
                                                  "\nLayout-Front engine, front wheel drive(F-F)"
                                                  "\nEngine type-  1.6 L B16B Inline 4"
                                                  "\nHorsepower- 182 hp"
                                                  "\nTorque-160 NM"
                                                  "\nTransmission-5 speed manual"
                                                  "\nWeight- 2,403 lb(1,090 kg)"
                                                  "\nProduction-  1997-2000"
                                                  "\nTop speed:146 MPH")
print()
# tech specs of Toyota cars
if JDM == "Toyota":
    JDM = input("Please select which Toyota you wish to select. "
                "\nToyota"
                "\nSupra A70"
                "\nSupra RZ"
                "\nSoarer 2.5 GT TT"
                "\nMR2"
                "\nCorolla AE86 Trueno"
                "\n:")
if JDM == "Supra A70":
    print("Tech specs of " + market + " " + JDM + "."
                                                  "\nBody Style- coupe"
                                                  "\nLayout- front engine, rear wheel drive"
                                                  "\nEngine type- Toyota 7m -GTE (Modified CT26 Turbo"
                                                  "\nHorsepower- 267 hp"
                                                  "\nTorque- 264 lb -ft"
                                                  "\nTransmission-5 speed manual, 4 speed automatic"
                                                  "\nWeight- 3,219-3,616 lbs(manual) 3,483-3,792 lbs(automatic)"
                                                  "\nProduction-  1986-1993"
                                                  "\nTop speed: 144 mph"
                                                  "\n0-60: 6.9 seconds")
if JDM == "Supra RZ":
    print("Tech specs of " + market + " " + JDM + "."
                                                  "\nBody Style- Coupe"
                                                  "\nLayout-front engine, rear wheel drive"
                                                  "\nEngine type- I6, 2JZ"
                                                  "\nHorsepower- 171 hp"
                                                  "\nTorque- 203 lb -ft"
                                                  "\nTransmission-6 speed manual"
                                                  "\nWeight- 3,616 lb(1,640 kg)"
                                                  "\nProduction-  1993-2002"
                                                  "\nTop speed: 155 mph"
                                                  "\n0-60:5.3 seconds")
if JDM == "Soarer 2.5 GT TT":
    print("Tech specs of " + market + " " + JDM + "."
                                                  "\nBody Style- 2 door coupe"
                                                  "\nLayout- Front engine, Rear wheel drive"
                                                  "\nEngine type-3.0 2JZ-GE I6(JZZ31)"
                                                  "\nmHorsepower- 222 hp"
                                                  "\nTorque- 210 lb -ft"
                                                  "\nTransmission- 5 speed manual,4 or 5 speed automatic"
                                                  "\nWeight- 3,395-3,814 Ib(1,540 kg-1,730 kg)"
                                                  "\nProduction-  1991-2000"
                                                  "\nTop speed:146-156 mph"
                                                  "\n0-60:7.4 seconds")
if JDM == "MR2":
    print("Tech specs of " + market + " " + JDM + "."
                                                  "\nBody Style- Coupe"
                                                  "\nLayout- Mid engine, rear wheel drive"
                                                  "\nEngine type- 2.2 L 5s -FE Inline 4"
                                                  "\nHorsepower-  200 hp"
                                                  "\nTorque- 137 lb -ft"
                                                  "\nTransmission-5 speed manual, 4 speed automatic"
                                                  "\nWeight- 2,579 lb(1170 kg)"
                                                  "\nProduction-  1989-1999"
                                                  "\nTop speed: 152 mph"
                                                  "\n0-60:6.5")
if JDM == "Corolla AE86 Trueno":
    print("Tech specs of " + market + " " + JDM + "."
                                                  "\nBody Style- Compact . 2 door"
                                                  "\nLayout- Front engine, rear wheel drive"
                                                  "\nEngine type-  1.6 L 4a-GEU Inline 4 DOHC"
                                                  "\nHorsepower- 122 hp"
                                                  "\nTorque- 108 lb -ft"
                                                  "\nTransmission-5 speed manual"
                                                  "\nWeight- 2138 lbs(970 kg)"
                                                  "\nProduction-  1983-1987"
                                                  "\nTop speed: 118 mph"
                                                  "\n0-60: 8.6 seconds")
    print()
# tech specs of Mazda cars
if JDM == "Mazda":
    JDM = input("Please select which Mazda model  you wish to select. "
                "\nRX 7 FD35"
                "\nRX 7 FC35"
                "\nMiata mx5 NA"
                "\nMiata mx5 NB"
                "\nRX 8"
                "\n: ")
if JDM == "RX 7 FD35":
    print("Tech specs of " + market + " " + JDM + "."
                                                  "\nBody Style- 2 seater Coupe"
                                                  "\nLayout-Front Mid engine, Rear wheel drive"
                                                  "\nEngine type-  1.3 L TT 13B-REW Twin rotor(Rotary engine)"
                                                  "\nHorsepower- 252 hp"
                                                  "\nTorque-217 lb -ft"
                                                  "\nTransmission-5 speed manual"
                                                  "\nWeight- 1,260 kg (2,778 lb)"
                                                  "\nProduction-  1992-2002"
                                                  "\nTop speed: 160 MPH")
if JDM == "RX 7 FC35":
    print("Tech specs of " + market + " " + JDM + "."
                                                  "\nBody Style- 2 DOOR COUPE"
                                                  "\nLayout-Front Mid engine, Rear wheel drive"
                                                  "\nEngine type-1.3 L 13B VIDEO (S4)"
                                                  "\nHorsepower-  185 hp"
                                                  "\nTorque- 25.0 kg-m"
                                                  "\nTransmission-5 Speed manual"
                                                  "\nWeight- 2,626-3,492 lb(1,223-1,584 kg)"
                                                  "\nProduction-  1985-1992"
                                                  "\nTop speed:120 MPH"
                                                  "\n0-60:")
if JDM == "Miata mx5 NA":
    print("Tech specs of " + market + " " + JDM + "."
                                                  "\nBody Style- 2 door  coupe"
                                                  "\nLayout-Front mid engine,Rear wheel drive"
                                                  "\nEngine type-1,598 cc B6ZE(RS)DOHC Inline 4"
                                                  "\nHorsepower-   128hp"
                                                  "\nTorque- 110 lb -ft"
                                                  "\nTransmission- 5 Speed manual"
                                                  "\nWeight- 2,120 IB(960 Kg)"
                                                  "\nProduction-  1989-1997"
                                                  "\nTop speed:116 MPH"
                                                  "\n0-60:")
if JDM == "Miata mx5 NB":
    print("Tech specs of " + market + " " + JDM + "."
                                                  "\nBody Style-  2 door coupe/convertible"
                                                  "\nLayout-Front mid engine(Rear wheel drive)"
                                                  "\nEngine type-1.8 L BP-5A Inline 4"
                                                  "\nHorsepower-  140 hp"
                                                  "\nTorque- 119 lb -ft"
                                                  "\nTransmission-5 or 6 speed manual transmission"
                                                  "\nWeight- 2,348 IB(1,065 KG)"
                                                  "\nProduction-  1998-2005"
                                                  "\nTop speed:127 MPH"
                                                  "\n0-60:")
if JDM == "RX 8":
    print("Tech specs of " + market + " " + JDM + "."
                                                  "\nBody Style- 4 door quad coupe"
                                                  "\nLayout-Front mid engine, rear wheel drive"
                                                  "\nEngine type- 1.3 L RENESIS "
                                                  "\nHorsepower- 189-238 hp"
                                                  "\nTorque- 159 lb -ft"
                                                  "\nTransmission-5 or 6 speed manual"
                                                  "\n4 and 6 speed automatic"
                                                  "\nWeight- Manual-2,886-3,027 lb(1,309-1,373 kg)"
                                                  "\nProduction-  2003-2012"
                                                  "\nTop speed: 145 MPH"
                                                  "\n0-60:6.4 seconds")
print()
# tech specs of mitsubishi
if JDM == "Mitsubishi":
    JDM = input("Please select which Mitsubishi model you wish to select."
                "\nMitsubishi "
                "\nGTO TT "
                "\nFTO "
                "\nLancer Evo iii "
                "\nLancer evo VI "
                "\nLancer Evo VIII"
                "\n>>")
if JDM == "GTO TT":
    print("Tech specs of " + market + " " + JDM + "."
                                                  "\nBody Style- 2 door liftback coupe"
                                                  "\nLayout-Transverse front engine.4WD"
                                                  "\nEngine type-3.0 L 6G72 DOHC 24v TT V6"
                                                  "\nHorsepower-276 hp"
                                                  "\nTorque- 308 lb -ft"
                                                  "\nTransmission-5 or 6 speed manual"
                                                  "\n4 speed automatic"
                                                  "\nWeight- 3,131(IB) 1,420(KG)"
                                                  "\nProduction- 1990-2000 "
                                                  "\nTop speed: 160 MPH"
                                                  "\n0-60: 5.9")
if JDM == "FTO":
    print("Tech specs of " + market + " " + JDM + "."
                                                  "\nBody Style- 2 door coupe"
                                                  "\nLayout-Front engine , front wheel drive"
                                                  "\nEngine type-1.8 L 4G93 SOHC 16V Inline 4"
                                                  "\nHorsepower- 123 hp"
                                                  "\nTorque- 199 NM"
                                                  "\nTransmission-5 speed manual"
                                                  "\n4 OR 5 speed automatic"
                                                  "\nWeight- 1,100-1,210(KG)2,425-2,668(IB)"
                                                  "\nProduction-  1994-2000"
                                                  "\nTop speed:140 MPH"
                                                  "\n0-60:6.9 seconds")
if JDM == "Lancer Evo iii":
    print("Tech specs of " + market + " " + JDM + "."
                                                  "\nBody Style- Sports sedan"
                                                  "\nLayout- All wheel drive"
                                                  "\nEngine type-2.0 L 4G63 I4 Turbocharged"
                                                  "\nHorsepower-266  hp"
                                                  "\nTorque- 309 Nm"
                                                  "\nTransmission-5 speed manual"
                                                  "\nWeight- 2,624 lb-2,778lb(1,190-1,260 kg)"
                                                  "\nProduction- 1995-1996"
                                                  "\nTop speed:  147 MPH"
                                                  "\n0-60:4.5 seconds")
if JDM == "Lancer evo VI":
    print("Tech specs of " + market + " " + JDM + "."
                                                  "\nBody Style- Sports sedan"
                                                  "\nLayout-All wheel drive"
                                                  "\nEngine type-2.0 L 4G63 Inline four engine"
                                                  "\nHorsepower- 276hp"
                                                  "\nTorque- 275 lb -ft"
                                                  "\nTransmission- 5 speed manual"
                                                  "\nWeight- 2,778-2,998 lb(1,260 kg-1,360 kg)"
                                                  "\nProduction-  1999-2001"
                                                  "\nTop speed:155 MPH"
                                                  "\n0-60:5 seconds")
if JDM == "Lancer Evo VIII":
    print("Tech specs of " + market + " " + JDM + "."
                                                  "\nBody Style- Sports sedan"
                                                  "\nLayout- All wheel drive"
                                                  "\nEngine type-2.0 L 4G63 Inline 4"
                                                  "\nHorsepower- 276 hp"
                                                  "\nTorque- 295 lb -ft"
                                                  "\nTransmission-5 or 6 speed manual,"
                                                  "\nWeight- 2,888-3,109lb(1,310-1,400 kg)"
                                                  "\nProduction-  2003-2005"
                                                  "\nTop speed:157 MPH"
                                                  "\n0-60:3.5 SECONDS")
    print()
# tech specs of Nissan
if JDM == "Nissan":
    JDM = input("Please select which Nissan model you wish to select."
                "\nNissan "
                "\nSkyline R34 "
                "\nSkyline R33 "
                "\nSkyline R32 "
                "\nSilvia S15 "
                "\nSilvia S14"
                "\nFairlady Z 300ZX "
                "\nFairlady 240z "
                "\nFairlady Z 350Z"
                "\n>>")
if JDM == "Skyline R34":
    print("Tech specs of " + market + " " + JDM + "."
                                                  "\nBody Style- 2 door coupe"
                                                  "\nLayout-front engine, 4WD"
                                                  "\nEngine type- 2.6 L TT RB26DETT I6"
                                                  "\nHorsepower- 166 hp"
                                                  "\nTorque- 173 lb -ft"
                                                  "\nTransmission-5 or 6 speed manual"
                                                  "\nWeight- 3,673 lbs(1666 kg)"
                                                  "\nProduction-  1998-2002"
                                                  "\nTop speed:165 mph"
                                                  "\n0-60:4.8 second")
if JDM == "Skyline R33":
    print("Tech specs of " + market + " " + JDM + "."
                                                  "\nBody Style- Coupe"
                                                  "\nLayout- Front, All wheel drive"
                                                  "\nEngine type- RB26DETT I6 Twincam,TT Intercooled"
                                                  "\nHorsepower- 276 hp"
                                                  "\nTorque- 173 lb -ft"
                                                  "\nTransmission-5 speed manual"
                                                  "\nWeight- 3530 lbs(1601 kg)"
                                                  "\nProduction-  1995-1998"
                                                  "\nTop speed:156 mph"
                                                  "\n0-60: 5.2 seconds")
if JDM == "Skyline R32":
    print("Tech specs of " + market + " " + JDM + "."
                                                  "\nBody Style- Coupe"
                                                  "\nLayout- front engine, all wheel drive"
                                                  "\nEngine type-RB26DETT I6 Twincam,TT Intercooled"
                                                  "\nHorsepower-  280 hp"
                                                  "\nTorque- 260 lb -ft"
                                                  "\nTransmission-5 speed manual"
                                                  "\nWeight- 3153 lbs(1430 kg)"
                                                  "\nProduction-  1989-1994"
                                                  "\nTop speed:156 mph"
                                                  "\n0-60:5.6 seconds")
if JDM == "Silvia S15":
    print("Tech specs of " + market + " " + JDM + "."
                                                  "\nBody Style- 2 door coupe "
                                                  "\nLayout- Front engine, rear wheel drive"
                                                  "\nEngine type- 2.0 L SR20DE Inline 4"
                                                  "\nHorsepower- 250 hp"
                                                  "\nTorque- 142 lb -ft"
                                                  "\nTransmission- 4 speed automatic, 5 speed manual"
                                                  "\nWeight- 2646 lbs(1200 kg)"
                                                  "\nProduction-  1999-2002"
                                                  "\nTop speed: 152 mph"
                                                  "\n0-60:5.5 seconds")
if JDM == "Silvia S14":
    print("Tech specs of " + market + " " + JDM + "."
                                                  "\nBody Style- Coupe"
                                                  "\nLayout- Front engine, rear wheel drive"
                                                  "\nEngine type-  2.0 SR20DE I4"
                                                  "\nHorsepower-  197 hp"
                                                  "\nTorque-  195 lb -ft"
                                                  "\nTransmission- 5 speed manual 4 speed automatic"
                                                  "\nWeight-  2762 lbs( 1253kg)"
                                                  "\nProduction-  1993-1998"
                                                  "\nTop speed:  146 mph"
                                                  "\n0-60:  7.5 seconds")
if JDM == "Fairlady Z 300ZX":
    print("Tech specs of " + market + " " + JDM + "."
                                                  "\nBody Style- Coupe"
                                                  "\nLayout- front engine, rear wheel drive"
                                                  "\nEngine type- 3.0 VG30DE V6"
                                                  "\nHorsepower- 222 hp"
                                                  "\nTorque- 198 lb -ft"
                                                  "\nTransmission-5 speed manual, 4 speed automatic"
                                                  "\nWeight- 3329-3538 lbs(1510-1605 kg)"
                                                  "\nProduction-  1989-2000"
                                                  "\nTop speed: 155 mph"
                                                  "\n0-60: 5-6 seconds")
if JDM == "Fairlady 240z":
    print("Tech specs of " + market + " " + JDM + "."
                                                  "\nBody Style- 3 door hatchback coupe"
                                                  "\nLayout-front engine, rear wheel drive"
                                                  "\nEngine type- 2.4 L L24 I6"
                                                  "\nHorsepower- 151 hp"
                                                  "\nTorque- 146 lb -ft"
                                                  "\nTransmission-3 speed automatic, 4 or 5 speed manual"
                                                  "\nWeight- 2,301.6 lbs(1,044 kg)"
                                                  "\nProduction-  1969-1973"
                                                  "\nTop speed: 126 mph"
                                                  "\n0-60: 8 seconds")
if JDM == "Fairlady Z 350Z":
    print("Tech specs of " + market + " " + JDM + "."
                                                  "\nBody Style- Hatchback coupe/roadster"
                                                  "\nLayout-Front engine, rear wheel drive"
                                                  "\nEngine type-3.5 L VQ35DE V6"
                                                  "\nHorsepower- 287 hp"
                                                  "\nTorque- 276 lb -ft"
                                                  "\nTransmission-5 speed automatic, 6 speed manual"
                                                  "\nWeight- 3,188-3,602 lbs(1,446-1,634 kg)"
                                                  "\nProduction-  2002-2008"
                                                  "\nTop speed:155 mph"
                                                  "\n0-60: 1.2 seconds")
    print()
# Tech specs of Subaru
if JDM == "Subaru":
    JDM = input("Please select which Subaru model you wish to select."
                "(\nSubaru "
                "\nImpreza WRX STI "
                "\nImpreza WRX STI Version VI "
                "\nBRZ"
                "\n>>")
if JDM == "Impreza WRX STI":
    print("Tech specs of " + market + " " + JDM + "."
                                                  "\nBody Style- 4 door saloon"
                                                  "\nLayout-front engine, all wheel drive"
                                                  "\nEngine type-Boxer 4, turbocharged,16 v"
                                                  "\nHorsepower- 276 hp"
                                                  "\nTorque- 193 lb -ft"
                                                  "\nTransmission-6 speed manual"
                                                  "\nWeight- 3307 lbs(1500 kg)"
                                                  "\nProduction-  2000-2007"
                                                  "\nTop speed: 174 mph"
                                                  "\n0-60:4.6 seconds")
if JDM == "Impreza WRX STI Version VI":
    print("Tech specs of " + market + " " + JDM + "."
                                                  "\nBody Style- 4 door saloon"
                                                  "\nLayout-front engine,all wheel drive"
                                                  "\nEngine type- 16 valve DOHC boxer 4, turbocharged"
                                                  "\nHorsepower- 276 hp"
                                                  "\nTorque- 251 lb -ft"
                                                  "\nTransmission-5 speed manual"
                                                  "\nWeight- 2800 lbs(1270 kg)"
                                                  "\nProduction-  1992-2000"
                                                  "\nTop speed: 152 mph"
                                                  "\n0-60: 4.8 seconds")
elif JDM == "BRZ":
    print("Tech specs of " + market + " " + JDM + "."
                                                  "\nBody Style- 2 door fastback coupe"
                                                  "\nLayout- front engine, rear wheel drive"
                                                  "\nEngine type-2.0 L 4U-GSE-FA20 H4"
                                                  "\nHorsepower- 197-204hp"
                                                  "\nTorque-151-156 lb -ft"
                                                  "\nTransmission-6 speed manual, 6 speed automatic"
                                                  "\nWeight- 2,624-2,800 lb(1,190-1,270 kg)"
                                                  "\nProduction-2012-present"
                                                  "\nTop speed:143 mph"
                                                  "\n0-60:6.4 seconds")
print()
# Time of day options
TOD = input("Select the time of day you wish to drive."
            "\nMorning🌅"
            "\nEvening🌇"
            "\n:")
# The beggining of the game.  First choices(Well not really ;)
# Adding mods. (Its as special surprise tool that will help us later ;)

mods = input("Do you wish to add modifications to your " + market + " " + JDM + ". "
                                                                                "\nThese include Spoilers,Tires,Engine swaps,Exhausts,etc.."
                                                                                "\nDo you wish to add these modifications"
                                                                                "\nyes"
                                                                                "\nno"
                                                                                "\n:")
print()
# Stage 1 beggining(Wangen sen)
city = input("Wonderful choice " + playa + ". I see you got style.."
                                           "\nWelcome to Tokyo, Japan.  This stage will have 3 stages.Each with their own storyline."
                                           "\nThe Wangan sen stage, the C1 inner stage, and the Tokyo bay aqualine."
                                           "\nWe will start with the Wangan sen stage.  As you progress. You will be able to access other stages."
                                           "\nRemember, each choice you make will lead to a different outcome."
                                           "\noh and you'll start off with  ¥600000"
                                           "\nAre you ready?"
                                           "\n(1)yes"
                                           "\n(2)no"
                                           "\n>>")

if city == "yes" or city == "1":
    print("Alrighty, onto stage 1 than")
else:
    print("We still going G. Hehehe.")
print()
# Toll booths/start of stage 1
yen = 600000

# Course 1 description
input("Current Balance: ¥" + str(yen))
input("Course name:Bayshore route(Wangen sen)"
      "\nTotal Length:43 Miles(70 km)"
      "\nCompleted Construction:1976"
      "\nThe legendary Bayshore route(湾岸線,Shuto Kōsokudōro Wangan-sen)..commonly known by the locals as the Wangan sen"
      "\nA 43 mile stretch of highway which connects Tokyo to Yokohama."
      "\nBy day, its busy as hell, but by night, is the hub of street races by Hashiriya(走り屋)"
      "\nThis is due to the route containing long stretches and emptiness as night. "
      "\nThis route known for the infamous Midnight club races which took place in the 90s"
      "\nThe infamous street racing group who only did max velocity, and pushed their cars to the limit.")
print()
print()
Bayshore = input("While crusin in your " + market + " " + JDM + " you arrive at a toll booth,and "
                                                                "\nDepending on the type of car you are required to pay a different type of amount. "
                                                                "\nFollowing prices are listed below "
                                                                "\nShuto Expressway Bayshore Route Toll Booth:"
                                                                "\nNormal cars:  3,000JPY"
                                                                "\nMidsize cars: 3,600JPY"
                                                                "\nLarge cars:   4,950JPY"
                                                                "\nSpecific large cars:  8,250JPY"
                                                                "\nKei-cars and motorcycles: 2,400JPY"
                                                                "\nNote:Kei cars are just mini cars"
                                                                "\nWhat type of car do you have?"
                                                                "\n(1)Normal car"
                                                                "\n(2)Midsize car"
                                                                "\n(3)Large car"
                                                                "\n(4)Specific large car"
                                                                "\n(5)Kei-car"
                                                                "\n:")
# Decrease in yen. you just payed toll booth

if Bayshore == "Normal car" or Bayshore == "1":
    yen -= 3000
if Bayshore == "Midsize car" or Bayshore == "2":
    yen -= 3600
if Bayshore == "Large car" or Bayshore == "3":
    yen -= 4950
elif Bayshore == "Specific large car" or Bayshore == "4":
    yen -= 8250
elif Bayshore == "Kei-car" or Bayshore == "5":
    yen -= 2400

Bayshore = input("Current Balance: ¥" + str(yen))
input("As you cruise in your  " + market + " " + JDM + ", "
                                                       "\nyou notice another Hashriya driving. One with a Porsche 911 GT2(95)"
                                                       "\nHe flickers at you... ")
print()
input("Hashiriya - Hey you, I like your  " + market + " " + JDM + ","
                                                                  "\nHow about we do a friendly race from here to Yokohama Bay Bridge."
                                                                  "\nWinner gets ¥100000 ")
print()
dajou = input("\nDo you...."
              "\n(Accept)Accept the challenge"
              "\n(Decline)Decline and call it a night"
              "\n>>")
print()
print()
# Option 1(Challenge 1)
if dajou == "Accept the challenge" or dajou == "Accept":
    print("Driver- Last one to the Yokohama Bay bridge loses ")
elif dajou == "Decline and call it a night" or dajou == "Decline":
    print("Too bad " + playa + ", challenge still stands")

waitime = 10

while waitime > 0:
    mins, secs = divmod(waitime, 60)
    timeformat = '{:02d}:{:02d}'.format(mins, secs)
    print(timeformat)
    time.sleep(1)
    waitime -= 1
print("GO!")
# Option 2 Cop Shows up
print()
# Manual layout(6th gear layout)
input("Manual layout of " + market + " " + JDM + ","
                                                 "R"
                                                 "\n|  1  3  5"
                                                 "\n---|--|--|"
                                                 "\n   2  4  6")
shift1 = input("Current gear-1st gear"
               "\nWhich gear would you like to shift too"
               "\nNote:You can skip gears, but this will result in waiting for a rev drop"
               "\n>> ")
if shift1 > "2":
    print("Ehh, its fine if you skip gears, but"
          "\nNow, you'll have to wait a bit for the rev's to drop")
    print()
    # Rev hang result(8 second delay)
    import time

    waitime = 8
    while waitime > 0:
        mins, secs = divmod(waitime, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat)
        time.sleep(1)
        waitime -= 1

# Smooth transmission
print()
if shift1 == "2":
    print("Going for the smooth transition I see."
          "\nHashiriya- Coming up, but you gotta long way to go buddy. ")
print()
input("Now nearing the tokyo international cruise line, "
      "\nyou realize its time to shift gears again")
print()
# Second shift:Option
shift2 = input("R"
               "\n|  1  3  5"
               "\n---|--|--|"
               "\n   2  4  6 "
               "\nWhich gear do you wish to shift to"
               "\nNote:Currently on " + shift1 + " gear."
                                                 "\n>>")
# If the second shift is greater than the first gear ration. increase in acceleration/cost of top speed
print()
if shift2 > shift1:
    print("Since you decided to increase gears, you're still in the come up."
          "\nYou have increased in acceleration but not speed....."
          "\nHashiriya-you gotta long way to go ")
    print()
# If second gear ratio is lower than 1st gear ratio, increase in top speed/cost of acceleration
elif shift2 < shift1:
    print("Hashiriya-Wait where the hell did you come from?"
          "\nWow, you're right behind the driver."
          "\nNow entering the kawasaki tunnel, you aren't so far,"
          "\nfrom the Kawasaki Kōro tunnel ")
    print()
shift3 = input("This will determine who will most likely get ahead in the long run."
               "\nCurrent gear:" + shift2 + " gear"
                                            "\nR"
                                            "\n|  1  3  5"
                                            "\n---|--|--|"
                                            "\n   2  4  6 "
                                            "\nWhich gear do you want to shift to"
                                            "\n>>")
if shift3 < shift2:
    print("Because you decided to increase the top speed in cost,"
          "\nthe other Hashiriya suppresses you, and leaves you in the dust💨💨."
          "\nYou lose......🤧🤧")
elif shift3 > shift2:
    print("Hashiriya - Wha, 何 (なに),how did you get behind me?"
          "\nOh shit, you're actually catching up 🤯😳"
          "\nAt the cost of top speed, you decided to increase the acceleration,"
          "\nWhich resulted in you surpassing the other Hashiriya. ")
print()
Kawasaki = input('Now in a intense head to head Kawasaki Kōro tunnel'
                 '\nIt time to shift gears, but you hit your foot on the clutch...'
                 '\nDo you release your fot off the clutch.....'
                 '\n(Q)Quickly'
                 '\nor (S)Slowly'
                 '\n>>')
if Kawasaki == "Quickly" or Kawasaki == "Q":
    print("Andddd just like that you stalled your car letting your opponent 💨 you"
          "\nGAME OVER")
    exit()
elif Kawasaki == "Slowly" or "S":
    print("With a increasing gap between you and the other driver,"
          "\nYou successfully keep that gap long enough to surpass him"
          "\nIn the Kawasaki Kōro tunnel.")
print()
poliezi = input("\nUnfortunately, this intense head to head is brought to a halt once you exit out the tunnel..."
                "\nYou spot  a black and white Toyota crown police car!🚔🚔"
                "\nSirens start wailing."
                "\nBecause you dont feel like being a idiot this " + TOD + ","
                                                                           "\nYou decided to pull over... ")

# Pull over result
if poliezi == "Pull Over":
    input("👮‍️-Good " + TOD + ".")
print()
input("you- Good " + TOD + " officer.")
print()
input("SGT Yoshida- I am Sergeant Yoshida. Im a currently part of the traffic bureau((交通部))"
      "\nof the  Tokyo Metropolitan Police(警視庁)")
print()
input("you- Really? Well what did I do Officer")
print()
input("SGT Yoshida- Sir you were going pulling a 160 MPH Speed run on the Wangan sen.")
print()
input("you- How is that a problem....")
print()
input("SGT Yoshida- The speed limit is 50 mph......")
print()
input("Anyway, I must fine you ¥15000 for a speeding violation.")
# Pull over actual choices
osaka = input("\nWhile the cop goes to his vehicle"
              "\nYou have a choice of either escaping or just staying"
              "\nDo you...... (1)escape or (2)stay?"
              "\n>>")
print()
if osaka == "stay" or osaka == "2":
    print("Sergeant Yoshida- Okay Sir, this just  a warning, if you are found street racing again, you might be arrested"
          "\nand  your car can potentially become in possession of the Tokyo Metropolitan Police.")
    input("you- Understood Officer."
          "\nyou- Have a wonderful " + TOD + " officer."
                                             "\nAnyway you pay the fine, and go about you way."
                                             "\nGAME OVER")
    yen -= 15000
    osaka = input("Current Balance: ¥" + str(yen))
    exit()
elif osaka == "escape" or osaka == "1" or poliezi == "Outrun":
    print("Unit 4, Suspect is attempting a escape on the Wangan sen!!"
          "\nRequesting backup!!")
print()
chase = input("Now the chase is on because for some reason you still want to race..."
              "\nbut other than that, some sirens are coming at ya"
              "\nand now you see two exits, in which one of them is a life saver"
              "\nexit 7 leads to Haneda airport"
              "\nexit 8 leads to yokohama bay bridge, and leads to the city of Yokohama"
              "\nChoose a exit, and remember, choose wisely...."
              "\n(1)exit 7"
              "\n(2)exit 8"
              "\n>>")
print()
if chase == "exit 7" or chase == "1":
    chase = input("🚨Turn off you car, stay where you are! Driver, you are under arrest.🚨"
                  "\nDamn, you've been busted.  There was a roadblock at the airport waiting for you"
                  "\nTip:Never go to a airport during a pursuit. Thats just dumb"
                  "\n🚨Busted. Game over🚨")
    exit()
if chase == "exit 8" or chase == "2":
    print("Ehhh, he gave me the slip. I've lost him, breaking pursuit.")
    print()
selector = input("Bueno.You have evaded arrest, but now you must swap your car or you'll get caught"
                 "\nYou recieve a phone call from your friend Hiroshi,"
                 "\n. 📱 Hiroshi- Yo, " + playa + ", wanna meet up at Daikoku parking lot?"
                                                  "\nDo you accept?"
                                                  "\n(1)accept"
                                                  "\n(2)deny"
                                                  "\n>>")
print()
if selector == "deny" or selector == "2":
    print("\n. 📱Hiroshi- maybe another time"
          "\n. 📱you- Yeah, maybe another time...."
          "\nThank you for playing my game..Have a wonderful day " + playa + "!!")
    exit()
else:
    stage3 = input("Are you sure you wish to proceed to Stage 2 of Hashriya Undergrounds"
                   "\n(1)yes"
                   "\n(2)no"
                   "\n>>")
if stage3 == "no" or stage3 == "2":
    print(".Hiroshi- maybe another time"
          "\n.you- Yeah, maybe another time...."
          "Thank you for playing my game..Have a wonderful day " + playa + "!!")
    exit()
else:
    print("Welcome to Stage 2:C1 Inner Loop.")

# Stage 2 C1 Inner
print()
sasuke = input("Because you just got caught by the cops and probably are in their database by now.."
               "\nits time to swap your car,"
               "\nChoose a Japanese car manufactuer"
               "\nHonda"
               "\nMazda"
               "\nMitsubishi"
               "\nNissan"
               "\nSubaru"
               "\nToyota"
               "\n>>")
print()
yokohama = input("Because you just got caught by the cops and probably are in their database by now.."
                 "\nits time to swap your car,"
                 "\nChoose a Japanese car manufactuer"
                 "\nJust add the Car manufacturer from the top you selected."
                 "\nHonda"
                 "\nMazda"
                 "\nMitsubishi"
                 "\nNissan"
                 "\nSubaru"
                 "\nToyota"
                 "\n>>")
print()
if yokohama == "Honda":
    yokohama = input("Please select which Honda  model you wish to select. "
                     "(\nHonda S2000"
                     "\nNsx(NC1)"
                     "\nCivic EK9"
                     "\n>")
    # Tech specs of Honda cars
    if yokohama == "S2000":
        print("Tech specs of " + market + " " + JDM + "."
                                                      "\nBody Style-2  door roadster"
                                                      "\nLayout-Front engine and Rear wheel drive"
                                                      "\nEngine type-  Naturally Aspirated inline 4"
                                                      "\nHorsepower-237 hp"
                                                      "\nTorque-162 lb per feet"
                                                      "\nTransmission-6 speed manual"
                                                      "\nWeight-1,250 kg(2,756 lb)"
                                                      "\nProduction- 1999-2009"
                                                      "\nTop speed:160 mph")
    elif yokohama == "Nsx(NC1)":
        print("Tech specs of " + market + " " + yokohama + "."
                                                           "\nBody Style- 2 door coupe,2 door targa top"
                                                           "\nLayout- Transverse mid-engine,RWD"
                                                           "\nEngine type-  Honda C30A V6"
                                                           "\nHorsepower- 270 hp"
                                                           "\nTorque-210 lb-ft"
                                                           "\nTransmission-5 OR 6 SPEED MANUAL"
                                                           "\nWeight- 3,020 lb(1,370 kg)"
                                                           "\nProduction-  1990-2005"
                                                           "\nTop speed:191 MPH")
    if yokohama == "EK9":
        print("Tech specs of " + market + " " + yokohama + "."
                                                           "\nBody Style- 2 door hatchback"
                                                           "\nLayout-Front engine, front wheel drive(F-F)"
                                                           "\nEngine type-  1.6 L B16B Inline 4"
                                                           "\nHorsepower- 182 hp"
                                                           "\nTorque-160 NM"
                                                           "\nTransmission-5 speed manual"
                                                           "\nWeight- 2,403 lb(1,090 kg)"
                                                           "\nProduction-  1997-2000"
                                                           "\nTop speed:146 MPH")
        print()
# Tech specs of Toyota

elif yokohama == "Toyota":
    yokohama = input("Please select which Toyota you wish to select. "
                     "\nToyota"
                     "\nSupra A70"
                     "\nSupra RZ"
                     "\nSoarer 2.5 GT TT"
                     "\nMR2"
                     "\nCorolla AE86 Trueno"
                     "\n>>")
if yokohama == "Supra A70":
    print("Tech specs of " + market + " " + yokohama + "."
                                                       "\nBody Style- coupe"
                                                       "\nLayout- front engine, rear wheel drive"
                                                       "\nEngine type- Toyota 7m -GTE (Modified CT26 Turbo"
                                                       "\nHorsepower- 267 hp"
                                                       "\nTorque- 264 lb -ft"
                                                       "\nTransmission-5 speed manual, 4 speed automatic"
                                                       "\nWeight- 3,219-3,616 lbs(manual) 3,483-3,792 lbs(automatic)"
                                                       "\nProduction-  1986-1993"
                                                       "\nTop speed: 144 mph"
                                                       "\n0-60: 6.9 seconds")
if yokohama == "Supra RZ":
    print("Tech specs of " + market + " " + yokohama + "."
                                                       "\nBody Style- Coupe"
                                                       "\nLayout-front engine, rear wheel drive"
                                                       "\nEngine type- I6, 2JZ"
                                                       "\nHorsepower- 171 hp"
                                                       "\nTorque- 203 lb -ft"
                                                       "\nTransmission-6 speed manual"
                                                       "\nWeight- 3,616 lb(1,640 kg)"
                                                       "\nProduction-  1993-2002"
                                                       "\nTop speed: 155 mph"
                                                       "\n0-60:5.3 seconds")
if yokohama == "Soarer 2.5 GT TT":
    print("Tech specs of " + market + " " + yokohama + "."
                                                       "\nBody Style- 2 door coupe"
                                                       "\nLayout- Front engine, Rear wheel drive"
                                                       "\nEngine type-3.0 2JZ-GE I6(JZZ31)"
                                                       "\nmHorsepower- 222 hp"
                                                       "\nTorque- 210 lb -ft"
                                                       "\nTransmission- 5 speed manual,4 or 5 speed automatic"
                                                       "\nWeight- 3,395-3,814 Ib(1,540 kg-1,730 kg)"
                                                       "\nProduction-  1991-2000"
                                                       "\nTop speed:146-156 mph"
                                                       "\n0-60:7.4 seconds")
if yokohama == "MR2":
    print("Tech specs of " + market + " " + yokohama + "."
                                                       "\nBody Style- Coupe"
                                                       "\nLayout- Mid engine, rear wheel drive"
                                                       "\nEngine type- 2.2 L 5s -FE Inline 4"
                                                       "\nHorsepower-  200 hp"
                                                       "\nTorque- 137 lb -ft"
                                                       "\nTransmission-5 speed manual, 4 speed automatic"
                                                       "\nWeight- 2,579 lb(1170 kg)"
                                                       "\nProduction-  1989-1999"
                                                       "\nTop speed: 152 mph"
                                                       "\n0-60:6.5")
if yokohama == "Corolla AE86 Trueno":
    print("Tech specs of " + market + " " + yokohama + "."
                                                       "\nBody Style- Compact . 2 door"
                                                       "\nLayout- Front engine, rear wheel drive"
                                                       "\nEngine type-  1.6 L 4a-GEU Inline 4 DOHC"
                                                       "\nHorsepower- 122 hp"
                                                       "\nTorque- 108 lb -ft"
                                                       "\nTransmission-5 speed manual"
                                                       "\nWeight- 2138 lbs(970 kg)"
                                                       "\nProduction-  1983-1987"
                                                       "\nTop speed: 118 mph"
                                                       "\n0-60: 8.6 seconds")
    print()
# Tech specs of Mazda
if yokohama == "Mazda":
    yokohama = input("Please select which Mazda model  you wish to select. "
                     "\nMazda RX 7 FD35"
                     "\nRX 7 FC35"
                     "\nMiata mx5 NA"
                     "\nMiata mx5 NB"
                     "\nRX 8"
                     "\n>>")
    if yokohama == "RX 7 FD35":
        print("Tech specs of " + market + " " + yokohama + "."
                                                           "\nBody Style- 2 seater Coupe"
                                                           "\nLayout-Front Mid engine, Rear wheel drive"
                                                           "\nEngine type-  1.3 L TT 13B-REW Twin rotor(Rotary engine)"
                                                           "\nHorsepower- 252 hp"
                                                           "\nTorque-217 lb -ft"
                                                           "\nTransmission-5 speed manual"
                                                           "\nWeight- 1,260 kg (2,778 lb)"
                                                           "\nProduction-  1992-2002"
                                                           "\nTop speed: 160 MPH")
    if yokohama == "RX 7 FC35":
        print("Tech specs of " + market + " " + yokohama + "."
                                                           "\nBody Style- 2 DOOR COUPE"
                                                           "\nLayout-Front Mid engine, Rear wheel drive"
                                                           "\nEngine type-1.3 L 13B VIDEO (S4)"
                                                           "\nHorsepower-  185 hp"
                                                           "\nTorque- 25.0 kg-m"
                                                           "\nTransmission-5 Speed manual"
                                                           "\nWeight- 2,626-3,492 lb(1,223-1,584 kg)"
                                                           "\nProduction-  1985-1992"
                                                           "\nTop speed:120 MPH"
                                                           "\n0-60:")
    if yokohama == "Miata mx5 NA":
        print("Tech specs of " + market + " " + yokohama + "."
                                                           "\nBody Style- 2 door  coupe"
                                                           "\nLayout-Front mid engine,Rear wheel drive"
                                                           "\nEngine type-1,598 cc B6ZE(RS)DOHC Inline 4"
                                                           "\nHorsepower-   128hp"
                                                           "\nTorque- 110 lb -ft"
                                                           "\nTransmission- 5 Speed manual"
                                                           "\nWeight- 2,120 IB(960 Kg)"
                                                           "\nProduction-  1989-1997"
                                                           "\nTop speed:116 MPH"
                                                           "\n0-60:")
    if yokohama == "Miata mx5 NB":
        print("Tech specs of " + market + " " + yokohama + "."
                                                           "\nBody Style-  2 door coupe/convertible"
                                                           "\nLayout-Front mid engine(Rear wheel drive)"
                                                           "\nEngine type-1.8 L BP-5A Inline 4"
                                                           "\nHorsepower-  140 hp"
                                                           "\nTorque- 119 lb -ft"
                                                           "\nTransmission-5 or 6 speed manual transmission"
                                                           "\nWeight- 2,348 IB(1,065 KG)"
                                                           "\nProduction-  1998-2005"
                                                           "\nTop speed:127 MPH"
                                                           "\n0-60:")
    if yokohama == "RX 8":
        print("Tech specs of " + market + " " + yokohama + "."
                                                           "\nBody Style- 4 door quad coupe"
                                                           "\nLayout-Front mid engine, rear wheel drive"
                                                           "\nEngine type- 1.3 L RENESIS "
                                                           "\nHorsepower- 189-238 hp"
                                                           "\nTorque- 159 lb -ft"
                                                           "\nTransmission-5 or 6 speed manual"
                                                           "\n4 and 6 speed automatic"
                                                           "\nWeight- Manual-2,886-3,027 lb(1,309-1,373 kg)"
                                                           "\nProduction-  2003-2012"
                                                           "\nTop speed: 145 MPH"
                                                           "\n0-60:6.4 seconds")
        print()
# Tech specs of Mitsubishi
elif yokohama == "Mitsubishi":
    yokohama = input("Please select which Mitsubishi model you wish to select."
                     "\nMitsubishi "
                     "\nGTO TT "
                     "\nFTO "
                     "\nLancer Evo iii "
                     "\nLancer evo VI "
                     "\nLancer Evo VIII"
                     "\n>>")
    if yokohama == "GTO TT":
        print("Tech specs of " + market + " " + yokohama + "."
                                                           "\nBody Style- 2 door liftback coupe"
                                                           "\nLayout-Transverse front engine.4WD"
                                                           "\nEngine type-3.0 L 6G72 DOHC 24v TT V6"
                                                           "\nHorsepower-276 hp"
                                                           "\nTorque- 308 lb -ft"
                                                           "\nTransmission-5 or 6 speed manual"
                                                           "\n4 speed automatic"
                                                           "\nWeight- 3,131(IB) 1,420(KG)"
                                                           "\nProduction- 1990-2000 "
                                                           "\nTop speed: 160 MPH"
                                                           "\n0-60: 5.9")
    if yokohama == "FTO":
        print("Tech specs of " + market + " " + yokohama + "."
                                                           "\nBody Style- 2 door coupe"
                                                           "\nLayout-Front engine , front wheel drive"
                                                           "\nEngine type-1.8 L 4G93 SOHC 16V Inline 4"
                                                           "\nHorsepower- 123 hp"
                                                           "\nTorque- 199 NM"
                                                           "\nTransmission-5 speed manual"
                                                           "\n4 OR 5 speed automatic"
                                                           "\nWeight- 1,100-1,210(KG)2,425-2,668(IB)"
                                                           "\nProduction-  1994-2000"
                                                           "\nTop speed:140 MPH"
                                                           "\n0-60:6.9 seconds")
    if yokohama == "Lancer Evo iii":
        print("Tech specs of " + market + " " + yokohama + "."
                                                           "\nBody Style- Sports sedan"
                                                           "\nLayout- All wheel drive"
                                                           "\nEngine type-2.0 L 4G63 I4 Turbocharged"
                                                           "\nHorsepower-266  hp"
                                                           "\nTorque- 309 Nm"
                                                           "\nTransmission-5 speed manual"
                                                           "\nWeight- 2,624 lb-2,778lb(1,190-1,260 kg)"
                                                           "\nProduction- 1995-1996"
                                                           "\nTop speed:  147 MPH"
                                                           "\n0-60:4.5 seconds")
    if yokohama == "Lancer evo VI":
        print("Tech specs of " + market + " " + yokohama + "."
                                                           "\nBody Style- Sports sedan"
                                                           "\nLayout-All wheel drive"
                                                           "\nEngine type-2.0 L 4G63 Inline four engine"
                                                           "\nHorsepower- 276hp"
                                                           "\nTorque- 275 lb -ft"
                                                           "\nTransmission- 5 speed manual"
                                                           "\nWeight- 2,778-2,998 lb(1,260 kg-1,360 kg)"
                                                           "\nProduction-  1999-2001"
                                                           "\nTop speed:155 MPH"
                                                           "\n0-60:5 seconds")
    if yokohama == "Lancer Evo VIII":
        print("Tech specs of " + market + " " + yokohama + "."
                                                           "\nBody Style- Sports sedan"
                                                           "\nLayout- All wheel drive"
                                                           "\nEngine type-2.0 L 4G63 Inline 4"
                                                           "\nHorsepower- 276 hp"
                                                           "\nTorque- 295 lb -ft"
                                                           "\nTransmission-5 or 6 speed manual,"
                                                           "\nWeight- 2,888-3,109lb(1,310-1,400 kg)"
                                                           "\nProduction-  2003-2005"
                                                           "\nTop speed:157 MPH"
                                                           "\n0-60:3.5 SECONDS")
        print()
# Tech specs of Nissan cars
if yokohama == "Nissan":
    yokohama = input("Please select which Nissan model you wish to select."
                     "\nNissan "
                     "\nSkyline R34 "
                     "\nSkyline R33 "
                     "\nSkyline R32 "
                     "\nSilvia S15"
                     "\nSilvia S14 "
                     "\nFairlady Z 300ZX "
                     "\nFairlady 240z, "
                     "\nFairlady Z 350Z"
                     "\n>>")
    if yokohama == "Skyline R34":
        print("Tech specs of " + market + " " + yokohama + "."
                                                           "\nBody Style- 2 door coupe"
                                                           "\nLayout-front engine, 4WD"
                                                           "\nEngine type- 2.6 L TT RB26DETT I6"
                                                           "\nHorsepower- 166 hp"
                                                           "\nTorque- 173 lb -ft"
                                                           "\nTransmission-5 or 6 speed manual"
                                                           "\nWeight- 3,673 lbs(1666 kg)"
                                                           "\nProduction-  1998-2002"
                                                           "\nTop speed:165 mph"
                                                           "\n0-60:4.8 second")
    if yokohama == "Skyline R33":
        print("Tech specs of " + market + " " + yokohama + "."
                                                           "\nBody Style- Coupe"
                                                           "\nLayout- Front, All wheel drive"
                                                           "\nEngine type- RB26DETT I6 Twincam,TT Intercooled"
                                                           "\nHorsepower- 276 hp"
                                                           "\nTorque- 173 lb -ft"
                                                           "\nTransmission-5 speed manual"
                                                           "\nWeight- 3530 lbs(1601 kg)"
                                                           "\nProduction-  1995-1998"
                                                           "\nTop speed:156 mph"
                                                           "\n0-60: 5.2 seconds")
    if yokohama == "Skyline R32":
        print("Tech specs of " + market + " " + yokohama + "."
                                                           "\nBody Style- Coupe"
                                                           "\nLayout- front engine, all wheel drive"
                                                           "\nEngine type-RB26DETT I6 Twincam,TT Intercooled"
                                                           "\nHorsepower-  280 hp"
                                                           "\nTorque- 260 lb -ft"
                                                           "\nTransmission-5 speed manual"
                                                           "\nWeight- 3153 lbs(1430 kg)"
                                                           "\nProduction-  1989-1994"
                                                           "\nTop speed:156 mph"
                                                           "\n0-60:5.6 seconds")
    if yokohama == "Silvia S15":
        print("Tech specs of " + market + " " + yokohama + "."
                                                           "\nBody Style- 2 door coupe "
                                                           "\nLayout- Front engine, rear wheel drive"
                                                           "\nEngine type- 2.0 L SR20DE Inline 4"
                                                           "\nHorsepower- 250 hp"
                                                           "\nTorque- 142 lb -ft"
                                                           "\nTransmission- 4 speed automatic, 5 speed manual"
                                                           "\nWeight- 2646 lbs(1200 kg)"
                                                           "\nProduction-  1999-2002"
                                                           "\nTop speed: 152 mph"
                                                           "\n0-60:5.5 seconds")
    if yokohama == "Silvia S14":
        print("Tech specs of " + market + " " + yokohama + "."
                                                           "\nBody Style- Coupe"
                                                           "\nLayout- Front engine, rear wheel drive"
                                                           "\nEngine type-  2.0 SR20DE I4"
                                                           "\nHorsepower-  197 hp"
                                                           "\nTorque-  195 lb -ft"
                                                           "\nTransmission- 5 speed manual 4 speed automatic"
                                                           "\nWeight-  2762 lbs( 1253kg)"
                                                           "\nProduction-  1993-1998"
                                                           "\nTop speed:  146 mph"
                                                           "\n0-60:  7.5 seconds")
    if yokohama == "Fairlady Z 300ZX":
        print("Tech specs of " + market + " " + yokohama + "."
                                                           "\nBody Style- Coupe"
                                                           "\nLayout- front engine, rear wheel drive"
                                                           "\nEngine type- 3.0 VG30DE V6"
                                                           "\nHorsepower- 222 hp"
                                                           "\nTorque- 198 lb -ft"
                                                           "\nTransmission-5 speed manual, 4 speed automatic"
                                                           "\nWeight- 3329-3538 lbs(1510-1605 kg)"
                                                           "\nProduction-  1989-2000"
                                                           "\nTop speed: 155 mph"
                                                           "\n0-60: 5-6 seconds")
    if yokohama == "Fairlady 240z":
        print("Tech specs of " + market + " " + yokohama + "."
                                                           "\nBody Style- 3 door hatchback coupe"
                                                           "\nLayout-front engine, rear wheel drive"
                                                           "\nEngine type- 2.4 L L24 I6"
                                                           "\nHorsepower- 151 hp"
                                                           "\nTorque- 146 lb -ft"
                                                           "\nTransmission-3 speed automatic, 4 or 5 speed manual"
                                                           "\nWeight- 2,301.6 lbs(1,044 kg)"
                                                           "\nProduction-  1969-1973"
                                                           "\nTop speed: 126 mph"
                                                           "\n0-60: 8 seconds")
    if yokohama == "Fairlady Z 350Z":
        print("Tech specs of " + market + " " + yokohama + "."
                                                           "\nBody Style- Hatchback coupe/roadster"
                                                           "\nLayout-Front engine, rear wheel drive"
                                                           "\nEngine type-3.5 L VQ35DE V6"
                                                           "\nHorsepower- 287 hp"
                                                           "\nTorque- 276 lb -ft"
                                                           "\nTransmission-5 speed automatic, 6 speed manual"
                                                           "\nWeight- 3,188-3,602 lbs(1,446-1,634 kg)"
                                                           "\nProduction-  2002-2008"
                                                           "\nTop speed:155 mph"
                                                           "\n0-60: 1.2 seconds")
# Tech  specs of Subaru cars
elif yokohama == "Subaru":
    yokohama = input("Please select which Subaru model you wish to select."
                     "(\nSubaru"
                     "\nImpreza WRX STI"
                     "\nImpreza WRX STI Version VI"
                     "\nSubarau BRZ"
                     "\n>>")
    if yokohama == "Impreza WRX STI":
        print("Tech specs of " + market + " " + yokohama + "."
                                                           "\nBody Style- 4 door saloon"
                                                           "\nLayout-front engine, all wheel drive"
                                                           "\nEngine type-Boxer 4, turbocharged,16 v"
                                                           "\nHorsepower- 276 hp"
                                                           "\nTorque- 193 lb -ft"
                                                           "\nTransmission-6 speed manual"
                                                           "\nWeight- 3307 lbs(1500 kg)"
                                                           "\nProduction-  2000-2007"
                                                           "\nTop speed: 174 mph"
                                                           "\n0-60:4.6 seconds")
    if yokohama == "Impreza WRX STI Version VI":
        print("Tech specs of " + market + " " + yokohama + "."
                                                           "\nBody Style- 4 door saloon"
                                                           "\nLayout-front engine,all wheel drive"
                                                           "\nEngine type- 16 valve DOHC boxer 4, turbocharged"
                                                           "\nHorsepower- 276 hp"
                                                           "\nTorque- 251 lb -ft"
                                                           "\nTransmission-5 speed manual"
                                                           "\nWeight- 2800 lbs(1270 kg)"
                                                           "\nProduction-  1992-2000"
                                                           "\nTop speed: 152 mph"
                                                           "\n0-60: 4.8 seconds")
    elif yokohama == "BRZ":
        print("Tech specs of " + market + " " + yokohama + "."
                                                           "\nBody Style- 2 door fastback coupe"
                                                           "\nLayout- front engine, rear wheel drive"
                                                           "\nEngine type-2.0 L 4U-GSE-FA20 H4"
                                                           "\nHorsepower- 197-204hp"
                                                           "\nTorque-151-156 lb -ft"
                                                           "\nTransmission-6 speed manual, 6 speed automatic"
                                                           "\nWeight- 2,624-2,800 lb(1,190-1,270 kg)"
                                                           "\nProduction-2012-present"
                                                           "\nTop speed:143 mph"
                                                           "\n0-60:6.4 seconds")
    print()
# Stage 2 C1 inner
parking = input("The next day......"
                "\nWhile cruisin in your  " + sasuke + " " + yokohama + " around " + TOD + " you recieve a call from ya boi Hiroshi"
                                                                                           "\nHe ask you to come to a car meet around  Daifoku Parking lot."
                                                                                           "\nWanna go?"
                                                                                           "\nYes"
                                                                                           "\nNo"
                                                                                           "\n>>")
if parking == "yes":
    print("Lets goooo")
else:
    print("You still coming G")
# Actual start of Stage 2/Description
print()
input("Current Balance: ¥" + str(yen))
print()
input("Course name:C1 Inner Loop"
      "\nTotal Length:9.2 mi(14.8 km)"
      "\nCompleted Construction:1967"
      "\nPartially built in anticipation for the 1964 Tokyo Summer Olympics,"
      "\nThe Inner Circular Route(都心環状線, Toshin Kanjō-sen),commonly known as the C1 Loop"
      "\nis a route part of the Shuto Expressway, located around the central part of the  Greater Tokyo Area."
      "\nThe C1 loop completes a loop around special wards Chidoya, Chuo and Minato.")
print()
city = input("You have just left Fujiwara's Tuning shop in Yokohama, "
             "\nand is now on the way to Daikoku parking lot. You arrive and meet the bois. "
             "\nYour homie hiroshi ask,"
             "\nHiroshi- hey " + playa + ", wanna go for a midnight run?"
                                         "\nStay"
                                         "\nGo"
                                         "\n>>")
print()
if city == "Go":
    city = input("Hiroshi- Bet. Wanna do a run on the Daikoku route to C1 inner?"
                 "\nyes"
                 "\nno"
                 "\n>>")
if city == "yes":
    print("すごい(Sugoi)!! Start your " + sasuke + " " + yokohama + ", Off to C1 Loop we go!!!")
elif city == "Stay":
    print("Hiroshi- You still coming with us")
else:
    exit()
print()
toll = input("Right before you leave,"
             "\nYou must pay at the Daikoku parking lot toll booth."
             "\nFollowing prices are listed below:"
             "\nNormal cars:  3,000JPY"
             "\nMidsize cars: 3,600JPY"
             "\nLarge cars:   4,950JPY"
             "\nSpecific large cars:  8,250JPY"
             "\nKei-cars and motorcycles: 2,400JPY"
             "\nNote:Kei cars are just mini cars"
             "\nWhat type of car do you have?"
             "\n(1)Normal car"
             "\n(2)Midsize car"
             "\n(3)Large car"
             "\n(4)Specific large car"
             "\n(5)Kei-car and motorcycle"
             "\n>>")
print()
# Decrease in yen. you just payed toll booth

if toll == "Normal car" or toll == "1":
    yen -= 3000
if toll == "Midsize car" or toll == "2":
    yen -= 3600
if toll == "Large car" or toll == "3":
    yen -= 4950
elif toll == "Specific large car" or toll == "4":
    yen -= 8250
elif toll == "Kei-car" or toll == "5":
    yen -= 2400
toll = input("Current Balance: ¥" + str(yen))
print()
# Next part of game(C1 inner)
input(
    "You and the bois are known crusin through Daikoku route during the " + TOD + " "
                                                                                  "\nAll of a sudden, a Porsche 911 GT2(95) appears and flickers its lights."
                                                                                  "\nyou pull over, and a female walks out of the car.")
input("Female driver- Nice ride.  Ain't that a " + market + " " + JDM + "?"
                                                                        "\n" + playa + "-Uhh, yeah.... This is my " + JDM + ". My name is " + playa + ".")
print()
femaledriver = "Naomi"
input("Female driver- " + femaledriver + ", my name is " + femaledriver + ".")
print()
input("" + femaledriver + "- Anyway, I was just curious because i saw your ride, "
                          "\nI was thinking about doing a friendly competition.")
print()
input("" + playa + ". what type of competition")
print()
input("Reina- A PINKSLIP RACE OFC."
      "\n2 laps around city inner. Last lap, whoever, can cross Rainbow bridge")
pinkslip = input("(1)What the hell is a pinkslip race?"
                 "\n(2)Ummm sure....")
if pinkslip == "1" or "What the hell is a pinkslip race?":
    print("In a nutshell, you're basiclly putting your car on the line,"
          "\nIf i were to win, you would lose your car, and i would basically have your car."
          "\nIf you were to win, you would have my car, and I would lose my car.")
else:
    print("Hmm, you sure are bold to put your car on the line?")
    print()
city = input("\nDo you accept the challenge?"
             "\n(1)yes"
             "\n(2)no"
             "\n>>")
print()
if city == "no" or city == "2":
    print("Hmmm. maybe another ti....SIKKEEEE "
          "\nNow being pressured by your friends and actually have a chance to show of your" + sasuke + " " + yokohama + ", you agree, to a friendly...competition...."
                                                                                                                         "\nTwo laps along the C1 inner loop, with a final stretch on the Rainbow Bridge."
                                                                                                                         "\nYa Boi Tadashi says"
                                                                                                                         "\nI WILL START THE COUNTDOWN.")
    print()
    import time

    waitime = 10

    while waitime > 0:
        mins, secs = divmod(waitime, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat)
        time.sleep(1)
        waitime -= 1
    print("GO!")
    print()
    print()
elif city == "yes" or city == "1":
    print("Ya boi Tadashi says..."
          "\nI WILL START THE COUNTDOWN.")
    print()
    import time

    waitime = 10

    while waitime > 0:
        mins, secs = divmod(waitime, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat)
        time.sleep(1)
        waitime -= 1
    print("GO!")
    print()
input("As you blast, you start noticing your rival starts gaining the "
      "high ground")
layout = input("R"
               "\n|  1  3  5"
               "\n---|--|--|"
               "\n   2  4  6 "
               "\nWhich gear do you wish to shift to"
               "\nCurrently on first gear."
               "\n>>")
if layout == "2":
    print(""+femaledriver+"-You're getting somewhere, but not for long,,")
print()
input("Oh shoot, you already in the Ichinohashi Junction. Already in a tunnel, you can already hear that flat six engine  going at it "
      "\nA couple of loops later.  We're already on lap 2.  Now we're at the colorful Rainbow bridge"
      "\nBut all of a sudden, you see smokey flames coming from your rivals car. A BLOWOUT!"
      "\nYou pull to the side. She exists out of her car shocked. She admits defeat")
print()
race = input("Since you somehow have empathy for her, and a chance to slide in them dms."
             "\nDo you"
             "\n(Drive)Take the car to the Yokohama tuning Garage"
             "\n(Call)Call a tow truck and dip"
             "\n>>")
print()
print()
# Choice after race incident
# Tow truck option result
if race == "Call a tow truck and dip" or race == "Call":
    race = input("Female driver-Thanks. I appreciate it alot."
                 "\n.Hiroshi- yo " + playa + ", do you want to follow her to the tuning shop?"
                                             "\nTo make sure she arrives safely?"
                                             "\nyes"
                                             "\nno"
                                             "\n>>")
print()
print()
if race == "yes":
    print("She is very thankful, and you and the bois drive along to Fujiwara tuning garage in Minato city"
          "\non a breezy " + TOD + "."
                                   "\nOnce you arrive,she thanks you again, but right before she leaves, she wants to give a gift.....")
else:
    print("She still is thankful "
          "\nBut right before she leaves,she wants to give you something as a thank you gift......")

# Tuning garage option result
if race == "Take the car to the Yokohama tuning Garage":
    race = input("You and the bois hook her car to your " + sasuke + " " + yokohama + ""
                 "\nYou drive on the Bayshore route, during a beautiful " + TOD + ""
                                                                                                                                                       "\nYou call up your homie Kotori, and ask him to be ready to fix a porsche."
                                                                                                                                                       "\nYou arrive at the tuning shop, and the driver says,Arigato!"
                                                                                                                                                       "\nAs a gift, she has a surprise for you....")
surprise = input("Do you Wanna see the gift from the female driver?"
                 "\nyes"
                 "\nhell yes"
                 "\n>>")
print()
# Surprise from female driver
if surprise == "yes":
    print("She gives you ¥40000 and adds you on Insta.")
elif surprise == "hell yes":
    print("She gives you ¥40000 and adds you on Insta. "
          "\nYou really think she was finna give you more?"
          "\nYou just got caught lacking.")
yen += 40000
surprise = input("Current Balance: ¥" + str(yen))
print()

mods = input("As you and the homies head back to Daifoku parking. You see flashing lights..."
             "\nDamn near 10-15 police cars surrounded the parking.A sting operation!!"
             "\nand you just remember that is 7 day..."
             "\nBut yet you still stay in line for the inspection...."
             "\n👮‍♀️-Good " + TOD + ", we are currently doing inspections for illegal car modifications."
                                     "\nWe would like to see if you currently have these illegal modifications in your vehicle."
                                     "\nIs there and illegal modifications installed in your car."
                                     "\nyes"
                                     "\nno"
                                     "\n>>")
print()
if mods == "no":
    print("Very well. You passed inspection, have a wonderful day!")
elif mods == "yes":
    mods = input("Either you return the car, or you attempt escape?(escape/return):")
    print()
    # Police chase
    print()
if mods == "escape":
    mods = input("You messed up G.  The whole squad after you now"
                 "\nShit, now you broke the toll booth just to escape"
                 "\nNow you're back on the Wangan, and hear wailing on wailing from the 警察庁, Keisatsu-chō(Police)"
                 "\nIt is " + TOD + " so you have somewhat of a chance to escape...."

                                    "\nBut you also hear. In Pursuit"
                                    "\nNow you are nearing the Kawasaki-Ukishima JCT"
                                    "\nAnd you see two exits,"
                                    "\nexit a leads to the Tamagawa tunnel which eventually leads to Haneda Airport."
                                    "\nMeanwhile exit b leads to the Tokyo Bay aqualine.."
                                    "\nOne of these exits lead to freedom,the other, your licence goes bye bye."
                                    "\nDo you choose..."
                                    "\n(a)exit a"
                                    "\n(b)exit b"
                                    "\n>")
    print()

if mods == "exit a" or mods == "a":
    input("You hear..Stay where you are. stay where you are. Pull over immediately. Exit your vehicle."
          "\nIf you only realized that there was a police station at Haneda"
          "\nYou would've pulled it off...."
          "\nBUSTED."
          "\nBecause you are arrested. This also means you you got some stuff to pay..."
          "\nListed below is what you gotta pay and the total amount"
          "\n¥3000 for toll damage"
          "\n¥100000 for evasion of police"
          "\n¥50000 for illegal modifications"
          "\n¥45000 for illegal street racing(caught on camera)"
          "\n¥10000 for being caught by the police and taking the airport route"
          "\n¥100000 for bail"
          "\n48 hrs later......"
          "\nYou go to your " + yokohama + ", at the impound lot, "
                                           "\nbut now, its stocked and stripped of its Mods..."
                                           "\nGAME OVER")
    yen -= 3000
    yen -= 100000
    yen -= 50000
    yen -= 45000
    yen -= 10000
    yen -= 100000
    mods = input("Current Balance: ¥" + str(yen))
    exit()
if mods == "exit b" or mods == "b":
    print("Going over 150 MPH, You have successfully evaded arrest. "
          "\nBut you're probably in the police database again..."
          "\nYou call some friends and  you are now on your way to Top Secret in Chiba Japan")

    print()
# Return option
if mods == "return":
    input("The Keibu-ho(警部補)(Inspector) wants you to remove the mods immediately, and should be done by tomorrow evening "
          "\nThe next day.....")
    print()
    input("While walking on a bright afternoon in Yokohama,"
          "\nYou pay a fee of ¥2000 and forced to watch your sweet,sweet mods at the police station. "
          "\nNow, your " + sasuke + " " + yokohama + "  is....STOCK!!"
                                                     "\nLooks like for a while, you aren't finna be doing midnight runs with the bois for a while....")
yen -= 2000
kiryuchan = input("Current Balance: ¥" + str(yen))
print()
# Ending
stage3 = input("Whether we ended in a good or bad way, do you want to continue to the next stage?"
               "\nyes"
               "\nno"
               "\n>>")

# Asking player if they want to start Stage 3. Tokyo Bay Aqualine
if stage3 == "no":
    print("Thank you for playing my game..Have a wonderful day " + playa + "!!")
    exit()
else:
    stage5 = input("Are your sure you want to proceed to the next stage?"
                   "\nproceed"
                   "\nno"
                   "\n>>")
if stage5 == "no":
    print("Thank you for playing my game..Have a wonderful day " + playa + "!!")
    exit()
else:
    print("Welcome " + playa + " to the last and final stage of Hashriya Undergrounds. Tokyo Bay Aqualine....")
# Start of the Tokyo Bay Aqualine stage 3.
input("Current Balance: ¥" + str(yen))
input("Course name:Tokyo Bay Aqua-line"
      "\nTotal length:14.7 mi(23.7 km)"
      "\nCompleted Construction:1997"
      "\nConsidered the 4th longest underwater tunnel in the world."
      "\nThe Tokyo Bay Aqua-Line(東京湾アクアライン, Tōkyō-wan Akua-rain) is a expressway which consists of a bridge and tunnel and a artificial island(Umihotaru),"
      "\nthat runs across Tokyo bay."
      "\nThis route connects the city of Kawasaki(Kanagawa prefecture) to the city of Kisarazu(Chiba prefecture)"
      "\nThis tunnel also helped reduce the time driving time from these two prefectures from 90 minutes to 15 minutes.")
# Actual start of course 3
input(" You hope on your 📱, and call your boi Kosuke.")
print()
input("📱 Kosuke-yo," + playa + ", im not here right now, but Smokey is there.  He can help.")
print()
input("📱You-Wait, Smokey...Smokey Nagata?! Didn't he go over 200MPH on a British Highway,and got arrested?!")
print()
input(" The Top Secret Modified Gold Supra Smokey Nagata, him?")
print()
input("📱 Kosuke-yep, that Smokey Nagata.")
print()
input("📱 you- すごい(Sugoi).On my way.")
# Introduction to Smokey Nagata
input("1 hour later........")
input("You arrive at Top secret in Chiba City"
      "\nYou see a familiar person smoking a joint outside the shop..."
      "\nthe legendary..Smokey Nagata."
      "\nyou- Smokey, its a honor to meet you."
      "\nSmokey- I heard, lets change your car quick before the cops find you."
      "\nMaybe I can use your " + yokohama + ", as a project car")
# Choosing car again.  But only top secret cars.
smokey = input("For now, you can use one of the Top secret cars:"
               "\n(Silvia)Top Secret Nissan Silvia S15"
               "\n(Supra)Top Secret Toyota Supra"
               "\n(Skyline)Top Secret Nissan Skyline R34"
               "\n>>")
if smokey == "Top Secret Toyota Supra" or smokey == "Supra":
    print("So i see you like stealing other peoples cars...."
          "\nespecially newer ones I see...")

elif smokey == "Top Secret Nissan Skyline R34" or smokey == "Skyline":
    print("Shoot, i was just working on that one.")

if smokey == "Top Secret Nissan Silvia S15" or smokey == "Silvia":
    print("A drift build car on the expressway?"
          "\nYou got style, but maybe you should use it in Gunma rather than Tokyo")

input("Smokey- Hmm....Interesting that you chose the " + smokey + "."
                                                                  "\nBut you my friend have made a interesting choice, but for now, I'll ride in my Supra.")
print()
input("By the way, I heard that there is a car meet at Umihotaru Parking area."
      "\nI even heard that a old friend of mine might be there.")
print()
input("If you want you can 📱, your friends and ask them to come and check it out. ")
print()
# Asking if you want to go to car meet on Umigotaru(Artificial island on Aqualine)
umihotaru = input("Nagata- You wanna go to the Car meet " + playa + "?"
                                                                    "\nyes"
                                                                    "\nyes"
                                                                    "\n>>")
if umihotaru == "yes":
    input("🗣Nagata- Alright, いくぞ(Ikuzo!)."
          "\nCome to think if it, maybe I can see your driving skills for once")
print()
input("you- Wait, my driving skills?")
print()
input(" Nagata- I mean, you did evade from the Police(警察)🚔 right?")
print()
input("you- Eh, you gotta a point.  That was one hell of a pursuit.")
print()
input("Nagata -Hell, I even got caught by the cops(🚔) in the Uk when i pulled 200MPH(322 kph) 😂😂 "
      "\nAnyway, lets go to this car meet.")
# Toll booth. Paying for toll to enter aqualine
meet = input("One hour later..........."
             "\nYou and Smokey arrive at Toll booths of Tokyo-bay Aqua Line:"
             "\nKawasaki-Ukishima Junction – Kisarazu-Kaneda Interchange"
             "\nDepending on your car type:"
             "\nYou are expected to pay a certain amount of 💴 in order to enter the Tokyo-Bay Aqua Line: "
             "\nFollowing prices are listed below "
             "\nNormal cars:  3,000JPY"
             "\nMidsize cars: 3,600JPY"
             "\nLarge cars:   4,950JPY"
             "\nSpecific large cars:  8,250JPY"
             "\nKei-cars and motorcycles: 2,400JPY"
             "\nNote:Kei cars are just mini cars"
             "\nWhat type of car do you have?"
             "\n(N)Normal car"
             "\n(M)Midsize car"
             "\n(L)Large car"
             "\n(SLC)Specific large car"
             "\n(KC)Kei-car"
             "\n>>")
if meet == "Normal car" or meet == "N":
    yen -= 3000
if meet == "Midsize car" or meet == "M":
    yen -= 3600
if meet == "Large car" or meet == "L":
    yen -= 4950
elif meet == "Specific large car" or meet == "SLC":
    yen -= 8250
elif meet == "Kei-car" or meet == "KC":
    yen -= 2400
# Balance after paying toll
meet = input("Current Balance: ¥" + str(yen))
print()
input("You payed the toll, but once you arrive, for some reason Smokey stopped in the middle of the road...")
print()
input("📱 you- Yo Smokey, why are did you stop in the middle of the road? 🤨 ")
print()
input("📱 Smokey- I am about to do, what is called a pro gamer move.😉")
print()
input("📱 you- What about that race? Yk, that cat and mouse race?")
print()
input("📱 Smokey- oh we doing a Cat and Mouse race alright, but here's the thing...."
      "\nIm the mouse🐭, you're the cat🐱"
      "\nGood luck chasing me!!!"
      "\nHere we go!!!!!!")

waitime = 10

while waitime > 0:
    mins, secs = divmod(waitime, 60)
    timeformat = '{:02d}:{:02d}'.format(mins, secs)
    print(timeformat)
    time.sleep(1)
    waitime -= 1
input("listed below is your Manual Transmission pattern of your " + smokey + ". ")
print()
# Shifting intro.  6 gear stick shift layout.
print("R"
      "\n|  1  3  5"
      "\n---|--|--|"
      "\n   2  4  6")
print("BTW, You're on 1st gear atm.^")
print()
bayline = input("All of a sudden you see 💨, and now realize that Smokey is about to smoke yo ass in this race.]"
                "\nNow you start driving, but now you have to shift gears."
                "\nWhich gear are you going to shift to?"
                "\n>>")
# Another 6 gear stick shift layout
print("R"
      "\n|  1  3  5"
      "\n---|--|--|"
      "\n   2  4  6")
if bayline == "2":
    input("Aah, now we're getting somewhere, The smooth transition."
          "\nHowever, you're still far behind from Smokey.")
else:
    print("Ehhh, its fine if you skip gears,  but you got  wait a few seconds for your rev to drop. ")
    import time

    waitime = 8

    while waitime > 0:
        mins, secs = divmod(waitime, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat)
        time.sleep(1)
        waitime -= 1
input("📱 Smokey- Not bad kid, but you got a long way to go.")
print()
input("📱 you- This is where the fun begins. ")

aqua = input("Alright, don't lose hope yet, you still got a way to go. "
             "\nREMEMBER: THIS COURSE IS JUST ⬆️"
             "\nNow its time to shift gears again...."
             "\nBTW, You are currently on " + bayline + " gear.")
print()
input("Which gear are you going to shift to....."
      "\n>>")
print("R"
      "\n|  1  3  5"
      "\n---|--|--|"
      "\n   2  4  6")
if aqua == "3":
    print("What a smooth and ez transition.  But don't get too cocky now.")
if aqua == "4":
    print("Now you're getting the hang of things. Plus you flowing a little better ")
elif aqua == "5":
    print("LETS GOOOOOOOOOOOOO.  You're actually catching up")
else:
    print("You car is now at max gear, and you can already hear that top secret special going at it")

input("Smokey- damn kid, you're actually coming up,")
print()
input("Smokey- But not for long...")
print()
input("Already on " + aqua + " gear, you must hit the clutch in order to go to the next gear of your choice."
                             "\nBut while shifting, you are kinda excited you might beat Smokey.")
print()
# Clutch(Determines what happens in race if you hit release foot off clutch too quickly or slowly
junction = input("But what you're about to do, will determine whether you win..."
                 "\nHaving your foot on the clutch, do you release your foot off the clutch...."
                 "\n(Q)quickly"
                 "\n(S)slowly"
                 "\n>>")
if junction == "quickly" or junction == "Q":
    print("Oh shit you just stalled the car."
          "\nSmokey- I thought you said escaped from the cops."
          "\nYOU LOSE."
          "\nGAME OVER")
    exit()
if junction == "slowly" or junction == "S":
    print("Great, now you're right behind  Smokey Nagata"
          "\nSmokey- nANI??? How did you manage to get right behind me?!?!?"
          "\nyou-  Just like the simulations....")
input("You somehow manage to align your " + smokey + " right behind Smokey's car,"
                                                     "\nYou have a high chance of actually winning this cat n mouse race.")
# Final push of cat and mouse race(Smokey Nagata)
print()
input("But it all comes down to one more option.....")
print()
print("R"
      "\n|  1  3  5"
      "\n---|--|--|"
      "\n   2  4  6")
print("PS: you're on " + aqua + " gear.")
print()
finale = input("Since you're about to shift gears.."
               "\nBut you hit the clutch..."
               "\nHowever, do release the foot off the  clutch...."
               "\n(Q)quickly or (S)slowly?")
if finale == "quickly" or finale == "Q":
    print("Smokey- Could've sworn you said escaped from the cops.."
          "\nSurvey says that was a lie!"
          "\nYOU LOSE"
          "\nGAME OVER")
    exit()
elif finale == "slowly" or finale == "S":
    print("You end up passing smoking..."
          "\nIncreasing the gap between you and Smokey."
          "\nYou eventually gain more and more distance, and boom you win!"
          "\nYou've Won 🏆 🏆 ")
print()
input("Smokey- Looks like Kosuke was right.."
      "\nYou really did escape the cops....")
input("You- So you thought I was lyin or somethin?!?!"
      "\nBut hey that was a pretty good race.")
print()
input("Smokey- Haven't done this on the aqualine since 97..Good times")
print()
input("You arrive at the Car meet on the aqualine on a calm " + TOD + ". Cars of all kinds."
                                                                      "\nSome stocked Skylines.  Some modified Silvia's and Supra. RX 7's tuned to the max"
                                                                      "\nHell even some bozozku cars. ")
print()
input("Smokey- Oh, hey Koseki. Long time no see"
      "\nKoseki- If ain't Smokey Nagata......")
print()
koseki = input("You turn around and see a red Mazda RX 7 FD35."
               "\nA RX 7 with some unique car spats and a wild spoiler."
               "\nKoseki san takes notice of your " + smokey + ", and wants to duel with you on the Aqualine."
                                                               "\nDo you accept or deny?"
                                                               "\naccept"
                                                               "\ndeny"
                                                               "\n>>")
if koseki == "deny":
    print("Koseki-  It would've been fun if we could've duel..."
          "\nBut I understand.  Have a good night."
          "\nYou drive into the breezy " + TOD + ", going to whatever the roads take ya...."
                                                 "\nCONGRATULATIONS " + playa + "!! You have successfully Completed Hashiriya Undergrounds(Phase 1)!!")
    exit()

if koseki == "accept":
    print("Alright, good thing your boi Kosuke is here."
          "\nNote: This is a cat and mouse race(you're the mouse. Koseki is the cat")
nobita = input("\nBTW, do you want to change your car"
               "\nyes"
               "\nno"
               "\n>>")
if nobita == "no":
    print("Thats cool..."
          "\nKosuke- I will start the Countdown!!!!")
else:
    nobita = input("Hmm, which are do you want. Be quick about it"
                   "\nNissan Fairlady S130Z(Devil Z)"
                   "\nSkyline R32 GTR"
                   "\nFerrari Testarossa"
                   "\n>>")
    print()
if nobita == "Nissan Fairlady S130Z(Devil Z)":
    print("🗣 Koseki-  Be careful with that car...."
          "\nLegend has it that some died in it and now this car is (possessed)."
          "\nBe gentle with it")

elif nobita == "Skyline R32 GTR":
    print("Koseki-  Heard this car belonged to this fashion model and this tv show host."
          "\nSome show called(Drive go go)! Or somethin like that"
          "\nThe drivers name i think is Reina or something along those lines."
          "\nBut this AWD car is has some pretty good handing and acceleration and has a 300hp."
          "\nIn a nutshell. You'll be driving a pretty good car on the aqualine")

if nobita == "Ferrari Testarossa":
    print("Koseki-  Ah, those fancy italian cars eh"
          "\nThe previous owner is some photographer by the name of Ishida"
          "\nAs any Ferrari, its pretty fast with 385hp, making this thing a monster on the expressway."
          "\nWell, as long as the driver can handle it😉.")
print()
input("The race between you and Koseki will now commence..")
print()
input("Similar to before, this is just cat and mouse race between the Aqualine to the Bayshore route.")
print()
input("Kosuke- I will start the Countdown!!!!")

waitime = 10

while waitime > 0:
    mins, secs = divmod(waitime, 60)
    timeformat = '{:02d}:{:02d}'.format(mins, secs)
    print(timeformat)
    time.sleep(1)
    waitime -= 1
print()
print("GO!")
print("And you're off!!!")

input("Alright you're still in the front,"
      "\nBut you can see the RX 7 catching up."
      "\nDodging cars one by one and you are already nearing the exit of the aqualine.")
print()
naruhito = input("Unfourantly,you see another 🚔."
                 "\nYou see two exits, one goes up⬆️ , the other goes left⬅️."
                 "\nOne leads to freedom, the other puts you into the slammer."
                 "\nWanna go (⬆️)up or (⬅️)left:  ")
if naruhito == "left" or naruhito == "⬅️":
    print("Oh shoot, you somehow gained a blowout."
          "\nDamn....⚠️🚨🚧ACCIDENT ON THE AQUALINE🚨🚧⚠️"
          "\n⚠️🚨🚧ACCIDENT ON THE AQUALINE⚠️️🚨🚧"
          "\nOh and btw, you probably got arrested^"
          "\nGAME OVER.")
    exit()
else:
    print("👮🏻🗣🚔- TOKYO METROPOLITAN POLICE. STOP YOUR VEHICLE!")
print()
input("Koseki- Shoot " + playa + ".  Could've at least told me you're a wanted man")
print()
input("you- Hey man, what do you expect.  They got cameras setup in these tunnels nowadays.")
print()
input("You now end up breaking the toll booth station and end up fleeing te police"
      "\n you- Imma lay low for a bit."
      "\nKoseki- you better."
      "\nYou go drive during a breezy and  " + TOD + ", and go whatever the roads take you....")
input("Congratulations " + playa + "!! You have successfully completed phase 1 of Hashiriya Undergrounds!! ")
exit()
