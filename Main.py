# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger
import pandas as pd

LOGGER = get_logger(__name__)
st.write("# MVP Petroleo! :oil_drum: ")


petroleo_base = pd.read_csv("https://raw.githubusercontent.com/Raphabal/techchallenge04deploy/main/BDBase.csv", sep=';')
petroleo_base.set_index('data', inplace=True)

previsao_base = pd.read_csv("https://raw.githubusercontent.com/Raphabal/techchallenge04deploy/main/base_predicao.csv", sep=';')
previsao_base = previsao_base.rename(columns={'ds': 'data', 'yhat': 'valor'})
previsao_base.set_index('data', inplace=True)

st.write("## Grafico de preços do petroleo ao longo dos anos! :chart_with_upwards_trend:")
st.line_chart(data=petroleo_base['valor'])


st.write("## Grafico previsao! :chart:")
st.line_chart(data=previsao_base['valor'])

st.write(" Tabela de preços do petroleo ao longo dos anos! :dollar:")
st.dataframe(data=petroleo_base['valor'])
st.dataframe(previsao_base['valor'])


def run():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )

    st.write("# Welcome to Streamlit! 👋")

    st.sidebar.success("Select a demo above.")

    st.markdown(
        """
        Streamlit is an open-source app framework built specifically for
        Machine Learning and Data Science projects.
        **👈 Select a demo from the sidebar** to see some examples
        of what Streamlit can do!
        ### Want to learn more?
        - Check out [streamlit.io](https://streamlit.io)
        - Jump into our [documentation](https://docs.streamlit.io)
        - Ask a question in our [community
          forums](https://discuss.streamlit.io)
        ### See more complex demos
        - Use a neural net to [analyze the Udacity Self-driving Car Image
          Dataset](https://github.com/streamlit/demo-self-driving)
        - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
    """
    )


if __name__ == "__main__":
    run()
