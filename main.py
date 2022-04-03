import selenium
from selenium import webdriver
import time
import pandas as pd

# Especifiquem la ruta del Driver de Chrome
driver_path = 'C:\Mis documentos\Màster UOC\Semestre 2\Tipologia i Cicle de Vida de les Dades\PRAC 1\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)

# Escribim les nostres credencials:
email = "replace_your_mail"
password = "replace_your_password"

# Especifiquem el número de pàgines
num_pag = 11

# Anem a la URL que li donem i iniciem sessió
driver.get('https://www.linkedin.com/login')
time.sleep(1)
driver.find_element_by_id('username').send_keys(email)
driver.find_element_by_id('password').send_keys(password)

# Busquem el botó per loggejar-nos
log_in_button = driver.find_element_by_class_name('login__form_action_container')

# Cliquem en ell
log_in_button.click()

# Confirmació de les dades (igual no és necessàri)
# confirm_button = driver.find_element_by_class_name('primary-action-new')
# confirm_button.click()

# Anem a la pestanya de 'jobs'
driver.get("https://www.linkedin.com/jobs/")
time.sleep(1)

# Fem una búsqueda en funció de paraules clau i una ubicació
keywords = "Analista de datos"
location = "Barcelona"

# Busquem els elements de la búsqueda i els hi posem els valors que volguem
search_keywords = driver.find_element_by_xpath('//*[@id="jobs-search-box-keyword-id-ember31"]')
search_keywords.send_keys(keywords)

search_location = driver.find_element_by_xpath('//*[@id="jobs-search-box-location-id-ember31"]')
search_location.send_keys(location)

# Busquem el pathing del botó per cercar
search_button = driver.find_element_by_xpath('//*[@id="global-nav-search"]/div/div[2]/button[1]')

# Cliquem en ell
search_button.click()
time.sleep(3) 

company = []
location = []
offer = []
time_offer = []
# n_rivals = []
schedule = []
id = 0
# Probarem de fer un bucle que vagi avançant les pàgines
for i in range(1,num_pag):
     driver.find_element_by_css_selector(f'[aria-label="Página {i}"]').click()
     # Anem a extreure la informació del llistat d'ofertes que hem buscat
     list_items = driver.find_element_by_class_name('jobs-search-results__list')
     jobs = list_items.find_elements_by_class_name('jobs-search-results__list-item')
     time.sleep(2) 
     
     # Agafem 25 ofertes de cada pàgina
     for job in jobs:
         # Molaria anar fent roll entrre pagines i no nomes en la llista
         driver.execute_script("arguments[0].scrollIntoView();", job)
         job.click()
         time.sleep(1)
         # Agafem la info
         company.append(driver.find_element_by_class_name('jobs-unified-top-card__company-name').text)
         location.append(driver.find_element_by_class_name('jobs-unified-top-card__bullet').text)
         time_offer.append(driver.find_element_by_class_name('jobs-unified-top-card__posted-date').text)
         time.sleep(1)
         schedule.append(driver.find_element_by_class_name('jobs-unified-top-card__job-insight').text)
         # aqui peta !!!! nombre de solicituds i nom de l'oferta
         # n_rivals.append(driver.find_element_by_class_name('jobs-unified-top-card__applicant-count').text)
         offer.append(driver.find_element_by_class_name('jobs-search__right-rail').text.split('\n')[2])
         id = id + 1

print("S'han extret un total de {} ofertes de treball".format(id))

data = pd.DataFrame(list(zip(offer, company, location, time_offer, schedule)), 
                    columns=['Nom_Oferta', 'Empresa', 'Ubicació', 'Temps_Oferta', 'Horari'])

data.to_csv('C:\Mis documentos\Màster UOC\Semestre 2\Tipologia i Cicle de Vida de les Dades\PRAC 1\dades.csv')

# Coses extres per veure:
# - Intentar agafar el nº de sol·licituds, encara no sé com fer-ho
# - Igual agafar la descripció de l'oferta
# - Hem de parlar sobre la quantitat d'ofertes a af¡gafar, ara mateix s'agafen 10 pagines, 250 ofertes,
#   però igual si n'agafem menys però més variables pot ser interessant també
    
    
