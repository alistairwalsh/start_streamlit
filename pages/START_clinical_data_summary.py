import streamlit as st

st.write("""
START-PrePARE
(sub-study and stand alone)""")

option = st.multiselect(
    'Which timepoints?',
    ('Baseline', 'T=0', '12-24 hours','Day 3-7','90 days','12 months'),default = 'Baseline')


if 'Baseline' in option:

    st.write("""Baseline
(recruitment up to 3 days post-stroke)""")

    st.json({"Assessment":
    ["Radiological scans and report",
    "Physical examination",
    "Past medical history",
    "Concomitant medications",
    "Current stroke information",
    {"Neurological": ["NIHSS"]},
    "Pre Stroke mRS",
    "Blood for biomarkers",
    "Laboratory tests"]
})


if 'T=0' in option:

    st.write("""T=0
(2-3 hours after baseline if recruited <24 hrs)""")
    st.json({"Assessment":
    ["Blood for biomarkers",
    "Laboratory tests"
]})

if '12-24 hours' in option:

    st.write("""12-24 hours
(12-24 hrs post T=0 or 12-24 hrs for those recruited > 24 hrs post stroke and < 48 hrs)""")
    st.json({"Assessment":
    [{"Neurological": ["NIHSS"]},
    "Blood for biomarkers",
    "Laboratory tests"]
})

if 'Day 3-7' in option:
    st.write("""Day 3-7
(3-7 days post stroke onset, can be the same time point at recruitment)""")
    st.json({"Assessments":
    ["Blood for biomarkers",
        {"Neurological": ["NIHSS"]},
        {"Cognition": ["MoCA"]},
        {"Depression": ["History of depression (pre-stroke)", "MADRS"]},
        {"Lifestyle":["Physical Risk Factors",{"Physical Activity": ["RAPA"]},"Diet Q"]},
            "Demographics",
        "Laboratory tests",
        "Concomitant medications"]})


if '90 days' in option:
    st.write("""90 days
(+/- 7 days)""")
    st.json(
    {"Assessments":
    [{"Neurological": ["NIHSS"]},
"Physical examination",
{"Lifestyle":
["Physical Risk Factors",
"RAPA",
"Diet Q",
"WSAS"]},
{"Function":
["mRS",
"BI",
"SIS"]},
"Neuroimaging",
{"Cognition":
["Yes/no",
"Shape cancellation",
"Trail making test B",
"Digit Span",
"Ravens",
"STROOP",
"MMSE",
"MoCA"]},
{"Depression": 
["MADRS",
"History of depression"]}, 
{"Sensorimotor":
["ARAT",
"TUGT",
"TDT"]},
{"Participation": ["ACS"]},
"Blood for biomarkers",
"Concomitant medications",
"Laboratory tests",
"Further stroke"
]
}
)

if '12 months' in option:
    st.write("""12 months
(+/- 7 days)""")
    st.json({"Assessments":[{"Neurological": "NIHSS"},
"Physical examination",
{"Lifestyle":
["Physical Risk Factors",
"RAPA",
"Diet Q",
"WSAS"]},
{"Function":
["mRS",
"BI",
"SIS"]},
"Neuroimaging",
{"Cognition":
["Yes/no",
"Shape cancellation",
"Trail making test B",
"Digit Span",
"Raven’s",
"STROOP",
"MMSE",
"MoCA"]},
{"Depression": 
["MADRS",
"History of depression"]},
{"Sensorimotor":
["ARAT",
"TUGT",
"TDT"]},
{"Participation": ["ACS"]},
"Blood for biomarkers",
"Concomitant medications",
"Laboratory tests",
"Further stroke"
]})

