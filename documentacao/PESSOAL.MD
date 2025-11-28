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

**Estrutura de Vault:**

```
MeuVapoMind/
├── 📁 Perfil/
│   └── meu-perfil.md
├── 📁 Inventario/
│   ├── flores.md
│   ├── botanicos.md
│   └── dispositivos.md
├── 📁 Protocolos/
│   ├── sono-profundo.md
│   ├── foco-criativo.md
│   └── recovery-pos-treino.md
├── 📁 Sessoes/
│   ├── 2025/
│   │   ├── 2025-01/
│   │   │   ├── 2025-01-15-sessao-22h30.md
│   │   │   └── 2025-01-20-sessao-21h00.md
│   │   └── 2025-02/
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

Cada nota de sessão usa **Properties/Frontmatter** para dados estruturados e corpo Markdown para reflexões qualitativas.

```markdown
---
# Metadados Estruturados (Extraíveis pelo ETL)
tipo: sessao
data: 2025-01-20
hora_inicio: "22:30"
status: aberta  # aberta | fechada | pendente_checkout

# Check-in
atividade_antes: estudo
mood_pre: 4
mood_tags_pre: [mente_acelerada, tensao_ombros]
intencao_tipo: medicinal
estado_desejado: [calmo, sono_profundo]
expectativa: "Desacelerar pensamentos sem ficar grogue"

# Protocolo
blend: "60% Skunk + 30% Lavanda + 10% Camomila"
temperatura_inicial: 185
temperatura_final: 200
dispositivo: "V3 Pro"
acessorio: bubbler
ritual_pre: "5min respiracao 4-7-8"

# Check-out (preenchido depois - pode ficar vazio inicialmente)
hora_checkout: ""
mood_pos: null
mood_tags_pos: []
alinhamento: null
vontade_redosar: null
reflexao_curta: ""

# Metadados de Análise
gatilho_detectado: false
tipo_gatilho: ""
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
```

### Exemplo Preenchido

```markdown
# Sessão: 2025-01-20 | 22:30

## PRÉ-SESSÃO

**O que eu fiz antes:**
- Atividade: Estudei 4h para certificação, cabeça quente
- Estado emocional: 4/10 (cansado, ansioso)
- Tags: [mente acelerada, tensão nos ombros]

**Minha Intenção:**
- Tipo: Medicinal + Fuga/Ansiedade (honestidade)
- Estado desejado: Desacelerar pensamentos, relaxar ombros, dormir bem
- Expectativa: Conseguir desligar sem ficar grogue amanhã

**Protocolo:**
- Blend: 60% Skunk Wolf + 30% Lavanda + 10% Camomila
- Temperatura: 185°C (primeira sessão) → 200°C (segunda)
- Dispositivo: XMAX V3 Pro com bubbler
- Ritual: 5min de respiração 4-7-8 + alongamento de ombro

---

## DURANTE

**Observações:**
- Sabor: Floral no início (lavanda), depois terroso
- Sensações: Relaxamento começou nos ombros, depois desceu
- Pensamentos: Menos looping, consegui "assistir" os pensamentos passarem
- Harshness: 2/10 (bubbler ajudou muito)

---

## PÓS-SESSÃO (23:45)

**Estado final:**
- Humor: 7/10 (relaxado, sonolento)
- Tags: [calmo, corpo pesado, mente clara]
- Alinhamento: 85%

**Reflexão:**
- Aprendi: Lavanda + camomila juntas = knockout, mas preciso usar ANTES de 22h se quiser acordar bem
- Vontade de redosar: Não (isso é progresso!)
- Próxima ação: Banho morno + cama

**Análise:**
- Intenção cumprida? Totalmente
- Dose: Ideal (talvez até 10% menos lavanda)
- Temperatura: 185°C foi perfeito, 200°C ficou muito forte

---

