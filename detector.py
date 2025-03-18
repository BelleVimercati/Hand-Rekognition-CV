import cv2
import mediapipe as mp
import numpy as np
import time  # utilizado para checar o framerate


class AsimovDetector:
    def __init__(
        self,
        mode: bool = False,
        number_hands: int = 2,
        model_complexity: int = 1,
        min_detec_confidence: float = 0.5,
        min_tracking_confidence: float = 0.5,
    ):

        # Parâmetros necessários para inicializar o Hands
        self.mode = mode
        self.max_num_hands = number_hands
        self.complexity = model_complexity
        self.detection_con = min_detec_confidence
        self.tracking_con = min_tracking_confidence

        # Inicializando o Hands
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            self.mode,
            self.max_num_hands,
            self.complexity,
            self.detection_con,
            self.tracking_con,
        )
        self.mp_draw = mp.solutions.drawing_utils

    def find_hands(self, img: np.ndarray, draw_hands: bool = True):

        # Correção de cor
        img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Coletar resultados do processo das hands e analizar
        self.results = self.hands.process(img_RGB)
        if self.results.multi_hand_landmarks:
            for hand in self.results.multi_hand_landmarks:
                if draw_hands:
                    self.mp_draw.draw_landmarks(
                        img, hand, self.mp_hands.HAND_CONNECTIONS
                    )
        return img

    def find_position(self, img: np.ndarray, hand_number: int = 0):
        self.required_landmark_list = []

        if self.results.multi_hand_landmarks:
            my_hand = self.results.multi_hand_landmarks[0]
            for id, lm in enumerate(my_hand.landmark):
                height, width, _ = img.shape
                center_x = int(lm.x * width)
                center_y = int(lm.y * height)

                self.required_landmark_list.append([id, center_x, center_y])
        return self.required_landmark_list


if __name__ == "__main__":
    # Dados de video
    capture = cv2.VideoCapture(0)
    previous_time = 0
    current_time = 0

    """ if not capture.isOpened():
        print("Erro ao acessar a câmera.")
        exit(1) """

    Detector = AsimovDetector()

    while True:
        _, img = capture.read()

        # Manipular o frame
        img = Detector.find_hands(img)

        landmark_list = Detector.find_position(img)
        """ if landmark_list:
            print(landmark_list) """


        # Contando os dedos
        fingers = [8, 12, 16, 20]
        cont = 0

        if landmark_list:
            # Lógica para o dedão
            if landmark_list[4][1] < landmark_list[2][1]:
                cont += 1
            # Lógica para os outros dedos
            for x in fingers:
                if landmark_list[x][2] < landmark_list[x - 2][2]:
                    cont += 1
        cv2.putText(
            img, str(cont), (10, 100), cv2.FONT_HERSHEY_DUPLEX, 3, (0, 0, 255), 2
        )

        # Determinar framerate
        current_time = time.time()
        fps = 1 / (current_time - previous_time)
        previous_time = current_time

        cv2.putText(
            img, str(int(fps)), (10, 20), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 255, 0), 2
        )

        # Retornar o frame com desenho da mão
        cv2.imshow("Imagem", img)

        if cv2.waitKey(20) & 0xFF == ord(
            "q"
        ):  # Cv2 wait fica aguardado uma tecla de 32 bits, como a tabela ascii devolve com 8, realizamos uma mascara para ler os 8 bits mais relevantes
            break
