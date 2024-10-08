import cv2
import mediapipe as mp
import requests
ESP_IP = "192.168.137.71"
ESP_PORT = 80
def send_command(command):
    url = f"http://{ESP_IP}:{ESP_PORT}/"
    try:
        requests.get(url, params={"command": command})
    except Exception as e:
        print(f"Failed to send command {command}: {e}")

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands


vid = cv2.VideoCapture(0)
hands = mp_hands.Hands()

 
#def left(hand_landmarks):

def stop(hand_landmarks):
    thumb_tip_y = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y
    index_tip_y = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
    middle_tip_y = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y
    ring_tip_y = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y
    pinky_tip_y = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y

    thumb_mcp_y = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].y
    index_mcp_y = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].y
    middle_mcp_y = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y
    ring_mcp_y = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP].y
    pinky_mcp_y = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP].y

    if (thumb_tip_y < thumb_mcp_y and 
        index_tip_y < index_mcp_y and
        middle_tip_y < middle_mcp_y and
        ring_tip_y < ring_mcp_y and
        pinky_tip_y < pinky_mcp_y):
        return True
    return False


def reverse(hand_landmarks):
    thumb_tip_y = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y
    index_tip_y = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
    middle_tip_y = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y
    ring_tip_y = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y
    pinky_tip_y = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y

    thumb_pip_y = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].y
    index_pip_y = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].y
    middle_pip_y = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y
    ring_pip_y = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].y
    pinky_pip_y = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].y

    thumb_mcp_y = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].y
    index_mcp_y = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].y
    middle_mcp_y = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y
    ring_mcp_y = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP].y
    pinky_mcp_y = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP].y

    #thumb_dip_y = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_DIP].y
    index_dip_y = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP].y
    middle_dip_y = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP].y
    ring_dip_y = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_DIP].y
    pinky_dip_y = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_DIP].y


    if ((thumb_tip_y > thumb_pip_y and 
        index_tip_y > index_pip_y and
        middle_tip_y > middle_pip_y and
        ring_tip_y > ring_pip_y and
        pinky_tip_y > pinky_pip_y)) or (thumb_mcp_y < thumb_pip_y and 
        index_mcp_y < index_pip_y and
        middle_mcp_y < middle_pip_y and
        ring_mcp_y < ring_pip_y and
        pinky_mcp_y < pinky_pip_y) or (  
        index_mcp_y < index_dip_y and
        middle_mcp_y < middle_dip_y and
        ring_mcp_y < ring_dip_y and
        pinky_mcp_y < pinky_dip_y):
        return True
    return False


 
    
    return False
def right(hand_landmarks):
    thumb_tip_y = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y
    index_tip_y = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
    middle_tip_y = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y
    ring_tip_y = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y
    pinky_tip_y = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y

    thumb_mcp_y = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].y
    index_mcp_y = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].y
    middle_mcp_y = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y
    ring_mcp_y = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP].y
    pinky_mcp_y = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP].y

    if (thumb_tip_y < thumb_mcp_y and 
        index_tip_y < index_mcp_y and
        middle_tip_y < middle_mcp_y and ring_tip_y > ring_mcp_y and pinky_tip_y > pinky_mcp_y ):
        return True
    return False
def left(hand_landmarks):
    thumb_tip_y = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y
    index_tip_y = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
    middle_tip_y = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y
    ring_tip_y = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y
    pinky_tip_y = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y

    thumb_mcp_y = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].y
    index_mcp_y = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].y
    middle_mcp_y = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y
    ring_mcp_y = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP].y
    pinky_mcp_y = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP].y

    if (thumb_tip_y < thumb_mcp_y and 
        index_tip_y > index_mcp_y and
        middle_tip_y < middle_mcp_y and ring_tip_y < ring_mcp_y and pinky_tip_y < pinky_mcp_y ):
        return True
    return False
def forward(hand_landmarks):
    thumb_tip_y = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y
    index_tip_y = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
    middle_tip_y = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y
    ring_tip_y = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y
    pinky_tip_y = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y
    thumb_pip_y = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].y

    thumb_mcp_y = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].y
    index_mcp_y = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].y
    middle_mcp_y = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y
    ring_mcp_y = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP].y
    pinky_mcp_y = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP].y

    if (thumb_tip_y < thumb_pip_y and thumb_tip_y < thumb_mcp_y and
        index_tip_y < index_mcp_y and
        middle_tip_y > middle_mcp_y and ring_tip_y > ring_mcp_y and pinky_tip_y > pinky_mcp_y ):
        return True
    return False
     







     

    
    


gesture_detected = False

while True:
    ret, img = vid.read()
    if not ret:
        break

    img = cv2.cvtColor(cv2.flip(img, 1), cv2.COLOR_BGR2RGB)

    results = hands.process(img)

    if results.multi_hand_landmarks:
         
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            if stop(hand_landmarks):
                cv2.putText(img, 'stopped', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
                if not gesture_detected:
                    send_command('n')  
                    gesture_detected = True
            if reverse(hand_landmarks):
                cv2.putText(img, 'moving reverse', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
                if not gesture_detected:
                    send_command('s')  
                    gesture_detected = True
            if left(hand_landmarks):
                cv2.putText(img, 'moving left', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
                if not gesture_detected:
                    send_command('a')  
                    gesture_detected = True
            if right(hand_landmarks):
                cv2.putText(img, 'moving right', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
                if not gesture_detected:
                    send_command('d')  
                    gesture_detected = True
            if forward(hand_landmarks):
                cv2.putText(img, 'moving forward', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
                if not gesture_detected:
                    send_command('w')  
                    gesture_detected = True
            

                 
    if not gesture_detected:
        send_command(b'n')
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)


    cv2.imshow("Hand Gesture Recognition", img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

   
    if gesture_detected:
        cv2.waitKey(10)   
        gesture_detected = False


 