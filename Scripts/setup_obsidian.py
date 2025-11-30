import os

def create_structure():
    # Define a raiz do Vault (Apontando para a pasta de ferramentas externa)
    base_path = r"f:\ferramentas\meu-vapo-mind"
    # base_path = os.path.abspath(base_path)
    
    # Estrutura de pastas
    folders = [
        "Perfil/_anexos",
        "Inventario/_anexos",
        "Protocolos/_anexos",
        "Sessoes/_anexos",
        "Sessoes/_templates",
        "Sessoes/2025",
        "Analises",
        "Diario Pessoal/_templates",
        "Scripts" # Para guardar cópias dos scripts dentro do vault se quiser
    ]

    print(f"🚀 Iniciando setup do Vault em: {base_path}")

    for folder in folders:
        path = os.path.join(base_path, folder)
        os.makedirs(path, exist_ok=True)
        print(f"✅ Pasta criada: {folder}")

    # Conteúdo dos arquivos iniciais
    files = {
        "Inventario/Inventario-Geral.md": """# Inventário Geral

## 🌿 Flores (Cannabis)

### Lemon Haze
![[inv-flor-lemonhaze-macro.jpg|right|250]]
- **Tipo:** Sativa Dominante
- **Terpeno Principal:** Limoneno (Cítrico/Energia)
- **Estoque:** Alto
- **Efeito Esperado:** Foco, criatividade, leve euforia.
- **Melhor Temperatura:** 175°C - 185°C

### OG Kush
![[inv-flor-ogkush-macro.jpg|right|250]]
- **Tipo:** Indica Dominante
- **Terpeno Principal:** Mirceno (Terroso/Relaxamento)
- **Estoque:** Baixo
- **Efeito Esperado:** Relaxamento físico, sono, anti-ansiedade.

---

## 🍂 Botânicos (Ervas Legais)

### Lavanda
- **Propriedade:** Calmante, ansiolítico.
- **Temp. Vaporização:** 130°C - 190°C
- **Sinergia:** Ótima com Indicas para sono.

### Camomila
- **Propriedade:** Sedativo leve, relaxante muscular.
- **Temp. Vaporização:** 190°C

---

## 🎮 Dispositivos e Acessórios

### XMAX V3 Pro
![[inv-disp-v3pro-montagem.jpg|right|250]]
- **Tipo:** Convecção Híbrida
- **Modos de Operação:**
    - **Sessão 4min:** Ideal para microdosing ou sabor intenso rápido.
    - **Sessão 6min:** Ideal para extração completa (AVB escuro).
    - **On-Demand:** Para tragadas únicas e rápidas (foco em efeito imediato).
- **Dicas de Uso:** Puxada longa e suave (>10s) para ativar a convecção.

### Dynavap M
- **Tipo:** Condução/Mecânico
- **Modos:**
    - **Aquecimento na Base:** Nuvens densas, extração rápida (1-2 ciclos).
    - **Aquecimento na Ponta:** Sabor, extração lenta (3-4 ciclos).
""",
        "Sessoes/_templates/template-sessao.md": """---
tipo: sessao
data: <% tp.date.now("YYYY-MM-DD") %>
hora_inicio: "<% tp.date.now("HH:mm") %>"
status: aberta

# Check-in
atividade_antes: 
mood_pre: 
mood_tags_pre: []
intencao_tipo: 
estado_desejado: []

# Protocolo
protocolo_ref: "[[]]"
blend: "[[Inventario-Geral#NomeDaFlor]] (XX%) + [[Inventario-Geral#NomeBotanico]] (XX%)"
temperatura_inicial: 
temperatura_final: 
dispositivo: "[[Inventario-Geral#NomeDispositivo]]"
modo_dispositivo: "" 
acessorio: ""

# Check-out
hora_checkout: ""
mood_pos: 
alinhamento: 
vontade_redosar: 
reflexao_curta: ""
---

# Sessão: <% tp.date.now("YYYY-MM-DD") %> | <% tp.date.now("HH:mm") %>

## 🔵 PRÉ-SESSÃO (Check-in)

**Contexto:**
...

**Intenção:**
...

**Protocolo Escolhido:**
...

---

## 🟢 DURANTE A SESSÃO

**Observações:**
- ...

## 📷 Registros Visuais
![[sess-<% tp.date.now("YYYYMMDD") %>-residuo.jpg|right|200]]

---

## 🟡 PÓS-SESSÃO (Check-out)

<!-- Template para preencher depois:
- Hora do check-out: 
- Humor final (0-10): 
- Tags finais: 
- Alinhamento (0-100%): 
- Redosar? Sim/Não
- Reflexão: O que aprendi?
-->
""",
        "Perfil/meu-perfil.md": """# Meu Perfil - Autoconhecimento

## 1. Dados Pessoais
- **Nome:** Eu
- **Idade:** 
- **Gênero:** 
- **Altura:** 
- **Peso:** 

## 2. Objetivos
- [ ] Melhorar a qualidade do sono
- [ ] Aumentar o foco e a produtividade
- [ ] Reduzir a ansiedade
"""
    }

    for filename, content in files.items():
        path = os.path.join(base_path, filename)
        if not os.path.exists(path):
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"📄 Arquivo criado: {filename}")
        else:
            print(f"⚠️ Arquivo já existe (ignorado): {filename}")

    print("\n✨ Setup concluído! Abra a pasta 'MeuVapoMind' como um Vault no Obsidian.")

if __name__ == "__main__":
    create_structure()
