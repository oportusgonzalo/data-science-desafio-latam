import matplotlib.pyplot as plt

def get_descriptive(df, columnas):
    for k, v in df.iteritems():
        if k in columnas:
            print(f'{k}:')
            print(v.describe())
            print('-'*90)

def missing_cases(df, var, print_list=False):
    tmp = df.copy()
    tmp['flagnull'] = tmp[var].isnull()
    count_na = 0
    for i, r in tmp.iterrows():
        if r['flagnull'] is True:
            count_na += 1
            if print_list == True:
                print(r['cname'])
    
    print('Casos nulos para {}: {}'.format(var, count_na))
    print('Porcentaje nulos para {}: {}'.format(var, count_na/df.shape[0]))

def hist_plot(sample_df, full_df, var, sample_mean=False, true_mean=False):
    plt.hist(sample_df[var].dropna(), color='grey', alpha=.5)
    plt.title('Histograma: {}'.format(var))
    if sample_mean is True:
        plt.axvline(sample_df[var].mean(), color='blue', lw=3)
    if true_mean is True:
        plt.axvline(full_df[var].mean(), color='red', lw=3)
    plt.show()

def dot_plot(df, plot_var, plot_by='ht_region', statistic='mean', global_stat=False):
    tmp = df.loc[:, [plot_var, plot_by]]
    tmp = df.groupby(plot_by).agg({plot_var: statistic})
    plt.plot(tmp.values, tmp.index, 'o', color='grey')
    plt.title('Dotplot {} by {}'.format(plot_by, plot_var))
    if statistic == 'mean':
        plt.axvline(tmp[plot_var].mean(), color='red', linestyle='--')
    if statistic == 'median':
        plt.axvline(tmp[plot_var].median(), color='blue', linestyle='--')
    plt.show()
    