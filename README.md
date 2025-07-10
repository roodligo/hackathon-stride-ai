
# STRIDE IA – Modelagem de Ameaças a partir de Diagramas de Arquitetura

## Objetivo
Analisar automaticamente **diagramas de arquitetura de software (AWS, Azure, Oracle, etc)** e gerar um **Relatório de Ameaças STRIDE** com base em visão computacional.

---

## Pipeline Inteligente
1. **YOLOv8** detecta os componentes na imagem
2. **Interpretação automática** (sem OCR ou mapeamento externo)
3. **Geração de grafo dinâmico de conexões**
4. **Aplicação da metodologia STRIDE**
5. **Relatório completo com imagem, ameaças e contramedidas**

---

## Tecnologias Utilizadas
- Python 3.12.6
- [Ultralytics YOLOv8](https://docs.ultralytics.com/)
- OpenCV
- EasyOCR (apenas para etapa opcional de análise híbrida)
- NetworkX + Matplotlib (grafo)
- FPDF (relatório PDF)
- Streamlit (interface web)

---

## Estrutura de Pastas
```
hackathon-stride-ai/
├── dataset/
│   └── images/test/            # Imagens de entrada
├── models/                     # Modelo base YOLOv8
├── outputs/                    # Saídas (em uso futuro)
├── runs/
│   ├── detect/                 # Imagens de predição YOLO
│   │   └── train/              # Modelo treinado YOLOv8     
│   └── graph/                  # Grafos e imagens anotadas
├── src/
│   ├── detection/              # YOLO e detecção híbrida
│   ├── processing/             # STRIDE, grafo, OCR
│   └── reports/                # Relatório em PDF e JSON
├── main.py                     # Pipeline completo
├── app.py                      # Interface Streamlit
├── requirements.txt
├── README.md
```

---

## Como Executar via Terminal

### 1. Clone o repositório
```bash
git clone https://github.com/roodligo/hackathon-stride-ai.git
cd hackathon-stride-ai
```

### 2. Instale os pacotes
```bash
pip install -r requirements.txt
```

### 3. Coloque sua imagem
Salve a imagem do diagrama em: `dataset/images/test/1.png`

### 4. Rode a análise
```bash
python main.py
```

---

## Interface Web (opcional)
Execute com Streamlit para ter uma interface:
```bash
streamlit run app.py
```

### Funcionalidades da Interface:
- Upload de imagens
- Visualização do grafo
- Lista de ameaças STRIDE por componente
- Download do relatório em PDF

---

## Resultados Esperados
- `relatorio_stride.pdf` – Relatório com imagem + ameaças e contramedidas
- `relatorio_stride.json` – Dados estruturados
- `runs/graph/grafo.png` – Visualização das conexões
- `runs/detect/predict*/1.jpg` – Imagem anotada com os componentes

---


## Autor
Projeto criado por **Rodrigo Ferreira** durante o Hackathon 3IADT — Fase 5

---

## Licença
MIT License
