import os

from flask import Flask, render_template, request, jsonify, send_from_directory, url_for, redirect

app=Flask(__name__, template_folder='.',static_folder='static')
@app.get("/")
def index_get():
    return render_template("index.html")

@app.get("/AboutUs")
def AboutUs_get():
    return render_template("AboutUs.html")

@app.get("/contact")
def contact_get():
    return render_template("contact.html")

@app.route("/EEE")
def EEE_get():
    return render_template("EEE.html")
@app.route("/AIML")
def AIML_get():
    return render_template("AIML.html")
@app.route("/EC")
def EC_get():
    return render_template("EC.html")
@app.route("/BankingExams")
def BankingExams_get():
    return render_template("BankingExams.html")
@app.route("/CivilEng")
def CivilEng_get():
    return render_template("CivilEng.html")

@app.route("/CivilServices")
def CivilServices_get():
    return render_template("CivilServices.html")
@app.route("/CSISDS")
def CSISDS_get():
    return render_template("CSISDS.html")
@app.route("/DefenceService")
def DefenceService_get():
    return render_template("DefenceService.html")
@app.route("/GATE")
def GATE_get():
    return render_template("GATE.html")
@app.route("/IES")
def IES_get():
    return render_template("IES.html")

@app.route("/Mechanical")
def Mechanical_get():
    return render_template("Mechanical.html")
@app.route("/PSU")
def PSU_get():
    return render_template("PSU.html")



# EEE GATE Question Papers

@app.route("/EE2021")
def EE2021_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/EEE/GATE/EE2021.pdf')
@app.route("/EE2022")
def EE2022_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/EEE/GATE/EE2022.pdf')
@app.route("/EE2023")
def EE2023_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/EEE/GATE/EE2023.pdf')
@app.route("/EE2024")
def EE2024_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/EEE/GATE/EE_2024.pdf')
@app.route("/EE2025")
def EE2025_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/EEE/GATE/EE2025.pdf')


#EEE KPTCL Question Papers

@app.route("/KPTCL2019_P1")
def KPTCL2019_P1_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/EEE/KPTCL/KPTCL2019_Paper1.pdf')

@app.route("/KPTCL2019_P2")
def KPTCL2019_P2_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/EEE/KPTCL/KPTCL2019_Paper2.pdf')

@app.route("/KPTCL2019_P3")
def KPTCL2019_P3_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/EEE/KPTCL/KPTCL2019_Paper3.pdf')

@app.route("/KPTCL2021_P1")
def KPTCL2021_P1_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/EEE/KPTCL/KPTCL2021_Paper1.pdf')

@app.route("/KPTCL2021_P2")
def KPTCL2021_P2_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/EEE/KPTCL/KPTCL2021_Paper2.pdf')

@app.route("/KPTCL2021_P3")
def KPTCL2021_P3_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/EEE/KPTCL/KPTCL2021_Paper3.pdf')

@app.route("/KPTCL2022_P1")
def KPTCL2022_P1_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/EEE/KPTCL/KPTCL2022_Paper1.pdf')

@app.route("/KPTCL2022_P2")
def KPTCL2022_P2_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/EEE/KPTCL/KPTCL2022_Paper2.pdf')

@app.route("/KPTCL2022_P3")
def KPTCL2022_P3_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/EEE/KPTCL/KPTCL2022_Paper3.pdf')

@app.route("/KPTCL2023_P1")
def KPTCL2023_P1_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/EEE/KPTCL/KTPCL2023_Paper1.pdf')

@app.route("/KPTCL2023_P2")
def KPTCL2023_P2_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/EEE/KPTCL/KPTCL2022_Paper2.pdf')

@app.route("/KPTCL2023_P3")
def KPTCL2023_P3_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/EEE/KPTCL/KTPCL2023_Paper3.pdf')


#EEE Syllabus Links

@app.route("/BHEL_Syllabus")
def BHELSyllabus_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/EEE/BHEL_Syllabus.pdf')

