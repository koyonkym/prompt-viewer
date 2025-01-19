import streamlit as st
import pandas as pd
from difflib import Differ
from io import StringIO
import re
import tiktoken
from tiktoken import Encoding


st.set_page_config(layout="wide")

encoding = tiktoken.encoding_for_model("gpt-4o")


def display_raw_text(content: str, split_option: str | None, encoding: Encoding) -> None:
    if split_option is None:
        st.text(content)
    elif split_option == "##":
        pattern = r"\n(?=##\s)"
        parts = re.split(pattern, content)
        for part in parts:
            with st.container(border=True):
                st.text(part)
                st.divider()
                st.info(f"- Tokens: {len(encoding.encode(part))}\n- Length: {len(part)}")
    elif split_option == "###":
        pattern = r"\n(?=###\s)"
        parts = re.split(pattern, content)
        for part in parts:
            with st.container(border=True):
                st.text(part)
                st.divider()
                st.info(f"- Tokens: {len(encoding.encode(part))}\n- Length: {len(part)}")


def display_markdown(content: str, split_option: str | None, encoding: Encoding) -> None:
    if split_option is None:
        st.markdown(content)
    elif split_option == "##":
        pattern = r"\n(?=##\s)"
        parts = re.split(pattern, content)
        for part in parts:
            with st.container(border=True):
                st.markdown(part)
                st.divider()
                st.info(f"- Tokens: {len(encoding.encode(part))}\n- Length: {len(part)}")
    elif split_option == "###":
        pattern = r"\n(?=###\s)"
        parts = re.split(pattern, content)
        for part in parts:
            with st.container(border=True):
                st.markdown(part)
                st.divider()
                st.info(f"- Tokens: {len(encoding.encode(part))}\n- Length: {len(part)}")


def select_column_options(prefix: str, df: pd.DataFrame) -> tuple:
    col1, col2, col3 = st.columns(3)
    with col1:
        index = st.selectbox(f"{prefix}. Index", df.index, df.index[-1])
    with col2:
        column = st.selectbox(f"{prefix}. Column", df.columns)
    with col3:
        split_option = st.selectbox(f"{prefix}. Split", [None, "##", "###"], None)
    return index, column, split_option


def display_content_with_toggle(prefix: str, content: str, split_option: str | None, encoding: Encoding) -> None:
    if st.toggle(f"{prefix}. Raw Text"):
        st.divider()
        with st.container(height=700, border=False):
            display_raw_text(content, split_option, encoding)
    else:
        st.divider()
        with st.container(height=700, border=False):
            display_markdown(content, split_option, encoding)
    st.divider()
    st.info(f"- Tokens: {len(encoding.encode(str(content)))}\n- Length: {len(str(content))}")


def compare_texts(text1: str, text2: str) -> None:
    d = Differ()
    comparison = list(d.compare(list(text1), list(text2)))
    formatted_comparison = []
    for line in comparison:
        if line.startswith("? "):
            continue
        elif line.startswith("+ "):
            formatted_comparison.append(f":green[{line[2:]}]")
        elif line.startswith("- "):
            formatted_comparison.append(f":red[~~{line[2:]}~~]")
        else:
            formatted_comparison.append(line[2:])
    st.markdown("".join(formatted_comparison))


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
            option1_ind, option1_col, option1_split = select_column_options("1", df)
            display_content_with_toggle("1", df.loc[option1_ind, option1_col], option1_split, encoding)

    with col2:
        with st.container(border=True):
            option2_ind, option2_col, option2_split = select_column_options("2", df)
            display_content_with_toggle("2", df.loc[option2_ind, option2_col], option2_split, encoding)

    with st.container(border=True):
        if st.toggle("Compare"):
            st.divider()
            with st.container(height=700, border=False):
                compare_texts(
                    str(df.loc[option1_ind, option1_col]),
                    str(df.loc[option2_ind, option2_col])
                )