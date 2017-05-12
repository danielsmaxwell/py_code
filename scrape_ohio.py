from selenium import webdriver  # not standard, get with pip
from selenium.webdriver.support.ui import Select
import time
import urllib
from os import listdir
from os.path import isfile, join
from os import rename
import zipfile # possibly not standard (don't remember)
import zlib # possibly not standard (don't remember)
import csv
import xlrd # not standard, get with pip

# i guess it'll just throw an error if you don't have one of the packages
# so you'll know if you don't have it





# not used for actual date purposes, just for file labeling.
date = "20161006"


# i have a folder, "ohioabs", within which I have subfolders for
# each day's scrapes. these are named based on the date variable.
# this doesn't create those subfolders, you will have to before running.
parentfolder = "/Users/brianamos/Documents/ohioabs/"
placetoputfiles = parentfolder + date + "/"

# your browser's default download folder.
# this is a little hacky, but I dig files out of the downloads
# folder assuming there aren't any others that match the same leading character
# string that I'm looking for. if you've got files in there that lead with
# "absentee" or something like that, it may be a problem.
# search this code for "listdir(", the if statements underneath
# will tell you what I'm searching on.
downloadpath = "/Users/brianamos/Downloads/"

# where dropbox is on your local machine
dropboxfolder = "/Users/brianamos/Dropbox/Election Data Center/ohioabs/"



# voterfind counties without date selection

countylist = ["adams","allen","ashtabula","athens","auglaize",
              "belmont","brown","champaign","clark","clinton",
              "columbiana","coshocton","darke","defiance",
              "delaware","erie","fayette","fulton","gallia",
              "greene","hardin","harrison",
              "highland","hocking","jackson","jefferson",
              "knox","lake","lawrence","licking","logan","lorain",
              "madison","mahoning","marion","meigs","miami",
              "monroe","muskingum","noble",
              "paulding","perry","pickaway","pike","portage",
              "preble","putnam","ross","scioto","seneca",
              "tuscarawas","union","vanwert","vinton","warren",
              "washington","williams"]

# voterfind counties with date selection

specialcounties = ["geauga","guernsey","montgomery","morgan"]



# open browser
# this points to where you put the ChromeDriver on your HD
driver = webdriver.Chrome('/Users/brianamos/Documents/chromedriver')



for onecounty in countylist:

    

    driver.get("http://www.voterfind.com/" + onecounty + "oh/avreport.aspx")

    time.sleep(5)

    radio = driver.find_element_by_id("rdo_file").click()
    submit = driver.find_element_by_id("btnStart").click()

    time.sleep(10)

    url = driver.find_element_by_name("hid_filename")
    fullurl = url.get_attribute("value")

    urlelements = fullurl.split("\\")[-3:]

    builturl = "http://www.voterfind.com/" + urlelements[0] + "/" + urlelements[1] + "/" + urlelements[2]

    writetofilename = placetoputfiles + onecounty + date + ".csv"

    urllib.urlretrieve(builturl, filename=writetofilename)




for onecounty in specialcounties:

    

    driver.get("http://www.voterfind.com/" + onecounty + "oh/avreport.aspx")

    time.sleep(5)

    radio = driver.find_element_by_id("rdo_file").click()
    radio2 = driver.find_element_by_id("rdo_dtno").click()
    submit = driver.find_element_by_id("btnStart").click()

    time.sleep(10)

    url = driver.find_element_by_name("hid_filename")
    fullurl = url.get_attribute("value")

    urlelements = fullurl.split("\\")[-3:]

    builturl = "http://www.voterfind.com/" + urlelements[0] + "/" + urlelements[1] + "/" + urlelements[2]

    writetofilename = placetoputfiles + onecounty + date + ".csv"

    urllib.urlre trieve(builturl, filename=writetofilename)




# butler county
driver.get("http://www.butlercountyelections.org/current_election_report/election_resources/absentee_labels.php")

time.sleep(5)

driver.switch_to_frame(driver.find_element_by_tag_name("iframe"))

select = Select(driver.find_element_by_name("election"))
select.select_by_value("90")

select = Select(driver.find_element_by_name("district"))
select.select_by_value("57")