@app.route("/KPSC_Syllabus")
def KPSCSyllabus_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/EEE/KPSC_Syllabus.pdf')

@app.route("/KPCL_Syllabus")
def KPCLSyllabus_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/EEE/KPCL_Syllabus.pdf')

@app.route("/GATE_Syllabus")
def GATESyllabus_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/EEE/GATE_Syllabus.pdf')

@app.route("/KPTCL_Syllabus")
def KPTCLSyllabus_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/EEE/KPTCL_Syllabus.pdf')

@app.route("/KPSCQP1")
def KPSCQP1_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/EEE/KPSC/KPSC2010.pdf')

@app.route("/KPSCQP2")
def KPSCQP2_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/EEE/KPSC/KPSC2011.pdf')

@app.route("/KPSCQP3")
def KPSCQP3_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/EEE/KPSC/KPSC2014.pdf')

@app.route("/KPSCQP4")
def KPSCQP4_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/EEE/KPSC/KPSC2015.pdf')

@app.route("/KPSCQP5")
def KPSCQP5_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/EEE/KPSC/ADEE1.pdf')

#BHEL Question Papers
@app.route("/BHEL1")
def BHEL1_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/EEE/BHEL/BHEL2019.pdf')

@app.route("/BHEL2")
def BHEL2_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/EEE/BHEL/BHEL2023.pdf')

@app.route("/BHEL3")
def BHEL3_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/EEE/BHEL/BHEL2025-1.pdf')

@app.route("/BHEL4")
def BHEL4_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/EEE/BHEL/BHEL2025-2.pdf')


#AIML Syllabus
@app.route("/CDACS")
def CDACS_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/AIML/Syllabus/CDAC.pdf')

@app.route("/DAS")
def DAS_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/AIML/Syllabus/DA.pdf')

@app.route("/DRDOS")
def DRDOS_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/AIML/Syllabus/DRDO.pdf')

@app.route("/GATES")
def GATES_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/AIML/Syllabus/GATE.pdf')

@app.route("/ISROS")
def ISROS_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/AIML/Syllabus/ISRO.pdf')

@app.route("/NICS")
def NICS_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/AIML/Syllabus/NIC.pdf')

#AIML GATE Question Papers

@app.route("/DA2024")
def DA2024_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/AIML/QP/GATEDA2024.pdf')

@app.route("/DA2025")
def DA2025_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/AIML/QP/GATEDA2025.pdf')

@app.route("/CS2021")
def CS2021_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/AIML/QP/GATECS2021.pdf')

@app.route("/CS2022")
def CS2022_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/AIML/QP/GATECS2022.pdf')

@app.route("/CS2023")
def CS2023_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/AIML/QP/GATECS2023.pdf')

@app.route("/CS2024P1")
def CS2024P1_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/AIML/QP/GATECS2024-1.pdf')

@app.route("/CS2024P2")
def CS2024P2_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/AIML/QP/GATECS2024-2.pdf')

#AIML DRDO QUESTION PAPERS

@app.route("/DRDO2022P1")
def DRDO2022P1_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/AIML/QP/DRDO2022-P1.pdf')

@app.route("/DRDO2022P2")
def DRDO2022P2_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/AIML/QP/DRDO2022-P2.pdf')

@app.route("/DRDO2022P3")
def DRDO2022P3_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/AIML/QP/DRDO2022-P3.pdf')

@app.route("/DRDO2026P1")
def DRDO2026P1_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/AIML/QP/DRDO2026-P1.pdf')

@app.route("/DRDO2026P2")
def DRDO2026P2_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/AIML/QP/DRDO2026-P2.pdf')

#AIML SAC QUESTION PAPERS
@app.route("/SAC2015")
def SAC2015_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/AIML/QP/SAC2015.pdf')

@app.route("/SAC2016")
def SAC2016_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/AIML/QP/SAC2016.pdf')

