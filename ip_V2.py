import tkinter as tk
from tkinter import messagebox, ttk
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

def consultar_ip():
    ip = ip_entry.get().strip()
    if not ip:
        ip = "me"  # Usa o próprio IP do usuário se o campo estiver vazio
    
    status_label.config(text="Consultando...", foreground="blue")
    root.update()  # Atualiza a interface durante o carregamento
    
    info = get_ip_info(ip)
    result_text.delete("1.0", tk.END)  # Limpa o resultado anterior
    
    if "Erro" in info:
        status_label.config(text="Erro ao consultar o IP", foreground="red")
        messagebox.showerror("Erro", info["Erro"])
    else:
        status_label.config(text="Consulta concluída", foreground="green")
        for key, value in info.items():
            result_text.insert(tk.END, f"{key}: {value}\n")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Ferramenta de Consulta de IP")
root.geometry("500x400")
root.resizable(False, False)

# Estilo
style = ttk.Style()
style.theme_use("clam")

# Título
title_label = tk.Label(root, text="Consulta de Informações de IP", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Campo para entrada de IP
frame = tk.Frame(root)
frame.pack(pady=10)

ip_label = tk.Label(frame, text="Endereço IP:", font=("Arial", 12))
ip_label.pack(side=tk.LEFT, padx=5)

ip_entry = ttk.Entry(frame, font=("Arial", 12), width=30)
ip_entry.pack(side=tk.LEFT, padx=5)

# Botão de consulta
consultar_button = ttk.Button(root, text="Consultar", command=consultar_ip)
consultar_button.pack(pady=10)

# Resultado
result_frame = tk.Frame(root)
result_frame.pack(pady=10, fill=tk.BOTH, expand=True)

result_text = tk.Text(result_frame, font=("Courier", 12), height=10, width=50)
result_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = ttk.Scrollbar(result_frame, orient=tk.VERTICAL, command=result_text.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
result_text.configure(yscrollcommand=scrollbar.set)

# Status
status_label = tk.Label(root, text="", font=("Arial", 10))
status_label.pack(pady=5)

# Rodapé
footer_label = tk.Label(root, text="Desenvolvido por Você", font=("Arial", 10, "italic"))
footer_label.pack(side=tk.BOTTOM, pady=5)

# Inicia o programa
root.mainloop()