startdate = driver.find_element_by_name("start_date")
startdate.send_keys("01012016")

enddate = driver.find_element_by_name("end_date")
enddate.send_keys("11092016")

radio = driver.find_element_by_id("Excel").click()

button = driver.find_element_by_name("submit").click()

time.sleep(90)

butlerfilename = ""

for f in listdir("/Users/brianamos/Downloads"):
    if f[0:18] == "absenteeLabelExcel":
        butlerfilename = f

if butlerfilename == "":

    print "no matching file for butler"

else:

    rename(downloadpath + butlerfilename, placetoputfiles + "butler" + date + ".xls")




# cuyahoga county

driver.get("http://boe.cuyahogacounty.us/en-US/absentee-voter-labels.aspx")

time.sleep(5)

startdate = driver.find_element_by_id("ContentPlaceHolder1_ContentPlaceHolderMain_txtDateIssuedFrom")
startdate.clear()
startdate.send_keys("1/1/2016")

enddate = driver.find_element_by_id("ContentPlaceHolder1_ContentPlaceHolderMain_txtDateIssuedTo")
enddate.clear()
enddate.send_keys("11/9/2016")

district = Select(driver.find_element_by_id("ContentPlaceHolder1_ContentPlaceHolderMain_ddlDistrictTypes"))
district.select_by_value("ALL")

time.sleep(5)

subdistrict = Select(driver.find_element_by_id("ContentPlaceHolder1_ContentPlaceHolderMain_ddlDistrict"))
subdistrict.select_by_value("2")



button = driver.find_element_by_id("ContentPlaceHolder1_ContentPlaceHolderMain_btnExport").click()

time.sleep(90)

cuyahogafilename = ""

for f in listdir("/Users/brianamos/Downloads"):
    if f[0:15] == "AbsenteeLabels-":

        cuyahogafilename = f

if cuyahogafilename == "":

    print "no matching file for cuyahoga"

else:

    rename(downloadpath + cuyahogafilename, placetoputfiles + "cuyahoga" + date + ".csv")




# franklin county

driver.get("http://vote.franklincountyohio.gov/absentee/labels.cfm")

time.sleep(5)

election = Select(driver.find_element_by_id("election"))
election.select_by_value("392")

district = Select(driver.find_element_by_id("category"))
district.select_by_value("c25")

time.sleep(5)

subdistrict = Select(driver.find_element_by_name("d25"))
subdistrict.select_by_value("1079")

button = driver.find_element_by_name("export").click()

time.sleep(120)

franklinfilename = ""

for f in listdir("/Users/brianamos/Downloads"):
    if f[0:8] == "absentee":

        franklinfilename = f

if franklinfilename == "":

    print "no matching file for franklin"

else:

    rename(downloadpath + franklinfilename, placetoputfiles + "franklin" + date + ".csv")




# hamilton county

driver.get("http://boe.hamilton-co.org/data/absentee-voters-list.aspx")

time.sleep(5)

startdate = driver.find_element_by_id("ContentMain_ContentMain_phMainContent_txtRequest1")
startdate.send_keys("1/1/2016")

enddate = driver.find_element_by_id("ContentMain_ContentMain_phMainContent_txtRequest2")
enddate.send_keys("11/9/2016")

button = driver.find_element_by_id("ContentMain_ContentMain_phMainContent_btncsv").click()

time.sleep(90)

hamiltonfilename = ""

for f in listdir("/Users/brianamos/Downloads"):
    if f[0:13] == "absentee-list":

        hamiltonfilename = f

if hamiltonfilename == "":

    print "no matching file for hamilton"

else:

    rename(downloadpath + hamiltonfilename, placetoputfiles + "hamilton" + date + ".csv")




# henry county

driver.get("http://www.henrycoelections.com/Absentee%20Reports.html")

print "make sure nothing's changed on this page!: http://www.henrycoelections.com/Absentee%20Reports.html"

time.sleep(15)

writetofilename = placetoputfiles + "henry" + date + ".txt"

urllib.urlretrieve("http://www.henrycoelections.com/Documents/Absentee/AV%20Multi-Purpose%20Flat%20File.txt", filename=writetofilename)



