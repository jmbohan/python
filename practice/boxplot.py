import matplotlib.pylab as pyp
import seaborn as sns

def custom_legend(colors,labels, legend_location = 'upper left', legend_boundary = (1,1)):
    # Create custom legend for colors
    recs = []
    for i in range(0,len(colors)):
        recs.append(mpatches.Rectangle((0,0),1,1,fc=colors[i]))
    pyp.legend(recs,labels,loc=legend_location, bbox_to_anchor=legend_boundary)

# Color boxplots by organ
organ_list = sorted(df_unique(grouped_samples,'type'))
colors = sns.color_palette("Paired", len(organ_list))
color_dict = dict(zip(organ_list, colors))
organ_palette = grouped_samples.drop_duplicates('id')['type'].map(color_dict)

# Plot grouped boxplot
g = sns.factorplot("id","num_mutations",data=grouped_samples, order=id_list, kind="box", size=7, aspect=3, palette=organ_palette)
sns.despine(left=True)
plot_setup_pre()
pyp.yscale('log')
custom_legend(colors,organ_list)    