@app.route("/SAC2017")
def SAC2017_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/AIML/QP/SAC2017.pdf')

@app.route("/SAC2020")
def SAC2020_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/AIML/QP/SAC2020.pdf')

@app.route("/SAC2024")
def SAC2024_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/AIML/QP/SAC2024.pdf')

#AIML VSSC QUESTION PAPERS

@app.route("/VSSC2018")
def VSSC2018_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/AIML/QP/VSSC2018.pdf')

@app.route("/VSSC2019")
def VSSC2019_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/AIML/QP/VSSC2019.pdf')

@app.route("/VSSC2021")
def VSSC2021_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/AIML/QP/VSSC2021.pdf')

@app.route("/VSSC2024")
def VSSC2024_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/AIML/QP/VSSC2024.pdf')

#AIML ISRO CDAC AND SDSC QUESTION PAPERS

@app.route("/ISROCS2025")
def ISROCS2025_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/AIML/QP/ISROCS_2025.pdf')

@app.route("/CDAC2021P1")
def CDAC2021P1_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/AIML/QP/CDAC-2021-1.pdf')

@app.route("/CDAC2021P2")
def CDAC2021P2_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/AIML/QP/CDAC-2021-2.pdf')

@app.route("/SDSC")
def SDSC_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/AIML/QP/SDSC.pdf')

#CIVIL SYLLABUS
@app.route("/CVLGATE")
def CVLGATE_get():
    pdf_dir = os.path.join(app.root_path, 'static','PDF','CIVIL','SYLLABUS')
    return send_from_directory(pdf_dir, 'GATE.pdf')

@app.route("/CVLCPWD")
def CVLCPWD_get():
    pdf_dir = os.path.join(app.root_path, 'static','PDF','CIVIL','SYLLABUS')
    return send_from_directory(pdf_dir, 'CPWD.pdf')

@app.route("/CVLMES")
def CVLMES_get():
    pdf_dir = os.path.join(app.root_path, 'static','PDF','CIVIL','SYLLABUS')
    return send_from_directory(pdf_dir, 'MES.pdf')

@app.route("/CVLPSU")
def CVLPSU_get():
    pdf_dir = os.path.join(app.root_path, 'static','PDF','CIVIL','SYLLABUS')
    return send_from_directory(pdf_dir, 'PSU.pdf')

@app.route("/CVLPWDJE")
def CVLPWDJE_get():
    pdf_dir = os.path.join(app.root_path, 'static','PDF','CIVIL','SYLLABUS')
    return send_from_directory(pdf_dir, 'PWDJE.pdf')

@app.route("/CVLPWDR")
def CVLPWDR_get():
    pdf_dir = os.path.join(app.root_path, 'static','PDF','CIVIL','SYLLABUS')
    return send_from_directory(pdf_dir, 'PWDR.pdf')

@app.route("/CVLRAILWAY")
def CVLRAILWAY_get():
    pdf_dir = os.path.join(app.root_path, 'static','PDF','CIVIL','SYLLABUS')
    return send_from_directory(pdf_dir, 'RAILWAY.pdf')

@app.route("/CVLRRBJE")
def CVLRRBJE_get():
    pdf_dir = os.path.join(app.root_path, 'static','PDF','CIVIL','SYLLABUS')
    return send_from_directory(pdf_dir, 'RRBJE.pdf')

@app.route("/CVLSSCJE")
def CVLSSCJE_get():
    pdf_dir = os.path.join(app.root_path, 'static','PDF','CIVIL','SYLLABUS')
    return send_from_directory(pdf_dir, 'SSCJE.pdf')

@app.route("/CVLNEW")
def CVLNEW_get():
    pdf_dir = os.path.join(app.root_path, 'static','PDF','CIVIL','SYLLABUS')
    return send_from_directory(pdf_dir, 'NEWSYL.pdf')

#CIVIL QUESTION PAPERS