# huron county

driver.get("https://huroncountyboe.wordpress.com/daily-absentee-listing/")

time.sleep(5)

content = driver.find_element_by_xpath("//div[@class='entry-content']")

linktofile = content.find_element_by_xpath(".//a")
huronfilename = linktofile.get_attribute("href")

writetofilename = placetoputfiles + "huron" + date + ".xls"

urllib.urlretrieve(huronfilename, filename=writetofilename)



# summit county

driver.get("http://www.summitcountyboe.com/WebApps/avreport.aspx")

time.sleep(5)

election = Select(driver.find_element_by_name("ctl00$Content$cmbelectionlist"))
election.select_by_value("20161108G")

time.sleep(10)

driver.find_element_by_xpath("//input[@value='rdo_file']").click()

time.sleep(2)

button = driver.find_element_by_name("ctl00$Content$btnStart").click()

time.sleep(30)

content = driver.find_element_by_xpath("//div[@id='content-main']")

linktofile = content.find_element_by_xpath(".//a")
summitfilename = linktofile.get_attribute("href")

writetofilename = placetoputfiles + "summit" + date + ".csv"

urllib.urlretrieve(summitfilename, filename=writetofilename)




# trumbull county

driver.get("http://www.boe.co.trumbull.oh.us/boe_absentdownload.html")

time.sleep(5)

content = driver.find_element_by_xpath("//div[@class='content']")

linktofile = content.find_element_by_xpath(".//a")
trumbullfilename = linktofile.get_attribute("href")

writetofilename = placetoputfiles + "trumbull" + date + ".xls"

urllib.urlretrieve(trumbullfilename, filename=writetofilename)



# send zip of raw files to dropbox

clipdir = placetoputfiles[0:-1]

onlyfiles = [f for f in listdir(clipdir) if isfile(join(clipdir, f))]

zipfilename = dropboxfolder + "separate_files_" + date + ".zip"

myzip = zipfile.ZipFile(zipfilename, "w")

for onefile in onlyfiles:
    
    myzip.write(placetoputfiles + onefile, arcname=onefile, compress_type=zipfile.ZIP_DEFLATED)

myzip.close()






# merge files


outp = open(placetoputfiles + "fulllist_" + date + ".csv", "w")

outp.write("county,name,party,countyid,zipcode,datemailed,datereturned\n")


# start with voterfind

voterfindlist = []

schema1 = ['LASTN', 'FIRSTN', 'MIDDLEN', 'PREFIXN', 'SUFFIXN', 'PARTYAFFIL', 'PHONE', 'CNTYIDNUM', 'AVADDR1', 'AVADDR2', 'CITY', 'STATE', 'ZIPCODE', 'COUNTRY', 'AVSENTDATE', 'AVSENTMETH', 'AVRECVDATE', 'AVRECVMETH', 'AVAPPTYPE', 'AVAPPCODE', 'PRSID', 'PRECNAME', 'AVAPPDATE']
schema2 = ['LASTN', 'FIRSTN', 'MIDDLEN', 'PREFIXN', 'SUFFIXN', 'PARTYAFFIL', 'CNTYIDNUM', 'AVADDR1', 'AVADDR2', 'CITY', 'STATE', 'ZIPCODE', 'COUNTRY', 'AVSENTDATE', 'AVSENTMETH', 'AVRECVDATE', 'AVRECVMETH', 'AVAPPTYPE', 'AVAPPCODE', 'PRSID', 'PRECNAME', 'AVAPPDATE']
schema3 = ['LASTN', 'FIRSTN', 'MIDDLEN', 'PREFIXN', 'SUFFIXN', 'PARTYAFFIL', 'CNTYIDNUM', 'AVADDR1', 'AVADDR2', 'CITY', 'STATE', 'ZIPCODE', 'COUNTRY', 'AVSENTDATE', 'AVSENTMETH', 'AVRECVDATE', 'AVRECVMETH', 'AVAPPTYPE', 'AVAPPCODE', 'PRSID', 'PRECNAME', 'AVAPPDATE', 'SOSID']

for i in countylist:

    voterfindlist.append(i)

