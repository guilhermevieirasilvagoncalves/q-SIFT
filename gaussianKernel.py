import numpy as np

def gKernel(tamanho, desvio):
    k1 = 0
    s = (tamanho, tamanho)
    f1 = np.zeros(s)
    step = (1 / ((tamanho - 1) / 2))
    for y in np.arange(-1, 1 + step, step):
        k2 = 0
        for x in np.arange(-1, 1 + step, step):
            f1[k1, k2] = np.exp((-((pow(x, 2) + pow(y, 2)) / (2 * pow(desvio, 2)))))
            #f1[k1, k2] = round(f1[k1, k2] / 2 * np.pi * pow(desvio, 2), 4)
            f1[k1, k2] = round(f1[k1, k2] / (np.sqrt(2 * np.pi) * desvio), 4)
            k2 = k2 + 1
        k1 = k1 + 1
    maxf1c = np.amax(np.amax(f1))
    posx, posy = np.where(f1 == maxf1c)
    k1 = 0
    H = np.zeros(s)
    for j in range(((posy[0]) - (tamanho // 2)), ((posy[0]) + (tamanho // 2)) + 1):
        k2 = 0
        for i in range(((posx[0]) - (tamanho // 2)), ((posx[0]) + (tamanho // 2)) + 1):
            H[k1, k2] = f1[i, j]
            k2 = k2 + 1
        k1 = k1 + 1
    H = H / np.max(H)

    # plot da gaussiana
    '''
    x = np.arange(0, tamanho, 1)
    y = np.arange(0, tamanho, 1)
    X, Y = np.meshgrid(x, y)
    Z = H
    norm = plt.Normalize(Z.min(), Z.max())
    colors = cm.viridis(norm(Z))
    rcount, ccount, _ = colors.shape
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    surf = ax.plot_surface(X, Y, Z, rcount=rcount, ccount=ccount,
                           facecolors=colors, shade=False)
    surf.set_facecolor((0, 0, 0, 0))
    plt.show()
    '''


    return H