import streamlit as st

st.set_page_config(
    page_title="Group 11 FYP | VHIS & Chronic Disease Management",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
    <style>
    .main {
        background-color: #f8fafc;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    .gradient-title {
        background: linear-gradient(90deg, #1e3a8a 0%, #0d9488 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        font-size: 2.2rem;
        margin-bottom: 0.2rem;
    }
    .card {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        margin-bottom: 1rem;
        border-left: 5px solid #0d9488;
    }
    [data-testid="stSidebar"] {
        background-color: #0f172a;
        color: white;
    }
    [data-testid="stSidebar"] .stRadio label {
        color: #f1f5f9 !important;
        font-weight: 500;
    }
    </style>
""", unsafe_allow_html=True)

st.sidebar.image("https://img.icons8.com/color/96/hospital-3.png", width=80)
st.sidebar.markdown("### **Group 11 FYP Portal**")
st.sidebar.markdown("---")

lang = st.sidebar.selectbox("🌐 Language / 語言", ["繁體中文", "English"])

st.sidebar.markdown("---")


if lang == "繁體中文":
    menu = st.sidebar.radio(
        "導航選單",
        [
            "🏠 首頁與摘要",
            "📌 背景與問題陳述",
            "🎯 研究目的與對象",
            "📊 研究方法與設定",
            "📈 進度與預期貢獻",
            "📱 參與問卷與 QR Code"
        ]
    )
else:
    menu = st.sidebar.radio(
        "Navigation",
        [
            "🏠 Home & Overview",
            "📌 Background & Rationale",
            "🎯 Objectives & Participants",
            "📊 Methodology & Settings",
            "📈 Timeline & Contributions",
            "📱 Survey & QR Code"
        ]
    )

if menu in ["🏠 首頁與摘要", "🏠 Home & Overview"]:
    if lang == "繁體中文":
        st.markdown('<p class="gradient-title">香港市民對慢性病管理自願醫療保險計劃 (VHIS) 之公眾認知與理解</p>', unsafe_allow_html=True)
        st.markdown("##### **畢業專題研究 | 第十一組 (Group 11)**[cite: 1]")
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div class="card">
            <h3>👋 歡迎來到我們的專案網站</h3>
            <p>本專案深入探討香港 40 至 60 歲居民對<b>自願醫療保險計劃 (VHIS)</b> 的認知、理解程度，以及其在慢性疾病管理（如糖尿病、高血壓等）中所扮演的角色[cite: 2]。</p>
            <p>透過本網站，您可以快速了解我們的研究背景、嚴謹的方法學、各階段進度，並在最後參與我們的學術問卷調查[cite: 2]。</p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div class="card" style="border-left-color: #1e3a8a;">
            <h4>📊 核心數據速覽</h4>
            <ul>
                <li><b>目標樣本數：</b> 200 位香港居民[cite: 2]</li>
                <li><b>研究對象：</b> 40–60歲、帶有慢性疾病者[cite: 2]</li>
                <li><b>調查地區：</b> 中西區、上環、觀塘[cite: 2]</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown('<p class="gradient-title">Public Awareness and Understanding of VHIS for Chronic Disease Management in Hong Kong</p>', unsafe_allow_html=True)
        st.markdown("##### **Final Year Project | Group 11**[cite: 1]")
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div class="card">
            <h3>👋 Welcome to Our Project Portal</h3>
            <p>This project investigates public awareness, understanding, and perceptions of the <b>Voluntary Health Insurance Scheme (VHIS)</b> regarding chronic disease management among Hong Kong residents aged 40–60[cite: 2].</p>
            <p>Explore our background, methodology, timeline, and participate in our survey[cite: 2].</p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div class="card" style="border-left-color: #1e3a8a;">
            <h4>📊 Key Metrics</h4>
            <ul>
                <li><b>Target Sample:</b> 200 HK residents[cite: 2]</li>
                <li><b>Target Cohort:</b> Aged 40–60 with NCDs[cite: 2]</li>
                <li><b>Districts:</b> Central, Sheung Wan, Kwun Tong[cite: 2]</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)

elif menu in ["📌 背景與問題陳述", "📌 Background & Rationale"]:
    if lang == "繁體中文":
        st.markdown('<p class="gradient-title">背景與問題陳述</p>', unsafe_allow_html=True)
        st.markdown("---")
        st.markdown("""
        <div class="card">
        <h4>🏥 香港面臨的醫療挑戰</h4>
        <p>香港正面臨嚴峻的人口老化問題，慢性疾病（如糖尿病、心血管疾病）逐年攀升[cite: 2]。公立醫院長期面臨專科輪候時間過長、醫療系統不勝負荷的困境[cite: 2]。</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div class="card">
            <h4>🔍 VHIS 的政策盲點</h4>
            <p>政府推出<b>自願醫療保險計劃 (VHIS)</b> 旨在引導市民使用私營醫療服務。然而，基層與中青年市民往往對保單條款認知不足，誤以為 VHIS 能全額賠償所有長期慢性藥物開支[cite: 2]。</p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div class="card">
            <h4>💡 研究契機</h4>
            <p>當慢性病患者發現私家藥費高昂時，往往會回流公立醫院拿藥，導致 VHIS 未能有效分流公營醫療壓力[cite: 2]。本研究旨在填補此一政策認知落差[cite: 2]。</p>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown('<p class="gradient-title">Background & Problem Statement</p>', unsafe_allow_html=True)
        st.markdown("---")
        st.markdown("""
        <div class="card">
        <h4>🏥 Healthcare Challenges in Hong Kong</h4>
        <p>Hong Kong is facing an aging population with rising noncommunicable diseases (NCDs) like diabetes and heart failure[cite: 2], placing heavy pressure on public hospitals[cite: 2].</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div class="card">
            <h4>🔍 Policy Blind Spots of VHIS</h4>
            <p>While VHIS encourages private healthcare utilization, citizens often misunderstand its coverage limits, especially regarding long-term outpatient chronic medications[cite: 2].</p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div class="card">
            <h4>💡 Rationale</h4>
            <p>High private drug costs drive chronic patients back to public clinics, limiting VHIS's effectiveness in relieving public sector workload[cite: 2]. This study aims to bridge this knowledge gap[cite: 2].</p>
            </div>
            """, unsafe_allow_html=True)

elif menu in ["🎯 研究目的與對象", "🎯 Objectives & Participants"]:
    if lang == "繁體中文":
        st.markdown('<p class="gradient-title">研究目的與參與者</p>', unsafe_allow_html=True)
        st.markdown("---")
        st.markdown("""
        <div class="card">
        <h4>🎯 研究目的 (Research Objectives)</h4>
        <ol>
            <li>評估香港 40–60 歲居民對 VHIS 的認知與理解水平[cite: 2]。</li>
            <li>識別公眾獲取 VHIS 資訊的主要管道[cite: 2]。</li>
            <li>探討公眾對 VHIS 在慢性疾病管理中效益的看法[cite: 2]。</li>
            <li>檢視不同人口學特徵及慢性病狀況與 VHIS 認知之關聯[cite: 2]。</li>
        </ol>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div class="card" style="border-left-color: #3b82f6;">
        <h4>👥 參與者納入與排除標準</h4>
        <ul>
            <li><b>納入條件：</b> 香港永久性居民 / 持有效香港身分證，年齡 40–60 歲，過去 12 個月內經醫生診斷至少患有一種慢性疾病[cite: 2]。</li>
            <li><b>排除條件：</b> 具認知或精神障礙、無法閱讀繁體中文或英文、居於院舍或醫院者[cite: 2]。</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown('<p class="gradient-title">Research Objectives & Participants</p>', unsafe_allow_html=True)
        st.markdown("---")
        st.markdown("""
        <div class="card">
        <h4>🎯 Research Objectives</h4>
        <ol>
            <li>Assess the level of awareness and understanding of VHIS among HK residents aged 40–60[cite: 2].</li>
            <li>Identify main sources of information regarding VHIS[cite: 2].</li>
            <li>Explore public perceptions of VHIS benefits in chronic disease management[cite: 2].</li>
            <li>Examine associations between demographics, chronic disease status, and VHIS awareness[cite: 2].</li>
        </ol>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div class="card" style="border-left-color: #3b82f6;">
        <h4>👥 Inclusion & Exclusion Criteria</h4>
        <ul>
            <li><b>Inclusion:</b> HK permanent/valid ID holders, aged 40–60, self-reported doctor-diagnosed chronic disease in the past 12 months[cite: 2].</li>
            <li><b>Exclusion:</b> Cognitive/mental illness, unable to read Traditional Chinese/English, institutionalized residents[cite: 2].</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

elif menu in ["📊 研究方法與設定", "📊 Methodology & Settings"]:
    if lang == "繁體中文":
        st.markdown('<p class="gradient-title">研究方法與設定</p>', unsafe_allow_html=True)
        st.markdown("---")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div class="card">
            <h4>📋 研究設計</h4>
            <ul>
                <li><b>設計：</b> 量化、觀察性、橫斷面調查設計[cite: 2]。</li>
                <li><b>問卷結構：</b> 人口統計、健康習慣、醫療尋求行為、VHIS 認知與醫改態度[cite: 2]。</li>
                <li><b>抽樣：</b> 於指定診所與醫院採用便利抽樣法，目標樣本 200 人[cite: 2]。</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div class="card">
            <h4>📍 研究設定地點</h4>
            <p>涵蓋香港不同社會經濟光譜地區：</p>
            <ul>
                <li><b>觀塘區：</b> 觀塘家庭醫學綜合診所、觀塘地區康健中心、聯合醫院[cite: 2]。</li>
                <li><b>中西區及上環：</b> 中區家庭醫學診所、東華醫院、卡諾撒醫院[cite: 2]。</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown('<p class="gradient-title">Methodology & Study Settings</p>', unsafe_allow_html=True)
        st.markdown("---")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div class="card">
            <h4>📋 Study Design</h4>
            <ul>
                <li><b>Design:</b> Quantitative, observational, cross-sectional survey[cite: 2].</li>
                <li><b>Questionnaire:</b> Demographics, health profile, healthcare-seeking behavior, VHIS literacy[cite: 2].</li>
                <li><b>Sampling:</b> Convenience sampling, target sample size of 200[cite: 2].</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div class="card">
            <h4>📍 Study Settings</h4>
            <ul>
                <li><b>Kwun Tong District:</b> GOPC, District Health Center, United Christian Hospital[cite: 2].</li>
                <li><b>Central & Sheung Wan:</b> Central District Family Medicine Clinic, Tung Wah Hospital, Canossa Hospital[cite: 2].</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)

elif menu in ["📈 進度與預期貢獻", "📈 Timeline & Contributions"]:
    if lang == "繁體中文":
        st.markdown('<p class="gradient-title">專案進度與預期貢獻</p>', unsafe_allow_html=True)
        st.markdown("---")
        st.markdown("""
        <div class="card">
        <h4>📅 專案進度</h4>
        <p>目前已完成文獻回顧、提案撰寫、問卷設計與先導研究（Pilot Study），正推進至倫理審批與正式數據收集[cite: 1, 2]。</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div class="card" style="border-left-color: #10b981;">
        <h4>🌟 預期貢獻</h4>
        <ul>
            <li>揭示市民對慢性病與 VHIS 的常見迷思與知識盲點[cite: 2]。</li>
            <li>協助公共機構與政策制定者優化公眾教育，提升基層醫療改革成效[cite: 2]。</li>
            <li>為香港未來可持續的醫療融資政策提供實證數據[cite: 2]。</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown('<p class="gradient-title">Timeline & Expected Contributions</p>', unsafe_allow_html=True)
        st.markdown("---")
        st.markdown("""
        <div class="card">
        <h4>📅 Project Timeline</h4>
        <p>Completed literature review, proposal drafting, questionnaire design, and pilot study. Moving forward to ethical approval and data collection[cite: 1, 2].</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div class="card" style="border-left-color: #10b981;">
        <h4>🌟 Expected Contributions</h4>
        <ul>
            <li>Identify public misconceptions regarding chronic diseases and VHIS[cite: 2].</li>
            <li>Assist public institutions in improving public health education and healthcare reform[cite: 2].</li>
            <li>Provide empirical evidence for sustainable healthcare financing policies in HK[cite: 2].</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

elif menu in ["📱 參與問卷與 QR Code", "📱 Survey & QR Code"]:
    if lang == "繁體中文":
        st.markdown('<p class="gradient-title">參與問卷與 QR Code 掃描</p>', unsafe_allow_html=True)
        st.markdown("---")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div class="card">
            <h3>🔗 線上問卷連結</h3>
            <p>如果您符合參與資格（香港居民、40–60 歲、具慢性病經驗），誠摯邀請您填寫我們的匿名問卷[cite: 2]：</p>
            <br>
            <a href="https://forms.gle/your-survey-link" target="_blank">
                <button style="background-color:#0d9488; color:white; padding:12px 24px; border:none; border-radius:8px; font-size:16px; font-weight:bold; cursor:pointer;">
                    🚀 點擊前往 Google 填寫問卷
                </button>
            </a>
            <br><br>
            <p style="font-size: 0.85rem; color: #64748b;">🔒 所有收集之資料絕對保密，僅供學術研究之用[cite: 2]。</p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div class="card" style="text-align: center;">
            <h4>📱 掃描 QR Code 了解更多 / 填寫問卷</h4>
            <p style="font-size: 0.85rem; color: #64748b;">請使用手機相機掃描下方 QR Code：</p>
            """, unsafe_allow_html=True)
            app_url = "https://share.streamlit.io/"
            qr_api_url = f"https://api.qrserver.com/v1/create-qr-code/?size=180x180&data={app_url}"
            st.image(qr_api_url, width=180)
            st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.markdown('<p class="gradient-title">Participate & QR Code</p>', unsafe_allow_html=True)
        st.markdown("---")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div class="card">
            <h3>🔗 Online Survey Link</h3>
            <p>If you are eligible, we warmly invite you to complete our anonymous questionnaire[cite: 2]:</p>
            <br>
            <a href="https://docs.google.com/forms/d/e/1FAIpQLSdFmp3cX8hKWT5GvhRTN-i7s_2ZM3UJv_lHaBG2c8cSfqNMUw/viewform?usp=header" target="_blank">
                <button style="background-color:#0d9488; color:white; padding:12px 24px; border:none; border-radius:8px; font-size:16px; font-weight:bold; cursor:pointer;">
                    🚀 Open Google Form Survey
                </button>
            </a>
            <br><br>
            <p style="font-size: 0.85rem; color: #64748b;">🔒 All data collected is strictly anonymous and for academic research only[cite: 2].</p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div class="card" style="text-align: center;">
            <h4>📱 Scan QR Code</h4>
            <p style="font-size: 0.85rem; color: #64748b;">Scan the QR code with your mobile camera:</p>
            """, unsafe_allow_html=True)
            app_url = "https://share.streamlit.io/"
            qr_api_url = f"https://api.qrserver.com/v1/create-qr-code/?size=180x180&data={app_url}"
            st.image(qr_api_url, width=180)
            st.markdown("</div>", unsafe_allow_html=True)