from sklearn.metrics import mean_squared_error, r2_score

def model_formula(df, var_obj):
    """Genera la fórmula del modelo logit con todos sus atributos y variable objetivo.

    Args:
        df (dataframe): Conjunto de datos
        var_obj (string): variable objetivo

    Returns:
        string: formula total
    """
    base_formula = f'{var_obj} ~ '
    for col in df.columns:
        if col != var_obj:
            base_formula += f'{col} + '
    return base_formula[:-3]