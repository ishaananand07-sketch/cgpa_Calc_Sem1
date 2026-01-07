import streamlit as st
import pandas as pd

st.set_page_config(page_title="CGPA Calculator", layout="centered")
st.title("🎓 CGPA Calculator – Semester 1")

# ---------------- Grade Point Function ----------------
def gp(perc):
    if perc >= 91: return 10
    elif perc >= 81: return 9
    elif perc >= 71: return 8
    elif perc >= 61: return 7
    elif perc >= 51: return 6
    elif perc >= 41: return 5
    else: return 0

group = st.selectbox("Select Group", [1, 2], key="group")
subjects = []

# ======================= GROUP 1 =======================
if group == 1:
    st.subheader("Group 1 – Enter Marks")

    # LAC (TW 60 → 25)
    st.markdown("### Linear Algebra & Calculus (LAC)")
    lac_ese = st.number_input("ESE (60)", 0.0, 60.0)
    lac_ise = st.number_input("ISE (20)", 0.0, 20.0)
    lac_cie = st.number_input("CIE (20)", 0.0, 20.0)
    lac_tw  = st.number_input("TW (60)", 0.0, 60.0)
    lac_total = lac_ese + lac_ise + lac_cie + (lac_tw / 60 * 25)
    lac_perc = lac_total / 125 * 100
    subjects.append(("LAC", 4, lac_perc, gp(lac_perc)))

    # QP
    st.markdown("### Quantum Physics (QP)")
    qp = (
        st.number_input("QP ESE (60)", 0.0, 60.0) +
        st.number_input("QP ISE (20)", 0.0, 20.0) +
        st.number_input("QP CIE (20)", 0.0, 20.0)
    )
    subjects.append(("QP", 2, qp, gp(qp)))

    # QPL (120 → 25)
    st.markdown("### Quantum Physics Lab (QPL)")
    qpl = st.number_input("QPL TW (120)", 0.0, 120.0)
    qpl_perc = (qpl / 120 * 25) / 25 * 100
    subjects.append(("QPL", 1, qpl_perc, gp(qpl_perc)))

    # MFR
    st.markdown("### Mechanics for Robotics (MFR)")
    mfr = (
        st.number_input("MFR ESE (60)", 0.0, 60.0) +
        st.number_input("MFR ISE (20)", 0.0, 20.0) +
        st.number_input("MFR CIE (20)", 0.0, 20.0)
    )
    subjects.append(("MFR", 2, mfr, gp(mfr)))

    # MFRL (110 → 25)
    st.markdown("### Mechanics for Robotics Lab (MFRL)")
    mfrl = st.number_input("MFRL TW (110)", 0.0, 110.0)
    mfrl_perc = (mfrl / 110 * 25) / 25 * 100
    subjects.append(("MFRL", 1, mfrl_perc, gp(mfrl_perc)))

    # IEEE
    st.markdown("### Integrated Electrical & Electronics (IEEE)")
    ieee = (
        st.number_input("IEEE ESE (60)", 0.0, 60.0) +
        st.number_input("IEEE ISE (20)", 0.0, 20.0) +
        st.number_input("IEEE CIE (20)", 0.0, 20.0)
    )
    subjects.append(("IEEE", 2, ieee, gp(ieee)))

    # IEEEL (120 → 25)
    st.markdown("### IEEE Lab (IEEEL)")
    ieeel = st.number_input("IEEEL TW (120)", 0.0, 120.0)
    ieeel_perc = (ieeel / 120 * 25) / 25 * 100
    subjects.append(("IEEEL", 1, ieeel_perc, gp(ieeel_perc)))

    # CPPS
    st.markdown("### C Programming for Problem Solving (CPPS)")
    cpps = (
        st.number_input("CPPS ESE (60)", 0.0, 60.0) +
        st.number_input("CPPS ISE (20)", 0.0, 20.0) +
        st.number_input("CPPS CIE (20)", 0.0, 20.0)
    )
    subjects.append(("CPPS", 2, cpps, gp(cpps)))

    # CPPSL (100 → 25)
    st.markdown("### CPPS Lab (CPPSL)")
    cppsl = st.number_input("CPPSL TW (100)", 0.0, 100.0)
    cppsl_perc = (cppsl / 100 * 25) / 25 * 100
    subjects.append(("CPPSL", 1, cppsl_perc, gp(cppsl_perc)))

    # FAB Lab (50 → 25)
    st.markdown("### FAB Lab")
    fab = st.number_input("FAB TW (50)", 0.0, 50.0)
    fab_perc = (fab / 50 * 25) / 25 * 100
    subjects.append(("FAB", 1, fab_perc, gp(fab_perc)))

    # IKS (30 → 25)
    st.markdown("### Indian Knowledge System (IKS)")
    iks = st.number_input("IKS TW (30)", 0.0, 30.0)
    iks_perc = (iks / 30 * 25) / 25 * 100
    subjects.append(("IKS", 2, iks_perc, gp(iks_perc)))

