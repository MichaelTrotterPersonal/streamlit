
import pandas as pd
import streamlit as st
from data_generation import get_records
from st_utils import filter_dataframe
import seaborn as sns

@st.cache_data
def get_record_data():

    return pd.DataFrame(get_records(1000))


def main():

    # st. set_page_config(layout="wide")
    
    df = filter_dataframe(get_record_data())
    print(df.dtypes)
    # st.dataframe(df,width=3000)

    # tab1, tab2, tab3 = st.tabs(["Usage trend", "Usage weekly heatmap", "User breakdown"])
    # with tab1:
    #     st.write(f"DF: {len(df)}")
    #     st.write(df.user_id.value_counts())
        
    #     sns.lineplot(data=df, x="timestamp", y="runtime", hue="user_id")

    # with tab2:
    #     st.write("This is the second tab")
    # with tab3:
    #     st.write("This is the third tab")
    #     #st.dataframe(df.groupby("user_id").count())
    
if __name__ == "__main__":
    main()