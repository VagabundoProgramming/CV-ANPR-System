directory = "Test/Frontal/Frontal/"
for name in os.listdir(directory)[:-1]:
    contours = find_relevant_contours(directory+name)
    contours = find_extremes(contours)
    index, error = calculate_error(contours)
    print(error, len(contours))
    img = cv2.cvtColor(cv2.imread(directory+name), cv2.COLOR_BGR2RGB)
    cv2.drawContours(img, contours[index], -1, (255,0,0), 100)
    plt.figure(figsize=(16, 16))
    plt.imshow(img, cmap="gray")
