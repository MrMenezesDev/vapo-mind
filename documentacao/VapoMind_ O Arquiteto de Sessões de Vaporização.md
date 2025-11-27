# **VapoMind: O Arquiteto de Sessões de Vaporização**

## **1\. Visão Geral do Produto**

O **VapoMind** é um assistente inteligente multiplataforma (Web/PWA, WhatsApp, Telegram, Instagram) projetado para usuários de vaporizadores de ervas.  

O sistema atua como um **Mentor Adaptativo e Arquiteto de Sessões**, integrando:

- **Gerenciamento técnico** de inventários e protocolos de temperatura
- **Inteligência Comportamental Modular:** Um sistema configurável que se adapta às crenças, práticas físicas e filosofia de vida do usuário (seja ele cristão, ateu, praticante de calistenia, lutador ou yogi), utilizando suas próprias subjetividades como ponte para a educação
- **Educação Canábica em Dois Eixos:**
  - **Prevenção de Uso Abusivo:** Identificação de gatilhos e padrões de dependência
  - **Orientação de Uso Consciente:** Transformação do consumo recreativo autômato em uso intencionado e ritualístico

**Propósito Central:** Aplicar uma **Pedagogia da Autonomia** (inspirada em Paulo Freire), onde o sistema dialoga com o universo cultural do usuário para guiá-lo em um uso **intencionado**, reduzindo a dependência da combustão e promovendo bem-estar.

A aplicação gerencia o inventário de ervas (cannabis e botânicos), concentrados e equipamentos do usuário para gerar **Protocolos de Sessão Personalizados** baseados em objetivos específicos (dormir, foco, treino, intimidade), utilizando lógica de temperatura, tipos de aquecimento (convecção/condução) e sinergia de terpenos.

**Diferencial Educacional:** O VapoMind atua em dois eixos complementares:
1. **Prevenção de Uso Abusivo:** Identifica padrões problemáticos e sugere alternativas
2. **Orientação de Uso Consciente:** Quando o uso é escolhido, maximiza benefícios e minimiza riscos

**Adaptabilidade:** A inteligência comportamental é configurável através de um **Motor de Contexto Modular** que carrega diferentes módulos de fé/filosofia (Cristianismo, Budismo, Estoicismo, Secular) e práticas corporais (Yoga, Lutas, Musculação, Calistenia, Corrida, Dança), ajustando linguagem, metáforas e referências para cada usuário.

## **2\. Arquitetura do Sistema (Omnichannel)**

A aplicação funcionará no modelo **API-First**. O "Cérebro" (Backend \+ IA + Motor Modular) é centralizado, e os canais são apenas interfaces de comunicação.

### **Núcleo (Backend)**

* **Gerenciador de Perfis:** Armazena dados do usuário, tolerância, dispositivos e módulos comportamentais ativos.  
* **Gerenciador de Inventário:** Banco de dados do que o usuário tem em mãos.  
* **Motor de Protocolos (AI Engine):** O algoritmo que cruza *Dispositivo* \+ *Inventário* \+ *Objetivo* \+ **Módulos Ativos** para gerar o passo a passo personalizado.
* **Motor de Contexto Modular:** Sistema que carrega e combina módulos de fé/filosofia e práticas corporais para adaptar a comunicação.

### **Canais de Acesso (Frontends)**

1. **Web App (PWA):** Interface visual rica, dashboard de inventário, histórico de sessões.  
2. **Chatbots (WhatsApp/Telegram/Instagram):** Interface conversacional. O usuário manda "Quero dormir" e o bot responde com o protocolo baseado no que ele já sabe que o usuário tem.

## **3\. Funcionalidades Principais**

### **3.1. Onboarding e Perfil (O "Setup" + Mapeamento Freiriano)**

No primeiro acesso, além do perfil técnico, o sistema realiza a "Sondagem" de subjetividades para adaptar linguagem e protocolos:

- Perfil Técnico: Dispositivos, Tolerância, Sensibilidade, Acessórios
- Eixo Físico: Levanto peso, Luto (Jiu-Jitsu/Muay Thai), Calistenia/Rua, Corro/Pedalo, Yoga/Alongamento, Sedentário buscando movimento
  - Metáforas aplicadas: séries/rounds/km/asanas
- Eixo Filosófico/Espiritual: Cristão/Evangélico, Espírita/Umbandista, Cético/Científico, Filosofia Oriental, Agnóstico
  - Ritual e linguagem: Oração/Gratidão, Mindfulness/Foco, Caminho do meio, Evidências
