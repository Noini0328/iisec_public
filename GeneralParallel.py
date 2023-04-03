import time
import pandas as pd
from concurrent.futures import ThreadPoolExecutor

def generate_random_string(length):
    import random
    import string

    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def update(data):
    time.sleep(timeout_num)
    random_string = generate_random_string(5)
    df.loc[df['index'] == data, 'data'] = random_string
    print(data)

def main():
    global df, thread_num, timeout_num

    # settings
    thread_num = 8
    timeout_num = 0.3

    # output data
    output_file = "result.csv"
    # inputs data
    lists = list(range(256))

    # results(can not append)
    df_columns = ["index", "data"]
    df = pd.DataFrame(columns=df_columns)

    with ThreadPoolExecutor(max_workers=thread_num) as executor:
        for i, data in enumerate(lists):

            df_append_list = [[data, "-"]]
            df_append = pd.DataFrame(data=df_append_list, columns=df_columns)
            df = pd.concat([df, df_append], ignore_index=True, axis=0)

            print(f"{i+1}/{len(lists)}, {data}")
            executor.submit(update, data)

    print(df)

if __name__ == '__main__':
    main()
