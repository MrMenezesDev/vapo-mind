# MeuVapoMind - Ferramenta Pessoal de Autoconhecimento

## 1. Visão Geral

O **MeuVapoMind** é uma ferramenta pessoal de autoconhecimento através da vaporização consciente. Diferente do VapoMind comercial, esta versão é focada exclusivamente no **uso individual**, sem infraestrutura de produto, monetização ou escala.

### Propósito
- Ferramenta de **auto-observação** e desenvolvimento pessoal
- Registro estruturado de experiências e padrões
- Experimentação guiada sem pressão comercial
- Construção de uma relação consciente e intencional com medicina natural

### Filosofia Central
Inspirado na **Pedagogia da Autonomia** (Paulo Freire), o sistema parte das minhas próprias subjetividades, crenças e práticas para criar um diálogo interno estruturado que promove consciência e redução de danos.

---

## 2. Diferenças do VapoMind Comercial

| Aspecto | VapoMind (Produto) | MeuVapoMind (Pessoal) |
|---------|-------------------|----------------------|
| **Objetivo** | Atender milhares de usuários | Ferramenta individual de autoconhecimento |
| **Infraestrutura** | Backend robusto, APIs, bots | Arquivo local, scripts simples ou planilha |
| **IA/LLM** | Agente conversacional premium | Prompts manuais para reflexão própria |
| **Escalabilidade** | Prioridade máxima | Irrelevante |
| **Monetização** | Freemium/BYOK | Gratuito (uso próprio) |
| **Complexidade** | Sistema modular completo | Minimalista e funcional |
| **Manutenção** | Contínua e profissional | Conforme necessidade pessoal |

---

## 3. Arquitetura Técnica (Obsidian-Centric + ETL)

### Filosofia Arquitetural

**Princípio Central:** Separação radical entre **Escrita** (interface humana) e **Análise** (processamento de dados).

- **Obsidian = Front-end:** Onde você escreve, reflete e registra (baixa fricção)
- **Python ETL = Processador:** Extrai, transforma e carrega os dados
- **SQLite/DuckDB = Backend Analítico:** Onde os dados estruturados vivem
- **Dashboard = Visualização:** Lê do banco, não do Markdown

**Por que essa separação é crítica:**
- Obsidian é excelente para escrita humana, péssimo para queries SQL complexas
- Markdown é flexível e versionável (Git), mas não é otimizado para análises longitudinais
- Um banco de dados local permite análises que seriam impossíveis com grep/regex em arquivos

### 3.1. Camada de Entrada: Obsidian (Interface de Baixa Fricção)

**Estrutura de Vault (Atualizada):**

```
MeuVapoMind/
├── 📁 Perfil/
│   ├── 📁 _anexos/          <-- Exames, fotos pessoais
│   └── meu-perfil.md
├── 📁 Inventario/
│   ├── 📁 _anexos/          <-- Fotos macro (flores) e montagens (devices)
│   └── Inventario-Geral.md  <-- Arquivo único consolidado (Flores, Botânicos, Devices)
├── 📁 Protocolos/
│   ├── 📁 _anexos/          <-- Gráficos de temp e GIFs de respiração
│   ├── sono-profundo.md
│   └── foco-criativo.md
├── 📁 Sessoes/
│   ├── 📁 _anexos/          <-- Fotos de resíduos (AVB) e ambiente (set)
│   ├── 2025/
│   │   └── ...
│   └── _templates/
│       └── template-sessao.md
├── 📁 Analises/
│   ├── insights-mensais.md
│   └── padroes-identificados.md
└── 📁 Scripts/
    ├── etl_obsidian_to_db.py
    ├── detect_open_loops.py
    ├── impact_metrics.py
    └── requirements.txt
```

**Plugins Essenciais do Obsidian:**

1. **Templater:** Para criar sessões rapidamente com Frontmatter pré-preenchido
2. **Dataview:** Para queries básicas dentro do Obsidian (opcional)
3. **Calendar:** Navegação temporal das sessões
4. **Periodic Notes:** Criação automática de notas diárias

**Formato de Nota de Sessão (YAML Frontmatter):**

Cada nota de sessão usa **Properties/Frontmatter** para dados estruturados e corpo Markdown para reflexões qualitativas. O uso de **Links ([[ ]])** é mandatório para conectar a experiência ao inventário.

