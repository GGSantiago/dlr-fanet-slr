import pandas as pd
import textwrap

slr_df_clean = pd.read_csv('slr_data.csv', index_col=0)
for i, row in slr_df_clean[['title', 'keywords', 'abstract']].iterrows():
    print(f'Paper ({i+1}):')
    print(f'{" "*4} {row["title"]}')
    print('Keywords:')
    if pd.isna(row['keywords']):
        print(f'{" "*4} No keywords available')
    else:
        for keyword in row['keywords'].split(','):
            print(f'{" "*4} - {keyword.strip()}')
    print()
    print('Abstract:')
    print(f'{textwrap.fill(row["abstract"], width=210, initial_indent="    ", subsequent_indent=" ")}')
    print('-'*80)
    user_input = input()