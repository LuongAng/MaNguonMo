def C_G():
    image = cv2.imread(file_path)
    gray_img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    color_img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    normalized_image_gray = cv2.normalize(gray_img, None, 0, 1, cv2.NORM_MINMAX, -1)
    normalized_image_color = cv2.normalize(color_img, None, 0, 1, cv2.NORM_MINMAX, -1)
    Titles = ["color_image", "normalized_image_color", "gray_image", "normalized_image_gray"]
    images = [color_img, normalized_image_color, gray_img, normalized_image_gray]
    fig, axs = plt.subplots(2, 2)
    for i in range(4):
        ax = axs[i // 2, i % 2]
        ax.set_title(Titles[i])
        if i < 2:
            ax.imshow(images[i])
        else:
            ax.imshow(images[i], cmap='gray')
        ax.axis('off')

    main = tk.Tk()
    main.title("C_G Function in Tkinter")

    canvas = FigureCanvasTkAgg(fig, master=main)
    canvas.get_tk_widget().pack()

    main.mainloop()