- Eixo de Intenção: Medicinal, Recreativo, Espiritual, Criativo, Fuga/Ansiedade
  - Direciona prevenção (alertas, respiração, T-Break) e uso consciente (temperatura/blend/técnica)

### **3.2. Gerenciamento de Inventário (A "Despensa")**

O usuário pode adicionar/remover itens. O sistema deve categorizá-los:

* **Flores (Strains):** Nome (ex: Skunk Wolf), Tipo (Indica/Sativa/Híbrida \- IA pode preencher isso).  
* **Botânicos:** Lavanda, Camomila, Hortelã, Sálvia, Lúpulo, Damiana.  
* **Concentrados:** Dry Ice, Rosin, BHO, Ice-O-Lator.  
* **Acessórios:** Cápsulas de dosagem, Bubblers (importante para permitir temps mais altas).

### **3.3. O Motor de Protocolos (O "Alquimista")**

Esta é a *core feature*. O usuário seleciona um "Modo":

* 💤 **Dormir / Sedação**  
* 🧘 **Meditação / Ansiedade**  
* ⚡ **Foco / Trabalho**  
* 🏋️ **Pré-Treino / Energia**  
* ❤️ **Intimidade / Sensorial**  
* 🚀 **Recreativo / Chapar**

**Saída do Sistema:** O sistema gera um card (imagem ou texto formatado) contendo:

1. **O Blend:** Proporções exatas (ex: 70% Skunk, 30% Hortelã).  
2. **Montagem:** Instruções específicas (ex: "Faça um sanduíche com o Dry Ice").  
3. **Ciclo de Temperatura:** (ex: 4 min a 180°C \-\> 2 min a 220°C).  
4. **Técnica de Puxada:** (ex: "Lenta e longa" ou "Curta e rápida").

### **3.4. Check-in/Check-out Intencional (MVP)**

Funcionalidade para o usuário relatar seu estado antes e depois da sessão, permitindo autoavaliação e ajuste fino dos protocolos.

**Entrada (Check-in):** O usuário descreve brevemente sua atividade anterior, estado emocional e intenção.

**Saída (Check-out):** O sistema fornece feedback sobre o alinhamento entre a intenção e o resultado percebido, com sugestões de ajuste.

### **3.5. Agente Holístico (Premium)**

Um assistente pessoal que guia o usuário através de sessões de vaporização, oferecendo:

- **Suporte Proativo:** Sugestões de uso baseadas em eventos da vida do usuário (ex: "Você tem um aniversário hoje, que tal um blend relaxante?").
- **Educação Contínua:** Informações sobre os efeitos de diferentes cepas e técnicas de vaporização.
- **Ajustes Dinâmicos:** Modificação automática dos protocolos com base no feedback em tempo real do usuário.

#### Modo SOS (Ancoragem Imediata)
- Detecção: análise de sentimento identifica pânico, paranóia ou sofrimento agudo (bad trip)
- Ação: agente abandona persona (xamã/cientista) e assume tom neutro, diretivo e calmante
- UI: alto contraste com instruções visuais simples (ex: gif de respiração sincronizada)
- Suporte: áudio guiado automático de aterramento sugerido
- Contenção: bloqueio temporário de sugestões de novas sessões
- Pós-evento: check-in de segurança 20–60min depois e plano breve de prevenção

## **4\. Fluxo de Usuário (User Journey)**

### **Cenário: Via WhatsApp**

1. **Usuário:** *Envia comando "/inventario"*  
2. **Bot:** "Seu estoque atual: Skunk Wolf, Lavanda, Dry Ice. Deseja adicionar algo?"  
3. **Usuário:** "Sim, comprei Sálvia."  
4. **Bot:** "Sálvia adicionada\! 🌿"  
5. **Usuário:** "Preciso acordar e trabalhar."  
6. **Bot (Processando):** Verifica que ele tem Sálvia (Foco) \+ Skunk (Base) \+ V3 Pro.  
7. **Bot:** Envia o **Protocolo "Bom Dia Vietnã"**:  
   * *Mistura:* 50% Skunk \+ 50% Sálvia.  
   * *Temp:* Máximo 185°C.  
   * *Dica:* Beba água antes.

## **5\. Modelo de Dados (Estrutura Simplificada)**