```markdown
---
# Metadados Estruturados (Extraíveis pelo ETL)
tipo: sessao
data: 2025-01-20
hora_inicio: "22:30"
status: aberta

# Check-in
atividade_antes: estudo
mood_pre: 4
mood_tags_pre: [mente_acelerada, tensao_ombros]
intencao_tipo: medicinal
estado_desejado: [calmo, sono_profundo]

# Protocolo (Link para o arquivo do protocolo)
protocolo_ref: "[[Sono Profundo]]" 
blend: "[[Inventario-Geral#Skunk Wolf|Skunk]] (60%) + [[Inventario-Geral#Lavanda|Lavanda]] (30%)"
temperatura_inicial: 185
temperatura_final: 200
dispositivo: "[[Inventario-Geral#XMAX V3 Pro|V3 Pro]]"
modo_dispositivo: "Sessão 4min" # Referência ao modo cadastrado no inventário
acessorio: bubbler

# Check-out
hora_checkout: ""
mood_pos: null
alinhamento: null
vontade_redosar: null
---

# Sessão: 2025-01-20 | 22:30

## 🔵 PRÉ-SESSÃO (Check-in)

**Contexto:**
Passei 4h estudando para certificação. Cabeça quente, ombros tensos.

**Intenção:**
Preciso desligar a mente e relaxar os ombros para dormir bem. Honestamente, também tem um componente de fuga/ansiedade aqui.

**Protocolo Escolhido:**
Vou fazer o blend "Sono Profundo" mas ajustado: mais lavanda que o normal porque estou muito acelerado.

---

## 🟢 DURANTE A SESSÃO

**[Espaço para notas rápidas durante, se quiser]**

- Sabor floral forte no início
- Ombros começaram a soltar aos 3min
- Pensamentos desaceleraram

---

## 🟡 PÓS-SESSÃO (Check-out)

**[ESTE BLOCO PODE FICAR VAZIO - O SCRIPT VAI DETECTAR E COBRAR DEPOIS]**

<!-- Template para preencher depois:
- Hora do check-out: 
- Humor final (0-10): 
- Tags finais: 
- Alinhamento (0-100%): 
- Redosar? Sim/Não
- Reflexão: O que aprendi?
-->

## 📷 Registros Visuais
![[sess-20250120-residuo.jpg|right|200]]
*Legenda: Resíduo marrom claro, extração eficiente.*

---

## 4. Protocolos Pessoais (Templates)

### Protocolo: Sono Profundo 💤

**Objetivo:** Dormir rápido e acordar descansado

**Blend Base:**
- 50-60% Indica ou Híbrida relaxante
- 30-40% Lavanda
- 10-20% Camomila ou Lúpulo

**Temperatura:**
- Início: 175°C (terpenos sedativos)
- Fim: 195°C (cannabinoides pesados)

**Timing:**
- 1-2h antes de dormir (não deixar pra última hora)

**Ritual:**
- Desligar telas 30min antes
- Banho morno
- Respiração 4-7-8 (3 ciclos)
- Sessão
- Leitura leve ou meditação guiada

---

### Protocolo: Foco Criativo ⚡

**Objetivo:** Trabalho mental sem sedação

**Blend:**
- 70% Sativa ou Híbrida energética
- 20% Hortelã-Pimenta
- 10% Sálvia

**Temperatura:**
- Máximo 185°C (evitar sonolência)

**Timing:**
- Manhã ou início da tarde
- Após café da manhã (nunca em jejum)

**Ritual:**
- Alongamento 5min
- Definir 1 tarefa específica
- Timer de 25min (Pomodoro)
- Hidratação constante

---

### Protocolo: Recovery Pós-Treino 🏋️

**Objetivo:** Relaxamento muscular sem perda de consciência

**Blend:**
- 60% Híbrida
- 30% Hortelã (anti-inflamatório)
- 10% Eucalipto (respiração)

**Temperatura:**
- 180-190°C

**Timing:**
- 30-45min após treino
- Após hidratação e refeição pós-treino

**Ritual:**
- Alongamento passivo
- Banho frio/contraste
- Sessão
- Foam roller ou auto-massagem

---

## 5. Sistema de Análise Pessoal

### Perguntas Semanais (Domingo à noite)

**Padrões da semana:**
1. Quantas vezes vaporizei? (Meta pessoal: _____)
2. Qual foi minha intenção predominante?
3. Média de alinhamento (intenção vs resultado): _____%
4. Houve escalada de dose ou frequência?
5. Identifiquei algum gatilho emocional?
6. Usei botânicos para diluir? (Sim/Não)
7. Fiz alguma pausa intencional (1+ dia)? (Sim/Não)

**Insights:**
- O que funcionou bem esta semana?
- O que quero ajustar na próxima?
- Algum padrão preocupante? (fuga, compulsão)

### Gráficos Manuais (se usar planilha)

**Gráfico 1: Frequência Semanal**
- Eixo X: Semanas
- Eixo Y: Número de sessões
- Meta: Identificar picos e tendências

**Gráfico 2: Alinhamento Médio**
- Acompanhar se estou melhorando na escolha de protocolos
- Meta: >75% sustentado = autonomia

**Gráfico 3: Intenções Predominantes**
- Pizza chart: Medicinal, Recreativo, Espiritual, Fuga
- Meta: Reduzir "Fuga" ao longo do tempo

---

## 6. Estrutura de Inventário Unificado e Rico

Para maximizar o poder dos links do Obsidian, o inventário será centralizado em um único arquivo (`Inventario-Geral.md`). Isso permite linkar diretamente para seções específicas (ex: `[[Inventario-Geral#Lemon Haze]]`) dentro das sessões e protocolos.

**Arquivo: `Inventario/Inventario-Geral.md`**

```markdown
# Inventário Geral

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
```

---

## 7. Protocolos Gerados e Linkagem

Quando o Agente (ou você) criar um novo protocolo, ele deve ser salvo em `Protocolos/` e fazer referência explícita aos itens do inventário.

**Exemplo: `Protocolos/Foco-Zen.md`**

```markdown
# Protocolo: Foco Zen

**Objetivo:** Trabalho criativo sem ansiedade.

## 🛠️ Setup Necessário
- **Erva:** [[Inventario-Geral#Lemon Haze]] (ou qualquer Sativa rica em Limoneno)
- **Botânico:** [[Inventario-Geral#Alecrim]] (Opcional para memória)
- **Dispositivo:** [[Inventario-Geral#XMAX V3 Pro]]
- **Modo Sugerido:** "Sessão 6min" (Baixa temperatura)

## 🌡️ Ciclo de Temperaturas
![[prot-foco-temp.jpg|right|300]]

1. **00:00 - 02:00:** 170°C (Sabor e Terpenos)
2. **02:00 - 04:00:** 180°C (Foco mental)
3. **04:00 - 06:00:** Manter 180°C (Não subir para evitar sedação)

## 🌬️ Respiração
![[prot-resp-box.gif|left|150]]
Utilize a **Respiração Quadrada (Box Breathing)** durante o aquecimento do aparelho.
```

---

## 8. Padrão de Imagens e Anexos

Para manter o Vault organizado e visualmente rico sem poluição.

### 8.1. Configuração Global (Obsidian)
1. Acesse **Configurações > Arquivos e Links**.
2. Em **Local padrão para novos anexos**, selecione: `Na subpasta abaixo da pasta atual`.
3. Em **Nome da subpasta**, digite: `_anexos`.

### 8.2. Nomenclatura e Localização

| Contexto | Pasta Local | Prefixo | Exemplo | Objetivo |
| :--- | :--- | :--- | :--- | :--- |
| **INVENTÁRIO** | `Inventario/_anexos/` | `inv-` | `inv-flor-lemon-macro.jpg` | Comparar tricomas, registrar rótulos, setups de devices. |
| **SESSÕES** | `Sessoes/_anexos/` | `sess-` | `sess-20250128-residuo.jpg` | Analisar eficiência da extração (cor do AVB), registrar o "Set & Setting". |
| **PROTOCOLOS** | `Protocolos/_anexos/` | `prot-` | `prot-sono-temp.jpg` | Gráficos de curva de temperatura, GIFs de respiração, âncoras visuais. |
| **PERFIL** | `Perfil/_anexos/` | `perf-` | `perf-exame-jan25.pdf` | Exames médicos, referências pessoais. |

### 8.3. Exibição Limpa (Snippet Visual)

Use a sintaxe de pipe `|` para redimensionar e alinhar, criando um visual de "Enciclopédia".

```markdown
![[nome-do-arquivo.jpg|right|250]]
```
*A imagem flutua à direita com 250px de largura, permitindo que o texto flua ao lado dela.*

---

## 9. Sistema de Diário Pessoal (Obsidian + Closed-Loop)

### 9.1. Estrutura do Diário

**Arquivo diário:** `Diario-YYYY-MM-DD.md`

```yaml
---
tipo: diario
data: 2025-01-21

# Estado Geral
humor: 7
energia: 6
ansiedade: 3

# Produtividade
horas_foco: 6.5
tarefas_concluidas: 8
qualidade_trabalho: 4

# Saúde
horas_sono: 7.5
qualidade_sono: 4
treino_realizado: true
dor_nivel: 2

# Social
interacoes_sociais: 5
qualidade_relacoes: 4

# Reflexões
reflexao: "Hoje foi um bom dia. Consegui focar no trabalho e ainda treinar."
---

# Dia: 2025-01-21

## 📊 Resumo do Dia

**Trabalho:**
- Consegui focar bem pela manhã
- Tarde foi mais difícil (reunião chata às 15h)

**Treino:**
- Calistenia 45min - bom

**Observações:**
- Dormi bem ontem depois da sessão com lavanda
- Acordei sem groguice
```

**Sincronização com banco:**

O mesmo ETL que processa sessões também processa essas métricas:

```python
# Adicionar ao etl_obsidian_to_db.py
def extract_life_metrics(vault_path):
    """Extrai métricas de vida dos diários"""
    metrics = []
    
    for md_file in vault_path.rglob("Diario-de-Vida-*.md"):
        with open(md_file, 'r', encoding='utf-8') as f:
            post = frontmatter.load(f)
            if post.metadata.get('tipo') == 'metrica_vida':
                metrics.append(post.metadata)
    
    return metrics
```

---

## 10. Próximos Passos Imediatos

### Configuração Inicial (Automatizada)

**Fase 1: Setup do Obsidian (Via Script)**
1. Execute o script de automação para criar pastas e templates:
   ```bash
   python Scripts/setup_obsidian.py
   ```
   *Isso criará a estrutura `MeuVapoMind/` com todas as pastas `_anexos`, o `Inventario-Geral.md` e o `template-sessao.md`.*

2. **Instalação Manual de Plugins (Obsidian):**
   - Abra o Obsidian e selecione "Open folder as vault" apontando para a pasta `MeuVapoMind` criada.
   - Vá em `Settings > Community Plugins > Turn on`.
   - Instale e habilite: **Templater**, **Calendar**, **Dataview**, **Periodic Notes**.
   - **Configuração do Templater:** Em `Settings > Templater`, aponte a "Template folder location" para `Sessoes/_templates`.

**Fase 2: Setup do Backend**
- [ ] Instalar Python 3.10+ e dependências:
  ```bash
  pip install sqlite3 pandas python-frontmatter pyyaml
  ```
- [ ] Criar pasta `Scripts/` e `Data/`
- [ ] Copiar scripts: `etl_obsidian_to_db.py`, `detect_open_loops.py`
- [ ] Rodar primeira extração (mesmo que vazia)

**Fase 3: Primeiro Ciclo Completo**
- [ ] Registrar 3 sessões com check-in completo
- [ ] Preencher check-out de pelo menos 1 delas
- [ ] Rodar ETL e verificar dados no banco
- [ ] Rodar script de detecção de pendências

**Fase 4: Dashboard (Opcional - depois de 10+ sessões)**
- [ ] Instalar Streamlit: `pip install streamlit plotly`
- [ ] Criar `dashboard.py` básico
- [ ] Rodar e explorar visualizações

### Primeira Semana
- [ ] Registrar TODAS as sessões (mesmo incompletas)
- [ ] Rodar ETL 1x por dia
- [ ] Identificar 1 gatilho emocional nos dados

### Primeiro Mês
- [ ] Preencher métricas de vida pelo menos 3x/semana
- [ ] Rodar análise de impacto
- [ ] Criar 1 protocolo próprio baseado nos dados
- [ ] Completar primeiro relatório mensal

---

**MeuVapoMind não é um produto. É um espelho.**

Quanto mais honesto eu for nos registros, mais aprendo sobre mim mesmo.  
Quanto mais intencional eu for nas sessões, menos automático fico.  
Quanto mais observo padrões, mais livre me torno.

**A arquitetura técnica existe para servir o autoconhecimento, não o contrário.**

---

**Última atualização:** Janeiro 2025  
**Versão:** 2.0 - Arquitetura Obsidian-Centric + ETL  
**Autor:** Eu (para mim)
