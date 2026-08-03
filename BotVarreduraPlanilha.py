from playwright.sync_api import sync_playwright
import openpyxl

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    
    page.goto('https://proxies-devaprender.netlify.app/')
    linhas = page.get_by_role('row').all()
    proxies = []
    for linha in linhas[1:]:
        celulas = linha.get_by_role('cell').all()
        ip = celulas[0].inner_text()
        porta = celulas[1].inner_text()
        protocolo = celulas[4].inner_text()
        
        proxies.append([ip, porta, protocolo])
        
    browser.close()

planilha = openpyxl.Workbook()
pagina_inicial = planilha.active

pagina_inicial.append(['IP','Porta', 'Protocolo'])

for proxy in proxies:
    pagina_inicial.append(proxy)
    
planilha.save('proxies.xlsx')