@app.route("/CVLM2025P1")
def CVLM2025P1_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/CIVIL/QP/CIVILM2025P1.pdf')

@app.route("/CVLM2025P2")
def CVLM2025P2_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/CIVIL/QP/CIVILM2025P2.pdf')

@app.route("/CVLM2024P1")
def CVLM2024P1_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/CIVIL/QP/CVLM2024P1.pdf')

@app.route("/CVLM2024P2")
def CVLM2024P2_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/CIVIL/QP/CVLM2024P2.pdf')

@app.route("/CVLM2023P1")
def CVLM2023P1_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/CIVIL/QP/CVLM2023P1.pdf')

@app.route("/CVLM2023P2")
def CVLM2023P2_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/CIVIL/QP/CVLM2023P2.pdf')

@app.route("/CVLP2024")
def CVLP2024_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/CIVIL/QP/CVLP2024.pdf')

@app.route("/CVLP2025")
def CVLP2025_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/CIVIL/QP/CVLP2025.pdf')

@app.route("/CVLP2026")
def CVLP2026_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/CIVIL/QP/CLVP2026.pdf')

@app.route("/RRB2026P1")
def RRB2026P1_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/CIVIL/QP/RRB2026P1.pdf')

@app.route("/RRB2026P2")
def RRB2026P2_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/CIVIL/QP/RRB2026P2.pdf')

@app.route("/RRB2026P3")
def RRB2026P3_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/CIVIL/QP/RRB2026P3.pdf')

@app.route("/RRB2026S1")
def RRB2026S1_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/CIVIL/QP/RRB2026S1.pdf')

@app.route("/RRB2026S2")
def RRB2026S2_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/CIVIL/QP/RRB2026S2.pdf')

@app.route("/RRB2026S3")
def RRB2026S3_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/CIVIL/QP/RRB2026S3.pdf')

@app.route("/RRB2026SS1")
def RRB2026SS1_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/CIVIL/QP/RRB2026SS1.pdf')

@app.route("/RRB2026SS2")
def RRB2026SS2_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/CIVIL/QP/RRB2026SS2.pdf')

@app.route("/RRB2026SS3")
def RRB2026SS3_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/CIVIL/QP/RRB2026SS3.pdf')

@app.route("/GATEP1")
def GATEP1_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/CIVIL/QP/GATEP1.pdf')

@app.route("/GATEP2")
def GATEP2_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/CIVIL/QP/GATEP2.pdf')

#ECE SYLLABUS

@app.route("/BSNL2024")
def BSNL2024_get():
    pdf_dir = os.path.join(app.root_path, 'static','PDF','ECE','SYLLABUS')
    return send_from_directory(pdf_dir, 'BSNL2024.pdf')

@app.route("/BSNL2026")
def BSNL2026_get():
    pdf_dir = os.path.join(app.root_path, 'static','PDF','ECE','SYLLABUS')
    return send_from_directory(pdf_dir, 'BSNL2026.pdf')

@app.route("/CEPTAM")
def CEPTAM_get():
    pdf_dir = os.path.join(app.root_path, 'static','PDF','ECE','SYLLABUS')
    return send_from_directory(pdf_dir, 'CEPTAM.pdf')

@app.route("/ECGATE2026")
def ECGATE2026_get():
    pdf_dir = os.path.join(app.root_path, 'static','PDF','ECE','SYLLABUS')
    return send_from_directory(pdf_dir, 'GATE2026.pdf')

@app.route("/NIC2024")
def NIC2024_get():
    pdf_dir = os.path.join(app.root_path, 'static','PDF','ECE','SYLLABUS')
    return send_from_directory(pdf_dir, 'NIC2024.pdf')

#ECE QUESTION PAPERS

@app.route("/AFCATP1")
def AFCATP1_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/ECE/QP/AFCATP1.pdf')

@app.route("/AFCATP2")
def AFCATP2_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/ECE/QP/AFCATP2.pdf')