for i in specialcounties:

    voterfindlist.append(i)


for county in voterfindlist:

    filename = placetoputfiles + county + date + ".csv"
    getdata = open(filename, "rb")
    datareader = csv.reader(getdata)

    counter = 0

    for line in datareader:

        if counter == 0:

            if line == schema1:

                lname = 0
                fname = 1
                mname = 2
                party = 5
                countyid = 7
                zipcode = 12
                sent = 14
                received = 16
                

            elif line == schema2:

                lname = 0
                fname = 1
                mname = 2
                party = 5
                countyid = 6
                zipcode = 11
                sent = 13
                received = 15


            elif line == schema3:

                lname = 0
                fname = 1
                mname = 2
                party = 5
                countyid = 6
                zipcode = 11
                sent = 13
                received = 15

            else:

                print county, "no matching schema!"

                break

            counter += 1
            continue

        sentpieces = line[sent].split("/")
        if len(sentpieces) != 3: sentstring = ""
        else:
            sentstring = "2016-" + sentpieces[0] + "-" + sentpieces[1]

        recpieces = line[received].split("/")
        if len(recpieces) != 3: recstring = ""
        else:
            recstring = "2016-" + recpieces[0] + "-" + recpieces[1]

        if line[party] == "DEM":
            partystring = "D"
        elif line[party] == "REP":
            partystring = "R"
        else:
            partystring = "O"


        outp.write("{0},{1},{2},{3},{4},{5},{6}\n".format(county,
                                                                line[fname] + " " + line[mname] + " " + line[lname],
                                                                partystring,
                                                                line[countyid],
                                                                line[zipcode][0:5],
                                                                sentstring,
                                                                recstring))
    del getdata
    del datareader


# butler

butlerschema = [u'ElectionId', u'VoterId', u'Name1', u'Name2', u'Precinct', u'Portion', u'Party', u'DateEntered', u'Address', u'City', u'State', u'Zip', u'Country']

butlerfile = placetoputfiles + "butler" + date + ".xls"

butler = xlrd.open_workbook(butlerfile)
butlersheet = butler.sheet_by_index(0)

counter = 0

for rownum in xrange(butlersheet.nrows):

    if counter == 0:

        if butlersheet.row_values(rownum) != butlerschema:

            print "butler no matching schema!"
            break


        counter += 1
        continue

    line = butlersheet.row_values(rownum)

    partystring = line[6]
    if partystring == "N": partystring = "O"

    outp.write("{0},{1},{2},{3},{4},{5},{6}\n".format("butler",
                                                      line[3],
                                                      partystring,
                                                      line[1],
                                                      line[11][0:5],
                                                      "",
                                                      ""))
                                                     


# cuyahoga

cuyahogafile = placetoputfiles + "cuyahoga" + date + ".csv"

cuyahogaschema = ['VOTERID', 'CONFIDENTIAL', 'NAMEFIRST', 'NAMEMIDDLE', 'NAMELAST', 'NAMESUFFIX', 'DISTRICT', 'PRECINCT', 'PARTY', 'HOUSENUMBER', 'PREDIR', 'STREET', 'TYPE', 'APARTMENTNUMBER', 'CITY', 'STATE', 'ZIP', 'CAREOF', 'MAILSTREET', 'CATEGORY', 'DATERETURNED', 'DATEISSUED', 'CHALLENGED*', 'MAILCITY', 'MAILSTATE', 'MAILZIP', 'MAILCOUNTRY']

getdata = open(cuyahogafile, "rb")
datareader = csv.reader(getdata)

counter = 0

for line in datareader:

    if counter == 0:

        counter += 1

        if line != cuyahogaschema:

            print "cuyahoga no matching schema!"

            break

        continue

    if line[8] == "DEM":
        partystring = "D"
    elif line[8] == "REP":
        partystring = "R"
    else:
        partystring = "O"

    issuedstring = ""


    returned = line[20]
    returneddatepieces = returned.split(" ")
    if len(returneddatepieces) != 3: returnedstring = ""
    else:
        returneddatepieces2 = returneddatepieces[0].split("/")
        if len(returneddatepieces2) != 3: returnedstring = ""
        else:
            returnedstring = "2016-" + returneddatepieces2[0] + "-" + returneddatepieces2[1]
    

    outp.write("{0},{1},{2},{3},{4},{5},{6}\n".format("cuyahoga",
                                                      line[2] + " " + line[3] + " " + line[4],
                                                      partystring,
                                                      line[0],
                                                      line[16][0:5],
                                                      issuedstring,
                                                      returnedstring))
    


