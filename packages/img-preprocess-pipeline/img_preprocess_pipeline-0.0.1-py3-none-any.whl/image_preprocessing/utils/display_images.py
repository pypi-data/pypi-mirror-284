import matplotlib.pyplot as plt

def plot_images(*args):
    fig,axs = plt.subplots(1,len(args),figsize=(12,6))

    for image_file,ax in zip(args,axs):
        image_name,image_temp = list(image_file.keys())[0],list(image_file.values())[0]
        ax.imshow(image_temp,cmap='grey')
        ax.set_title(image_name)

    plt.tight_layout()
    plt.show()

