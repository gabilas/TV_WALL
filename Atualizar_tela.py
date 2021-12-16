# versão do Chrome máquina BI COI: 93.0.4577.82

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

'''
[TELA 1]    [TELA 3]    [TELA 5]    [TELA 7]
[TELA 2]    [TELA 4]    [TELA 6]    [TELA 8]
'''

def main():

    options = Options()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    #TMAE (TELA 6) - COMPARTILHADO COM 'MONITORAMENTO'
    driver1 = webdriver.Chrome(chrome_options=options, executable_path = r'C:/WebDriver/Bin/chromedriver.exe', desired_capabilities={'ignoreZoomSetting':True})
    TMAE = "pbi.energisa.com.br/reports/powerbi/DEOP%20-%20ESE/COI/Tempo%20Real/TMAE%20-%20ONLINE%20v2"
    driver1.get("https://"+TMAE+"?rs:embed=true")
    driver1.set_window_position(4345,25, windowHandle = 'current')
    driver1.fullscreen_window()
    driver1.execute_script("document.body.style.zoom='25%'")

    #DEMANDA COMERCIAL LINHA DO TEMPO (TELA 2)
    driver2 = webdriver.Chrome(chrome_options=options, executable_path = r'C:/WebDriver/Bin/chromedriver.exe', desired_capabilities={'ignoreZoomSetting':True})
    COMERCIAL_LT = "pbi.energisa.com.br/reports/powerbi/DEOP%20-%20ESE/COI/Tempo%20Real/Demanda%20Comercial%20Linha%20do%20Tempo%20-%20COI%20BKP"
    driver2.get("https://"+COMERCIAL_LT+"?rs:embed=true")
    driver2.set_window_position(433,4, windowHandle = 'current')
    driver2.fullscreen_window()
    driver2.execute_script("document.body.style.zoom='25%'")

    #DEMANDA TÉCNICA (TELA 7 E 8)
    driver3 = webdriver.Chrome(chrome_options=options, executable_path = r'C:/WebDriver/Bin/chromedriver.exe', desired_capabilities={'ignoreZoomSetting':True})
    TECNICA = "pbi.energisa.com.br/reports/powerbi/DEOP%20-%20ESE/COI/Tempo%20Real/Demanda%20Técnica%20-%20COI%20v4%20(OC%20ENC%201)%20BKP"
    driver3.get("https://"+TECNICA+"?rs:embed=true")
    driver3.set_window_position(5808,-1098, windowHandle = 'current')
    driver3.set_window_size(1900, 2186, windowHandle= 'current')
    driver3.execute_script("document.body.style.zoom='25%'")

    #TV WALL (TELA 4)
    driver4 = webdriver.Chrome(chrome_options=options, executable_path = r'C:/WebDriver/Bin/chromedriver.exe', desired_capabilities={'ignoreZoomSetting':True})
    TV_WALL = "pbi.energisa.com.br/reports/powerbi/DEOP%20-%20ESE/COI/Tempo%20Real/Comercial%20TV%20Wall.v1%20BKP"
    driver4.get("https://"+TV_WALL+"?rs:embed=true")
    driver4.set_window_position(2358,18, windowHandle = 'current')
    driver4.fullscreen_window()
    driver4.execute_script("document.body.style.zoom='25%'")

    #CORTE (TELA 3)
    driver5 = webdriver.Chrome(chrome_options=options, executable_path = r'C:/WebDriver/Bin/chromedriver.exe', desired_capabilities={'ignoreZoomSetting':True})
    CORTE = "pbi.energisa.com.br/reports/powerbi/DEOP%20-%20ESE/COI/Tempo%20Real/Corte%20TV%20Wall.v8%20%20BKP"
    driver5.get("https://"+CORTE+"?rs:embed=true")
    driver5.set_window_position(2378,-1087, windowHandle = 'current')
    driver5.fullscreen_window()
    driver5.execute_script("document.body.style.zoom='25%'")

    #DEMANDA COMERCIAL (TELA 1)
    driver6 = webdriver.Chrome(chrome_options=options, executable_path = r'C:/WebDriver/Bin/chromedriver.exe', desired_capabilities={'ignoreZoomSetting':True})
    COMERCIAL = "pbi.energisa.com.br/reports/powerbi/DEOP%20-%20ESE/COI/Tempo%20Real/Demanda%20Comercial%20-%20COI%20v2%20BKP"
    driver6.get("https://"+COMERCIAL+"?rs:embed=true")
    driver6.set_window_position(464,-1064, windowHandle = 'current')
    driver6.fullscreen_window()
    driver6.execute_script("document.body.style.zoom='25%'")

    #COMPENSAÇÕES (TELA 5)
    driver7 = webdriver.Chrome(chrome_options=options, executable_path = r'C:/WebDriver/Bin/chromedriver.exe', desired_capabilities={'ignoreZoomSetting':True})
    COMPENSAÇÃO = "pbi.energisa.com.br/reports/powerbi/DEOP%20-%20ESE/COI/Tempo%20Real/compensações%20técnicas%20tv%20wall%20bkp"
    driver7.get("https://"+COMPENSAÇÃO+"?rs:embed=true")
    driver7.set_window_position(4327,-1091, windowHandle = 'current')
    driver7.fullscreen_window()
    driver7.execute_script("document.body.style.zoom='25%'")

    #MONITORAMENTO (TELA 6) - COMPARTILHADO COM 'TMAE'
    driver8 = webdriver.Chrome(chrome_options=options, executable_path = r'C:/WebDriver/Bin/chromedriver.exe', desired_capabilities={'ignoreZoomSetting':True})
    MONITORAMENTO = "pbi.energisa.com.br/reports/powerbi/dcmd%20-%20ese/Painel%20de%20Monitoramento%20de%20Ocorrências"
    driver8.get("https://"+MONITORAMENTO+"?rs:embed=true")
    driver8.set_window_position(4345,25, windowHandle = 'current')
    driver8.fullscreen_window()
    driver8.execute_script("document.body.style.zoom='25%'")

    while True:

        time.sleep(480)
        driver1.refresh()
        driver2.refresh()
        driver3.refresh()
        driver4.refresh()
        driver5.refresh()
        driver6.refresh()
        driver7.refresh()
        driver8.refresh()

        driver1.fullscreen_window()
        driver2.fullscreen_window()
        driver3.set_window_size(1900, 2186, windowHandle= 'current')
        driver4.fullscreen_window()
        driver5.fullscreen_window()
        driver6.fullscreen_window()
        driver7.fullscreen_window()
        driver8.fullscreen_window()

        driver1.execute_script("document.body.style.zoom='25%'")      
        driver2.execute_script("document.body.style.zoom='25%'")      
        driver3.execute_script("document.body.style.zoom='25%'")      
        driver4.execute_script("document.body.style.zoom='25%'")      
        driver5.execute_script("document.body.style.zoom='25%'")      
        driver6.execute_script("document.body.style.zoom='25%'")      
        driver7.execute_script("document.body.style.zoom='25%'")  
        driver8.execute_script("document.body.style.zoom='25%'")      


main()
