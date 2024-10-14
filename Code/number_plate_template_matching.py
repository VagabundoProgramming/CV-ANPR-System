import cv2
import os

def template_matching(img_rgb, figures_directory, spain_mark="Images/SpainMark.jpg"):
    img = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    img =  cv2.resize(img, (520, 110)) #Resizing the plate to its spectating shape

    t = cv2.cvtColor(cv2.imread("C:/Users/G733/Visual Studio Code/Visual&Learning/Challenge1/CV-ANPR-System/Images/SpainMark.jpg"), cv2.COLOR_BGR2GRAY)
    t = t[~np.all(t==255, axis=1)] #eliminatess white rows
    t = t[:,~np.all(t==255, axis=0)] #eliminates black columns
    t = cv2.resize(t, (40, 100))

    res = cv2.matchTemplate(img[:, 0:50], t, cv2.TM_CCOEFF_NORMED)
    print(res.max())
    if res.max() > 0.1:
        number_position = [(54, 125), (113, 184), (172, 243), (233, 302), (317, 388), (376, 447), (435, 506)]
    else:
        img = cv2.resize(img,(470, 110))
        number_position = [(4, 75), (63, 134), (122, 193), (183, 252), (267, 338), (326, 397), (375, 456)]

    _, img = cv2.threshold(img, 100, 255, 0)
    _, t = cv2.threshold(t, 100, 255, 0)

    plate = ""
    # This next loop search for each position each value of matching template where grabs the highest maching figure
    for y, pos in enumerate(number_position):
        max_value = [0, ""]
        for i, f in enumerate(os.listdir(figures_directory)):
            if (y < 4 and not f[0].isnumeric()) or (y >= 4 and f[0].isnumeric()):
                continue
            t = cv2.cvtColor(cv2.imread(figures_directory+"/"+f), cv2.COLOR_BGR2GRAY)
            t = cv2.resize(t, (45, 77)) #Resizing the template to its spectating shape in the plate
            _, t = cv2.threshold(t, 100, 255, 0)
            res = cv2.matchTemplate(img[:,pos[0]:pos[1]], t, cv2.TM_CCOEFF_NORMED)
            if res.max() > max_value[0]: #Find max value of template
                max_value = [res.max(), f[0]]
        plate = plate + max_value[1]
    return plate
