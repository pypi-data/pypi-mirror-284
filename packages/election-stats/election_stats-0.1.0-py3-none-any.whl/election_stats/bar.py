from .election import Election
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def bar(election):
    print("Bar chart time!")
    election = Election(election)
    print(election.parties)
    # print([(p.name,p.seats) for p in election.parties.values()])
    data = {p.abbrv:p.seats for p in election.parties.values()}
    data = dict(filter(lambda i:i[1], data.items()))
    print(data)
    df = pd.DataFrame(data, index=[0])
    print(df)
    c = [election.parties.get(x).colour for x in df]
    sns.barplot(df, palette=c)
    plt.show()