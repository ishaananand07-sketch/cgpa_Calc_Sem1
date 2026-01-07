import streamlit as st

st.set_page_config(page_title="CGPA Calculator", layout="centered")
st.title("🎓 CGPA Calculator – Semester 1")

def gp(perc):
    if perc >= 91: return 10
    elif perc >= 81: return 9
    elif perc >= 71: return 8
    elif perc >= 61: return 7
    elif perc >= 51: return 6
    elif perc >= 41: return 5
    else: return 0

g = st.selectbox("Select Group", [1, 2], key="group")

if g == 2:
    st.subheader("Enter Marks")

    # LAC
    st.markdown("### LAC")
    lacese = st.number_input("LAC Endsem (60)", 0.0, 60.0, key="lacese")
    lacise = st.number_input("LAC Insem (20)", 0.0, 20.0, key="lacise")
    lactw = st.number_input("LAC Term Work (60)", 0.0, 60.0, key="lactw")
    laccie = st.number_input("LAC CIE + Attendance (20)", 0.0, 20.0, key="laccie")
    lac_total = lacese + lacise + (lactw / 60 * 25) + laccie
    lac_gp = gp((lac_total / 125) * 100)

    # CST
    st.markdown("### CST")
    cstese = st.number_input("CST Endsem (60)", 0.0, 60.0, key="cstese")
    cstise = st.number_input("CST Insem (20)", 0.0, 20.0, key="cstise")
    cstcie = st.number_input("CST CIE + Attendance (20)", 0.0, 20.0, key="cstcie")
    cst_gp = gp(cstese + cstise + cstcie)

    # CSTL
    st.markdown("### CSTL")
    cstltw = st.number_input("CSTL Term Work (100)", 0.0, 100.0, key="cstltw")
    cstl_gp = gp((cstltw / 100) * 100)

    # CGD
    st.markdown("### CGD")
    cgdese = st.number_input("CGD Endsem (60)", 0.0, 60.0, key="cgdese")
    cgdise = st.number_input("CGD Insem (20)", 0.0, 20.0, key="cgdise")
    cgdcie = st.number_input("CGD CIE + Attendance (20)", 0.0, 20.0, key="cgdcie")
    cgd_gp = gp(cgdese + cgdise + cgdcie)

    # CGDL
    st.markdown("### CGDL")
    cgdltw = st.number_input("CGDL Term Work (70)", 0.0, 70.0, key="cgdltw")
    cgdl_gp = gp((cgdltw / 70) * 100)

    # CPPS
    st.markdown("### CPPS")
    cppsese = st.number_input("CPPS Endsem (60)", 0.0, 60.0, key="cppsese")
    cppsise = st.number_input("CPPS Insem (20)", 0.0, 20.0, key="cppsise")
    cppscie = st.number_input("CPPS CIE + Attendance (20)", 0.0, 20.0, key="cppscie")
    cpps_gp = gp(cppsese + cppsise + cppscie)

    # CPPSL
    st.markdown("### CPPSL")
    cppsltw = st.number_input("CPPSL Term Work (100)", 0.0, 100.0, key="cppsltw")
    cppsl_gp = gp((cppsltw / 100) * 100)

    # ESE
    st.markdown("### ESE")
    esee = st.number_input("ESE Endsem (60)", 0.0, 60.0, key="esee")
    eseie = st.number_input("ESE Insem (20)", 0.0, 20.0, key="eseie")
    esecie = st.number_input("ESE CIE + Attendance (20)", 0.0, 20.0, key="esecie")
    ese_gp = gp(esee + eseie + esecie)

    # IIDTL
    st.markdown("### IIDTL")
    iidltw = st.number_input("IIDTL Term Work (60)", 0.0, 60.0, key="iidltw")
    iidtl_gp = gp((iidltw / 60) * 100)

    # SS
    st.markdown("### SS")
    sstw = st.number_input("SS Term Work (40)", 0.0, 40.0, key="sstw")
    sscie = st.number_input("SS CIE + Attendance (25)", 0.0, 25.0, key="sscie")
    ss_gp = gp(((sstw / 40 * 25) + sscie) / 50 * 100)

    # CCA
    st.markdown("### CCA")
    ccatw = st.number_input("CCA Term Work (25)", 0.0, 25.0, key="ccatw")
    cca_gp = gp((ccatw / 25) * 100)

    if st.button("🎯 Calculate CGPA"):
        total_points = (
            lac_gp * 4 +
            cst_gp * 2 +
            cstl_gp * 1 +
            cgd_gp * 2 +
            cgdl_gp * 1 +
            cpps_gp * 2 +
            cppsl_gp * 1 +
            ese_gp * 2 +
            iidtl_gp * 1 +
            ss_gp * 2 +
            cca_gp * 1
        )

        cgpa = total_points / 19
        st.success(f"✅ Your CGPA is **{round(cgpa, 2)}**")
