
import pandas as pd
import streamlit as st
from data_generation import get_records
from st_utils import filter_dataframe
import seaborn as sns
from matplotlib import pyplot as plt
from io import BytesIO

@st.cache_data
def get_record_data():
    return pd.DataFrame(get_records(1000))


def main():

    st. set_page_config(layout="wide")
    
    df = filter_dataframe(get_record_data())
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    st.dataframe(df,width=3000)

    tab1, tab2, tab3 = st.tabs(["Usage trend", "Usage weekly heatmap", "User breakdown"])

    with tab1:
        count_by_day = df.groupby(pd.Grouper(key='timestamp', freq='D')).size()
        count_df = pd.DataFrame(count_by_day)
        count_df.reset_index(inplace=True)
        count_df.columns = ['timestamp', 'count']
        st.line_chart(data=count_df, x='timestamp', y='count',use_container_width=True)

    with tab2:
        df_pivot = df.pivot_table(index=df['timestamp'].dt.dayofweek, columns=df['timestamp'].dt.hour, aggfunc='size')
        fig = plt.figure(figsize=(12, 4))
        
        sns.heatmap(df_pivot,yticklabels = ['Mon','Tue','Wed','Thu','Fri'],xticklabels=[f"{i}:00" for i in range(9,17)], cmap='viridis',annot=True,fmt='g')
        plt.xlabel('Hour of day')
        plt.ylabel('Day of week')
        buf = BytesIO()
        fig.savefig(buf, format="png")
        st.image(buf)

    with tab3:
        df_grouped = df.groupby(['user_id', 'calling_file']).size().reset_index(name='count')
        df_pivot = df_grouped.pivot(index='user_id', columns='calling_file', values='count').fillna(0)
        ax = df_pivot.plot(kind='bar', stacked=True)
        st.bar_chart(df_pivot)

    
if __name__ == "__main__":
    main()