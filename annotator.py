import cv2
import sys
import pickle

cap = cv2.VideoCapture(sys.argv[1])
annotation_filename = "{}-annotations.pickle".format(".".join(sys.argv[1].split(".")[:-1]))

try:
    with open(annotation_filename, 'rb') as af:
        annotations = pickle.load(af)
    print("Skipping {n} frames".format(n=max(annotations.keys())))
    n = max(annotations.keys())
    for fn in range(n):
        print("skipping {fn}".format(fn=fn))

except IOError:
    n = 0
    annotations = {}

while True:
    status, frame = cap.read()
    if status:
        print("Frame {}".format(n))
        cv2.imshow("Frame", frame)
        cv2.waitKey(1)
        nppl = input("Number of people entering boundary: ")
        if nppl.lower().startswith("q"):
            sys.exit()
        elif nppl == "":
            nppl = 0
        annotations[n] = int(nppl)
        with open(annotation_filename, 'wb') as af:
            pickle.dump(annotations, af)
            print("Logged {} in frame {}".format(annotations[n], n))
        n+=1
    else:
        print("Failed to read frame")
