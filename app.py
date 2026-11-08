import streamlit as st

st.set_page_config(
    page_title="Public Awareness and Understanding of the Voluntary Health Insurance Scheme (VHIS) for Chronic Disease Management in Hong Kong 香港民眾對醫療改革「自願健保計畫」的認知情況 FYP (Group 11)",
    page_icon="🏥",
    layout="wide",
)

# Header Section
st.title(
    "Public Awareness and Understanding of the Voluntary Health Insurance Scheme (VHIS)"
    "for Chronic Disease Management in Hong Kong"
)
st.subheader("Group 11 Final Year Project")
st.markdown("---")

# Sidebar navigation
st.sidebar.title("Navigation")
section = st.sidebar.radio(
    "Go to",
    [
        "Home & Overview",
        "Background & Rationale",
        "Research Objectives",
        "Methodology",
        "Participate / Survey",
    ],
)

if section == "Home & Overview":
  st.header("Welcome to Our Final Year Project Portal")
  st.markdown(
      "This website outlines our research project investigating public"
      " awareness, understanding, and perceptions of the **Voluntary Health"
      " Insurance Scheme (VHIS)** in relation to chronic disease management"
      " among Hong Kong residents aged 40–60 years."
  )

  col1, col2 = st.columns(2)
  with col1:
    st.info("🎯 **Target Population**\nHong Kong residents aged 40–60 with chronic disease.")
  with col2:
    st.success(
        "📍 **Study Settings**\nCentral, Sheung Wan, and Kwun Tong districts."
    )

elif section == "Background & Rationale":
  st.header("Background & Problem Statement")
  st.markdown(
      "Noncommunicable diseases (NCDs) like diabetes and hypertension are rising"
      " in Hong Kong's aging population, putting immense pressure on public"
      " hospitals. While the government introduced the **Voluntary Health"
      " Insurance Scheme (VHIS)** to encourage private healthcare utilization,"
      " public awareness of its exact coverage, benefits, and limitations"
      " remains low—particularly regarding long-term outpatient chronic"
      " medication costs."
  )

elif section == "Research Objectives":
  st.header("Research Objectives")
  st.markdown(
      "1. **Assess Awareness:** Evaluate the level of awareness and"
      " understanding of VHIS among Hong Kong residents aged 40–60 years.\n2."
      " **Identify Information Sources:** Determine where respondents learn"
      " about VHIS.\n3. **Explore Perceptions:** Examine public perceptions of"
      " VHIS benefits and effectiveness in chronic disease management.\n4."
      " **Analyze Demographics:** Investigate associations between demographic"
      " characteristics, chronic disease status, and VHIS awareness."
  )

elif section == "Methodology":
  st.header("Methodology & Study Design")
  st.markdown(
      "- **Study Design:** Quantitative, observational, cross-sectional survey"
      " design.\n- **Sample Size:** Target of 200 participants using convenience"
      " sampling.\n- **Settings:** General and specialist outpatient clinics"
      " across Kwun Tong, Central, and Sheung Wan.\n- **Instrument:**"
      " Self-administered bilingual questionnaire (Traditional Chinese &"
      " English) covering demographics, health profiles, healthcare-seeking"
      " behavior, and VHIS literacy."
  )

elif section == "Participate / Survey":
  st.header("Participate in Our Study")
  st.markdown(
      "If you are eligible (Hong Kong resident, aged 40–60, self-reported"
      " chronic disease), we invite you to complete our anonymous survey!"
  )
  st.markdown(
      "[Click here to open the Google Form Survey]"
      "(https://docs.google.com/forms/d/e/1FAIpQLSdFmp3cX8hKWT5GvhRTN-i7s_2ZM3UJv_lHaBG2c8cSfqNMUw/viewform?usp=header)"
  )
  st.warning(
      "Note: All collected data is strictly anonymous and used exclusively for"
      " academic research purposes."
  )