# franklin

franklinfile = placetoputfiles + "franklin" + date + ".csv"
franklinschema = ['Precinct Name', 'Precinct Code', 'Precinct Code with Split', 'City or Village', 'School District', 'Township', 'House District', 'Senate District', 'Congress District', 'Police District', 'Road District', 'Fire District', 'Park District', 'Court Appeals Name', 'Board of Ed Name', 'Party', 'Date Mailed', 'Phone Number', 'Date Registered', 'Local ID', 'Year of Birth', 'First Name', 'Middle Name', 'Last Name', 'Suffix Name', 'Address Line 1', 'Address Line 2', 'Address Line 3', 'Address Line 4', 'City', 'State', 'Zip', 'Zip Plus 4', 'Mailed', 'Date Requested', 'Date Returned']

getdata = open(franklinfile, "rb")
datareader = csv.reader(getdata)

counter = 0

for line in datareader:

    if counter == 0:

        counter += 1

        if line != franklinschema:

            print "franklin no matching schema!"

            break

        continue


    if line[15] == "D":
        partystring = "D"
    elif line[15] == "R":
        partystring = "R"
    else:
        partystring = "O"

    issued = line[16]
    issueddatepieces = issued.split("/")
    if len(issueddatepieces) != 3: issuedstring = ""
    else:
        issuedstring = "2016-" + issueddatepieces[0] + "-" + issueddatepieces[1]


    returned = line[35]
    returneddatepieces = returned.split("/")
    if len(returneddatepieces) != 3: returnedstring = ""
    else:
        returnedstring = "2016-" + returneddatepieces[0] + "-" + returneddatepieces[1]
    

    outp.write("{0},{1},{2},{3},{4},{5},{6}\n".format("franklin",
                                                      line[21] + " " + line[22] + " " + line[23],
                                                      partystring,
                                                      line[19],
                                                      line[31][0:5],
                                                      issuedstring,
                                                      returnedstring))
        


# hamilton

hamiltonfile = placetoputfiles + "hamilton" + date + ".csv"
hamiltonschema = ['Request Application Date', 'Return Ballot Date', 'electionid', 'VoterId', 'PrecinctName', 'PrecinctId', 'PrecinctSplit', 'FirstName', 'MiddleName', 'LastName', 'MiddleName', 'SuffixName', 'Address1', 'Address2', 'Address3', 'Address4', 'Address5', 'Address6', 'CityState', 'Zip', 'Congress', 'Senate', 'House', 'Judicial', 'School', 'CountySchool', 'VocationalSchool', 'AbsenteeParty', 'VoterParty', 'Phone', 'BirthYear', 'OVID']

getdata = open(hamiltonfile, "rb")
datareader = csv.reader(getdata)

counter = 0

for line in datareader:

    if counter == 0:

        counter += 1

        if line != hamiltonschema:

            print "hamilton no matching schema!"

            break

        continue


    if line[28] == "DEM":
        partystring = "D"
    elif line[28] == "REP":
        partystring = "R"
    else:
        partystring = "O"

    issuedstring = ""

    returned = line[1]
    returneddatepieces = returned.split("/")
    if len(returneddatepieces) != 3: returnedstring = ""
    else:
        returnedstring = "2016-" + returneddatepieces[0] + "-" + returneddatepieces[1]
    

    outp.write("{0},{1},{2},{3},{4},{5},{6}\n".format("hamilton",
                                                      line[7] + " " + line[9],
                                                      partystring,
                                                      line[3],
                                                      line[19][0:5],
                                                      issuedstring,
                                                      returnedstring))




# henry

