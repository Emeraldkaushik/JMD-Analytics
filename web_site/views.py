from django.shortcuts import render
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
import webbrowser as web
from selenium.webdriver.chrome.options import Options
from time import sleep
import pandas as pd



# Create your views here.
def Index(request):
    template_name = 'index.html'

    return render(request, template_name)




def Whats_App_Automation(request):

    try:

        if request.method == "POST":

            excel_read = request.FILES['excel_file']
            print("EXCEL FILE --------->", excel_read)

            data_frame = pd.read_excel(excel_read, engine='openpyxl')
            data_frame = data_frame['Name'].tolist()
            print("Data-Frame -------->", data_frame)


            image_read = request.FILES['image_file']
            print("IMAGE FILE --------->", image_read)
    except Exception as e:
        print("EXCEPTION ----------->", e)
    
    template_name = 'whats_app_automation.html'

    # try:
    #     web.open('https://web.whatsapp.com/')
    # except Exception as e:
    #     print("EXCEPTION ----------->", e)
        
    # sleep(30)


    # driver_location = "/usr/bin/chromedriver"
    # binary_location = "/usr/bin/google-chrome"

    # option = webdriver.ChromeOptions()
    # option.binary_location = binary_location

    driver = webdriver.Chrome('/home/ubuntu/jmd/driver/chromedriver')

    driver.get('https://www.youtube.com/watch?v=CriSHYMtg9M')

    

    # options = Options ()
    # options.add_argument ('--profile-directory=Default')
    # options.add_argument ('-no-sandbox')
    # options.add_argument ('-ignore-certificate-errors')
    # options = Options()
    # options.headless = True
    # options.add_argument("--window-size=1920,1080")

    # driver = webdriver.Chrome()

    # driver = webdriver.Firefox(log_path='/home/ubuntu/env/bin/geckodriver')

    
    # driver.get('https://www.youtube.com/watch?v=CriSHYMtg9M')

    # sleep(30)

    # pyautogui.press(['tab', 'tab', 'tab'])

    # excel_path = r'C:\Users\admin\Desktop\jmd_marketing.xlsx'

    # contact_list = []
     
    # wb = xlrd.open_workbook(excel_path)
    # sheet = wb.sheet_by_index(0)
    # sheet.cell_value(0, 0)
     
    # for i in range(sheet.nrows):
    #     data = sheet.cell_value(i, 0) 
    # #     print(data)
    #     contact_list.append(data)
        
    # contact_lists = contact_list
    # # print(contact_lists)

    # path = r'C:\Users\admin\Django_Framework\jmd_web\JMD-Analytics\static\images\jmd-slider.jpeg'


    # for name in contact_lists:    
    #     send_message(name)

    return render(request, template_name)