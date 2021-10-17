import json
import getpass as g
open("text.json","w").close()
namelist = []
def get(name):
      try:
            with open("text.json","r") as r:
                  namelist = list(json.load(r))
            if name in namelist:
                  print("Hello!"+name)
            else:
                  ask = input("No such name,add it?(y/n)")
                  if ask == "y":
                        pw = g.getpass("Input password:")
                        if pw == "zyy441303087312":
                              namelist.append(name)
                              with open("text.json","w") as r:
                                    json.dump(namelist,r,indent=4)
                              print("Added")
                        else:
                              print("Invalid password!")
      except:
            ask = input("No such name,add it?(y/n)")
            if ask == "y":
                  pw = g.getpass("Input password:")
                  if pw == "zyy441303087312":
                        namelist = [name]
                        with open("text.json","w") as r:
                              json.dump(namelist,r,indent=4)
                        print("Added") 
                  else:
                        print("Invalid password!")
            
            
def delx(name):
      del_pw = g.getpass("Input administrator password!")
      if del_pw == "orangecatpkat324122":
            if name == "All":
                  r = open("text.json","w")
                  r.close()
                  print("Finished!")
            else:
                  try:
                        with open("text.json","r") as r:
                              namelist = list(json.load(r))
                        if name in namelist:
                              try:
                                    namelist.remove(name)
                                    with open("text.json","w") as r:
                                          json.dump(namelist,r,indent=4)
                                    print("Deleted!")
                              except:
                                    print("Fail!")
                        else:
                              print("No such name!")
                  except:
                        print("Fail!No data or other error appeared!")
      else:
            print("Invalid password!")
def check():
      try:
            with open("text.json","r") as r:
                  namelist = list(json.load(r))
            for out in namelist:
                  print(out)
      except:
            print("Fail!No data or other error appeared!")   
if __name__ == "__main__":            
      while True:
            name = input("What is your name(input 'check' to check present options):")
            name = name.title()
            if name == "":
                  print("No input!")
            elif name.endswith(" ") or name.startswith(" "):
                  print("Input correct name!")
            elif name == "Delete":
                  name = input("Which to delete(Input 'all' to delete all names ):")
                  name = name.title()
                  delx(name)
            elif name == "Check":
                  check()       
            else:
                  get(name)