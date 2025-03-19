# 👋 MediaPipe Hands

Este projeto foi criado com o proposito de ganhar familiaridade com a biblioteca MediaPipe e sua funcionalidades, o foco foi no módulo denominado Hands.

<div style="text-align: center;">
    <img src="img/hand_crops" alt="Prints" width="800">
</div>

## 🛠️ Tecnologias Utilizadas

- Python (3.9.13)
- OpenCV
- MediaPipe
- Poetry

## 📦 Como realizar a instalação

1. Clone este repositório

```bash
    git clone https://github.com/BelleVimercati/Hand-Rekognition-CV.git
```

1. Crie um ambiente virtual

```bash
    python -m venv venv
```

1. Ative o ambiente virtual

```bash
    venv\Scripts\activate
```

1. Instale as dependências

```bash
    pip install -r requirements.txt
```

1. Execute o script

```bash
    python detector.py
```

## 🎯 Funcionalidades testadas 

- [x] Detecção de mãos
- [x] Rastreamento de Landmarks
- [x] Posicionamento cartesiano dos pontos de Landmarks

<div style="text-align: center;">
    <img src="img/hand_landmarks" alt="Landmarks" width="800">
</div>

## 📜 Notas

1. Este script foi criado apenas para fins de aprendizado e experimentação
2. **A funcionalidade de contagem de dedos funciona apenas para a mão esquerda**
    Isso acontece pois a funcionalidade foi desenvolvida comparando o posicionamento das Landmarks no espaço cartesiano da tela, ao usar a mão direita a lógica de contagem do dedão se inverte.

## 📌 Referências

- [Documentação do MediaPipe](https://ai.google.dev/edge/mediapipe/solutions/vision/hand_landmarker?hl=pt-br)