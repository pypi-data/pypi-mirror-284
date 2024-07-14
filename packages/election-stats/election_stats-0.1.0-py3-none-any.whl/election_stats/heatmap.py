from .election import Election
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def heatmap(primary, secondary):
    """
    Create heatmaps showing party gains across elections
    """
    e1 = Election(primary)
    e2 = Election(secondary)
    heatmap_data = {}
    # for name in e2.constituencies.keys():
    #     if not e2.constituencies[name].candidates[0][dn] in heatmap_data.keys():
    #         heatmap_data[e2.constituencies[name].candidates[0][dn]] = {}
    #     try:
    #         heatmap_data[e2.constituencies[name].candidates[0][dn]
    #                      ][e1.constituencies[name].candidates[0][dn]] += 1
    #     except KeyError:
    #         heatmap_data[e2.constituencies[name].candidates[0][dn]
    #                      ][e1.constituencies[name].candidates[0][dn]] = 1
    
    ## Whole algorithm could be improved...
    ## those try... except clauses are only at runtime...
    ## could change to producing everything...
    for c in e2.constituencies.values():
        try:
            heatmap_data[c.winner.party.abbrv][e1.constituencies[c.name]] += 1
        except:
            try:
                heatmap_data[c.winner.party.abbrv][e1.constituencies[c.name].winner.party.abbrv] = 1
            except:
                heatmap_data[c.winner.party.abbrv] = {}
                heatmap_data[c.winner.party.abbrv][e1.constituencies[c.name].winner.party.abbrv] = 1
    
    
    heatmap_data["Total"] = {name: sum(
        [d.get(name, 0) for d in heatmap_data.values()]) for name in heatmap_data.keys()}
    heatmap_data = {k: (v | {"Total":sum(heatmap_data[k].values())}) for k, v in heatmap_data.items()}
    del heatmap_data["Total"]["Total"]
    print(heatmap_data)

    heatmapdf = pd.DataFrame(heatmap_data)
    srt = list(e1.parties.keys())
    heatmapdf = heatmapdf.reindex(srt + ["Total"], axis=0)
    heatmapdf = heatmapdf.reindex(["Total"] + srt, axis=1)
    print(heatmapdf)
    # fmt prevents scientific notation. yes, it is a float with 0 prisicion - this is to support NaN
    ax = sns.heatmap(heatmapdf, cmap="Blues", annot=True,
                     fmt=".0f", linewidths=.5)
    ax.set_title("Change of Seats from 2017-2019 UK General Elections")
    ax.set_xlabel("2017 Seats")
    ax.set_ylabel("2019 Seats")
    plt.show()

