import matplotlib.pyplot as plt
from matplotlib import cm
import pandas as pd

plt.style.use('ggplot')


def plot_history(history):
    acc = history.history['accuracy']
    val_acc = history.history['val_accuracy']
    loss = history.history['loss']
    val_loss = history.history['val_loss']
    x = range(1, len(acc) + 1)

    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.plot(x, acc, 'b', label='Training acc')
    plt.plot(x, val_acc, 'r', label='Validation acc')
    plt.title('Training and validation accuracy')
    plt.legend()
    plt.subplot(1, 2, 2)
    plt.plot(x, loss, 'b', label='Training loss')
    plt.plot(x, val_loss, 'r', label='Validation loss')
    plt.title('Training and validation loss')
    plt.legend()
    plt.show()


def frequency_histogram(df: pd.DataFrame, title='Most Common Words'):
    # get labels for columns
    cmap = cm.get_cmap('cool_r')
    cols = list(df.columns)
    num_cols = len(df)
    dff = pd.DataFrame(df, columns=[cols[1], cols[2]])
    dff.plot(kind='barh', x=cols[1],
             y=cols[2],
             xlabel=cols[1],
             ylabel=cols[2],
             title=title,
             legend=False,
             grid=False,
             cmap=cmap)