# ======================= GROUP 2 =======================
elif group == 2:
    st.subheader("Group 2 – Enter Marks")

    def theory(name, credits):
        ese = st.number_input(f"{name} ESE (60)", 0.0, 60.0)
        ise = st.number_input(f"{name} ISE (20)", 0.0, 20.0)
        cie = st.number_input(f"{name} CIE (20)", 0.0, 20.0)
        total = ese + ise + cie
        subjects.append((name, credits, total, gp(total)))

    def lab(name, credits, max_tw):
        tw = st.number_input(f"{name} TW ({max_tw})", 0.0, max_tw)
        perc = (tw / max_tw * 25) / 25 * 100
        subjects.append((name, credits, perc, gp(perc)))

    # LAC
    st.markdown("### LAC")
    lac_ese = st.number_input("LAC ESE (60)", 0.0, 60.0)
    lac_ise = st.number_input("LAC ISE (20)", 0.0, 20.0)
    lac_cie = st.number_input("LAC CIE (20)", 0.0, 20.0)
    lac_tw  = st.number_input("LAC TW (60)", 0.0, 60.0)
    lac_total = lac_ese + lac_ise + lac_cie + (lac_tw / 60 * 25)
    lac_perc = lac_total / 125 * 100
    subjects.append(("LAC", 4, lac_perc, gp(lac_perc)))

    theory("CST", 2)
    lab("CSTL", 1, 100)
    theory("CGD", 2)
    lab("CGDL", 1, 70)
    theory("CPPS", 2)
    lab("CPPSL", 1, 100)
    theory("ESE", 2)

    # IIDTL (60 → 50)
    iidtl = st.number_input("IIDTL TW (60)", 0.0, 60.0)
    iidtl_perc = (iidtl / 60 * 50) / 50 * 100
    subjects.append(("IIDTL", 1, iidtl_perc, gp(iidtl_perc)))

    # SS (40 → 25 + CIE 25)
    sstw = st.number_input("SS TW (40)", 0.0, 40.0)
    sscie = st.number_input("SS CIE (25)", 0.0, 25.0)
    ss_total = (sstw / 40 * 25) + sscie
    ss_perc = ss_total / 50 * 100
    subjects.append(("SS", 2, ss_perc, gp(ss_perc)))

    # CCA
    cca = st.number_input("CCA TW (25)", 0.0, 25.0)
    subjects.append(("CCA", 1, cca / 25 * 100, gp(cca / 25 * 100)))

# ======================= RESULT =======================
if subjects and st.button("🎯 Calculate CGPA"):
    df = pd.DataFrame(subjects, columns=["Subject", "Credits", "Percentage", "Grade Point"])
    df["Credit Points"] = df["Credits"] * df["Grade Point"]

    st.subheader("📊 Subject-wise Result")
    st.dataframe(df, use_container_width=True)

    cgpa = df["Credit Points"].sum() / df["Credits"].sum()
    st.success(f"✅ Your CGPA is **{round(cgpa, 2)}**")
