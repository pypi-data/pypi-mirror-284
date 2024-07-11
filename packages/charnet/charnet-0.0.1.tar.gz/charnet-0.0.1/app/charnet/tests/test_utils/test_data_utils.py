def default_agg_weight(df):
    dialogue_counts = dict()

    def agg_chars(series):
        if not isinstance(series, str) or series == '':
            return []
        return list(set(char.strip() for char in series.strip('[]').split(',')))

    for _, row in df.iterrows():
        speakers = agg_chars(row['speakers'])
        listeners = agg_chars(row['listeners'])

        for speaker in speakers:
            for listener in listeners:
                if speaker != listener:  # Avoid self-loops
                    dialogue_counts[frozenset([speaker, listener])] = 1

    return dialogue_counts
