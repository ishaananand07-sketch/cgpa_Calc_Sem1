import streamlit as st
import pandas as pd

st.set_page_config(page_title="CGPA Calculator", layout="centered")
st.title("🎓 CGPA Calculator – Semester 1")

def gp(p):
    if p >= 91: return 10
    elif p >= 81: return 9
    elif p >= 71: return 8
    elif p >= 61: return 7
    elif p >= 51: return 6
    elif p >= 41: return 5
    else: return 0

group = st.selectbox("Select Group", [1, 2])
subjects = []

# ======================= GROUP 1 =======================
if group == 1:
    st.subheader("Group 1")

    # LAC
    st.markdown("### Linear Algebra and Calculus (LAC)")
    ese = st.number_input("ESE (60)", 0.0, 60.0, 0.0, 1.0, key="g1_lac_ese")
    ise = st.number_input("ISE (20)", 0.0, 20.0, 0.0, 1.0, key="g1_lac_ise")
    cie = st.number_input("CIE (20)", 0.0, 20.0, 0.0, 1.0, key="g1_lac_cie")
    tw  = st.number_input("TW (60)", 0.0, 60.0, 0.0, 1.0, key="g1_lac_tw")
    total = ese + ise + cie + (tw / 60 * 25)
    subjects.append(("LAC", 4, total / 125 * 100, gp(total / 125 * 100)))

    # QP
    st.markdown("### Quantum Physics (QP)")
    qp = (
        st.number_input("ESE (60)", 0.0, 60.0, 0.0, 1.0, key="g1_qp_ese") +
        st.number_input("ISE (20)", 0.0, 20.0, 0.0, 1.0, key="g1_qp_ise") +
        st.number_input("CIE (20)", 0.0, 20.0, 0.0, 1.0, key="g1_qp_cie")
    )
    subjects.append(("QP", 2, qp, gp(qp)))

    # QPL
    st.markdown("### Quantum Physics Lab (QPL)")
    qpl = st.number_input("TW (120)", 0.0, 120.0, 0.0, 1.0, key="g1_qpl_tw")
    subjects.append(("QPL", 1, qpl / 120 * 100, gp(qpl / 120 * 100)))

    # MFR
    st.markdown("### Mechanics for Robotics (MFR)")
    mfr = (
        st.number_input("ESE (60)", 0.0, 60.0, 0.0, 1.0, key="g1_mfr_ese") +
        st.number_input("ISE (20)", 0.0, 20.0, 0.0, 1.0, key="g1_mfr_ise") +
        st.number_input("CIE (20)", 0.0, 20.0, 0.0, 1.0, key="g1_mfr_cie")
    )
    subjects.append(("MFR", 2, mfr, gp(mfr)))

    # MFRL
    st.markdown("### Mechanics for Robotics Lab (MFRL)")
    mfrl = st.number_input("TW (110)", 0.0, 110.0, 0.0, 1.0, key="g1_mfrl_tw")
    subjects.append(("MFRL", 1, mfrl / 110 * 100, gp(mfrl / 110 * 100)))

    # IEEE
    st.markdown("### Integrated Electrical and Electronics Engineering (IEEE)")
    ieee = (
        st.number_input("ESE (60)", 0.0, 60.0, 0.0, 1.0, key="g1_ieee_ese") +
        st.number_input("ISE (20)", 0.0, 20.0, 0.0, 1.0, key="g1_ieee_ise") +
        st.number_input("CIE (20)", 0.0, 20.0, 0.0, 1.0, key="g1_ieee_cie")
    )
    subjects.append(("IEEE", 2, ieee, gp(ieee)))

    # IEEEL
    st.markdown("### Integrated Electrical and Electronics Engineering Lab (IEEEL)")
    ieeel = st.number_input("TW (120)", 0.0, 120.0, 0.0, 1.0, key="g1_ieeel_tw")
    subjects.append(("IEEEL", 1, ieeel / 120 * 100, gp(ieeel / 120 * 100)))

    # CPPS
    st.markdown("### C Programming for Problem Solving (CPPS)")
    cpps = (
        st.number_input("ESE (60)", 0.0, 60.0, 0.0, 1.0, key="g1_cpps_ese") +
        st.number_input("ISE (20)", 0.0, 20.0, 0.0, 1.0, key="g1_cpps_ise") +
        st.number_input("CIE (20)", 0.0, 20.0, 0.0, 1.0, key="g1_cpps_cie")
    )
    subjects.append(("CPPS", 2, cpps, gp(cpps)))

    # CPPSL
    st.markdown("### C Programming for Problem Solving Lab (CPPSL)")
    cppsl = st.number_input("TW (100)", 0.0, 100.0, 0.0, 1.0, key="g1_cppsl_tw")
    subjects.append(("CPPSL", 1, cppsl, gp(cppsl)))

    # FAB
    st.markdown("### FAB Lab (FL)")
    fab = st.number_input("TW (50)", 0.0, 50.0, 0.0, 1.0, key="g1_fab_tw")
    subjects.append(("FL", 1, fab / 50 * 100, gp(fab / 50 * 100)))

    # IKS
    st.markdown("### Indian Knowledge System (IKS)")
    iks = st.number_input("TW (30)", 0.0, 30.0, 0.0, 1.0, key="g1_iks_tw")
    subjects.append(("IKS", 2, iks / 30 * 100, gp(iks / 30 * 100)))

