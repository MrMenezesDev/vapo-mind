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

## 3. Arquitetura Simplificada

### Opção A: Sistema de Arquivos (Zero Código)
**Estrutura de Pastas:**
```
MeuVapoMind/
├── inventario/
│   ├── flores.md
│   ├── botanicos.md
│   ├── concentrados.md
│   └── dispositivos.md
├── protocolos/
│   ├── sono.md
│   ├── foco.md
│   ├── meditacao.md
│   └── custom/
├── diario/
│   ├── 2025/
│   │   ├── 01-janeiro/
│   │   │   ├── 2025-01-15.md
│   │   │   └── 2025-01-20.md
│   │   └── 02-fevereiro/
│   └── insights/
├── meu-perfil.md
└── aprendizados.md
```

### Opção B: Planilha Google Sheets / Excel
**Abas:**
1. **Perfil** - Meus eixos (prática física, espiritualidade, intenções)
2. **Inventário** - O que tenho disponível
3. **Protocolos** - Receitas personalizadas
4. **Diário de Sessões** - Check-in/Check-out
5. **Análises** - Gráficos automáticos de padrões

### Opção C: Aplicativo Local Simples (Python/Obsidian)
- Script Python com CLI para logging rápido
- Plugin Obsidian para vincular notas de sessões
- Base de dados SQLite local

---

## 4. Meu Perfil (Template de Autoconhecimento)

### 4.1. Eixos de Identidade

**Práticas Corporais:**
- [ ] Musculação
- [ ] Calistenia
- [ ] Artes Marciais (especificar: ______)
- [ ] Corrida/Cardio
- [ ] Yoga/Meditação
- [ ] Pular Corda
- [ ] Outra: ______

**Espiritualidade/Filosofia:**
- [ ] Cristianismo/Evangelicalismo
- [ ] Budismo/Tradições Orientais
- [ ] Xamanismo
- [ ] Secular/Científico
- [ ] Estoicismo
- [ ] Outra: ______

**Estilo de Aprendizado:**
- [ ] Visual (gráficos, imagens)
- [ ] Científico (dados, mecanismos)
- [ ] Metafórico (comparações, narrativas)
- [ ] Prático (tentativa e erro)

### 4.2. Minhas Intenções de Uso

**Por que vaporizo?** (Marcar todas que se aplicam)
- [ ] Reduzir/eliminar combustão (cigarro/baseado)
- [ ] Gerenciar ansiedade/stress
- [ ] Tratamento de dor crônica
- [ ] Melhorar sono
- [ ] Exploração criativa/espiritual
- [ ] Uso social/recreativo consciente
- [ ] Melhorar foco/TDAH
- [ ] Recovery pós-treino
- [ ] Outra: ______

**Padrões que quero observar:**
- [ ] Frequência de uso
- [ ] Gatilhos emocionais
- [ ] Redosagem compulsiva
- [ ] Alinhamento intenção vs resultado
- [ ] Economia de consumo
- [ ] Outro: ______

### 4.3. Meus Dispositivos

| Vaporizador | Tipo (Convecção/Condução) | Temperatura Máxima |
|-------------|---------------------------|-------------------|
| Exemplo: XMAX V3 Pro | Convecção | 220°C |
|  |  |  |

**Acessórios:**
- [ ] Bubbler/Bong
- [ ] Cápsulas de dosagem
- [ ] Filtro de água
- [ ] Outro: ______

---

## 5. Sistema de Diário Pessoal

### Template de Sessão (Markdown)

```markdown
# Sessão: [Data - YYYY-MM-DD] [Hora]

## PRÉ-SESSÃO (Check-in)

**O que eu fiz antes:**
- Atividade: (ex: trabalho, treino, discussão)
- Estado emocional: (0-10): 
- Tags de humor: [ansioso, cansado, eufórico, etc]

**Minha Intenção:**
- Tipo: [Medicinal | Recreativo | Espiritual | Criativo | Fuga/Ansiedade]
- Estado desejado: (ex: calmo, focado, sem dor)
- Expectativa: (o que espero sentir/alcançar)

**Protocolo Escolhido:**
- Blend: (ex: 70% Skunk + 30% Lavanda)
- Temperatura: 
- Dispositivo: 
- Ritual pré-sessão: (respiração, alongamento, oração, etc)

---

## DURANTE A SESSÃO

**Observações:**
- Sabor/aroma: 
- Sensações corporais: 
- Pensamentos: 
- Harshness/tosse: (0-10):

---

## PÓS-SESSÃO (Check-out - 30-60min depois)

**Estado final:**
- Humor (0-10): 
- Tags finais: 
- Estado percebido vs desejado: (%)

**Reflexão:**
- O que aprendi: 
- Vontade de redosar: [Sim/Não]
- Próxima ação: (hidratação, alongamento, dormir, trabalhar)

**Análise de alinhamento:**
- Intenção cumprida? [Totalmente | Parcialmente | Não]
- Dose adequada? [Pouca | Ideal | Excessiva]
- Temperatura ideal? [Sim | Muito alta | Muito baixa]

---

## TAGS PARA ANÁLISE FUTURA
#intenção-[tipo] #dispositivo-[nome] #blend-[composição] #resultado-[alinhamento]
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

## 13. Modelo de Dados Simplificado (Se eu criar app)

```json
{
  "perfil": {
    "praticas_corporais": ["musculacao", "yoga"],
    "espiritualidade": ["budismo"],
    "estilo_aprendizado": "cientifico",
    "intencoes": ["reducao_combustao", "ansiedade"]
  },
  "inventario": {
    "flores": [
      {"nome": "Skunk Wolf", "tipo": "hibrida", "quantidade": "3.5g"}
    ],
    "botanicos": [
      {"nome": "Lavanda", "quantidade": "10g"}
    ]
  },
  "sessoes": [
    {
      "data": "2025-01-20T22:30:00",
      "pre": {
        "atividade": "estudo",
        "mood": 4,
        "intencao": "medicinal",
        "estado_desejado": ["calmo", "sem_pensamento_acelerado"]
      },
      "protocolo": {
        "blend": "60% Skunk + 30% Lavanda + 10% Camomila",
        "temp": 185,
        "dispositivo": "V3 Pro"
      },
      "pos": {
        "mood": 7,
        "alinhamento": 85,
        "redosar": false,
        "reflexao": "Lavanda + camomila = knockout"
      }
    }
  ]
}
```

---

## 14. Próximos Passos Imediatos

### Configuração Inicial (1-2h)
- [ ] Escolher sistema (arquivos/planilha/app)
- [ ] Preencher "Meu Perfil"
- [ ] Fazer inventário atual
- [ ] Criar 2-3 protocolos base

### Primeira Semana
- [ ] Registrar todas as sessões (mesmo as "ruins")
- [ ] Testar diferentes temperaturas
- [ ] Identificar 1 gatilho emocional

### Primeiro Mês
- [ ] Análise semanal consistente
- [ ] Criar 1 protocolo próprio
- [ ] Experimentar 2 botânicos novos

---

**MeuVapoMind não é um produto. É um espelho.**

Quanto mais honesto eu for nos registros, mais aprendo sobre mim mesmo.  
Quanto mais intencional eu for nas sessões, menos automático fico.  
Quanto mais observo padrões, mais livre me torno.

---

**Última atualização:** Janeiro 2025  
**Versão:** 1.0 - Pessoal  
**Autor:** Eu (para mim)
