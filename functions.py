import subprocess
import os
import tkinter
is_printed = False


def reprint():
    if is_printed:
        #home_dir = os.path.expanduser("~")
        relative_path = ["E:\\", "Python", "ReprinterV2", "labela.txt"]
        file_path = os.path.join(*relative_path)
        subprocess.run(["print", file_path, "/D:LPT2"])
    else:
        tkinter.messagebox.showinfo("Greska", "Mora biti odradjen print pre reprinta!")

def check_date_input(date_input_content): #Input moze da bude samo broj ili values_ignored! Ne sme da postoji razmak
    date_split = date_input_content.split(",")
    vales_ignored = ["/", ":", ","]
    if len(date_split) == 2:
        for number, character in enumerate(date_input_content):
            if check_if_integer(character):
                continue
            elif date_input_content[number] in vales_ignored:
                continue
            else:
                return 0
    else:
        return 0
    return 1

def check_if_integer(data):  #Proverava da li je input integer.
    try:
        int(data)
        return 1
    except ValueError:
        return 0

def execute_printing(operater, date_and_time, oid_lenght, qr_input):

    global is_printed
    qr_content_splited = qr_input.split("@")
    date_content = date_and_time.split(",")
    operater_id = operater

    (engineering_level, fyon,  apdm, date, time) = (qr_content_splited[2], qr_content_splited[4], qr_content_splited[13], date_content[0], date_content[1])
    (work_order, option_code) = (qr_content_splited[1], qr_content_splited[14])

    qr_content = f"ET@{work_order}@{fyon}@{engineering_level}@20240611105854@{option_code}@!{work_order}*="

    if oid_lenght == 17:  #Updejtuje apdm ukoliko se radi o WH familiji
        apdm = qr_content_splited[14]

    lmod_dict = {"C":(9401962, "15"), "D":(9401962, "15"), "E":(9401961, "15"), "A":(9401963, "00"), "3":(9401927, "30"),
                 "0":(9401927, "30"), "1":(9401927, "30"), "2":(9401927, "30"), "6":(9401963, "00"), "7":(9401962, "15"), "8":(9401961, "15")}

    #prva vrednost u dict value sluzi za odredjivanje lmod-a a druga sluzi za pozicioniranje aztek koda na labela(neke familije imaju manji neke veci aztek kod)

    lmod_input = engineering_level[0].upper()

    if lmod_input in lmod_dict:
        lmod = lmod_dict[lmod_input][0]
    else:
        lmod = "Nije pronadjen"

    label = """^XA^MTT^MPS^MD0^JS60
^FO10,5^GB530,25,25^FS
^B0,3,0,Q,^FO35,40^FD{qr}^FS
^FO2{qrsize},70,^BCN,100,N,N,N^FD{fyon}^FS
^A0N,20,17
^FO3{qrsize},180^FD{fyon}^FS
^A0N,30,25
^FO90,230^FDLear GODOLLO^FS
^A0N,30,25
^FO290,230^FDSup.code: AEBLU^FS
^A0N,30,25
^FO90,275^FDOperator :{operaterid}^FS
^A0N,30,25
^FO90,315^FDDate:{date}^FS
^A0N,30,25
^FO315,315^FDTime: {time}^FS
^A0N,30,25
^FO170,350^FDMade in SERBIA^FS
^A0N,30,25
^FO100,390^FDLMOD: {lmod}^FS
^A0N,30,25
^FO100,430^FDAPDM: {apdm}^FS
^FO90,500,^BCN,100,N,N,N^FD{lmod}^FS
^A0N,20,17
^FO190,610^FD{lmod}^FS
^FO90,650,^BCN,100,N,N,N^FD{fyon}^FS
^A0N,20,17
^FO190,760^FD{fyon}^FS
^XZ""".format(fyon = fyon, apdm = apdm,operaterid = operater_id, date = date, time = time, lmod = lmod, qrsize = lmod_dict[lmod_input][1], qr = qr_content)


    #home_directory = os.path.expanduser("~") #Dobijemo nesto poput "C:\Users\ggrozdanic"
    relative_path = ["E:\\", "Python", "ReprinterV2", "labela.txt"]  # Ovako dobijamo cross-platform path
    file_path = os.path.join(*relative_path)

    def missing_directory(rel_path):  # Proverava i vraca ako fali odredjeni direktorijum
        current_path = ""
        for directory in rel_path[:-1]:  # Stavljeno "-1" da bi se proveravali samo direktorijumi ne i txt file.
            current_path = os.path.join(current_path, directory)
            if not os.path.exists(current_path):
                missing_dir = directory
                return missing_dir

    try:
        file = open(file_path, 'w')
        file.write(label)
        file.close()
    except FileNotFoundError:
        print(f"File not found, missing directory: {missing_directory(relative_path)}")
    except Exception as e:
        print(f"An error occurred: {e}")

    subprocess.run(["print", file_path, "/D:LPT2"]) #COM1- prallel port, LPT1 - serial port
    is_printed = True

