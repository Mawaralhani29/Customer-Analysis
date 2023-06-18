import streamlit as st
import streamlit.components.v1 as components

import pandas as pd
import pickle

# Membuka file pickle
with open('test_results.pkl', 'rb') as file:
    dataset = pickle.load(file)

def predict(sk_id_curr):
    # Get the prediction and probability for the specified SK_ID_CURR
    result = dataset.loc[dataset['SK_ID_CURR'] == sk_id_curr]

    if result.empty:
        return None, ""
    else:
        prediction = result.iloc[0]['PREDICTION']
        probability = result.iloc[0]['PROBABILITY']
        return prediction, probability

def main():
    st.title('HOME CREDIT')

    sk_id_curr = st.text_input('SK ID CURR:', value='', help='100001 - 456250')
    prediction = None
    probability = ""
    if st.button("Predict"):
        if sk_id_curr:
            sk_id_curr = int(sk_id_curr)
            prediction, probability = predict(sk_id_curr)
            if prediction is None:
                st.warning("No prediction found for the specified SK_ID_CURR.")
            else:
                if prediction == 1:
                    st.success("Prediction: Defaulters")
                else:
                    st.success("Prediction: Non Defaulters")
                st.success("Probability: {}".format(probability))

    st.markdown(
        '''
        <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(to bottom, #ffffff, #2b80ff);
            margin: 0;
            padding: 130px;
        }

        h1 {
            text-align: center;
            color: #fffff;
            font-size: 40px;
            font-weight: bold;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
        }

        .result-container {
            max-width: 400px;
            margin: 0 auto;
            background-color: #fff;
            padding: 20px;
            border-radius: 4px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }

        .result-label {
            font-weight: bold;
        }

        .result-value {
            margin-bottom: 10px;
        }

        .back-next-buttons {
            text-align: center;
            margin-top: 20px;
        }

        .button {
            display: inline-block;
            padding: 8px 16px;
            font-size: 14px;
            font-weight: bold;
            text-align: center;
            text-decoration: none;
            background-color: #DCAE1D;
            color: #fff;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            transition: background-color 0.3s;
        }

        .button:hover {
            background-color: #a7880c;
        }

        .power-bi-embed {
            width: 100%;
            height: 500px;
            margin-top: 20px;
        }

        .hidden {
            display: none;
        }
        </style>
        ''',
        unsafe_allow_html=True
    )
    st.markdown('<div id="powerBISection" class="hidden">', unsafe_allow_html=True)
    power_bi_url = 'https://app.powerbi.com/view?r=eyJrIjoiZjI2ZmYzNTgtMWQ2Ny00MjE0LWJlMDQtYWI0NDdiZTBmNGFkIiwidCI6ImFmMmMwNzM0LWNiNDItNDY0Zi1iNmJmLTJhMjQxYjZhZGE1NiIsImMiOjEwfQ%3D%3D'
    st.markdown(f'<iframe id="powerBIEmbed" class="power-bi-embed" src="{power_bi_url}" frameborder="0" allowFullScreen="true"></iframe>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    components.html(
        '''
        <script>
            function showPowerBI() {
                document.getElementById("powerBISection").classList.remove("hidden");
            }
        </script>
        ''',
        height=0
    )
    st.write("Develop by: Mawar Alhani")
if __name__ == '__main__':
    main()