henryfile = placetoputfiles + "henry" + date + ".txt"
henryschema = ['voter_id', 'State_ID', 'name_prefix', 'name_last', 'name_first', 'name_middle', 'name_suffix', 'House_Number', 'House_Fraction', 'Pre_Direction', 'Street', 'Street_Type', 'Post_Direction', 'Building_Number', 'Apartment_Number', 'City', 'Zip', 'Precinct', 'Portion', 'Party', 'Reg_Date', 'Image_ID', 'phone_1', 'phone_2', 'Military', 'Gender', 'Perm_AV', 'Birth_Place', 'Birth_Date', 'Mailing_Address', 'Mail_Street', 'Mail_City', 'Mail_State', 'Mail_Zip', 'Mail_Country', 'Language', 'Drivers_License', 'Consolidation', 'ballot_Type', 'AV_election_id', 'Category', 'Source', 'date_entered', 'Date_Returned', 'Cassette', 'Frame', 'Sequence', 'election_id', 'Label', 'Ballot_Status', 'Original Party', 'ID_Required', 'Citizen', 'UnderAge', 'Challenged', 'Batch', 'Leg_Dist', 'Consolidation_Name', 'Precinct', 'House_District', 'School_District', 'Congressional_District', 'Verified', 'Consolidation_SerialNumber']


getdata = open(henryfile, "rb")
datareader = csv.reader((x.replace('\0', '') for x in getdata), delimiter="\t")

counter = 0

for line in datareader:

    if counter == 0:

        counter += 1

        if line != henryschema:

            print "henry no matching schema!"

            break

        continue



    if line[50] == "DEM":
        partystring = "D"
    elif line[50] == "REP":
        partystring = "R"
    else:
        partystring = "O"


    issuedstring = ""


    returned = line[43]
    returneddatepieces = returned.split(" ")
    if len(returneddatepieces) != 2: returnedstring = ""
    else:
        returneddatepieces2 = returneddatepieces[0].split("/")
        if len(returneddatepieces2) != 3: returnedstring = ""
        else:
            returnedstring = "2016-" + returneddatepieces2[0] + "-" + returneddatepieces2[1]
    

    outp.write("{0},{1},{2},{3},{4},{5},{6}\n".format("henry",
                                                      line[4] + " " + line[5] + " " + line[3],
                                                      partystring,
                                                      line[0],
                                                      line[16][0:5],
                                                      issuedstring,
                                                      returnedstring))
        



# huron


huronschema = [u'Category', u'Sourc', u'', u'', u'Issued', u'', u'', u'AV ID', u'Returned', u'Party', u'Name', u'Residence', u'City', u'', u'', u'State', u'Zip', u'Mailed To', u'Mail City', u'Mail S', u'Mail Z', u'Mail C', u'', u'Consolidatio', u'Precinct', u'School    \n', u'US Congress', u'OH Represe', u'Voter', u'State']
huronfile = placetoputfiles + "huron" + date + ".xls"

huron = xlrd.open_workbook(huronfile)
huronsheet = huron.sheet_by_index(0)

counter = 0

for rownum in xrange(huronsheet.nrows):

    if counter < 8:

        counter += 1
        continue

    if counter == 8:


        if huronsheet.row_values(rownum) != huronschema:

            print "huron no matching schema!"
            break


        counter += 1
        continue

    line = huronsheet.row_values(rownum)

    if line[0] == "": break


    partystring = line[9]
    if partystring != "D" and partystring != "R": partystring = "O"


    if line[4] == "": issuedstring = ""
    else:
        issued = xlrd.xldate.xldate_as_datetime(line[4],0)
        issuedstring = str(issued.year) + "-" + str(issued.month) + "-" + str(issued.day)

    if line[8] == "": returnedstring = ""
    else:
        returned = xlrd.xldate.xldate_as_datetime(line[8],0)
        returnedstring = str(returned.year) + "-" + str(returned.month) + "-" + str(returned.day)

    if line[28] == "": zipcode = ""
    else: zipcode = str(int(line[28]))

    namepieces = line[10].split(",")
    namestring = namepieces[1] + " " + namepieces[0]
    

    outp.write("{0},{1},{2},{3},{4},{5},{6}\n".format("huron",
                                                      namestring,
                                                      partystring,
                                                      zipcode,
                                                      line[16][0:5],
                                                      issuedstring,
                                                      returnedstring))




