""" import cv2
import mediapipe as mp

print("OpenCV version:", cv2.__version__)
print("MediaPipe version:", mp.__version__)
print(cv2.getBuildInformation()) """

import cv2
import mediapipe as mp

# Inicializa o MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Configuração do modelo
hands = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Inicializa a captura de vídeo
capture = cv2.VideoCapture(0)

if not capture.isOpened():
    print("Erro ao acessar a câmera.")
    exit()

while True:
    ret, frame = capture.read()
    if not ret:
        print("Erro ao capturar o frame.")
        break

    # Converte BGR para RGB (necessário para o MediaPipe)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Processa a imagem e detecta mãos
    results = hands.process(frame_rgb)

    # Verifica se alguma mão foi detectada
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Exibe o vídeo com as detecções
    cv2.imshow("Detecção de Mãos", frame)

    # Pressione 'q' para sair
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera recursos
capture.release()
cv2.destroyAllWindows()
