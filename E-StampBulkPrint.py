from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from tkinter import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


s = Service(ChromeDriverManager().install())


def runnn():

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.page_load_strategy = 'eager'
    chrome_driver = "C:\\Users\\HP\\Downloads\\chromedriver.exe"
    driver = webdriver.Chrome(service=s, options=options)
    driver.set_window_size(1024, 600)
    driver.maximize_window()
    driver.get(
        'https://www.shcilestamp.com/eStampIndia/useradmin/UserAdminLoginServlet?rDoAction=LoadLoginPage')
    driver.implicitly_wait(12)
    driver.find_element(By.CLASS_NAME, 'close-btn').click()
    USERid = driver.find_element(
        By.XPATH, '/html/body/form/table/tbody/tr[1]/td/table[3]/tbody/tr/td/table/tbody/tr[3]/td[2]/input')
    USERid.send_keys('upsandsiu')
    Password = driver.find_element(
        By.XPATH, '/html/body/form/table/tbody/tr[1]/td/table[3]/tbody/tr/td/table/tbody/tr[4]/td[2]/input')
    Password.send_keys('Qq2021q@11')
    Capcha = driver.find_element(By.XPATH, '//*[@id="searchjcaptcha"]').click()
    try:
        WebDriverWait(driver, 120).until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/form/b/div/table/tbody/tr[2]/td[1]/input')))
        checkbtn = driver.find_element(
            By.XPATH, '/html/body/form/b/div/table/tbody/tr[2]/td[1]/input').click()
        remove = driver.find_element(
            By.XPATH, '/html/body/form/b/table/tbody/tr/td[1]/div/input').click()
    except:
        print('Remove not found. Skipping...')

    element = WebDriverWait(driver, 120).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Create Submission")))
    driver.find_element(By.LINK_TEXT, "Create Submission").click()
    try:
        driver.implicitly_wait(3)
        driver.switch_to.alert.accept()
    except:
        print('Conquered Alert:)')

    Registrable = '//*[@id="RegSD"]'
    Non_Registrable = '//*[@id="NonRegSD"]'

    i = 1
    while i <= int(e.get()):

        statusvar.set('Printing ' + str(i) + ' of ' + str(e.get()))
        sbar.update()

        element = WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Create Submission"))).click()
        if var.get() == ('Affidavit शपथ पत्र [4]'):

            element = WebDriverWait(driver, 120).until(
                EC.presence_of_element_located((By.XPATH, (Non_Registrable))))
            select = Select(driver.find_element(By.XPATH, Non_Registrable))
            select.select_by_visible_text(var.get())

        if var.get() == ('General Loan Agreement सामान्य ऋण अनुबंध [5c]'):

            element = WebDriverWait(driver, 120).until(
                EC.presence_of_element_located((By.XPATH, (Non_Registrable))))
            select = Select(driver.find_element(By.XPATH, Non_Registrable))
            select.select_by_visible_text(var.get())

        if var.get() == ('Indemnity Bond क्षतिपूर्ति-बंधपत्र [34]'):

            element = WebDriverWait(driver, 120).until(
                EC.presence_of_element_located((By.XPATH, (Non_Registrable))))
            select = Select(driver.find_element(By.XPATH, Non_Registrable))
            select.select_by_visible_text(var.get())

        if var.get() == ('Agreement or Memorandum of an agreement करार या करार का ज्ञापन या इकरारनामा [5]'):
            element = WebDriverWait(driver, 120).until(
                EC.presence_of_element_located((By.XPATH, (Registrable))))

            select = Select(driver.find_element(By.XPATH, Registrable))
            select.select_by_visible_text(var.get())

        if var.get() == ('Bank Guarantee बैंक गारंटी [12 (A)]'):
            element = WebDriverWait(driver, 120).until(
                EC.presence_of_element_located((By.XPATH, (Registrable))))

            select = Select(driver.find_element(By.XPATH, Registrable))
            select.select_by_visible_text(var.get())

        Next_1 = driver.find_element(
            By.XPATH, '/html/body/table/tbody/tr[1]/td/table[3]/tbody/tr[1]/td[2]/form/table/tbody/tr[4]/td/table/tbody/tr/td/input').click()

        element = WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="TextField6Mand"]')))

        Purchaser = driver.find_element(
            By.XPATH, '//*[@id="TextField6Mand"]').send_keys(FPENTRY.get())

        FirstP = driver.find_element(
            By.XPATH, '//*[@id="TextField11Mand"]').send_keys(FPENTRY.get())

        Addressl1 = driver.find_element(
            By.XPATH, '//*[@id="TextField12Mand"]').send_keys(AF1ENTRY.get())

        Addressl2 = driver.find_element(
            By.XPATH, '//*[@id="TextField13Mand"]').send_keys(AF2ENTRY.get())

        SecondP = driver.find_element(
            By.XPATH, '//*[@id="TextField18Mand"]').send_keys(SPENTRY.get())

        Amount = driver.find_element(
            By.XPATH, '//*[@id="TextField28Mand"]').send_keys(int(gh.get()))

        actions = ActionChains(driver).send_keys(Keys.TAB * 1).perform()
        driver.switch_to.alert.accept()

        MobileNO = driver.find_element(
            By.XPATH, '//*[@id="fpMobNo"]').send_keys(M1ENTRY.get())

        Save = driver.find_element(
            By.XPATH, '/html/body/table/tbody/tr/td/table[3]/tbody/tr[2]/td[2]/input[2]').click()

        driver.switch_to.alert.accept()

        # PROCEED
        element = WebDriverWait(driver, 120).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="frmStampDuty"]/table/tbody/tr[2]/td/table[3]/tbody/tr/td[2]/input'))).click()

        # ACCEPT
        element = WebDriverWait(driver, 120).until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/table/tbody/tr/td/table[3]/tbody/tr[2]/td[2]/input[3]'))).click()
        driver.switch_to.alert.accept()
        element = WebDriverWait(driver, 120).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="frmPrevCert"]/table/tbody/tr[6]/td/table[4]/tbody/tr/td/input'))).click()
        element = WebDriverWait(driver, 120).until(EC.text_to_be_present_in_element(
            (By.XPATH, '//*[@id="printerListContainer"]/select'), 'HP LaserJet Pro M304-M305'))
        element = WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="printBtn"]'))).click()
        element = WebDriverWait(driver, 120).until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/table/tbody/tr[1]/td/table[3]/tbody/tr[1]/td[2]/form/table/tbody/tr[4]/td/table/tbody/tr/td/input[2]')))

        statusvar.set('Printed Certificates: ' + str(i))

        i += 1


