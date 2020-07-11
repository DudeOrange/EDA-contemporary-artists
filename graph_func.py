from matplotlib import pyplot
import numpy
import pandas

def bar_count_prices(x, y, name):
    '''
    Display bar chart
    Arguments:
      x - price column, pandas series
      y - aggregation column, count of each price, pandas series
      name - name of the artist by whom we perform aggregation, string

    Returns:
      Display bar chart in jupiter notebook
    '''
    fig, ax = pyplot.subplots()

    ax.bar(x, y, width = 200)

    ax.set_title('Most popular price of pictures by ' + name, fontsize = 15)
    ax.set_xlabel('Prices')
    ax.set_ylabel('Count of pictures')
    ax.grid()
    ax.set_facecolor('seashell')
    fig.set_facecolor('floralwhite')
    fig.set_figwidth(12)
    fig.set_figheight(6)

    pyplot.show()
    
def crosstab_graph(x, y, name):
    '''
    Display chart of computing a cross tabulation
    Arguments:
      x - year or square column, pandas series
      y - price column, pandas series
      name - name of the artist by whom we compute a cross tabulation, string

    Returns:
      Display chart in jupiter notebook
    '''
    xaxis = numpy.sort(x.unique())
    yaxis = numpy.sort(y.unique())

    xaxis = xaxis[::5]
    yaxis = yaxis[::5]

    fig, ax = pyplot.subplots(figsize=(20, 20))
    fig.set_facecolor('floralwhite')
    ax.imshow(pandas.crosstab(y, x))
    
    if x.name == 'year':
        ax.set_title('The ratio of price to year painting by ' + name, fontsize = 15)
        ax.set_xlabel('Years')
    else:
        ax.set_title('The ratio of price to square painting by ' + name, fontsize = 15)
        ax.set_xlabel('Squares')
    ax.set_ylabel('Prices')
    pyplot.xticks(range(0, len(xaxis)*5, 5), xaxis, rotation='vertical')
    pyplot.yticks(range(0, len(yaxis)*5, 5), yaxis)
    pyplot.show()
    
def boxplot_graph(data, x, y):
    '''
    Display box plot chart 
    Arguments:
      data - data frame including needed columns: price, style or genre, pandas DataFrame
      x - name of the column, string
      y - name of the column, string

    Returns:
      Display chart in jupiter notebook
    '''
    fig, ax = pyplot.subplots()

    data.boxplot(column=[x], by=y, ax=ax)

    ax.set_title('Boxplot by price to ' + y, fontsize = 15)
    ax.set_xlabel(y)
    ax.set_ylabel('price')
    ax.set_facecolor('seashell')
    fig.set_facecolor('floralwhite')
    fig.set_figwidth(12)
    fig.set_figheight(6)
    pyplot.suptitle('')
    pyplot.show()