# summit


summitfile = placetoputfiles + "summit" + date + ".csv"
summitschema = ['LASTN', 'FIRSTN', 'MIDDLEN', 'PREFIXN', 'SUFFIXN', 'PARTYAFFIL', 'CNTYIDNUM', 'AVADDR1', 'AVADDR2', 'CITY', 'STATE', 'ZIPCODE', 'COUNTRY', 'AVSENTDATE', 'AVSENTMETH', 'AVRECVDATE', 'AVRECVMETH', 'AVAPPTYPE', 'PRSID', 'PRECNAME', 'AVAPPDATE']


getdata = open(summitfile, "rb")
datareader = csv.reader(getdata)

counter = 0

for line in datareader:

    if counter == 0:


        counter += 1

        if line != summitschema:

            print "summit no matching schema!"

            break

        continue



    if line[5] == "DEM":
        partystring = "D"
    elif line[5] == "REP":
        partystring = "R"
    else:
        partystring = "O"

    issued = line[13]
    issueddatepieces = issued.split("/")
    if len(issueddatepieces) != 3: issuedstring = ""
    else:
        issuedstring = "2016-" + issueddatepieces[0] + "-" + issueddatepieces[1]


    returned = line[15]
    returneddatepieces = returned.split("/")
    if len(returneddatepieces) != 3: returnedstring = ""
    else:
        returnedstring = "2016-" + returneddatepieces[0] + "-" + returneddatepieces[1]
    

    outp.write("{0},{1},{2},{3},{4},{5},{6}\n".format("summit",
                                                      line[1].strip() + " " + line[2].strip() + " " + line[0].strip(),
                                                      partystring,
                                                      line[6],
                                                      line[11][0:5],
                                                      issuedstring,
                                                      returnedstring))
        


# trumbull

trumbullschema = [u'Care Of', u'', u'', u'', u'  Mailed To', u'', u'', u'', u'', u'PCT', u' Party', u'', u'Category', u'', u'', u'Issued', u'Returned', u'', u'Voter ID', u'', u'State Id']
trumbullfile = placetoputfiles + "trumbull" + date + ".xls"

trumbull = xlrd.open_workbook(trumbullfile)
trumbullsheet = trumbull.sheet_by_index(0)

counter = 0

for rownum in xrange(trumbullsheet.nrows):


    if counter == 0:

        if trumbullsheet.row_values(rownum) != trumbullschema:

            print "trumbull no matching schema!"
            break


        counter += 1
        continue

    line = trumbullsheet.row_values(rownum)


    if line[5] == "": continue
    

    partystring = line[10]
    if partystring != "D" and partystring != "R": partystring = "O"


    if line[14] == "": issuedstring = ""
    else:
        issued = xlrd.xldate.xldate_as_datetime(line[14],0)
        issuedstring = str(issued.year) + "-" + str(issued.month) + "-" + str(issued.day)

    if line[17] == "": returnedstring = ""
    else:
        returned = xlrd.xldate.xldate_as_datetime(line[17],0)
        returnedstring = str(returned.year) + "-" + str(returned.month) + "-" + str(returned.day)    

    zipcode = line[7].split(" ")[-1:][0][0:5]

    voterid = str(int(line[19]))

    if line[0].strip() == "":
        line[5] = line[5].replace(",", "")

    else:

        line[5] = line[0].replace(",", "").strip()

    outp.write("{0},{1},{2},{3},{4},{5},{6}\n".format("trumbull",
                                                      line[5],
                                                      partystring,
                                                      voterid,
                                                      zipcode,
                                                      issuedstring,
                                                      returnedstring))    


outp.close()



# zip it and put it on dropbox


zipfilename = dropboxfolder + "merged_file_" + date + ".zip"

myzip = zipfile.ZipFile(zipfilename, "w")

myzip.write(placetoputfiles + "fulllist_" + date + ".csv", arcname="fulllist_" + date + ".csv", compress_type=zipfile.ZIP_DEFLATED)

myzip.close()
