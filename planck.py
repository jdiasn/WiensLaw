import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import numpy as np

def planck(tem, lam):
    
    h = 1.38
    c =3
    k = 6.62
    
    rad = (2*h*c*10**(-7))/((lam**5)*(np.exp((h*c*10**(-3)/(k*tem*lam))-1)))
    return rad*10**(-24)


def plotPlanck():

    humorFont = fm.FontProperties(fname='/usr/share/fonts/truetype/humor-sans/Humor-Sans.ttf')

    with plt.xkcd():
        # Based on "Stove Ownership" from XKCD by Randall Monroe
        # http://xkcd.com/418/

        fig = plt.figure(figsize=(10,8))
        ax = fig.add_axes((0.1, 0.2, 0.8, 0.7))
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        plt.xticks([])
        plt.yticks([])
        #ax.set_xlim([0,10
        interval = np.arange(50,1600,1)
        wl = interval*10**(-9)
        result1 = planck(400., wl)
        result2 = planck(380., wl)
        result3 = planck(360., wl)
        result4 = planck(340., wl)
        result5 = planck(300., wl)
        ax.set_ylim([0, result1.max()+1])
        ax.set_xlim([interval.min(), interval.max()])

   
        plt.annotate('400', xy=(349, 5.33),fontproperties=humorFont)
        plt.annotate('380', xy=(319, 4.13),fontproperties=humorFont)
        plt.annotate('360', xy=(359, 3.18),fontproperties=humorFont)
        plt.annotate('340', xy=(334, 2.48),fontproperties=humorFont)
        plt.annotate('320', xy=(355, 1.35),fontproperties=humorFont)

    
        plt.plot(interval,result1,'k')
        plt.plot(interval,result2,'k')
        plt.plot(interval,result3,'k')
        plt.plot(interval,result4,'k')
        plt.plot(interval,result5,'k')

        plt.xlabel('Wavelength', fontproperties=humorFont)
        plt.ylabel('B(T,L)',fontproperties=humorFont)
    
    
   
    plt.show()