## TAGS
#intenção-medicinal #dispositivo-v3pro #blend-lavanda-camomila #resultado-85
```

---

## 6. Protocolos Pessoais (Templates)

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

## 7. Sistema de Análise Pessoal

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

## 8. Calibração Pessoal de Tolerância

### Primeiras 5 Sessões

**Regra de Ouro:**
Começar com **10-15% menos** do que acho que preciso

**Registro:**
| Sessão | Dose/Temp | Alinhamento | Harshness | Notas |
|--------|-----------|-------------|-----------|-------|
| 1 | 0.1g / 175°C | 60% | 3/10 | Pouco efeito, mas suave |
| 2 | 0.12g / 180°C | 75% | 4/10 | Melhor, mas ainda leve |
| 3 | 0.15g / 185°C | 85% | 5/10 | Sweet spot! |
| 4 | 0.15g / 185°C | 80% | 5/10 | Confirmado |
| 5 | 0.18g / 190°C | 70% | 7/10 | Excessivo, voltar |

**Conclusão:**
Minha dose ideal atual: **0.15g a 185°C**

---

## 9. Modo SOS (Protocolo de Ancoragem)

### Se eu entrar em pânico/paranóia:

**PARE. RESPIRE. ANCORE.**

**Passo 1: Reconhecer**
- "Estou em bad trip. Isso é temporário. Vai passar."

**Passo 2: Respiração 4-7-8 (Repetir 5x)**
- Inspire (nariz): 4 segundos
- Segure: 7 segundos
- Expire (boca): 8 segundos

**Passo 3: Aterramento Físico**
- Toque 5 objetos ao redor
- Diga seus nomes em voz alta
- Água gelada no rosto

**Passo 4: Áudio Guiado**
- [Link para meditação de emergência salva]
- Ou música conhecida e confortável

**Passo 5: Registro Pós-Crise**
- O que desencadeou? (dose? contexto? emoção?)
- Protocolo de prevenção para próxima vez

**BLOQUEIO:**
Não vaporizar novamente nas próximas 24-48h. Refletir primeiro.

---

## 10. Jornada de Autonomia (Gamificação Pessoal)

Não preciso de badges ou pontos externos. Minha progressão é interna:

### 🌱 Aprendiz (Primeiros 30 dias)
- **Foco:** Conhecer meu corpo e tolerância
- **Meta:** Completar 15 sessões com check-in/check-out completo
- **Aprendizado:** Temperatura ideal, blends que funcionam, gatilhos

### 🧪 Praticante (Meses 2-4)
- **Foco:** Refinar e experimentar
- **Meta:** Alinhamento médio >70%
- **Aprendizado:** Criar 3 protocolos próprios, identificar padrões semanais

### ⚗️ Artífice (Meses 5-12)
- **Foco:** Maestria e prevenção
- **Meta:** Alinhamento >80%, redução de 20% no consumo total via botânicos
- **Aprendizado:** Completar 1 T-Break de 7 dias, ajudar alguém (se aplicável)

### 🔮 Mestre (Ano 2+)
- **Foco:** Autonomia total
- **Meta:** Não preciso mais do sistema para decidir, só para registrar
- **Aprendizado:** Uso intencional 95% do tempo, sem padrões compulsivos

---

## 11. Princípios Éticos Pessoais

### Honestidade Radical
- Registrar a verdade, mesmo quando for "uso por fuga"
- O diário não julga, eu aprendo

### Não-Julgamento
- Recaídas fazem parte do processo
- O objetivo é progresso, não perfeição

### Curiosidade Científica
- Cada sessão é um experimento
- Coletar dados sem apego emocional ao resultado

### Respeito à Planta
- Cannabis é uma ferramenta, não uma muleta
- Uso com gratidão e propósito

---

## 12. Recursos e Referências Pessoais

### Leituras Fundamentais
- "Pedagogia da Autonomia" - Paulo Freire
- "The Psychedelic Explorer's Guide" - James Fadiman
- "How to Change Your Mind" - Michael Pollan

### Ferramentas Úteis
- **Obsidian:** Para sistema de notas vinculadas
- **Notion:** Alternativa visual para diário
- **Google Sheets:** Análises automáticas
- **Insight Timer:** Meditações guiadas

### Comunidades (Opcional)
- r/vaporents (Reddit)
- Grupos de Redução de Danos

---

## 13. Modelo de Dados e Métricas de Impacto

### 13.1. Schema Expandido (SQLite)

**Além das tabelas já descritas na seção 3.3, adicionamos:**

```sql
-- Tabela de métricas de vida (para cruzamento)
CREATE TABLE metricas_vida (
    id INTEGER PRIMARY KEY,
    data DATE UNIQUE,
    
    -- Produtividade
    horas_foco REAL,
    tarefas_concluidas INTEGER,
    qualidade_trabalho INTEGER CHECK(qualidade_trabalho BETWEEN 1 AND 5),
    
    -- Saúde
    horas_sono REAL,
    qualidade_sono INTEGER CHECK(qualidade_sono BETWEEN 1 AND 5),
    treino_realizado BOOLEAN,
    dor_nivel INTEGER CHECK(dor_nivel BETWEEN 0 AND 10),
    
    -- Bem-estar geral
    humor_geral INTEGER CHECK(humor_geral BETWEEN 0 AND 10),
    ansiedade_nivel INTEGER CHECK(ansiedade_nivel BETWEEN 0 AND 10),
    energia_nivel INTEGER CHECK(energia_nivel BETWEEN 0 AND 10),
    
    -- Social
    interacoes_sociais INTEGER,
    qualidade_relacoes INTEGER CHECK(qualidade_relacoes BETWEEN 1 AND 5),
    
    -- Notas
    observacoes TEXT,
    registrado_em DATETIME
);

