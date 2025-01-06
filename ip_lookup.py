import requests

def get_ip_info(ip):
    """Consulta informações sobre o IP usando o serviço ipinfo.io"""
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        if response.status_code == 200:
            data = response.json()
            return {
                "IP": data.get("ip", "Desconhecido"),
                "Cidade": data.get("city", "Desconhecida"),
                "Região": data.get("region", "Desconhecida"),
                "País": data.get("country", "Desconhecido"),
                "Org": data.get("org", "Desconhecida"),
                "Latitude/Longitude": data.get("loc", "Desconhecido"),
                "Hostname": data.get("hostname", "Desconhecido"),
            }
        else:
            return {"Erro": "Não foi possível obter informações sobre o IP."}
    except Exception as e:
        return {"Erro": str(e)}

def main():
    print("=== Ferramenta de Consulta de IP ===")
    ip = input("Digite o endereço IP (ou pressione Enter para usar seu próprio IP): ").strip()
    if not ip:
        ip = "me"
    
    print("\nConsultando informações...\n")
    info = get_ip_info(ip)
    
    for key, value in info.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
