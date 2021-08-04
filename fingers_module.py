import numpy as np


class Fingers:
    def __init__(self):
        # self.thumb_mcp_id = 2
        # self.thumb_tip_id  = 4
        # self.index_pip_id  = 6
        # self.index_tip_id  = 8
        # self.middle_pip_id  = 10
        # self.middle_tip_id  = 12
        # self.ring_pip_id = 14
        # self.ring_tip_id = 16
        # self.pinky_pip_id = 18
        # self.pinky_tip_id = 20
        self.tip_ids = np.array([4, 8, 12, 16, 20])
        self.pip_ids = self.tip_ids - 2

    def count_fingers(self, landmarks):
        count = 0
        for idx in range(1, self.tip_ids.shape[0]):
            if landmarks[self.tip_ids[idx]][2] < landmarks[self.pip_ids[idx]][2]:
                count += 1
        # thumb finger case is different check x value instead
        # check whether it's left or right hand
        # left hand the wrist x value is higher than the thumb pip
        if landmarks[0][1] > landmarks[self.pip_ids[0]][1]:     # left hand
            if landmarks[self.tip_ids[0]][1] < landmarks[self.tip_ids[0]-1][1]:
                count += 1
        elif landmarks[0][1] < landmarks[self.pip_ids[0]][1]:   # right hand
            if landmarks[self.tip_ids[0]][1] > landmarks[self.tip_ids[0]-1][1]:
                count += 1
        return count


def main():
    fingers = Fingers()
    print(fingers.pip_ids[1])
    fingers.count_fingers(landmarks=None)


if __name__ == '__main__':
    main()