-- Tabela de eventos de vida (para análise de gatilhos)
CREATE TABLE eventos_vida (
    id INTEGER PRIMARY KEY,
    data DATE,
    tipo TEXT,  -- 'trabalho' | 'conflito' | 'celebracao' | 'perda' | 'estresse'
    descricao TEXT,
    intensidade INTEGER CHECK(intensidade BETWEEN 1 AND 5),
    registrado_em DATETIME
);

-- View de correlação: Uso vs Vida
CREATE VIEW vw_impacto_vida AS
SELECT 
    m.data,
    m.humor_geral,
    m.qualidade_sono,
    m.horas_foco,
    COUNT(s.id) as sessoes_dia,
    AVG(s.alinhamento) as alinhamento_medio,
    SUM(CASE WHEN s.intencao_tipo = 'Fuga/Ansiedade' THEN 1 ELSE 0 END) as sessoes_fuga
FROM metricas_vida m
LEFT JOIN sessoes s ON DATE(s.data) = m.data
GROUP BY m.data;
```

### 13.2. Métricas de Impacto Real na Vida

**Pergunta Central:** "O VapoMind está melhorando minha vida ou só gerando dados?"

**Métricas Implementadas:**

#### A. Métricas de Processo (O que você controla)

1. **Taxa de Fechamento de Loops**
   ```sql
   SELECT 
       COUNT(CASE WHEN is_incomplete = FALSE THEN 1 END) * 100.0 / COUNT(*) as taxa_completas
   FROM sessoes
   WHERE data >= date('now', '-30 days');
   ```
   - Meta: >80% de sessões com check-out completo

2. **Alinhamento Médio Mensal**
   ```sql
   SELECT 
       strftime('%Y-%m', data) as mes,
       AVG(alinhamento) as alinhamento_medio,
       COUNT(*) as num_sessoes
   FROM sessoes
   WHERE alinhamento IS NOT NULL
   GROUP BY mes
   ORDER BY mes;
   ```
   - Meta: Tendência crescente ao longo dos meses

3. **Taxa de Uso Intencional vs Escapismo**
   ```sql
   SELECT 
       intencao_tipo,
       COUNT(*) as quantidade,
       COUNT(*) * 100.0 / SUM(COUNT(*)) OVER() as percentual
   FROM sessoes
   WHERE data >= date('now', '-30 days')
   GROUP BY intencao_tipo;
   ```
   - Meta: Reduzir "Fuga/Ansiedade" abaixo de 20%

#### B. Métricas de Resultado (O impacto na vida real)

4. **Correlação: Uso vs Qualidade do Sono**
   ```sql
   SELECT 
       CASE 
           WHEN sessoes_dia = 0 THEN 'Sem uso'
           WHEN sessoes_dia = 1 THEN '1 sessão'
           ELSE '2+ sessões'
       END as frequencia,
       AVG(qualidade_sono) as sono_medio,
       AVG(humor_geral) as humor_medio
   FROM vw_impacto_vida
   WHERE data >= date('now', '-60 days')
   GROUP BY frequencia;
   ```
   - Análise: Identificar se há relação positiva, negativa ou neutra

5. **Delta de Produtividade (Dias com uso vs sem uso)**
   ```sql
   SELECT 
       CASE WHEN sessoes_dia > 0 THEN 'Com uso' ELSE 'Sem uso' END as grupo,
       AVG(horas_foco) as foco_medio,
       AVG(tarefas_concluidas) as tarefas_media,
       AVG(qualidade_trabalho) as qualidade_media
   FROM vw_impacto_vida
   WHERE horas_foco IS NOT NULL
     AND data >= date('now', '-60 days')
   GROUP BY grupo;
   ```
   - Pergunta: "Nos dias que uso, sou mais ou menos produtivo?"

6. **Análise de Gatilhos Emocionais**
   ```sql
   SELECT 
       s.atividade_antes,
       COUNT(*) as vezes,
       AVG(s.mood_pre) as humor_pre_medio,
       AVG(s.alinhamento) as alinhamento_medio,
       SUM(CASE WHEN s.intencao_tipo = 'Fuga/Ansiedade' THEN 1 ELSE 0 END) as sessoes_fuga
   FROM sessoes s
   WHERE s.data >= date('now', '-60 days')
   GROUP BY s.atividade_antes
   HAVING COUNT(*) >= 3
   ORDER BY sessoes_fuga DESC, vezes DESC
   ```
   - Identificar padrões: "Sempre vaporizo depois de reuniões?"

#### C. Métricas de Autonomia (Evolução do autoconhecimento)

7. **Precisão de Previsão (Expectativa vs Realidade)**
   ```sql
   SELECT 
       AVG(alinhamento) as precisao_media,
       strftime('%Y-%m', data) as mes
   FROM sessoes
   WHERE alinhamento IS NOT NULL
   GROUP BY mes
   ORDER BY mes;
   ```
   - Meta: Alinhamento aumentando = você está aprendendo a se conhecer

8. **Taxa de Redosagem**
   ```sql
   SELECT 
       strftime('%Y-%W', data) as semana,
       SUM(CASE WHEN vontade_redosar = TRUE THEN 1 ELSE 0 END) * 100.0 / COUNT(*) as taxa_redosagem
   FROM sessoes
   WHERE vontade_redosar IS NOT NULL
   GROUP BY semana
   ORDER BY semana;
   ```
   - Meta: Tendência decrescente = maior controle

### 13.3. Dashboard de Impacto de Vida

**Script adicional (`impact_metrics.py`):**

```python
# filepath: f:\repositorios\projetos\vapo-mind\MeuVapoMind\Scripts\impact_metrics.py
import sqlite3
import pandas as pd
from datetime import datetime, timedelta