root = Tk()
root.geometry("590x336")
root.title("Ayush's Program")

Label(root, text="E Submission", font='Bahnschrift 19').grid(row=0, column=3)

First_Party = Label(root, text='FIRST PARTY',   font='Bahnschrift 10').grid(
    row=1, column=2, sticky=W)
AddressF1 = Label(root, text='ADDRESS_L1',    font='Bahnschrift 10').grid(
    row=2, column=2, sticky=W)
AddressF2 = Label(root, text='ADDRESS_L2',    font='Bahnschrift 10').grid(
    row=3, column=2, sticky=W)
Second_Party = Label(root, text='SECOND PARTY',  font='Bahnschrift 10').grid(
    row=4, column=2, sticky=W)
MOB1 = Label(root, text='MOBILE NO.',    font='Bahnschrift 10').grid(
    row=5, column=2, sticky=W)

FPvalue = StringVar()
AF1value = StringVar()
AF2value = StringVar()
SPvalue = StringVar()
M1value = IntVar()


FPENTRY = Entry(root, textvariable=FPvalue,
                font='Bahnschrift 10', width=50, borderwidth=2)
AF1ENTRY = Entry(root, textvariable=AF1value,
                 font='Bahnschrift 10', width=50, borderwidth=2)
AF2ENTRY = Entry(root, textvariable=AF2value,
                 font='Bahnschrift 10', width=50, borderwidth=2)
SPENTRY = Entry(root, textvariable=SPvalue,
                font='Bahnschrift 10', width=50, borderwidth=2)
M1ENTRY = Entry(root, textvariable=M1value,
                font='Bahnschrift 10', width=50, borderwidth=2)


FPENTRY.grid(row=1, column=3,  padx=15, pady=3)
AF1ENTRY.grid(row=2, column=3,  padx=15, pady=3)
AF2ENTRY.grid(row=3, column=3,  padx=15, pady=3)
SPENTRY.grid(row=4, column=3,  padx=15, pady=3)
M1ENTRY.grid(row=5, column=3,  padx=15, pady=3)


mybutton = Button(text='FAST PRINT', font='Bahnschrift 12',
                  command=runnn, relief=GROOVE, padx=10, pady=12)
mybutton.grid(row=6, column=3)


evar = IntVar()
e = Label(root, text='                                                                                           NO. OF STAMPS',
          font='Bahnschrift 10').grid(row=20, column=3)
e = Entry(root, textvariable=evar,
          font='Bahnschrift 12', width=10, borderwidth=3)
e.grid(row=20, column=4)
app = e.get()

ghvar = IntVar()
gh = Label(root, text='                                                                                          AMOUNT',
           font='Bahnschrift 10').grid(row=22, column=3)
gh = Entry(root, textvariable=ghvar,
           font='Bahnschrift 12', width=10, borderwidth=3)
gh.grid(row=22, column=4)


statusvar = StringVar()
statusvar.set('')
sbar = Label(root, textvariable=statusvar)
sbar.grid(row=24, column=4, columnspan=4)


statusvar = StringVar()
statusvar.set('Ready')
sbar = Label(root, textvariable=statusvar, bd=1, relief=SUNKEN, anchor=W)
sbar.grid(row=26, column=0, columnspan=10, sticky=W+E)


var = StringVar()
var.set('General Loan Agreement [5c]')


Label(root, text='PURPOSE', font='Bahnschrift 12').grid(row=0, column=4)

radio = Radiobutton(root, text='Affidavit', font='Bahnschrift 10', variable=var,
                    value="Affidavit शपथ पत्र [4]").grid(row=1, column=4, sticky=W)
radio = Radiobutton(root, text='Agreement', font='Bahnschrift 10', variable=var,
                    value="Agreement or Memorandum of an agreement करार या करार का ज्ञापन या इकरारनामा [5]").grid(row=2, column=4, sticky=W)
radio = Radiobutton(root, text='Loan', font='Bahnschrift 10', variable=var,
                    value="General Loan Agreement सामान्य ऋण अनुबंध [5c]").grid(row=3, column=4, sticky=W)
radio = Radiobutton(root, text='BANK G', font='Bahnschrift 10', variable=var,
                    value="Bank Guarantee बैंक गारंटी [12 (A)]").grid(row=4, column=4, sticky=W)
radio = Radiobutton(root, text='Indemnity', font='Bahnschrift 10', variable=var,
                    value="Indemnity Bond क्षतिपूर्ति-बंधपत्र [34]").grid(row=5, column=4, sticky=W)


root.mainloop()
