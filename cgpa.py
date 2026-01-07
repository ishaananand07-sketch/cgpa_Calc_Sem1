import streamlit as st

st.set_page_config(page_title="CGPA Calculator", layout="centered")

st.title("🎓 CGPA Calculator – Semester 1")

def gp(perc):
    if perc >= 91:
        return 10
    elif perc >= 81:
        return 9
    elif perc >= 71:
        return 8
    elif perc >= 61:
        return 7
    elif perc >= 51:
        return 6
    elif perc >= 41:
        return 5
    else:
        return 0

st.subheader("Select Group")
g = st.selectbox("Group", [1, 2])

if g == 2:
    st.subheader("Enter Marks")

    # LAC
    st.markdown("### LAC")
    lacese = st.number_input("LAC Endsem (out of 60)", 0.0, 60.0)
    lacise = st.number_input("LAC Insem (out of 20)", 0.0, 20.0)
    lactw = st.number_input("LAC Term Work (out of 60)", 0.0, 60.0)
    laccie = st.number_input("LAC CIE + Attendance (out of 20)", 0.0, 20.0)
    lactotal = lacese + lacise + (lactw / 60 * 25) + laccie
    lacgp = gp((lactotal / 125) * 100)

    # CST
    st.markdown("### CST")
    cstese = st.number_input("CST Endsem (out of 60)", 0.0, 60.0)
    cstise = st.number_input("CST Insem (out of 20)", 0.0, 20.0)
    cstcie = st.number_input("CST CIE + Attendance (out of 20)", 0.0, 20.0)
    cstgp = gp(cstese + cstise + cstcie)

    # CSTL
    st.markdown("### CSTL")
    cstltw = st.number_input("CSTL Term Work (out of 100)", 0.0, 100.0)
    cstlgp = gp((cstltw / 100) * 100)

    # CGD
    st.markdown("### CGD")
    cgdese = st.number_input("CGD Endsem (out of 60)", 0.0, 60.0)
    cgdise = st.number_input("CGD Insem (out of 20)", 0.0, 20.0)
    cgdcie = st.number_input("CGD CIE + Attendance (out of 20)", 0.0, 20.0)
    cgdgp = gp(cgdese + cgdise + cgdcie)

    # CGDL
    st.markdown("### CGDL")
    cgdltw = st.number_input("CGDL Term Work (out of 70)", 0.0, 70.0)
    cgdlgp = gp((cgdltw / 70) * 100)

    # CPPS
    st.markdown("### CPPS")
    cppsese = st.number_input("CPPS Endsem (out of 60)", 0.0, 60.0)
    cppsise = st.number_input("CPPS Insem (out of 20)", 0.0, 20.0)
    cppscie = st.number_input("CPPS CIE + Attendance (out of 20)", 0.0, 20.0)
    cppsgp = gp(cppsese + cppsise + cppscie)

    # CPPSL
    st.markdown("### CPPSL")
    cppsltw = st.number_input("CPPSL Term Work (out of 100)", 0.0, 100.0)
    cppslgp = gp((cppsltw / 100) * 100)

    # ESE
    st.markdown("### ESE")
    esee = st.number_input("ESE Endsem (out of 60)", 0.0, 60.0)
    eseie = st.number_input("ESE Insem (out of 20)", 0.0, 20.0)
    esecie = st.number_input("ESE CIE + Attendance (out of 20)", 0.0, 20.0)
    esegp = gp(esee + eseie + esecie)

    # IIDTL
    st.markdown("### IIDTL")
    iidltw = st.number_input("IIDTL Term Work (out of 60)", 0.0, 60.0)
    iidlgp = gp((iidltw / 60) * 100)

    # SS
    st.markdown("### SS")
    sstw = st.number_input("SS Term Work (out of 40)", 0.0, 40.0)
    sscie = st.number_input("SS CIE + Attendance (out of 25)", 0.0, 25.0)
    ssgp = gp(((sstw / 40 * 25) + sscie) / 50 * 100)

    # CCA
    st.markdown("### CCA")
    ccatw = st.number_input("CCA Term Work (out of 25)", 0.0, 25.0)
    ccagp = gp((ccatw / 25) * 100)

    if st.button("🎯 Calculate CGPA"):
        total_points = (
            lacgp * 4 +
            cstgp * 2 +
            cstlgp * 1 +
            cgdgp * 2 +
            cgdlgp * 1 +
            cppsgp * 2 +
            cppslgp * 1 +
            esegp * 2 +
            iidlgp * 1 +
            ssgp * 2 +
            ccagp * 1
        )

        cgpa = total_points / 19
        st.success(f"✅ Your CGPA is: **{round(cgpa, 2)}**")
