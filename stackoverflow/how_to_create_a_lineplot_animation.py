import pandas as pd
import matplotlib.animation as animation
import seaborn as sns
import matplotlib.pyplot as plt


d = {'time': [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],
     'method1': [0.864231038, 0.874805716, 0.890315836, 0.906831719, 0.91634293, 0.928120905, 0.938231839, 0.947280697,
                 0.951635588, 0.951468784],
     'method2': [0.867868393, 0.878908199, 0.893329853, 0.911470465, 0.924099528, 0.934628044, 0.945209861, 0.951776017,
                 0.954180089, 0.95553498]}

df = pd.DataFrame(data=d)
print(df)


fig, ax = plt.subplots()


def animate(i):
    ax.clear()
    x_labels = df['time'][:i + 1]
    ax.set_xlim([1, 19])
    ax.set_xlabel('Time', fontsize=14)
    ax.set_ylabel('Popularity', fontsize=14)
    sns.lineplot(x=x_labels, y=df['method1'][:i+1], ax=ax, label='method1')
    sns.lineplot(x=x_labels, y=df['method2'][:i+1], ax=ax, label='method2')
    # ax.set_ylim([1, 1])
    plt.legend()


anim = animation.FuncAnimation(fig, animate, frames=len(df), interval=500)
anim.save('test.gif')