DB_PATH = "../Data/vapomind.db"

def analise_impacto_vida():
    """Gera relatório de impacto do uso na qualidade de vida"""
    conn = sqlite3.connect(DB_PATH)
    
    print("=" * 60)
    print("📊 RELATÓRIO DE IMPACTO NA VIDA REAL")
    print("=" * 60)
    print()
    
    # 1. Correlação: Uso vs Sono
    print("💤 SONO")
    df_sono = pd.read_sql("""
        SELECT 
            CASE 
                WHEN sessoes_dia = 0 THEN 'Sem uso'
                WHEN sessoes_dia = 1 THEN '1 sessão'
                ELSE '2+ sessões'
            END as frequencia,
            AVG(qualidade_sono) as sono_medio,
            COUNT(*) as dias
        FROM vw_impacto_vida
        WHERE qualidade_sono IS NOT NULL
          AND data >= date('now', '-60 days')
        GROUP BY frequencia
    """, conn)
    
    if not df_sono.empty:
        print(df_sono.to_string(index=False))
        print()
        
        # Interpretação automática
        if len(df_sono) >= 2:
            sem_uso = df_sono[df_sono['frequencia'] == 'Sem uso']['sono_medio'].values
            com_uso = df_sono[df_sono['frequencia'] != 'Sem uso']['sono_medio'].mean()
            
            if len(sem_uso) > 0:
                delta = com_uso - sem_uso[0]
                if delta > 0.5:
                    print("✅ Seu sono parece MELHOR nos dias de uso")
                elif delta < -0.5:
                    print("⚠️ Seu sono parece PIOR nos dias de uso")
                else:
                    print("➡️ Uso parece NEUTRO para o sono")
                print()
    
    # 2. Produtividade
    print("⚡ PRODUTIVIDADE")
    df_prod = pd.read_sql("""
        SELECT 
            CASE WHEN sessoes_dia > 0 THEN 'Com uso' ELSE 'Sem uso' END as grupo,
            AVG(horas_foco) as foco_medio,
            AVG(tarefas_concluidas) as tarefas_media,
            COUNT(*) as dias
        FROM vw_impacto_vida
        WHERE horas_foco IS NOT NULL
          AND data >= date('now', '-60 days')
        GROUP BY grupo
    """, conn)
    
    if not df_prod.empty:
        print(df_prod.to_string(index=False))
        print()
    
    # 3. Gatilhos mais comuns
    print("🎯 GATILHOS IDENTIFICADOS")
    df_gatilhos = pd.read_sql("""
        SELECT 
            atividade_antes,
            COUNT(*) as vezes,
            AVG(mood_pre) as humor_pre,
            SUM(CASE WHEN intencao_tipo = 'Fuga/Ansiedade' THEN 1 ELSE 0 END) as sessoes_fuga
        FROM sessoes
        WHERE data >= date('now', '-60 days')
          AND atividade_antes IS NOT NULL
        GROUP BY atividade_antes
        HAVING COUNT(*) >= 3
        ORDER BY sessoes_fuga DESC, vezes DESC
        LIMIT 5
    """, conn)
    
    if not df_gatilhos.empty:
        print(df_gatilhos.to_string(index=False))
        print()
        
        # Alertas
        for _, row in df_gatilhos.iterrows():
            if row['sessoes_fuga'] / row['vezes'] > 0.5:
                print(f"⚠️ ALERTA: '{row['atividade_antes']}' é um gatilho forte de fuga ({row['sessoes_fuga']}/{row['vezes']} sessões)")
        print()
    
    # 4. Evolução de alinhamento
    print("📈 EVOLUÇÃO DE CONSCIÊNCIA")
    df_evolucao = pd.read_sql("""
        SELECT 
            strftime('%Y-%m', data) as mes,
            AVG(alinhamento) as alinhamento_medio,
            COUNT(*) as sessoes
        FROM sessoes
        WHERE alinhamento IS NOT NULL
        GROUP BY mes
        ORDER BY mes DESC
        LIMIT 6
    """, conn)
    
    if not df_evolucao.empty:
        print(df_evolucao.to_string(index=False))
        
        # Tendência
        if len(df_evolucao) >= 3:
            tendencia = df_evolucao['alinhamento_medio'].diff().mean()
            if tendencia > 2:
                print("\n✅ Tendência POSITIVA: Você está melhorando no autoconhecimento!")
            elif tendencia < -2:
                print("\n⚠️ Tendência NEGATIVA: Alinhamento caindo - revisar protocolos")
            else:
                print("\n➡️ Tendência ESTÁVEL: Mantendo consistência")
    
    print("\n" + "=" * 60)
    print("💡 PRÓXIMAS AÇÕES SUGERIDAS:")
    print("=" * 60)
    print("1. Se há gatilhos de fuga frequentes, considere alternativas (respiração, exercício)")
    print("2. Se sono está pior, experimente parar uso 2h antes de dormir")
    print("3. Se alinhamento está baixo, revise seus protocolos - eles ainda fazem sentido?")
    print()
    
    conn.close()

if __name__ == "__main__":
    analise_impacto_vida()
```

### 13.4. Registro de Métricas de Vida (Template Obsidian)

**Arquivo diário complementar: `Diario-de-Vida-YYYY-MM-DD.md`**

```yaml
---
tipo: metrica_vida
data: 2025-01-21

# Produtividade
horas_foco: 6.5
tarefas_concluidas: 8
qualidade_trabalho: 4

# Saúde
horas_sono: 7.5
qualidade_sono: 4
treino_realizado: true
dor_nivel: 2

# Bem-estar
humor_geral: 7
ansiedade_nivel: 3
energia_nivel: 6

# Social
interacoes_sociais: 5
qualidade_relacoes: 4
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

## 14. Próximos Passos Imediatos

### Configuração Inicial (2-3h)

**Fase 1: Setup do Obsidian**
- [ ] Criar estrutura de pastas no Vault
- [ ] Instalar plugins: Templater, Calendar, Dataview
- [ ] Criar template de sessão
- [ ] Testar criação de primeira nota de sessão

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