`// User Profile`  
`{`  
  `"user_id": "12345",`  
  `"name": "Alex",`  
  `"tolerance": "medium",`  
  `"devices": ["XMAX V3 Pro", "Dynavap M"],`  
  `"preferences": ["no_combustion", "sensitive_throat"]`  
`}`

`// Inventory`  
`{`  
  `"user_id": "12345",`  
  `"herbs": [`  
    `{"name": "Skunk Wolf", "type": "hybrid_flower"},`  
    `{"name": "Peppermint", "type": "botanical"},`  
    `{"name": "Sage", "type": "botanical"}`  
  `],`  
  `"concentrates": [`  
    `{"name": "Dry Sift", "potency": "high"}`  
  `]`  
`}`

`// Protocol Template (Logic)`  
`{`  
  `"goal": "focus",`  
  `"forbidden_ingredients": ["Lavender", "Chamomile"],`  
  `"recommended_ingredients": ["Sage", "Mint", "Pinene_Strains"],`  
  `"max_temp": 185,`  
  `"heating_mode": "session_short"`  
`}`

`// Session Log Simplificado (MVP)`  
`{`  
  `"session_id": "uuid",`  
  `"timestamp": "2025-11-27T18:30:00Z",`  
  `"protocol": "Bom_Dia_Vietna",`  
  `"check_in": {`  
    `"atividade_antes": "acabei de acordar",`  
    `"mood_score": 5,`  
    `"mood_tags": ["sonolento"],`  
    `"intenção_tipo": "Foco",`  
    `"estado_desejado": ["alerta", "hidratado"]`  
  `},`  
  `"check_out": {`  
    `"mood_score_final": 7,`  
    `"estado_percebido": ["mais alerta"],`  
    `"alinhamento_com_estado_desejado": 70,`  
    `"urge_redosagem": false`  
  `}`  
`}`

## **6\. Stack Tecnológica Sugerida**

* **Backend:** Python (FastAPI ou Flask). Python é essencial para integrar facilmente com bibliotecas de LLM (LangChain).  
* **Database:** PostgreSQL (Relacional para usuários) ou Firebase (NoSQL para inventários flexíveis e tempo real).  
* **IA / Lógica:** Gemini API ou OpenAI API.  
  * *Uso:* Interpretar "Skunk Wolf" e saber que ela tem Mirceno, sem precisar de um banco de dados manual de 10.000 strains.  
* **Frontend Web:** React.js ou Vue.js (PWA).  
* **Integração de Mensageria:**  
  * **Twilio** ou **Meta Business API** (WhatsApp).  
  * **Telegram Bot API** (Gratuito e fácil).  
  * **ManyChat** ou API direta (Instagram).

- Segurança de Chaves (BYOK):
  - API Keys nunca expostas no frontend
  - Armazenamento cifrado (AES-256) no banco
  - Descriptação apenas durante a requisição no backend (FastAPI) e descarte imediato em memória

## **7\. Diferenciais Competitivos**
1. Motor de Contexto Modular: Protocolos e linguagem adaptados a fé/filosofia + prática corporal + intenção.
2. Onboarding Freiriano (Mapeamento multi-eixo): Não pergunta só “o que você usa”, mas “quem você é”.
3. Check-in/Check-out Intencional (MVP já preparado para expansão): Estado desejado + atividade anterior + alinhamento.
4. Uso Estruturado de Botânicos: Modulação da brisa + diluição consciente da carga de THC.
5. Prevenção Ativa Antecipatória: Alertas antes da escalada (gatilhos emocionais + padrão de redosagem).
6. Acessibilidade Cultural: Remove estética “stoner” para usuários conservadores/religiosos.
7. Ajuste Profundo por Dispositivo: Curvas térmicas diferentes por convecção, condução, híbridos.
8. Multicanal Simples: Mesmo “cérebro” servindo Web, WhatsApp, Telegram, Instagram.
9. Linguagem Contextual Dinâmica: System Prompts gerados a partir dos eixos do usuário.
10. Dados Estruturados para Insight Longitudinal: Alinhamento (%) entre intenção e resultado.
11. SOS Kill Switch: protocolo de ancoragem imediata com UI diretiva e bloqueio de redosagem automática.

## **8\. Próximos Passos (Roadmap MVP)**
1. **Fase 1 (O Cérebro):** Criar o prompt do sistema (System Prompt) que recebe os inputs e devolve o protocolo. Testar manualmente.  
2. **Fase 1.1 (Calibração):** Nas 5 primeiras sessões, sugerir 10–15% menos temperatura/potência e coletar feedback para calibra