@app.route("/BSNLJE2016S1")
def BSNLJE2016S1_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/ECE/QP/BSNLJE2016S1.pdf')

@app.route("/BSNLJE2016S2")
def BSNLJE2016S2_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/ECE/QP/BSNLJE2016S2.pdf')

@app.route("/BSNLJTOTLICE2019")
def BSNLJTOTLICE2019_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/ECE/QP/BSNLJTOTLICE2019.pdf')

@app.route("/BSNLJTOTLICE2022")
def BSNLJTOTLICE2022_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/ECE/QP/BSNLJTOTLICE2022.pdf')

@app.route("/BSNLSE")
def BSNLSE_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/ECE/QP/BSNLSE.pdf')

@app.route("/ECEGATE2023")
def ECEGATE2023_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/ECE/QP/GATE2023.pdf')

@app.route("/ECEGATE2024")
def ECEGATE2024_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/ECE/QP/GATE2024.pdf')

@app.route("/NIC2017")
def NIC2017_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/ECE/QP/NIC2017.pdf')

@app.route("/NIC2020")
def NIC2020_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/ECE/QP/NIC2020.pdf')

#MECHANICAL SYLLABUS

@app.route("/MGATE")
def MGATE_get():
    pdf_dir = os.path.join(app.root_path, 'static','PDF','MECHANICAL','SYLLABUS')
    return send_from_directory(pdf_dir, 'GATE.pdf')

@app.route("/MKPSC")
def MKPSC_get():
    pdf_dir = os.path.join(app.root_path, 'static','PDF','MECHANICAL','SYLLABUS')
    return send_from_directory(pdf_dir, 'KPSC.pdf')

@app.route("/MSSCJE")
def MSSCJE_get():
    pdf_dir = os.path.join(app.root_path, 'static','PDF','MECHANICAL','SYLLABUS')
    return send_from_directory(pdf_dir, 'SSCJE.pdf')

@app.route("/MUPSC")
def MUPSC_get():
    pdf_dir = os.path.join(app.root_path, 'static','PDF','MECHANICAL','SYLLABUS')
    return send_from_directory(pdf_dir, 'UPSC.pdf')

#MECHANICAL QUESTION PAPERS

@app.route("/MESE2023P1")
def MESE2023P1_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/MECHANICAL/QP/ESE2023P1.pdf')

@app.route("/MESE2023P2")
def MESE2023P2_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/MECHANICAL/QP/ESE2023P2.pdf')

@app.route("/MESE2024P1")
def MESE2024P1_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/MECHANICAL/QP/ESE2024P1.pdf')

@app.route("/MESE2024P2")
def MESE2024P2_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/MECHANICAL/QP/ESE2024P2.pdf')

@app.route("/MESE2025P1")
def MESE2025P1_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/MECHANICAL/QP/ESE2025P1.pdf')

@app.route("/MESE2025P2")
def MESE2025P2_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/MECHANICAL/QP/ESE2025P2.pdf')

@app.route("/MESEP2024")
def MESEP2024_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/MECHANICAL/QP/ESEP2024.pdf')

@app.route("/MESEP2025")
def MESEP2025_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/MECHANICAL/QP/ESEP2025.pdf')

@app.route("/MESEP2026")
def MESEP2026_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/MECHANICAL/QP/ESEP2026.pdf')

@app.route("/MGATE2023")
def MGATE2023_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/MECHANICAL/QP/GATE2023.pdf')

@app.route("/MGATE2024")
def MGATE2024_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/MECHANICAL/QP/GATE2024.pdf')

@app.route("/MGATE2025")
def MGATE2025_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/MECHANICAL/QP/GATE2025.pdf')

@app.route("/IFS2022P1")
def IFS2022P1_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/MECHANICAL/QP/IFS2022P1.pdf')

@app.route("/SSE2024P1")
def SSE2024P1_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/MECHANICAL/QP/SSE2024P1.pdf')

