

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver import ActionChains
import time
import webbrowser
import random
from bs4 import BeautifulSoup


print("\nOlá seja bem vindo ao")
time.sleep(2)

print("""  
                        ▀▀█▀▀ █░░█ █▀▀   █▀▀█ █▀▀█ █▀▀ █░█   █▀▀█ █░░█ █▀▀█ ░▀░ █▀▀ █▀▀
                        ░▒█░░ █▀▀█ █▀▀   █▄▄▀ █░░█ █░░ █▀▄   █░░░ █▀▀█ █░░█ ▀█▀ █░░ █▀▀
                        ░▒█░░ ▀░░▀ ▀▀▀   █░▒█ ▀▀▀▀ ▀▀▀ ▀░▀   █▄▄█ ▀░░▀ ▀▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀""")

time.sleep(2)

print("\nNão sabe qual filme do THE ROCK VER HOJE?\n")

time.sleep(2)

print("\nSeus problemas acabaram, iremos escolher o filme perfeito para você de acordo com seus dados\n")
time.sleep(2)

nome = input("\nPor favor digite seu nome:\n")
time.sleep(3)
idade = input("\nAgora preciso de sua idade:\n")
time.sleep(3)
color = input("\nMuito bem, agora sua cor favorita:\n")
time.sleep(3)
signo = input("\nQual o seu signo:\n")
time.sleep(2)
print("\nCarregando dados")
print("\n-", nome, "-", idade, "-", color, "-", signo,
      "-", signo, "-", color, "-", idade, "-", nome)
time.sleep(2)
print("\nAnalisando informações sanguineas")
time.sleep(2)
print("\nA pagina do filme ideal do The Rock escolhido irá abrir nos próximos segundos, aproveite o filme.💪")
time.sleep(1)
print("5")
time.sleep(1)
print("4")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)


luck = random.randint(0, 67)


navegador = webdriver.Edge()

lista_The_Rock = ["https://www.adorocinema.com/filmes/filme-276114/",
                  "https://www.adorocinema.com/filmes/filme-253389/",
                  "https://www.adorocinema.com/filmes/filme-282524/",
                  "https://www.adorocinema.com/filmes/filme-266572/",
                  "https://www.adorocinema.com/filmes/filme-266572/",
                  "https://www.adorocinema.com/series/serie-26080/temporada-47165/",
                  "https://www.adorocinema.com/filmes/filme-262468/",
                  "https://www.adorocinema.com/filmes/filme-251824/",
                  "https://www.adorocinema.com/filmes/filme-57197/",
                  "https://www.adorocinema.com/filmes/filme-245225/",
                  "https://www.adorocinema.com/series/serie-26080/temporada-42799/",
                  "https://www.adorocinema.com/series/serie-26080/temporada-37634/",
                  "https://www.adorocinema.com/filmes/filme-267380/",
                  "https://www.adorocinema.com/series/serie-17304/temporada-34696/",
                  "https://www.adorocinema.com/filmes/filme-262124/",
                  "https://www.adorocinema.com/filmes/filme-253878/",
                  "https://www.adorocinema.com/filmes/filme-219944/",
                  "https://www.adorocinema.com/filmes/filme-203842/",
                  "https://www.adorocinema.com/series/serie-17304/temporada-31964/",
                  "https://www.adorocinema.com/filmes/filme-236733/",
                  "https://www.adorocinema.com/filmes/filme-217881/",
                  "https://www.adorocinema.com/filmes/filme-204486/",
                  "https://www.adorocinema.com/series/serie-17304/temporada-29475/",
                  "https://www.adorocinema.com/filmes/filme-89997/",
                  "https://www.adorocinema.com/filmes/filme-244111/",
                  "https://www.adorocinema.com/filmes/filme-210318/",
                  "https://www.adorocinema.com/filmes/filme-146565/",
                  "https://www.adorocinema.com/filmes/filme-221541/",
                  "https://www.adorocinema.com/series/serie-17304/temporada-26729/",
                  "https://www.adorocinema.com/filmes/filme-225958/",
                  "https://www.adorocinema.com/filmes/filme-171204/",
                  "https://www.adorocinema.com/series/serie-17304/temporada-23488/",
                  "https://www.adorocinema.com/filmes/filme-227832/",
                  "https://www.adorocinema.com/filmes/filme-200433/",
                  "https://www.adorocinema.com/filmes/filme-198750/",
                  "https://www.adorocinema.com/filmes/filme-138335/",
                  "https://www.adorocinema.com/filmes/filme-170252/",
                  "https://www.adorocinema.com/filmes/filme-130326/",
                  "https://www.adorocinema.com/filmes/filme-201413/",
                  "https://www.adorocinema.com/filmes/filme-41005/",
                  "https://www.adorocinema.com/filmes/filme-189651/",
                  "https://www.adorocinema.com/filmes/filme-144687/",
                  "https://www.adorocinema.com/filmes/filme-178061/",
                  "https://www.adorocinema.com/filmes/filme-134501/",
                  "https://www.adorocinema.com/filmes/filme-144195/",
                  "https://www.adorocinema.com/filmes/filme-146402/",
                  "https://www.adorocinema.com/filmes/filme-145709/",
                  "https://www.adorocinema.com/filmes/filme-130201/",
                  "https://www.adorocinema.com/filmes/filme-126662/",
                  "https://www.adorocinema.com/filmes/filme-114624/",
                  "https://www.adorocinema.com/series/serie-3581/temporada-8977/",
                  "https://www.adorocinema.com/series/serie-3096/temporada-5308/",
                  "https://www.adorocinema.com/series/serie-769/temporada-5814/",
                  "https://www.adorocinema.com/filmes/filme-126617/",
                  "https://www.adorocinema.com/filmes/filme-119357/",
                  "https://www.adorocinema.com/filmes/filme-57851/",
                  "https://www.adorocinema.com/filmes/filme-118957/",
                  "https://www.adorocinema.com/filmes/filme-60696/",
                  "https://www.adorocinema.com/filmes/filme-57664/",
                  "https://www.adorocinema.com/filmes/filme-53031/",
                  "https://www.adorocinema.com/filmes/filme-50988/",
                  "https://www.adorocinema.com/filmes/filme-46372/",
                  "https://www.adorocinema.com/filmes/filme-29140/",
                  "https://www.adorocinema.com/filmes/filme-27430/",
                  "https://www.adorocinema.com/filmes/filme-109093/",
                  "https://www.adorocinema.com/series/serie-305/temporada-1587/",
                  "https://www.adorocinema.com/series/serie-3/temporada-8/"]


pum = lista_The_Rock[luck]

webbrowser.open_new_tab(pum)

#navegador.find_element(By.XPATH, '//*[@id="actor"]/table/tbody/tr[1]/td[2]/a').click()

input("Quer escolher novamente?")
