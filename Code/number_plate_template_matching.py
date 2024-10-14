import cv2

def template_matching(img_rgb, figures_directory):
    img = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    img =  cv2.resize(img, (520, 110)) #Resizing the plate to its spectating shape
    _, img = cv2.threshold(img, 100, 255, 0)
    number_position = [(56, 123), (115, 182), (174, 241), (235, 300), (319, 386), (378, 445), (437, 504)] # These are the main positions for each number on the plate
    plate = ""
    # This next loop search for each position each value of matching template where grabs the highest maching figure
    for pos in number_position:
        max_value = [0, ""]
        for i, f in enumerate(os.listdir(figures_directory)):
            t = cv2.cvtColor(cv2.imread(figures_directory+"/"+f), cv2.COLOR_BGR2GRAY)
            t = cv2.resize(t, (45, 77)) #Resizing the template to its spectating shape in the plate
            _, t = cv2.threshold(t, 100, 255, 0)
            res = cv2.matchTemplate(img[:,pos[0]:pos[1]], t, cv2.TM_CCOEFF_NORMED)
            if res.max() > max_value[0]: #Find max value of template
                max_value = [res.max(), f[0]]
        plate = plate + max_value[1]
    return plate