@app.route("/SSE2024P2")
def SSE2024P2_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/MECHANICAL/QP/SSE2024P2.pdf')

@app.route("/SSEJE2024")
def SSEJE2024_get():
    pdf_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(pdf_dir, 'PDF/MECHANICAL/QP/SSEJE2024.pdf')

#CSISDS SYLLABUS

@app.route("/CSGATE")
def CSGATE_get():
    pdf_dir = os.path.join(app.root_path, 'static','PDF','CSISDS','SYLLABUS')
    return send_from_directory(pdf_dir, 'GATE.pdf')

@app.route("/CSISGATE")
def CSISGATE_get():
    pdf_dir = os.path.join(app.root_path, 'static','PDF','CSISDS','SYLLABUS')
    return send_from_directory(pdf_dir, 'CSISGATE.pdf')

@app.route("/CSDRDO")
def CSDRDO_get():
    pdf_dir = os.path.join(app.root_path, 'static','PDF','CSISDS','SYLLABUS')
    return send_from_directory(pdf_dir, 'DRDO2026.pdf')

@app.route("/CSISRO")
def CSISRO_get():
    pdf_dir = os.path.join(app.root_path, 'static','PDF','CSISDS','SYLLABUS')
    return send_from_directory(pdf_dir, 'ISRO2023.pdf')

#CSISDS QUESTION PAPERS

@app.route("/CSDA")
def CSDA_get():
    pdf_dir = os.path.join(app.root_path, 'static','PDF','CSISDS','QP')
    return send_from_directory(pdf_dir, 'DA.pdf')

@app.route("/CSDA2024")
def CSDA2024_get():
    pdf_dir = os.path.join(app.root_path, 'static','PDF','CSISDS','QP')
    return send_from_directory(pdf_dir, 'DA2024.pdf')

@app.route("/CSGATE2020")
def CSGATE2020_get():
    pdf_dir = os.path.join(app.root_path, 'static','PDF','CSISDS','QP')
    return send_from_directory(pdf_dir, 'GATE2020.pdf')

@app.route("/CSGATE2021P1")
def CSGATE2021P1_get():
    pdf_dir = os.path.join(app.root_path, 'static','PDF','CSISDS','QP')
    return send_from_directory(pdf_dir, 'GATE2021P1.pdf')

@app.route("/CSGATE2021P2")
def CSGATE2021P2_get():
    pdf_dir = os.path.join(app.root_path, 'static','PDF','CSISDS','QP')
    return send_from_directory(pdf_dir, 'GATE2021P2.pdf')

@app.route("/CSGATE2023")
def CSGATE2023_get():
    pdf_dir = os.path.join(app.root_path, 'static','PDF','CSISDS','QP')
    return send_from_directory(pdf_dir, 'GATE2023.pdf')

@app.route("/CSGATE2024P1")
def CSGATE2024P1_get():
    pdf_dir = os.path.join(app.root_path, 'static','PDF','CSISDS','QP')
    return send_from_directory(pdf_dir, 'GATE2024P1.pdf')

@app.route("/CSGATE2024P2")
def CSGATE2024P2_get():
    pdf_dir = os.path.join(app.root_path, 'static','PDF','CSISDS','QP')
    return send_from_directory(pdf_dir, 'GATE2024P2.pdf')





#REGISTER

@app.route("/register")
def register_get():
    return render_template("register.html")

#LOGIN

@app.route("/login")
def login_get():
    return render_template("login.html")



#CHATBOT RESPONSE LINKS

@app.route("/CGATE")
def CGATE_get():
   return render_template('GATE.html')


@app.post("/predict")
def predict():
    from chat import get_response
    text=request.get_json().get("message")
    #TODO check if text is valid
    response=get_response(text)
    message={"answer":response}
    return jsonify(message)
    
if __name__ == "__main__":
    port=int(os.environ.get("PORT",10000))
    app.run(host="0.0.0.0",port=port)

