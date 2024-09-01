import streamlit as st
import pandas as pd
from difflib import Differ
from io import StringIO
import re
import tiktoken


st.set_page_config(layout="wide")

encoding = tiktoken.encoding_for_model("gpt-4o")

text = st.text_area("Paste")

if text != "":
    io = StringIO(text)

    df = pd.read_csv(io, sep="\t")
    # df = df.dropna(axis=0, how="all")

    st.dataframe(df, use_container_width=True)

    st.divider()

    col1, col2 = st.columns(2)
    with col1:
        with st.container(border=True):
            col11, col12, col13 = st.columns(3)
            with col11:
                option1_ind = st.selectbox("1. Index", df.index, df.index[-1])
            with col12:
                option1_col = st.selectbox("1. Column", df.columns)
            with col13:
                option1_split = st.selectbox("1. Split", [None, "##", "###"], None)
            if st.toggle("1. Raw Text"):
                st.divider()
                with st.container(height=700, border=False):
                    if option1_split is None:
                        st.text(df.loc[option1_ind, option1_col])
                    elif option1_split == "##":
                        pattern = r"\n(?=##\s)"
                        parts = re.split(pattern, df.loc[option1_ind, option1_col])
                        for part in parts:
                            with st.container(border=True):
                                st.text(part)
                                st.divider()
                                st.info(f"- Tokens: {len(encoding.encode(part))}\n- Length: {len(part)}")
                    elif option1_split == "###":
                        pattern = r"\n(?=###\s)"
                        parts = re.split(pattern, df.loc[option1_ind, option1_col])
                        for part in parts:
                            with st.container(border=True):
                                st.text(part)
                                st.divider()
                                st.info(f"- Tokens: {len(encoding.encode(part))}\n- Length: {len(part)}")
            else:
                st.divider()
                with st.container(height=700, border=False):
                    if option1_split is None:
                        st.markdown(df.loc[option1_ind, option1_col])
                    elif option1_split == "##":
                        pattern = r"\n(?=##\s)"
                        parts = re.split(pattern, df.loc[option1_ind, option1_col])
                        for part in parts:
                            with st.container(border=True):
                                st.markdown(part)
                                st.divider()
                                st.info(f"Length: {len(part)}")
                    elif option1_split == "###":
                        pattern = r"\n(?=###\s)"
                        parts = re.split(pattern, df.loc[option1_ind, option1_col])
                        for part in parts:
                            with st.container(border=True):
                                st.markdown(part)
                                st.divider()
                                st.info(f"Length: {len(part)}")
            st.divider()
            st.info(f"- Tokens: {len(encoding.encode(str(df.loc[option1_ind, option1_col])))}\n- Length: {len(str(df.loc[option1_ind, option1_col]))}")

    with col2:
        with st.container(border=True):
            col21, col22, col23 = st.columns(3)
            with col21:
                option2_ind = st.selectbox("2. Index", df.index, df.index[-1])
            with col22:
                option2_col = st.selectbox("2. Column", df.columns)
            with col23:
                option2_split = st.selectbox("2. Split", [None, "##", "###"], None)
            if st.toggle("2. Raw Text"):
                st.divider()
                with st.container(height=700, border=False):
                    if option2_split is None:
                        st.text(df.loc[option2_ind, option2_col])
                    elif option2_split == "##":
                        pattern = r"\n(?=##\s)"
                        parts = re.split(pattern, df.loc[option2_ind, option2_col])
                        for part in parts:
                            with st.container(border=True):
                                st.text(part)
                                st.divider()
                                st.info(f"- Tokens: {len(encoding.encode(part))}\n- Length: {len(part)}")
                    elif option2_split == "###":
                        pattern = r"\n(?=###\s)"
                        parts = re.split(pattern, df.loc[option2_ind, option2_col])
                        for part in parts:
                            with st.container(border=True):
                                st.text(part)
                                st.divider()
                                st.info(f"- Tokens: {len(encoding.encode(part))}\n- Length: {len(part)}")
            else:
                st.divider()
                with st.container(height=700, border=False):
                    if option2_split is None:
                        st.markdown(df.loc[option2_ind, option2_col])
                    elif option2_split == "##":
                        pattern = r"\n(?=##\s)"
                        parts = re.split(pattern, df.loc[option2_ind, option2_col])
                        for part in parts:
                            with st.container(border=True):
                                st.markdown(part)
                                st.divider()
                                st.info(f"- Tokens: {len(encoding.encode(part))}\n- Length: {len(part)}")
                    elif option2_split == "###":
                        pattern = r"\n(?=###\s)"
                        parts = re.split(pattern, df.loc[option2_ind, option2_col])
                        for part in parts:
                            with st.container(border=True):
                                st.markdown(part)
                                st.divider()
                                st.info(f"- Tokens: {len(encoding.encode(part))}\n- Length: {len(part)}")
            st.divider()
            st.info(f"- Tokens: {len(encoding.encode(str(df.loc[option2_ind, option2_col])))}\n- Length: {len(str(df.loc[option2_ind, option2_col]))}")

    with st.container(border=True):
        if st.toggle("Compare"):
            st.divider()
            with st.container(height=700, border=False):
                d = Differ()
                l = list(d.compare(list(str(df.loc[option1_ind, option1_col])), list(str(df.loc[option2_ind, option2_col]))))
                l_tmp = []
                for s in l:
                    if s[:2] == "? ":
                        continue
                    elif s[:2] == "+ ":
                        l_tmp.append(f":green[{s[2:]}]")
                    elif s[:2] == "- ":
                        l_tmp.append(f":red[~~{s[2:]}~~]")
                    else:
                        l_tmp.append(s[2:])
                st.markdown("".join(l_tmp))