# ======================= GROUP 2 =======================
elif group == 2:
    st.subheader("Group 2")

    st.markdown("### Linear Algebra and Calculus (LAC)")
    ese = st.number_input("ESE (60)", 0.0, 60.0, 0.0, 1.0, key="g2_lac_ese")
    ise = st.number_input("ISE (20)", 0.0, 20.0, 0.0, 1.0, key="g2_lac_ise")
    cie = st.number_input("CIE (20)", 0.0, 20.0, 0.0, 1.0, key="g2_lac_cie")
    tw  = st.number_input("TW (60)", 0.0, 60.0, 0.0, 1.0, key="g2_lac_tw")
    total = ese + ise + cie + (tw / 60 * 25)
    subjects.append(("LAC", 4, total / 125 * 100, gp(total / 125 * 100)))

    st.markdown("### Chemical Science and Technology (CST)")
    cst = (
        st.number_input("ESE (60)", 0.0, 60.0, 0.0, 1.0, key="g2_cst_ese") +
        st.number_input("ISE (20)", 0.0, 20.0, 0.0, 1.0, key="g2_cst_ise") +
        st.number_input("CIE (20)", 0.0, 20.0, 0.0, 1.0, key="g2_cst_cie")
    )
    subjects.append(("CST", 2, cst, gp(cst)))

    st.markdown("### Chemical Science and Technology Lab (CSTL)")
    cstl = st.number_input("TW (100)", 0.0, 100.0, 0.0, 1.0, key="g2_cstl_tw")
    subjects.append(("CSTL", 1, cstl, gp(cstl)))

    st.markdown("### Computer Graphics and Design (CGD)")
    cgd = (
        st.number_input("ESE (60)", 0.0, 60.0, 0.0, 1.0, key="g2_cgd_ese") +
        st.number_input("ISE (20)", 0.0, 20.0, 0.0, 1.0, key="g2_cgd_ise") +
        st.number_input("CIE (20)", 0.0, 20.0, 0.0, 1.0, key="g2_cgd_cie")
    )
    subjects.append(("CGD", 2, cgd, gp(cgd)))

    st.markdown("### Computer Graphics and Design Lab (CGDL)")
    cgdl = st.number_input("TW (70)", 0.0, 70.0, 0.0, 1.0, key="g2_cgdl_tw")
    subjects.append(("CGDL", 1, cgdl / 70 * 100, gp(cgdl / 70 * 100)))

    st.markdown("### C Programming for Problem Solving (CPPS)")
    cpps = (
        st.number_input("ESE (60)", 0.0, 60.0, 0.0, 1.0, key="g2_cpps_ese") +
        st.number_input("ISE (20)", 0.0, 20.0, 0.0, 1.0, key="g2_cpps_ise") +
        st.number_input("CIE (20)", 0.0, 20.0, 0.0, 1.0, key="g2_cpps_cie")
    )
    subjects.append(("CPPS", 2, cpps, gp(cpps)))

    st.markdown("### C Programming for Problem Solving Lab (CPPSL)")
    cppsl = st.number_input("TW (100)", 0.0, 100.0, 0.0, 1.0, key="g2_cppsl_tw")
    subjects.append(("CPPSL", 1, cppsl, gp(cppsl)))

    st.markdown("### Innovative Idea and Design Thinking Lab (IIDTL)")
    iidtl = st.number_input("TW (60)", 0.0, 60.0, 0.0, 1.0, key="g2_iidtl_tw")
    subjects.append(("IIDTL", 1, iidtl / 60 * 100, gp(iidtl / 60 * 100)))

    st.markdown("### Environment and Sustainable Engineering (ESE)")
    ese2 = (
        st.number_input("ESE (60)", 0.0, 60.0, 0.0, 1.0, key="g2_ese_ese") +
        st.number_input("ISE (20)", 0.0, 20.0, 0.0, 1.0, key="g2_ese_ise") +
        st.number_input("CIE (20)", 0.0, 20.0, 0.0, 1.0, key="g2_ese_cie")
    )
    subjects.append(("ESE", 2, ese2, gp(ese2)))

    st.markdown("### Soft Skills (SS)")
    ss_tw = st.number_input("TW (40)", 0.0, 40.0, 0.0, 1.0, key="g2_ss_tw")
    ss_cie = st.number_input("CIE (25)", 0.0, 25.0, 0.0, 1.0, key="g2_ss_cie")
    ss_total = (ss_tw / 40 * 25) + ss_cie
    subjects.append(("SS", 2, ss_total / 50 * 100, gp(ss_total / 50 * 100)))

    st.markdown("### Cocurricular Activity-1 (CCA-1)")
    cca = st.number_input("TW (25)", 0.0, 25.0, 0.0, 1.0, key="g2_cca_tw")
    subjects.append(("CCA-1", 1, cca / 25 * 100, gp(cca / 25 * 100)))

# ================= RESULT =================
if subjects and st.button("🎯 Calculate CGPA"):
    df = pd.DataFrame(subjects, columns=["Subject", "Credits", "Percentage", "Grade Point"])
    df["Credit Points"] = df["Credits"] * df["Grade Point"]
    df.index = range(1, len(df) + 1)  # SR starts from 1
    st.dataframe(df, use_container_width=True)
    cgpa = df["Credit Points"].sum() / df["Credits"].sum()
    st.success(f"✅ Your CGPA is **{round(cgpa, 2)}**")
