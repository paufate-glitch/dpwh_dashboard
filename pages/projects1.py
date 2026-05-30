import base64
import json
import os
import pathlib
import random
import streamlit as st
import streamlit.components.v1 as components

# ════════════════════════════════════════════════════════════════════════════
# ── SECTION: STREAMLIT PAGE CONFIG  ────────────────────────────────────
# ════════════════════════════════════════════════════════════════════════════

st.set_page_config(
    page_title="DPWH Iloilo – Infrastructure Dashboard",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

nav_target = st.query_params.get("navigate", "")
if nav_target == "home":
    st.switch_page("homepage.py")
elif nav_target == "about":
    st.switch_page("pages/about.py")
elif nav_target == "contacts":
    st.switch_page("pages/contacts.py")

LOGO_PATH = "pages/Dashboard figures/DPWH_LOGO.png"

# ════════════════════════════════════════════════════════════════════════════
# ── SECTION A: PROJECT DATA  ─────────────────────────────────────────────
# ════════════════════════════════════════════════════════════════════════════

PROJECTS: list[dict] = [
    {
        "id": 1,
        "project_name": "RETROFITTING/STRENGTHENING OF QUIRINO-LOPEZ BRIDGE ALONG ILOILO AIRPORT DIRECT ROAD (B00117PN)",
        "category": "Bridges",
        "district": "City District",
        "implementing_office": "DPWH – Iloilo City DEO",
        "status": "Completed",
        "year": 2016,
        "date": "2016-09-21",
        "budget_allocated": 39493941.94,
        "budget_spent": 38074201.14,
        "completion_percentage": 100,
        "contractor": "MONOLITHIC CONSTRUCTION & CONCRETE PRODUCTS, INC.",
        "image_path": "https://www.iloilotoday.com/wp-content/uploads/2016/01/muelleloneybridge.jpg",
    },
    {
        "id": 2,
        "project_name": "COMPLETION OF EMERGENCY DEPARTMENT AND REPAIR/RENOVATION OF WARDS, WESTERN VISAYAS MEDICAL CENTER, ILOILO CITY",
        "category": "Buildings and Facilities",
        "district": "City District",
        "implementing_office": "DPWH – Iloilo City DEO",
        "status": "Completed",
        "year": 2016,
        "date": "2016-02-22",
        "budget_allocated": 33863814.67,
        "budget_spent": 32339943.0,
        "completion_percentage": 100,
        "contractor": "A.D. PENDON CONSTRUCTION & SUPPLY, INC.",
        "image_path": "https://mb.com.ph/manilabulletin/uploads/images/2025/07/29/30325.webp",
    },
    {
        "id": 3,
        "project_name": "ASPHALT OVERLAY OF IZNART - LEDESMA - MOLO ROAD, K000+236-K000+545, CHAINAGE 0-339",
        "category": "Roads",
        "district": "City District",
        "implementing_office": "DPWH – Iloilo City DEO",
        "status": "Completed",
        "year": 2016,
        "date": "2016-02-09",
        "budget_allocated": 11601850.34,
        "budget_spent": 10954187.11,
        "completion_percentage": 100,
        "contractor": "ALLENCON DEVELOPMENT CORPORATION",
        "image_path": "https://www.dailyguardian.com.ph/_next/image?url=https%3A%2F%2Fold.dailyguardian.com.ph%2Fwp-content%2Fuploads%2F2024%2F06%2FIloilo-Diversion-Road-repaving-eases-traffic-flow.jpg&w=1920&q=75",
    },
    {
        "id": 4,
        "project_name": "CONSTRUCTION/REHABILITATION OF DRAINAGE SYSTEM INCLUDING WATER PUMPING SYSTEM WITHIN THE VICINITY OF CITY PROPER AREA, ILOILO CITY",
        "category": "Flood Control and Drainage",
        "district": "City District",
        "implementing_office": "DPWH – Iloilo City DEO",
        "status": "Completed",
        "year": 2017,
        "date": "2017-06-13",
        "budget_allocated": 83299793.53,
        "budget_spent": 81998413.83,
        "completion_percentage": 100,
        "contractor": "F. GURREA CONSTRUCTION, INCORPORATED",
        "image_path": "https://files01.pna.gov.ph/ograph/2024/11/05/iloilo---dpwh-project.jpg",
    },
    {
        "id": 5,
        "project_name": "ROAD CONCRETING, BARANGAY PUNONG ROAD, LAPUZ, ILOILO CITY",
        "category": "Roads",
        "district": "City District",
        "implementing_office": "DPWH – Iloilo City DEO",
        "status": "Completed",
        "year": 2017,
        "date": "2017-05-09",
        "budget_allocated": 2969993.04,
        "budget_spent": 2945624.36,
        "completion_percentage": 100,
        "contractor": "PESOM CONSTRUCTION SERVICES",
        "image_path": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQR9AJfOOKkFSlU9RdgoTxPHAat17yzvOnBOg&s",
    },
    {
        "id": 6,
        "project_name": "CONSTRUCTION OF MULTIPURPOSE BUILDING HALL BARANGAY RIZAL LAPUZ SUR, ILOILO CITY",
        "category": "Buildings and Facilities",
        "district": "City District",
        "implementing_office": "DPWH – Iloilo City DEO",
        "status": "Completed",
        "year": 2017,
        "date": "2017-07-31",
        "budget_allocated": 1979054.33,
        "budget_spent": 1921386.25,
        "completion_percentage": 100,
        "contractor": "EZ GOLD CONSTRUCTION & SUPPLY",
        "image_path": "https://scontent.fcgy2-4.fna.fbcdn.net/v/t39.30808-6/539941860_1202425188583083_4538329746057195393_n.jpg?stp=dst-jpg_s590x590_tt6&_nc_cat=108&ccb=1-7&_nc_sid=127cfc&_nc_ohc=tEP1Xx_tW1gQ7kNvwF8Dbp2&_nc_oc=AdqwCx-YSgZwt-sPeeOIf5858QMY7jdDF1-WHwzu9veohjdT8LMCYoynPLG2QB28j0ubumF057DTk-of0WgBAmYQ&_nc_zt=23&_nc_ht=scontent.fcgy2-4.fna&_nc_gid=yODL_2MAZkcmrs0ZodhcTQ&_nc_ss=7b289&oh=00_Af50liQs1wQhjqdsP7RIG52VuE6TEaWeTnwmXEn-O1ghzw&oe=6A189A01",
    },
    {
        "id": 7,
        "project_name": "RETROFITTING/ STRENGTHENING OF PERMANENT BRIDGES, ILOILO BRIDGE (B00501PN) ALONG SEN. BENIGNO S. AQUINO, JR. AVE",
        "category": "Bridges",
        "district": "City District",
        "implementing_office": "DPWH – Iloilo City DEO",
        "status": "Completed",
        "year": 2017,
        "date": "2017-05-09",
        "budget_allocated": 39282320.0,
        "budget_spent": 39199919.73,
        "completion_percentage": 100,
        "contractor": "IBC INTERNATIONAL BUILDERS CORPORATION",
        "image_path": "https://scontent.fcgy2-1.fna.fbcdn.net/v/t1.6435-9/39995735_1786497001469483_2289401114195394560_n.jpg?_nc_cat=102&ccb=1-7&_nc_sid=833d8c&_nc_ohc=ojLtWK-u8UsQ7kNvwFdMaHE&_nc_oc=AdrxtQgzYc18LsF63BG7qxa_x9IYBHllmmv6iu4QHcKwTQg2BYCuSXEwvQrr9S2JLTo6zq-2oJryox5JMxZGdnh1&_nc_zt=23&_nc_ht=scontent.fcgy2-1.fna&_nc_gid=AMIYylyWeS2OuipAHkk7ZA&_nc_ss=7b289&oh=00_Af7GUOURe9WJA8VHlmnvxNxgbiu7qD1-21xFzJ1AasPPsw&oe=6A3A33C3",
    },
    {
        "id": 8,
        "project_name": "CONSTRUCTION OF FLOOD MITIGATION STRUCTURE - CONSTRUCTION OF SLOPE PROTECTION WORKS AND IMPROVEMENT ALONG ILOILO RIVER, LEFT BANK (FROM FORBES BRIDGE TO MUELLELONEY BRIDGE RIZAL), ILOILO CITY",
        "category": "Flood Control and Drainage",
        "district": "City District",
        "implementing_office": "DPWH – Iloilo City DEO",
        "status": "Completed",
        "year": 2018,
        "date": "2018-03-22",
        "budget_allocated": 9799926.91,
        "budget_spent": 9278406.6,
        "completion_percentage": 100,
        "contractor": "VANNIE CONSTRUCTION AND SUPPLY",
        "image_path": "https://scontent.fcgy2-1.fna.fbcdn.net/v/t1.6435-9/46432659_10158082635224488_6169922667634753536_n.jpg?_nc_cat=100&ccb=1-7&_nc_sid=127cfc&_nc_ohc=IaEFOZXXslcQ7kNvwGH8rA2&_nc_oc=AdrFbKLn2_vesBM2t-4lW0qiS_SoDHAWzN96gT2bpN3wRe3YXYocPPuTKXlo1O8A1dkFSLR8t2YQmcAaInwr68OV&_nc_zt=23&_nc_ht=scontent.fcgy2-1.fna&_nc_gid=-UW4dM-QFeyl0SBPqtHItg&_nc_ss=7b289&oh=00_Af62Jhozm7ohQTzISxcxqRIUXev-OKfwSAlzbBu2dtP-dg&oe=6A3A4636",
    },
    {
        "id": 9,
        "project_name": "PREVENTIVE MAINTENANCE OF ROAD: ASPHALT OVERLAY - MUELLE LONEY MARGINAL WHARF RD - K0000 + 000 - K0000 + 083",
        "category": "Roads",
        "district": "City District",
        "implementing_office": "DPWH – Iloilo City DEO",
        "status": "Completed",
        "year": 2018,
        "date": "2018-02-26",
        "budget_allocated": 2189063.76,
        "budget_spent": 2023990.49,
        "completion_percentage": 100,
        "contractor": "ALJ CONSTRUCTION AND SUPPLY",
        "image_path": "https://scontent.fcgy2-1.fna.fbcdn.net/v/t39.30808-6/486700670_1064426992386641_6290978603726998917_n.jpg?stp=dst-jpg_s590x590_tt6&_nc_cat=102&ccb=1-7&_nc_sid=833d8c&_nc_ohc=o3LMNxon8dQQ7kNvwHZSWFr&_nc_oc=AdoScnyRwX3BpMS60BIhLSiCjq_H3-IltI5errC3MK3lsiuKDzOLxPYAmQPYLgfAJYgcb5eULGeEluAAxKLUqTgP&_nc_zt=23&_nc_ht=scontent.fcgy2-1.fna&_nc_gid=-TkKXBK2Rdj_o2a2_kUosA&_nc_ss=7b289&oh=00_Af54ESNW9v1idi6wMOpxKV7z0QQtiGZkdYR20gcc6EWlIQ&oe=6A189160",
    },
    {
        "id": 10,
        "project_name": "WIDENING OF BRIDGE -BATIANO BR. (B00488PN) ALONG MOLO BLVD INCL. ROW",
        "category": "Bridges",
        "district": "City District",
        "implementing_office": "DPWH – Iloilo City DEO",
        "status": "Completed",
        "year": 2018,
        "date": "2018-05-03",
        "budget_allocated": 23361124.98,
        "budget_spent": 21988576.38,
        "completion_percentage": 100,
        "contractor": "J.S. LAYSON & CO., INC.",
        "image_path": "https://cmpancho.com/wp-content/uploads/2025/07/aloragat1-1536x1152.jpg",
    },
    {
        "id": 11,
        "project_name": "REHABILITATION OF MULTI-PURPOSE BUILDING (HALL), LA PAZ PUBLIC MARKET (FISH SECTION), ILOILO CITY",
        "category": "Buildings and Facilities",
        "district": "City District",
        "implementing_office": "DPWH – Iloilo City DEO",
        "status": "Completed",
        "year": 2018,
        "date": "2018-05-12",
        "budget_allocated": 10245739.59,
        "budget_spent": 9938089.32,
        "completion_percentage": 100,
        "contractor": "G.F. FALCIS CONSTRUCTION & SUPPLY",
        "image_path": "https://scontent.fcgy2-1.fna.fbcdn.net/v/t39.30808-6/486261272_1063008222528518_1341718129031818900_n.jpg?stp=dst-jpg_s590x590_tt6&_nc_cat=107&ccb=1-7&_nc_sid=833d8c&_nc_ohc=S8-T4RK01qYQ7kNvwH0nFwr&_nc_oc=AdoPAQZjRqHtsH-LTNtDF1uhm4rQjsX6d4YQYS9wlktiB5MVHLvG0ewIYPFLJN-D5BD98yN0xyvMzl6wxBYYwOvS&_nc_zt=23&_nc_ht=scontent.fcgy2-1.fna&_nc_gid=Wn9hU_mZWQEkVZ7EQwYHBQ&_nc_ss=7b289&oh=00_Af6-dmfyAx-jVUuGMSz6yoBYpCy1AbooCM6zarN6-aInHQ&oe=6A18B589",
    },
    {
        "id": 12,
        "project_name": "CONSTRUCTION OF FLOOD MITIGATION STRUCTURE CONSTRUCTION OF SLOPE PROTECTION/BANK IMPROVEMENT ALONG ILOILO RIVER, RIGHT BANK (FROM JALANDONI BRIDGE TO FORBES BRIDGE), (ESPLANADE 6), STA. 0+820-STA. 1+660, ILOILO CITY)",
        "category": "Flood Control and Drainage",
        "district": "City District",
        "implementing_office": "DPWH – Iloilo City DEO",
        "status": "Completed",
        "year": 2019,
        "date": "2019-08-19",
        "budget_allocated": 9899871.96,
        "budget_spent": 9899812.3,
        "completion_percentage": 100,
        "contractor": "VANNIE CONSTRUCTION AND SUPPLY",
        "image_path": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRMMiRL_6CeETXoeOCpDPZlRxA3QuafyZglyYMbO52ok3DsPz9w",
    },
    {
        "id": 13,
        "project_name": "CONCRETING OF BRGY. BUNTATALA FMR PHASE II. BRGY. BUNTATALA, ILOILO CITY, ILOILO",
        "category": "Roads",
        "district": "City District",
        "implementing_office": "DPWH – Iloilo City DEO",
        "status": "Completed",
        "year": 2019,
        "date": "2019-09-12",
        "budget_allocated": 4974987.85,
        "budget_spent": 4836140.3,
        "completion_percentage": 100,
        "contractor": "G.F. FALCIS CONSTRUCTION & SUPPLY",
        "image_path": "https://upload.wikimedia.org/wikipedia/commons/5/57/Iloilo_Airport_Access_Road.jpg",
    },
    {
        "id": 14,
        "project_name": "RETROFITTING/STRENGTHENING OF BRIDGE - DUNGON BR. 5 (B00115PN) ALONG AIRPORT SPUR RD",
        "category": "Bridges",
        "district": "City District",
        "implementing_office": "DPWH – Iloilo City DEO",
        "status": "Completed",
        "year": 2019,
        "date": "2019-06-17",
        "budget_allocated": 24511779.23,
        "budget_spent": 25580705.01,
        "completion_percentage": 100,
        "contractor": "A.D. PENDON CONSTRUCTION & SUPPLY, INC.",
        "image_path": "https://cdn-jakjb.nitrocdn.com/sThawxWtFDrkHhwPRYgAfXTVSNGHQytk/assets/images/optimized/rev-cddf8c0/rmbretrobuild.com/wp-content/uploads/2023/01/Baan-Bridge_span-2-view_after_retrofitting-351x240.jpg",
    },
    {
        "id": 15,
        "project_name": "CONSTRUCTION OF SECONDARY CLASSROOMS 3STY REG. WORKSHOP JARO NATIONAL HIGH SCHOOL, ILOILO CITY",
        "category": "Buildings and Facilities",
        "district": "City District",
        "implementing_office": "DPWH – Iloilo City DEO",
        "status": "Completed",
        "year": 2019,
        "date": "2019-09-27",
        "budget_allocated": 24753284.65,
        "budget_spent": 24258145.02,
        "completion_percentage": 100,
        "contractor": "A.D. PENDON CONSTRUCTION & SUPPLY, INC.",
        "image_path": "https://scontent.fcgy2-2.fna.fbcdn.net/v/t39.30808-6/474464125_1150605790019029_1127079124113697355_n.jpg?stp=dst-jpg_s960x960_tt6&_nc_cat=103&ccb=1-7&_nc_sid=cc71e4&_nc_ohc=JMd6ZOrl9qMQ7kNvwHlkJ3Q&_nc_oc=Adq7nCYVHVwk77gFTAkCY5NFC0QLWW3P10H7Nlqc_2Q5l0E0sduBA1fTCklx6BMzs4OWvM5uFDLjkLIDA8kXvwKB&_nc_zt=23&_nc_ht=scontent.fcgy2-2.fna&_nc_gid=zYGYt9EwJ0ATy-tMTB3oZQ&_nc_ss=7b289&oh=00_Af5LpXzq2opklHee0HHKtnbIWAKuHhwSpx--9-8SK5nzJA&oe=6A18B234",
    },
    {
        "id": 16,
        "project_name": "REHABILITATION OF PAVED ROAD AT SPECIFIC LOCATION ALONG PRESIDENT CORAZON C. AQUINO AVE.",
        "category": "Roads",
        "district": "City District",
        "implementing_office": "DPWH – Iloilo City DEO",
        "status": "Completed",
        "year": 2020,
        "date": "2020-10-29",
        "budget_allocated": 4288701.48,
        "budget_spent": 4311582.2,
        "completion_percentage": 100,
        "contractor": "PCG BUILDERS CORPORATION",
        "image_path": "https://static.rappler.com/images/DaangHari_510x340a.jpg",
    },
    {
        "id": 17,
        "project_name": "CONSTRUCTION OF DRAINAGE STRUCTURE - FRONT OF WVMC HOSPITAL (FROM MC DO MEGAWORLD TO PLAZA) AT Q. ABETO, MANDURRIAO, ILOILO CITY",
        "category": "Flood Control and Drainage",
        "district": "City District",
        "implementing_office": "DPWH – Iloilo City DEO",
        "status": "Completed",
        "year": 2020,
        "date": "2020-05-31",
        "budget_allocated": 1979446.98,
        "budget_spent": 1891124.88,
        "completion_percentage": 100,
        "contractor": "VEONG CONSTRUCTION & SUPPLY",
        "image_path": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQoD-T63hRoHDyjiXo0VZH_vHvsWKhfSpvCkdX98WIEw-fjgSzW",
    },
    {
        "id": 18,
        "project_name": "REHABILITATION/MAJOR REPAIR OF MULTI-PURPOSE BUILDING - REHABILITATION OF BRGY. HALL, BRGY. PUNONG LAPUZ, ILOILO CITY",
        "category": "Buildings and Facilities",
        "district": "City District",
        "implementing_office": "DPWH – Iloilo City DEO",
        "status": "Completed",
        "year": 2020,
        "date": "2020-11-13",
        "budget_allocated": 989720.31,
        "budget_spent": 930302.71,
        "completion_percentage": 100,
        "contractor": "GGMU CONSTRUCTION AND SUPPLY",
        "image_path": "https://scontent.fcgy2-4.fna.fbcdn.net/v/t1.6435-9/129734278_3818179624866908_8523667708409155350_n.jpg?_nc_cat=110&ccb=1-7&_nc_sid=833d8c&_nc_ohc=Id52avZE7M0Q7kNvwGd6GeA&_nc_oc=Adovzf3uALfJM7lyEPeWmedFKkEz_jI9VQn1F_PBnzzO_9MF42j0wqzxf0GqT4djG9kcTQsZ_UXYJfnju52wNFRs&_nc_zt=23&_nc_ht=scontent.fcgy2-4.fna&_nc_gid=bVSjJoFsu_a2vV0o3JFAvQ&_nc_ss=7b289&oh=00_Af5rhWfEH58LtMdFycCNIQW6nEIMaKjzA-pqzhxV5TXBrg&oe=6A3A7A5D",
    },
    {
        "id": 19,
        "project_name": "CONSTRUCTION OF FLYOVER - JIBAO-AN FLYOVER, BRGY. JIBAO-AN NORTE, MANDURRIAO, ILOILO CITY",
        "category": "Bridges",
        "district": "City District",
        "implementing_office": "DPWH – Iloilo City DEO",
        "status": "Completed",
        "year": 2020,
        "date": "2020-06-18",
        "budget_allocated": 96500000.0,
        "budget_spent": 96465479.57,
        "completion_percentage": 100,
        "contractor": "A.M. ORETA & CO., INC. / ALLENCON DEVELOPMENT CORPORATION",
        "image_path": "https://old.dailyguardian.com.ph/wp-content/uploads/2023/12/Jibao-an-Flyover-1.jpg",
    },
    {
        "id": 20,
        "project_name": "CONSTRUCTION OF FLYOVER-JIBAO-AN PHASE II, ILOILO CITY",
        "category": "Bridges",
        "district": "City District",
        "implementing_office": "DPWH – Iloilo City DEO",
        "status": "Completed",
        "year": 2021,
        "date": "2021-12-10",
        "budget_allocated": 24125000.0,
        "budget_spent": 24091862.02,
        "completion_percentage": 100,
        "contractor": "ALLENCON DEVELOPMENT CORPORATION",
        "image_path": "https://img.bomboradyo.com/iloilo/2023/09/JIBAOAN-flyover-1024x576.jpg",
    },
    {
        "id": 21,
        "project_name": "CONSTRUCTION OF MULTI PURPOSE BUILDING (GRACIANO LOPEZ JAENA ELEMENTARY SCHOOL), BARANGAY BURGOS MABINI, ILOILO CITY",
        "category": "Buildings and Facilities",
        "district": "City District",
        "implementing_office": "DPWH – Iloilo City DEO",
        "status": "Completed",
        "year": 2020,
        "date": "2021-05-22",
        "budget_allocated": 1980000.0,
        "budget_spent": 1897392.85,
        "completion_percentage": 100,
        "contractor": "S.T. SALCEDO CONSTRUCTION CORP.",
        "image_path": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQbjzOiGiugNL3JJjPTQNUs7cCuRVmd5TCHjOjyaADtZkFmNvHR",
    },
    {
        "id": 22,
        "project_name": "CONSTRUCTION OF DRAINAGE STRUCTURE - CONSTRUCTION/REHABILITATION OF DRAINAGE SYSTEM IN MV HECHANOVA, JARO, ILOILO CITY",
        "category": "Flood Control and Drainage",
        "district": "City District",
        "implementing_office": "DPWH – Iloilo City DEO",
        "status": "Completed",
        "year": 2021,
        "date": "2021-06-18",
        "budget_allocated": 2969999.02,
        "budget_spent": 2741529.44,
        "completion_percentage": 100,
        "contractor": "S.T. SALCEDO CONSTRUCTION CORP.",
        "image_path": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQ-R_405OUB0YuhqR_68iLQ7G7fea9fbmzajn8qjyDuJC_WZFzj",
    },
    {
        "id": 23,
        "project_name": "REHABILITATION OF CONCRETE ROAD - REHABILITATION OF ROAD IN BARANGAY SINIKWAY, LAPUZ, ILOILO CITY",
        "category": "Roads",
        "district": "City District",
        "implementing_office": "DPWH – Iloilo City DEO",
        "status": "Completed",
        "year": 2021,
        "date": "2021-06-09",
        "budget_allocated": 4950000.0,
        "budget_spent": 4910980.09,
        "completion_percentage": 100,
        "contractor": "STELLAR BUILDERS",
        "image_path": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS5h0o8mLdsTDGLvu0zpp_QavTIoov1PtS2VDtaF0ZSpJ8x1GIf",
    },
    {
        "id": 24,
        "project_name": "REHABILITATION/MAJOR REPAIR OF BRIDGE - MANSAYA BR. 1 (B00486PN) ALONG LA PAZ DEEP SEA WATER PORT RD",
        "category": "Bridges",
        "district": "City District",
        "implementing_office": "DPWH – Iloilo City DEO",
        "status": "Completed",
        "year": 2022,
        "date": "2022-02-21",
        "budget_allocated": 2352000.0,
        "budget_spent": 2351698.19,
        "completion_percentage": 100,
        "contractor": "AQUA DRAGON CONSTRUCTION & SUPPLY",
        "image_path": "https://scontent.fcgy2-2.fna.fbcdn.net/v/t39.30808-6/474696651_1121644796091641_7133478553687127702_n.jpg?stp=dst-jpg_s590x590_tt6&_nc_cat=101&ccb=1-7&_nc_sid=833d8c&_nc_ohc=MwhuwNF9tK8Q7kNvwGaV1zq&_nc_oc=AdpmJJQrvmogBqGyT_H-s3mIOHjNf_C6fQROOM_ST25C6l1Bpga66f6l8a3nPDR1T6ZYHCxr02wIG6Y9Vu7Hv10G&_nc_zt=23&_nc_ht=scontent.fcgy2-2.fna&_nc_gid=XLKW7xLEmwAeCsMSjV8G-Q&_nc_ss=7b289&oh=00_Af7IemH8Y8LEPyLvZcaxfPCbrQQoGXXjD3U_KKZmBGfLrg&oe=6A18F220",
    },
    {
        "id": 25,
        "project_name": "CONSTRUCTION OF MULTI PURPOSE BUILDING IN JARO DISTRICT, JARO, ILOILO CITY, ILOILO",
        "category": "Buildings and Facilities",
        "district": "City District",
        "implementing_office": "DPWH – Iloilo City DEO",
        "status": "Completed",
        "year": 2022,
        "date": "2022-07-13",
        "budget_allocated": 4900000.0,
        "budget_spent": 4948892.7,
        "completion_percentage": 100,
        "contractor": "GOLDEN HEAVEN BUILDERS AND CONSTRUCTION SUPPLY",
        "image_path": "https://www.awbenterprises.com/wp-content/uploads/2016/09/sri-lanka-roller-shutter-2.jpg",
    },
    {
        "id": 26,
        "project_name": "CONSTRUCTION OF REVETMENT WALL ALONG JARO RIVER, BRGY. SAN ISIDRO, JARO, ILOILO CITY",
        "category": "Flood Control and Drainage",
        "district": "City District",
        "implementing_office": "DPWH – Iloilo City DEO",
        "status": "Completed",
        "year": 2022,
        "date": "2022-04-05",
        "budget_allocated": 96499990.6,
        "budget_spent": 95504856.13,
        "completion_percentage": 100,
        "contractor": "F. GURREA CONSTRUCTION, INCORPORATED",
        "image_path": "https://scontent.fcgy2-4.fna.fbcdn.net/v/t39.30808-6/474513231_1021200953377389_3606177099529291923_n.jpg?stp=dst-jpg_s590x590_tt6&_nc_cat=108&ccb=1-7&_nc_sid=833d8c&_nc_ohc=m213G3lA9-UQ7kNvwGqZaI_&_nc_oc=AdpJ6H7XRqb674vlYwFer5hzkl0T_oNuEg8j33sdMONHTZ0i9QltxRX55oPz_puij5Yb-ia8IhHi_e9R75tM5bZ8&_nc_zt=23&_nc_ht=scontent.fcgy2-4.fna&_nc_gid=DzziX3awD7OOC0qq5gVqIw&_nc_ss=7b289&oh=00_Af6A12tz34dL7-3MhvVlSxcC9YTjqkAqau-SjJ-s8u3_Ow&oe=6A195408",
    },
    {
        "id": 27,
        "project_name": "ROAD WIDENING - MOLO BLVD K0009-(585)-K0009+165",
        "category": "Roads",
        "district": "City District",
        "implementing_office": "DPWH – Iloilo City DEO",
        "status": "Completed",
        "year": 2022,
        "date": "2023-10-05",
        "budget_allocated": 45436207.28,
        "budget_spent": 43718579.54,
        "completion_percentage": 100,
        "contractor": "WOODLAND CONSTRUCTION & SUPPLY, INC.",
        "image_path": "https://scontent.fcgy2-1.fna.fbcdn.net/v/t39.30808-6/489457263_1091624296319103_1212327796884017682_n.jpg?_nc_cat=102&ccb=1-7&_nc_sid=833d8c&_nc_ohc=qPqHMMMAJAYQ7kNvwEadjE1&_nc_oc=AdrU7Ads0AwYADjylvApe8zE6P_7-Y70pZGeL4c8nO9K9HHeRdrlK_7nb6vPBWTBR3TdrBkb6nXL3Te5SN3KqVH0&_nc_zt=23&_nc_ht=scontent.fcgy2-1.fna&_nc_gid=XEKqyYmo667OTIaSA9XK4w&_nc_ss=7b289&oh=00_Af7QfKL805d93p_M9Ji6tOMF23kKTR9oYiiivaZNCnalOw&oe=6A194448",
    },
    {
        "id": 28,
        "project_name": "(RE-BID) CONSTRUCTION OF FLYOVER - JIBAO-AN FLYOVER, BRGY.JIBAO-AN NORTE, MANDURRIAO, ILOILO CITY",
        "category": "Bridges",
        "district": "City District",
        "implementing_office": "DPWH – Iloilo City DEO",
        "status": "Completed",
        "year": 2023,
        "date": "2024-01-03",
        "budget_allocated": 83267000.0,
        "budget_spent": 83266983.32,
        "completion_percentage": 100,
        "contractor": "IBC INTERNATIONAL BUILDERS CORPORATION",
        "image_path": "https://img.bomboradyo.com/iloilo/2023/09/JIBAOAN-flyover-1024x576.jpg",
    },
    {
        "id": 29,
        "project_name": "CONSTRUCTION (COMPLETION) OF MULTI-PURPOSE BUILDING, BRGY. TABUC SUBA, JARO, ILOILO CITY",
        "category": "Buildings and Facilities",
        "district": "City District",
        "implementing_office": "DPWH – Iloilo City DEO",
        "status": "Completed",
        "year": 2023,
        "date": "2023-09-21",
        "budget_allocated": 2475000.0,
        "budget_spent": 2475000.0,
        "completion_percentage": 100,
        "contractor": "NOE'S BUILDERS",
        "image_path": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRDizP8aqQKc8dn88PnD9tGfdAw_X4bejqCkdOIkLpmzGwSmNbl",
    },
    {
        "id": 30,
        "project_name": "CONSTRUCTION OF DRAINAGE SYSTEM IN AREVALO, ILOILO CITY, ILOILO",
        "category": "Flood Control and Drainage",
        "district": "City District",
        "implementing_office": "DPWH – Iloilo City DEO",
        "status": "Completed",
        "year": 2023,
        "date": "2023-08-30",
        "budget_allocated": 4950000.0,
        "budget_spent": 4945183.08,
        "completion_percentage": 100,
        "contractor": "PAG BUILDERS",
        "image_path": "https://scontent.fcgy2-3.fna.fbcdn.net/v/t39.30808-6/477792360_1136809157908538_3648341458732598231_n.jpg?stp=dst-jpg_s590x590_tt6&_nc_cat=111&ccb=1-7&_nc_sid=833d8c&_nc_ohc=ynypln1FPP4Q7kNvwFjOdnK&_nc_oc=Adr6QNQHaeBTNVIjSi_n8LXhFE9UdJ_0behvnYAoBblHpG5a5-sJdABCjGEwSHcM_LaGgEq4p6IYXTOiICekGDj1&_nc_zt=23&_nc_ht=scontent.fcgy2-3.fna&_nc_gid=n1xswuRa60_7o7lsMacKeg&_nc_ss=7b289&oh=00_Af6g9mQmRA2_vMF8zLIOUfgZttDHMIvzUfWGMFHQnOqa2w&oe=6A197424",
    },
    {
        "id": 31,
        "project_name": "PREVENTIVE MAINTENANCE OF ROAD: ASPHALT OVERLAY - ILOILO - CAPIZ RD (NEW ROUTE)",
        "category": "Roads",
        "district": "City District",
        "implementing_office": "DPWH – Iloilo City DEO",
        "status": "Completed",
        "year": 2023,
        "date": "2024-03-24",
        "budget_allocated": 8596560.0,
        "budget_spent": 5957418.09,
        "completion_percentage": 100,
        "contractor": "S.T. SALCEDO CONSTRUCTION CORP.",
        "image_path": "https://old.dailyguardian.com.ph/wp-content/uploads/2024/06/Iloilo-Diversion-Road-repaving-eases-traffic-flow1.jpg",
    },
    {
        "id": 32,
        "project_name": "CONSTRUCTION OF DUNGON B BRIDGE, BRGY. DUNGON B, JARO, ILOILO CITY",
        "category": "Bridges",
        "district": "City District",
        "implementing_office": "DPWH – Iloilo City DEO",
        "status": "Ongoing",
        "year": 2024,
        "date": "2024-01-01",
        "budget_allocated": 46777500.0,
        "budget_spent": 46520000.0,
        "completion_percentage": 5.26,
        "contractor": "IBC INTERNATIONAL BUILDERS CORPORATION",
        "image_path": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSkoAEapGfqDH4L7-Ih9ZsQXqvthhsf3BHOPQ&s",
    },
    {
        "id": 33,
        "project_name": "REHABILITATION OF MULTI-PURPOSE BUILDING, BRGY. ALALASAN, LAPUZ DISTRICT, ILOILO CITY",
        "category": "Buildings and Facilities",
        "district": "City District",
        "implementing_office": "DPWH – Iloilo City DEO",
        "status": "Ongoing",
        "year": 2024,
        "date": "2024-01-01",
        "budget_allocated": 2970000.0,
        "budget_spent": 2950000.0,
        "completion_percentage": 68.56,
        "contractor": "5'S CONSTRUCTION & SUPPLY",
        "image_path": "https://img.bomboradyo.com/iloilo/2024/05/MULTIPURPOSE-BUILDING.jpg.webp",
    },
    {
        "id": 34,
        "project_name": "CONSTRUCTION OF FLOOD MITIGATION STRUCTURE IN LAPUZ, ILOILO CITY, SECTION 2",
        "category": "Flood Control and Drainage",
        "district": "City District",
        "implementing_office": "DPWH – Iloilo City DEO",
        "status": "Ongoing",
        "year": 2024,
        "date": "2024-01-01",
        "budget_allocated": 144750000.0,
        "budget_spent": 141799122.88,
        "completion_percentage": 91.24,
        "contractor": "ST. TIMOTHY CONSTRUCTION CORPORATION",
        "image_path": "https://www.miagao.gov.ph/wp-content/uploads/2024/03/430905720_844412774397485_8897730914410355801_n-300x168.jpg",
    },
    {
        "id": 35,
        "project_name": "CONSTRUCTION OF ROAD AND DRAINAGE IN AREVALO, ILOILO CITY",
        "category": "Roads",
        "district": "City District",
        "implementing_office": "DPWH – Iloilo City DEO",
        "status": "Ongoing",
        "year": 2024,
        "date": "2024-01-01",
        "budget_allocated": 14700000.0,
        "budget_spent": 14562638.13,
        "completion_percentage": 57.91,
        "contractor": "UBS UNITED BUILDERS AND SUPPLY INC.",
        "image_path": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSUTCy7GKOOrs0d0lrIcWxHr-zIfz85HcWdfsilxodiZSjRhOpB",
    },
    {
        "id": 36,
        "project_name": "CONSTRUCTION OF MULTI-PURPOSE BUILDING (GOVERNMENT CENTER) ILOILO CITY",
        "category": "Buildings and Facilities",
        "district": "City District",
        "implementing_office": "DPWH – Iloilo City DEO",
        "status": "Ongoing",
        "year": 2025,
        "date": "2025-01-01",
        "budget_allocated": 14850000.0,
        "budget_spent": 14739143.67,
        "completion_percentage": 83.88,
        "contractor": "LUCKY H&K CONSTRUCTION",
        "image_path": "https://www.dailyguardian.com.ph/_next/image?url=https%3A%2F%2Fold.dailyguardian.com.ph%2Fwp-content%2Fuploads%2F2023%2F10%2FMulti-purpose-structure-built-to-house-beneficiaries-of-St-Patrick-Homes-in-Cadiz-City-Negros-Occidental.jpg&w=1920&q=75",
    },
    {
        "id": 37,
        "project_name": "CONSTRUCTION OF ILOILO CITY FLOOD MITIGATION STRUCTURES - SECTION 1",
        "category": "Flood Control and Drainage",
        "district": "City District",
        "implementing_office": "DPWH – Iloilo City DEO",
        "status": "Ongoing",
        "year": 2025,
        "date": "2025-01-01",
        "budget_allocated": 144750000.0,
        "budget_spent": 143303900.68,
        "completion_percentage": 42.33,
        "contractor": "YPR GEN. CONTRACTOR AND CONSTRUCTION SUPPLY INC.",
        "image_path": "https://scontent.fcgy2-3.fna.fbcdn.net/v/t39.30808-6/542703830_24833363086280920_756740332133155690_n.webp?stp=dst-jpg_s590x590_tt6&_nc_cat=111&ccb=1-7&_nc_sid=127cfc&_nc_ohc=AWLME939mOoQ7kNvwH4isbq&_nc_oc=AdrcNOqK-DBlvVd4bhCqHe-ppie0N7S7OQ-C1Zyo3oBxqkHmEg-P8I8RpdTg4clw-S1mehCmPUlQrYJRlweH829V&_nc_zt=23&_nc_ht=scontent.fcgy2-3.fna&_nc_gid=-AKqr16hwbOjfmwuMAoH6A&_nc_ss=7b289&oh=00_Af7EF5Y8fvPj-O4cE1R0_8iSVAEPH1Px_5ClBIX8VzsQAQ&oe=6A198387",
    },
    {
        "id": 38,
        "project_name": "CONSTRUCTION OF ROAD AND DRAINAGE (SECTION 3), JARO, ILOILO CITY",
        "category": "Roads",
        "district": "City District",
        "implementing_office": "DPWH – Iloilo City DEO",
        "status": "Completed",
        "year": 2025,
        "date": "2025-01-01",
        "budget_allocated": 9900000.0,
        "budget_spent": 9849019.74,
        "completion_percentage": 100,
        "contractor": "EDISON C BUILDERS & CONSTRUCTION SUPPLY",
        "image_path": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcSlby8-agvyuHoI_q5pQJB5Mde74I6nRha0AvvzBIhmKkfCVFeR",
    },
    # ---- DISTRICT 1 -----
    {"id":39,"project_name":"Retrofitting/Strengthening of Iyasan Bridge (B00037PN) Along Guimbal-Igbaras-Tubungan-Leon Road, Guimbal, Iloilo","category":"Bridges","district":"1st District","implementing_office":"DPWH - Iloilo 1st DEO","status":"Completed","year":2016,"date":"2016-07-04","budget_allocated":4654000.0,"budget_spent":3723207.16,"completion_percentage":100,"contractor":"VANNIE CONSTRUCTION AND SUPPLY","image_path":""},
    {"id":40,"project_name":"Completion of Multi-Purpose Building in Oton and Tigbauan (Cluster 1)","category":"Buildings and Facilities","district":"1st District","implementing_office":"DPWH - Iloilo 1st DEO","status":"Completed","year":2016,"date":"2016-05-15","budget_allocated":11053000.0,"budget_spent":8842155.82,"completion_percentage":100,"contractor":"S.T. SALCEDO CONSTRUCTION CORP.","image_path":""},
    {"id":41,"project_name":"Construction of Siwaragan River Control, Siwaragan, San Joaquin, Iloilo","category":"Flood Control and Drainage","district":"1st District","implementing_office":"DPWH - Iloilo 1st DEO","status":"Completed","year":2016,"date":"2016-11-30","budget_allocated":11750000.0,"budget_spent":9399999.96,"completion_percentage":100,"contractor":"F. GURREA CONSTRUCTION, INCORPORATED","image_path":""},
    {"id":42,"project_name":"Rehabilitation/Improvement of Namocon-Zayco-Brgy. 4 Road Leading to Panay First Sugar Mill, Tigbauan, Iloilo","category":"Roads","district":"1st District","implementing_office":"DPWH - Iloilo 1st DEO","status":"Completed","year":2016,"date":"2016-11-30","budget_allocated":3683000.0,"budget_spent":2946738.83,"completion_percentage":100,"contractor":"J.E. TICO CONSTRUCTION CO., INC.","image_path":""},
    {"id":43,"project_name":"Retrofitting/Strengthening of Ingay Bridge (B00168PN) Along Guimbal-Tubungan Road, Tubungan, Iloilo","category":"Bridges","district":"1st District","implementing_office":"DPWH - Iloilo 1st DEO","status":"Completed","year":2017,"date":"2017-06-20","budget_allocated":9644000.0,"budget_spent":7715213.43,"completion_percentage":100,"contractor":"AQUA DRAGON CONSTRUCTION & SUPPLY","image_path":""},
    {"id":44,"project_name":"Rehabilitation of Multipurpose Buildings (Binaliuan ES, Barosong ES, Parara ES, Sta. Rita ES, Botong-Cabanbanan ES, Pakiad ES, Lawigan ES)","category":"Buildings and Facilities","district":"1st District","implementing_office":"DPWH - Iloilo 1st DEO","status":"Completed","year":2017,"date":"2017-11-17","budget_allocated":3081000.0,"budget_spent":2464552.8,"completion_percentage":100,"contractor":"ALJ CONSTRUCTION AND SUPPLY","image_path":""},
    {"id":45,"project_name":"Construction of Tiolas River Control, San Joaquin, Iloilo","category":"Flood Control and Drainage","district":"1st District","implementing_office":"DPWH - Iloilo 1st DEO","status":"Completed","year":2017,"date":"2017-06-01","budget_allocated":15479000.0,"budget_spent":12383129.91,"completion_percentage":100,"contractor":"GALENO CONSTRUCTION, INC.","image_path":""},
    {"id":46,"project_name":"Construction/Improvement of Igbaras-Passi-Igcabugao-Igbolo Road Leading to Igcabugao Cave (Package I), Igbaras, Iloilo","category":"Bridges","district":"1st District","implementing_office":"DPWH - Iloilo 1st DEO","status":"Completed","year":2018,"date":"2018-12-04","budget_allocated":2471000.0,"budget_spent":1976706.02,"completion_percentage":100,"contractor":"AQUA DRAGON CONSTRUCTION & SUPPLY","image_path":""},
    {"id":47,"project_name":"Construction of Guimbal Multi-Purpose Building, Atty. Blas and Maria Gerona Memorial Elementary School, Guimbal, Iloilo","category":"Buildings and Facilities","district":"1st District","implementing_office":"DPWH - Iloilo 1st DEO","status":"Completed","year":2018,"date":"2018-08-01","budget_allocated":3960000.0,"budget_spent":3949230.07,"completion_percentage":100,"contractor":"KRJ CONSTRUCTION","image_path":""},
    {"id":48,"project_name":"Construction of Tangyan River Control, Igbaras, Iloilo","category":"Flood Control and Drainage","district":"1st District","implementing_office":"DPWH - Iloilo 1st DEO","status":"Completed","year":2018,"date":"2018-12-02","budget_allocated":24455000.0,"budget_spent":19564305.9,"completion_percentage":100,"contractor":"HENSCHA PHILS. INC.","image_path":""},
    {"id":49,"project_name":"Concreting of Igcocolo-Paradahan Road, Brgy. Igcocolo, Guimbal, Iloilo","category":"Roads","district":"1st District","implementing_office":"DPWH - Iloilo 1st DEO","status":"Completed","year":2018,"date":"2018-07-01","budget_allocated":6181000.0,"budget_spent":4944413.9,"completion_percentage":100,"contractor":"SILVERGRACES CONSTRUCTION AND SUPPLY","image_path":""},
    {"id":50,"project_name":"Rehabilitation/Major Repair of Sinugbuhan Bridge (B00506PN) Along Tiolas-Sinugbuhan Road, San Joaquin, Iloilo","category":"Bridges","district":"1st District","implementing_office":"DPWH - Iloilo 1st DEO","status":"Completed","year":2019,"date":"2019-11-15","budget_allocated":8727000.0,"budget_spent":6981765.0,"completion_percentage":100,"contractor":"EC STRUCTURAL COMPOSITES, INC.","image_path":""},
    {"id":51,"project_name":"Rehabilitation of Multipurpose Buildings Cluster II (Bagumbayan ES, Parara ES, Cambitu NHS, Oton CES, Sta. Rita ES), Tigbauan, Oton & Miag-ao, Iloilo","category":"Buildings and Facilities","district":"1st District","implementing_office":"DPWH - Iloilo 1st DEO","status":"Completed","year":2019,"date":"2019-08-23","budget_allocated":2938000.0,"budget_spent":2350027.93,"completion_percentage":100,"contractor":"CHAMPION BUILDERS AND SUPPLY","image_path":""},
    {"id":52,"project_name":"Construction of Flood Mitigation Structure - Pitogo River Control Along Tiolas River, San Joaquin, Iloilo","category":"Flood Control and Drainage","district":"1st District","implementing_office":"DPWH - Iloilo 1st DEO","status":"Completed","year":2019,"date":"2020-03-03","budget_allocated":23177000.0,"budget_spent":18541404.79,"completion_percentage":100,"contractor":"GALENO CONSTRUCTION, INC.","image_path":""},
    {"id":53,"project_name":"Concreting of Abilay Sur - Pulo Maestra Vita (Relocation Site) Road, Oton, Iloilo","category":"Roads","district":"1st District","implementing_office":"DPWH - Iloilo 1st DEO","status":"Completed","year":2019,"date":"2019-12-05","budget_allocated":23511000.0,"budget_spent":18808769.4,"completion_percentage":100,"contractor":"CABILAUAN CONSTRUCTION AND SUPPLY","image_path":""},
    {"id":54,"project_name":"Retrofitting/Strengthening of Jalaua Bridge (B00078PN) Along Iloilo-Capiz Rd (New Route)","category":"Bridges","district":"1st District","implementing_office":"DPWH - Iloilo 1st DEO","status":"Completed","year":2020,"date":"2020-03-03","budget_allocated":4655000.0,"budget_spent":3723999.94,"completion_percentage":100,"contractor":"ABRIGHT BUILDERS CORPORATION","image_path":""},
    {"id":55,"project_name":"Rehabilitation of Multipurpose Buildings (Cluster II), Various Locations, Iloilo 1st District","category":"Buildings and Facilities","district":"1st District","implementing_office":"DPWH - Iloilo 1st DEO","status":"Completed","year":2020,"date":"2020-05-18","budget_allocated":5402000.0,"budget_spent":4321345.12,"completion_percentage":100,"contractor":"ABRIGHT BUILDERS CORPORATION","image_path":""},
    {"id":56,"project_name":"Construction of Pitogo River Control Along Tiolas River, San Joaquin, Iloilo","category":"Flood Control and Drainage","district":"1st District","implementing_office":"DPWH - Iloilo 1st DEO","status":"Completed","year":2020,"date":"2020-03-03","budget_allocated":36725000.0,"budget_spent":29380292.9,"completion_percentage":100,"contractor":"ARRIANNE MERCHANDISING AND CONSTRUCTION SERVICES INC.","image_path":""},
    {"id":57,"project_name":"Concreting of Guimbal-Igbaras-Tubungan-Leon Road, Guimbal, Iloilo","category":"Roads","district":"1st District","implementing_office":"DPWH - Iloilo 1st DEO","status":"Completed","year":2020,"date":"2020-07-06","budget_allocated":22460000.0,"budget_spent":17968060.5,"completion_percentage":100,"contractor":"PATRILA BUILDERS, INC.","image_path":""},
    {"id":58,"project_name":"Retrofitting/Strengthening of Jalaua Bridge (B00078PN) Along Iloilo-Capiz Rd (New Route), Zarraga, Iloilo","category":"Bridges","district":"1st District","implementing_office":"DPWH - Iloilo 1st DEO","status":"Completed","year":2021,"date":"2021-06-25","budget_allocated":8147000.0,"budget_spent":1957422.37,"completion_percentage":100,"contractor":"ABRIGHT BUILDERS CORPORATION","image_path":""},
    {"id":59,"project_name":"Rehabilitation of Multipurpose Buildings, Various Locations, Iloilo 1st District","category":"Buildings and Facilities","district":"1st District","implementing_office":"DPWH - Iloilo 1st DEO","status":"Completed","year":2021,"date":"2021-03-24","budget_allocated":3020000.0,"budget_spent":2415697.87,"completion_percentage":100,"contractor":"J.C. ALBASON BUILDERS AND SUPPLY","image_path":""},
    {"id":60,"project_name":"Construction of Flood Control Along Abuang River, Igbaras, Iloilo","category":"Flood Control and Drainage","district":"1st District","implementing_office":"DPWH - Iloilo 1st DEO","status":"Completed","year":2021,"date":"2021-04-12","budget_allocated":2060000.0,"budget_spent":1647987.34,"completion_percentage":100,"contractor":"ABRIGHT BUILDERS CORPORATION","image_path":""},
    {"id":61,"project_name":"Concreting of Access Road Leading to Maasin River Dam, Maasin, Iloilo","category":"Roads","district":"1st District","implementing_office":"DPWH - Iloilo 1st DEO","status":"Completed","year":2021,"date":"2021-09-10","budget_allocated":5872000.0,"budget_spent":4697901.2,"completion_percentage":100,"contractor":"DEACONS TEMPLE CONSTRUCTION & SUPPLY","image_path":""},
    {"id":62,"project_name":"Rehabilitation/Major Repair of Bucaya Bridge (B00141PN) Along Iloilo-Antique Rd","category":"Bridges","district":"1st District","implementing_office":"DPWH - Iloilo 1st DEO","status":"Completed","year":2022,"date":"2022-04-12","budget_allocated":6063000.0,"budget_spent":4850376.49,"completion_percentage":100,"contractor":"PAG-UN BUILDERS & SUPPLY","image_path":""},
    {"id":63,"project_name":"Construction (Completion) of Multi-Purpose Building Including Pavement, Oton National High School, Oton, Iloilo","category":"Buildings and Facilities","district":"1st District","implementing_office":"DPWH - Iloilo 1st DEO","status":"Completed","year":2022,"date":"2022-06-13","budget_allocated":2468000.0,"budget_spent":1974102.64,"completion_percentage":100,"contractor":"JBHRI CONSTRUCTION SERVICES","image_path":""},
    {"id":64,"project_name":"Construction of Calampitao River Flood Control Project, Guimbal, Iloilo","category":"Flood Control and Drainage","district":"1st District","implementing_office":"DPWH - Iloilo 1st DEO","status":"Completed","year":2022,"date":"2022-08-16","budget_allocated":12130000.0,"budget_spent":9704043.98,"completion_percentage":100,"contractor":"GOLDEN ROADRUNNER INTERNATIONAL CORP.","image_path":""},
    {"id":65,"project_name":"Concreting of Sitio Dolocutan, Brgy. Bitas FMR, Brgy. Bitas, Tigbauan, Iloilo","category":"Roads","district":"1st District","implementing_office":"DPWH - Iloilo 1st DEO","status":"Completed","year":2022,"date":"2022-09-17","budget_allocated":14850000.0,"budget_spent":11879940.76,"completion_percentage":100,"contractor":"CHAMPION BUILDERS AND SUPPLY","image_path":""},
    {"id":66,"project_name":"Construction of Dorong-an - Bagumbayan Hanging Bridge Including Access Road, Tigbauan, Iloilo","category":"Bridges","district":"1st District","implementing_office":"DPWH - Iloilo 1st DEO","status":"Completed","year":2023,"date":"2023-09-20","budget_allocated":6181000.0,"budget_spent":4944509.43,"completion_percentage":100,"contractor":"ABRIGHT BUILDERS CORPORATION","image_path":""},
    {"id":67,"project_name":"Construction (Completion) of Multi-Purpose Building (Municipal Covered Gym), Barangay Zone 1, Tubungan, Iloilo","category":"Buildings and Facilities","district":"1st District","implementing_office":"DPWH - Iloilo 1st DEO","status":"Completed","year":2023,"date":"2023-06-13","budget_allocated":6113000.0,"budget_spent":4890162.25,"completion_percentage":100,"contractor":"PAG-UN BUILDERS & SUPPLY","image_path":""},
    {"id":68,"project_name":"Construction of Tangyan River Control Project, Barangay Nito-an, Guimbal, Iloilo","category":"Flood Control and Drainage","district":"1st District","implementing_office":"DPWH - Iloilo 1st DEO","status":"Completed","year":2023,"date":"2023-12-19","budget_allocated":36364000.0,"budget_spent":29091213.14,"completion_percentage":100,"contractor":"ABRIGHT BUILDERS CORPORATION","image_path":""},
    {"id":69,"project_name":"Concreting of Brgy. Bongol San Miguel - Brgy. Bacong Road, Guimbal, Iloilo","category":"Roads","district":"1st District","implementing_office":"DPWH - Iloilo 1st DEO","status":"Completed","year":2023,"date":"2023-08-16","budget_allocated":6126000.0,"budget_spent":4900450.9,"completion_percentage":100,"contractor":"J'14 CONSTRUCTION & SUPPLY","image_path":""},
    {"id":70,"project_name":"Construction of Talento ES Multi-Purpose Building, Brgy. Talento, Tubungan, Iloilo","category":"Buildings and Facilities","district":"1st District","implementing_office":"DPWH - Iloilo 1st DEO","status":"Completed","year":2024,"date":"2024-05-23","budget_allocated":6181000.0,"budget_spent":4944902.11,"completion_percentage":100,"contractor":"FRINEL CONSTRUCTION SERVICES","image_path":""},
    {"id":71,"project_name":"Construction of Jarao River Control and Revetment Structure, Guimbal, Iloilo","category":"Flood Control and Drainage","district":"1st District","implementing_office":"DPWH - Iloilo 1st DEO","status":"Completed","year":2024,"date":"2024-11-15","budget_allocated":61807000.0,"budget_spent":49445882.19,"completion_percentage":100,"contractor":"IBC INTERNATIONAL BUILDERS CORPORATION","image_path":""},
    {"id":72,"project_name":"Construction of Calampitao-Gines Road, Miagao, Iloilo","category":"Roads","district":"1st District","implementing_office":"DPWH - Iloilo 1st DEO","status":"Completed","year":2024,"date":"2024-07-10","budget_allocated":6000000.0,"budget_spent":4881920.37,"completion_percentage":100,"contractor":"JUAN TONG & SONS BUILDER CORPORATION","image_path":""},
    {"id":73,"project_name":"Rehabilitation/Major Repair of Kuliatan Bridge (B00158PN) Along Tiolas-Sinugbuhan Rd","category":"Bridges","district":"1st District","implementing_office":"DPWH - Iloilo 1st DEO","status":"Completed","year":2025,"date":"2025-01-01","budget_allocated":14636000.0,"budget_spent":11709193.15,"completion_percentage":100,"contractor":"RINEL CONSTRUCTION SERVICES","image_path":""},
    {"id":74,"project_name":"Construction of Jarao River Flood Control Structure, Guimbal, Iloilo","category":"Flood Control and Drainage","district":"1st District","implementing_office":"DPWH - Iloilo 1st DEO","status":"Completed","year":2025,"date":"2025-06-07","budget_allocated":36562000.0,"budget_spent":29249837.93,"completion_percentage":100,"contractor":"ECQ ENHANCED CONSTRUCTION QUALITY CORP.","image_path":""},
    {"id":75,"project_name":"Construction of Road Including Facilities, Guimbal, Iloilo","category":"Roads","district":"1st District","implementing_office":"DPWH - Iloilo 1st DEO","status":"Ongoing","year":2025,"date":"2025-01-01","budget_allocated":24624000.0,"budget_spent":19699066.86,"completion_percentage":70.73,"contractor":"ECQ ENHANCED CONSTRUCTION QUALITY CORP.","image_path":""},
    # ---- 2nd DISTRICT -----
    {"id":76,"project_name":"Rehabilitation/Major Repair of Lamonan Bridge, Passi-Calinog Road, Passi City, Iloilo","category":"Bridges","district":"2nd District","implementing_office":"DPWH - Iloilo 2nd DEO","status":"Completed","year":2016,"date":"2016-11-24","budget_allocated":7318000.0,"budget_spent":5854237.44,"completion_percentage":100,"contractor":"CULASI GENERAL MERCHANDISING & CONSTRUCTION SERVICES","image_path":""},
    {"id":77,"project_name":"Construction of Two Units Two-Storey Four Classrooms (Batch 9), Caninguan NHS, Lambunao, Iloilo","category":"Buildings and Facilities","district":"2nd District","implementing_office":"DPWH - Iloilo 2nd DEO","status":"Completed","year":2016,"date":"2017-04-05","budget_allocated":7906000.0,"budget_spent":6324890.16,"completion_percentage":100,"contractor":"KJC CONSTRUCTION & SUPPLY","image_path":""},
    {"id":78,"project_name":"Repair/Rehabilitation of Flood Control at Poblacion Dingle, Brgy. Poblacion, Dingle, Iloilo","category":"Flood Control and Drainage","district":"2nd District","implementing_office":"DPWH - Iloilo 2nd DEO","status":"Completed","year":2016,"date":"2018-03-03","budget_allocated":48046000.0,"budget_spent":38436761.98,"completion_percentage":100,"contractor":"ST. GERRARD CONSTRUCTION GEN. CONTRACTOR & DEVELOPMENT CORP.","image_path":""},
    {"id":79,"project_name":"Retrofitting/Strengthening of Abangay Bridge (B00065PN) Along Iloilo-Capiz Road (Old Route), Janiuay, Iloilo","category":"Bridges","district":"2nd District","implementing_office":"DPWH - Iloilo 2nd DEO","status":"Completed","year":2017,"date":"2017-07-06","budget_allocated":2699000.0,"budget_spent":2159506.44,"completion_percentage":100,"contractor":"EC STRUCTURAL COMPOSITES, INC.","image_path":""},
    {"id":80,"project_name":"Construction of One Unit One-Storey Two Classrooms, Pughanan ES, Brgy. Pughanan, Lambunao, Iloilo","category":"Buildings and Facilities","district":"2nd District","implementing_office":"DPWH - Iloilo 2nd DEO","status":"Completed","year":2017,"date":"2018-02-25","budget_allocated":2722000.0,"budget_spent":2177335.12,"completion_percentage":100,"contractor":"KIT'Z CONSTRUCTION AND SUPPLY","image_path":""},
    {"id":81,"project_name":"Rehabilitation of Flood Control Along Jalaur River at Poblacion Passi City, Iloilo","category":"Flood Control and Drainage","district":"2nd District","implementing_office":"DPWH - Iloilo 2nd DEO","status":"Completed","year":2017,"date":"2018-02-04","budget_allocated":38550000.0,"budget_spent":30839987.97,"completion_percentage":100,"contractor":"STRONGLANE BUILDERS AND TRADING CORPORATION","image_path":""},
    {"id":82,"project_name":"Concreting of Mandurriao-San Miguel-Alimodian-Maasin-Cabatuan Road, Brgys. Siwalo & Magsaysay Section","category":"Roads","district":"2nd District","implementing_office":"DPWH - Iloilo 2nd DEO","status":"Completed","year":2017,"date":"2018-01-01","budget_allocated":27953000.0,"budget_spent":22362571.14,"completion_percentage":100,"contractor":"THREE W BUILDERS, INC.","image_path":""},
    {"id":83,"project_name":"Widening of Tigbauan Bridge (B00061PN) Along Iloilo-Capiz Road (Old Route), Cabatuan, Iloilo","category":"Bridges","district":"2nd District","implementing_office":"DPWH - Iloilo 2nd DEO","status":"Completed","year":2018,"date":"2019-03-24","budget_allocated":41887000.0,"budget_spent":33509916.23,"completion_percentage":100,"contractor":"A.D. PENDON CONSTRUCTION & SUPPLY, INC.","image_path":""},
    {"id":84,"project_name":"Construction of One Unit Two-Storey Six Classrooms, Alcarde Gustillo Memorial NHS (Batch 3), Calinog, Iloilo","category":"Buildings and Facilities","district":"2nd District","implementing_office":"DPWH - Iloilo 2nd DEO","status":"Completed","year":2018,"date":"2019-06-30","budget_allocated":14594000.0,"budget_spent":11675317.57,"completion_percentage":100,"contractor":"ACAMADA BUILDER'S & CONSTRUCTION SUPPLY","image_path":""},
    {"id":85,"project_name":"Construction of Suage River Control System at Pototan, Pototan, Iloilo","category":"Flood Control and Drainage","district":"2nd District","implementing_office":"DPWH - Iloilo 2nd DEO","status":"Completed","year":2018,"date":"2018-09-24","budget_allocated":58128000.0,"budget_spent":46502056.42,"completion_percentage":100,"contractor":"F. GURREA CONSTRUCTION, INCORPORATED","image_path":""},
    {"id":86,"project_name":"Tubungan-Igtuble-San Remigio Road (Molina-Igtuble Bridge), Tubungan, Iloilo","category":"Bridges","district":"1st District","implementing_office":"DPWH - Iloilo 1st DEO","status":"Completed","year":2018,"date":"2020-11-25","budget_allocated":8821000.0,"budget_spent":7056436.9,"completion_percentage":100,"contractor":"F. GURREA CONSTRUCTION, INCORPORATED","image_path":""},
    {"id":87,"project_name":"Construction of Footbridge, Brgy. Embarcadero - Tabucan, Dumangas, Iloilo","category":"Bridges","district":"2nd District","implementing_office":"DPWH - Iloilo 2nd DEO","status":"Completed","year":2019,"date":"2020-03-01","budget_allocated":1820000.0,"budget_spent":1455880.88,"completion_percentage":100,"contractor":"H.F. ENTERPRISES","image_path":""},
    {"id":88,"project_name":"Renovation of Public Market, Brgy. Poblacion, Banate, Iloilo","category":"Buildings and Facilities","district":"2nd District","implementing_office":"DPWH - Iloilo 2nd DEO","status":"Completed","year":2019,"date":"2019-09-21","budget_allocated":3526000.0,"budget_spent":2820515.07,"completion_percentage":100,"contractor":"VEONG CONSTRUCTION & SUPPLY","image_path":""},
    {"id":89,"project_name":"Construction of Suage River Control at Pototan, Iloilo","category":"Flood Control and Drainage","district":"2nd District","implementing_office":"DPWH - Iloilo 2nd DEO","status":"Completed","year":2019,"date":"2020-01-31","budget_allocated":58431000.0,"budget_spent":46745162.64,"completion_percentage":100,"contractor":"ROPRIM CONSTRUCTION CORPORATION","image_path":""},
    {"id":90,"project_name":"Reconstruction to Concrete Pavement of Lub-lub - Calao - Rosario - Cansilayan Road","category":"Roads","district":"2nd District","implementing_office":"DPWH - Iloilo 2nd DEO","status":"Completed","year":2019,"date":"2019-08-25","budget_allocated":5096000.0,"budget_spent":4076457.97,"completion_percentage":100,"contractor":"HORTINELA CONSTRUCTION & SUPPLY","image_path":""},
    {"id":91,"project_name":"Widening of Asisig Bridge (B00185PN) Along Passi-San Rafael-Lemery-Sara Road","category":"Bridges","district":"2nd District","implementing_office":"DPWH - Iloilo 2nd DEO","status":"Completed","year":2020,"date":"2021-10-15","budget_allocated":67711000.0,"budget_spent":54169027.03,"completion_percentage":100,"contractor":"A.D. PENDON CONSTRUCTION & SUPPLY, INC.","image_path":""},
    {"id":92,"project_name":"Construction (Completion) of Multi-Purpose Building of Brgy. Malag-it, Lambunao, Iloilo","category":"Buildings and Facilities","district":"2nd District","implementing_office":"DPWH - Iloilo 2nd DEO","status":"Completed","year":2020,"date":"2020-05-27","budget_allocated":2409000.0,"budget_spent":1927497.11,"completion_percentage":100,"contractor":"EZ GOLD CONSTRUCTION & SUPPLY","image_path":""},
    {"id":93,"project_name":"Construction of Jalaur River Control in Calinog, Iloilo","category":"Flood Control and Drainage","district":"2nd District","implementing_office":"DPWH - Iloilo 2nd DEO","status":"Completed","year":2020,"date":"2021-06-04","budget_allocated":46552000.0,"budget_spent":37241541.37,"completion_percentage":100,"contractor":"STRONGLANE BUILDERS AND TRADING CORPORATION","image_path":""},
    {"id":94,"project_name":"Concreting of Brgy. Mina East - Singay - Agmanaphao Road, Mina, Iloilo","category":"Roads","district":"2nd District","implementing_office":"DPWH - Iloilo 2nd DEO","status":"Completed","year":2020,"date":"2021-03-08","budget_allocated":11755000.0,"budget_spent":9404073.22,"completion_percentage":100,"contractor":"H.F. ENTERPRISES","image_path":""},
    {"id":95,"project_name":"Widening of Agtalosi Bridge (B00187PN) Along Passi-San Rafael-Lemery-Sara Road","category":"Bridges","district":"2nd District","implementing_office":"DPWH - Iloilo 2nd DEO","status":"Completed","year":2021,"date":"2022-03-21","budget_allocated":26066000.0,"budget_spent":20852863.46,"completion_percentage":100,"contractor":"A.D. PENDON CONSTRUCTION & SUPPLY, INC.","image_path":""},
    {"id":96,"project_name":"Construction of Multi-Purpose Building of Barangay Sariri, Badiangan, Iloilo","category":"Buildings and Facilities","district":"2nd District","implementing_office":"DPWH - Iloilo 2nd DEO","status":"Completed","year":2021,"date":"2021-06-30","budget_allocated":3880000.0,"budget_spent":3103647.0,"completion_percentage":100,"contractor":"SLW8 BUILDERS","image_path":""},
    {"id":97,"project_name":"Construction of Flood Control/Slope Protection Along Suage River, Pototan, Iloilo","category":"Flood Control and Drainage","district":"2nd District","implementing_office":"DPWH - Iloilo 2nd DEO","status":"Completed","year":2021,"date":"2022-05-11","budget_allocated":48020000.0,"budget_spent":38416028.0,"completion_percentage":100,"contractor":"ROPRIM CONSTRUCTION CORPORATION","image_path":""},
    {"id":98,"project_name":"Construction of Access Road Pavements and Drainage System Along Brgy. Bularan Reclamation Area, Banate, Iloilo","category":"Roads","district":"2nd District","implementing_office":"DPWH - Iloilo 2nd DEO","status":"Completed","year":2021,"date":"2022-09-22","budget_allocated":12001000.0,"budget_spent":9600756.51,"completion_percentage":100,"contractor":"GGMU CONSTRUCTION AND SUPPLY","image_path":""},
    {"id":99,"project_name":"Rehabilitation/Major Repair of Maquina Bridge (B00021PN) Along Balabag-Maquina-Cayos-Patlad Road","category":"Bridges","district":"2nd District","implementing_office":"DPWH - Iloilo 2nd DEO","status":"Completed","year":2022,"date":"2022-06-06","budget_allocated":4753000.0,"budget_spent":3802399.99,"completion_percentage":100,"contractor":"KENBE CONSTRUCTION & SUPPLY","image_path":""},
    {"id":100,"project_name":"Construction of Multi-Purpose Building, San Enrique, Iloilo","category":"Buildings and Facilities","district":"2nd District","implementing_office":"DPWH - Iloilo 2nd DEO","status":"Completed","year":2022,"date":"2023-01-22","budget_allocated":9863000.0,"budget_spent":7890706.03,"completion_percentage":100,"contractor":"5'S CONSTRUCTION & SUPPLY","image_path":""},
    {"id":101,"project_name":"Construction of Flood Control Structure/Slope Protection Along Suage River, Pototan, Iloilo","category":"Flood Control and Drainage","district":"2nd District","implementing_office":"DPWH - Iloilo 2nd DEO","status":"Completed","year":2022,"date":"2023-11-26","budget_allocated":77952000.0,"budget_spent":62361253.4,"completion_percentage":100,"contractor":"ROPRIM CONSTRUCTION CORPORATION","image_path":""},
    {"id":102,"project_name":"Construction of Road Slope Protection Structure Along Iloilo-Capiz Rd (Old Route)","category":"Roads","district":"2nd District","implementing_office":"DPWH - Iloilo 2nd DEO","status":"Completed","year":2022,"date":"2022-11-10","budget_allocated":3062000.0,"budget_spent":2449949.58,"completion_percentage":100,"contractor":"GGMU CONSTRUCTION AND SUPPLY","image_path":""},
    {"id":103,"project_name":"Rehabilitation/Major Repair of Suage Bridge (B00012PN) Along Pototan-Tina-Lambunao Rd","category":"Bridges","district":"2nd District","implementing_office":"DPWH - Iloilo 2nd DEO","status":"Completed","year":2023,"date":"2023-05-31","budget_allocated":22436000.0,"budget_spent":17949060.0,"completion_percentage":100,"contractor":"AFG ZILLION CONSTRUCTION CORPORATION","image_path":""},
    {"id":104,"project_name":"Construction of Multi-Purpose Building, Municipality of Lambunao, Iloilo","category":"Buildings and Facilities","district":"2nd District","implementing_office":"DPWH - Iloilo 2nd DEO","status":"Completed","year":2023,"date":"2023-11-06","budget_allocated":12955000.0,"budget_spent":10364111.74,"completion_percentage":100,"contractor":"LUCKY H&K CONSTRUCTION","image_path":""},
    {"id":105,"project_name":"Construction of Flood Control/Slope Protection Along Jalaur River, Dingle, Iloilo","category":"Flood Control and Drainage","district":"2nd District","implementing_office":"DPWH - Iloilo 2nd DEO","status":"Completed","year":2023,"date":"2023-12-20","budget_allocated":29705000.0,"budget_spent":23763658.51,"completion_percentage":100,"contractor":"STRONGLANE BUILDERS AND TRADING CORPORATION","image_path":""},
    {"id":106,"project_name":"Concreting of Barangay Road, Barangay Cunarom, Lambunao, Iloilo","category":"Roads","district":"2nd District","implementing_office":"DPWH - Iloilo 2nd DEO","status":"Completed","year":2023,"date":"2023-05-28","budget_allocated":12091000.0,"budget_spent":9672485.21,"completion_percentage":100,"contractor":"PCG BUILDERS CORPORATION","image_path":""},
    {"id":107,"project_name":"Rehabilitation/Major Repair of Monfort Bridge (B00533PN) Along Barotac Nuevo-Dumangas-Dacutan Wharf Rd","category":"Bridges","district":"2nd District","implementing_office":"DPWH - Iloilo 2nd DEO","status":"Completed","year":2024,"date":"2024-05-14","budget_allocated":9356000.0,"budget_spent":7485094.51,"completion_percentage":100,"contractor":"JMPTECH CONSTRUCTION & SUPPLY","image_path":""},
    {"id":108,"project_name":"Construction (Completion) of Multi-Purpose Building of Barangay Sta. Rita, Janiuay, Iloilo","category":"Buildings and Facilities","district":"2nd District","implementing_office":"DPWH - Iloilo 2nd DEO","status":"Completed","year":2024,"date":"2024-09-01","budget_allocated":3638000.0,"budget_spent":2910000.0,"completion_percentage":100,"contractor":"OTING CONSTRUCTION AND SUPPLY","image_path":""},
    {"id":109,"project_name":"Construction of Flood Control Structure Along Jalaur River, Barangay Bongco, Pototan, Iloilo","category":"Flood Control and Drainage","district":"2nd District","implementing_office":"DPWH - Iloilo 2nd DEO","status":"Completed","year":2024,"date":"2024-08-11","budget_allocated":42712000.0,"budget_spent":34169585.46,"completion_percentage":100,"contractor":"A.D. PENDON CONSTRUCTION & SUPPLY, INC.","image_path":""},
    {"id":110,"project_name":"Preventive Maintenance of Road: Asphalt Overlay - Baje-Ngi-Ngi-an-Bingawan Rd","category":"Roads","district":"2nd District","implementing_office":"DPWH - Iloilo 2nd DEO","status":"Completed","year":2024,"date":"2024-05-20","budget_allocated":26245000.0,"budget_spent":20996135.36,"completion_percentage":100,"contractor":"TOPMOST DEVELOPMENT & MKTG. CORP.","image_path":""},
    {"id":111,"project_name":"Preventive Maintenance of Road: Asphalt Overlay - Iloilo City-Leganes-Dumangas Coastal Rd","category":"Roads","district":"2nd District","implementing_office":"DPWH - Iloilo 2nd DEO","status":"Completed","year":2025,"date":"2025-07-16","budget_allocated":31680460.0,"budget_spent":31450090.47,"completion_percentage":100,"contractor":"A.D. PENDON CONSTRUCTION & SUPPLY, INC.","image_path":""},
    {"id":112,"project_name":"Construction of River Control Structure Along Jalaur River, Package 5, Barotac Nuevo, Iloilo","category":"Flood Control and Drainage","district":"2nd District","implementing_office":"DPWH - Iloilo 2nd DEO","status":"Completed","year":2025,"date":"2025-05-19","budget_allocated":54571300.0,"budget_spent":53703049.61,"completion_percentage":100,"contractor":"MJ BARCELONA CONSTRUCTION AND SUPPLY / STEVEN CONSTRUCTION & SUPPLY","image_path":""},
    {"id":113,"project_name":"Construction (Completion) of Multi-Purpose Building, Barangay Daan Banwa, Estancia, Iloilo","category":"Buildings and Facilities","district":"2nd District","implementing_office":"DPWH - Iloilo 2nd DEO","status":"Completed","year":2025,"date":"2025-07-06","budget_allocated":2970000.0,"budget_spent":2959990.34,"completion_percentage":100,"contractor":"BLOCK 15 CONSTRUCTION SERVICES","image_path":""},
    # ---- 3rd DISTRICT -----
    {"id":114,"project_name":"Rehabilitation/Major Repair of Bacjauan Bridge Along Concepcion-San Dionisio Road, Concepcion, Iloilo","category":"Bridges","district":"3rd District","implementing_office":"DPWH - Iloilo 3rd DEO","status":"Completed","year":2016,"date":"2016-03-07","budget_allocated":6071000.0,"budget_spent":4856556.5,"completion_percentage":100,"contractor":"WOODLAND CONSTRUCTION & SUPPLY, INC.","image_path":""},
    {"id":115,"project_name":"Construction/Rehabilitation of Barotac Viejo River Control, Brgy. Poblacion Ilawod, Barotac Viejo, Iloilo","category":"Flood Control and Drainage","district":"3rd District","implementing_office":"DPWH - Iloilo 3rd DEO","status":"Completed","year":2016,"date":"2016-11-03","budget_allocated":6169000.0,"budget_spent":4935454.6,"completion_percentage":100,"contractor":"SUPREME ABF CONSTRUCTION & CONSTRUCTION SUPPLY COMPANY INC.","image_path":""},
    {"id":116,"project_name":"Construction/Repair/Rehabilitation of Multi-Purpose Building (Covered Court) Brgy. Ardemil, Sara, Iloilo","category":"Buildings and Facilities","district":"3rd District","implementing_office":"DPWH - Iloilo 3rd DEO","status":"Completed","year":2016,"date":"2016-06-21","budget_allocated":6169000.0,"budget_spent":4935454.6,"completion_percentage":100,"contractor":"JHALL MARKETING & SERVICES","image_path":""},
    {"id":117,"project_name":"Construction of Covered Court, Brgy. Ipil, Balasan, Iloilo","category":"Buildings and Facilities","district":"3rd District","implementing_office":"DPWH - Iloilo 3rd DEO","status":"Completed","year":2017,"date":"2017-04-29","budget_allocated":2425000.0,"budget_spent":1939986.3,"completion_percentage":100,"contractor":"S.T. SALCEDO CONSTRUCTION CORP.","image_path":""},
    {"id":118,"project_name":"Construction of Barangay Road, Poblacion Ilaya, Sara, Iloilo","category":"Roads","district":"3rd District","implementing_office":"DPWH - Iloilo 3rd DEO","status":"Completed","year":2017,"date":"2017-05-10","budget_allocated":2437000.0,"budget_spent":1949822.41,"completion_percentage":100,"contractor":"JHALL MARKETING & SERVICES","image_path":""},
    {"id":119,"project_name":"Widening of Bacabac Bridge (B00221PN) Along Sara-Concepcion Road, Sara, Iloilo","category":"Bridges","district":"3rd District","implementing_office":"DPWH - Iloilo 3rd DEO","status":"Completed","year":2018,"date":"2018-08-18","budget_allocated":17033000.0,"budget_spent":13626696.32,"completion_percentage":100,"contractor":"WOODLAND CONSTRUCTION & SUPPLY, INC.","image_path":""},
    {"id":120,"project_name":"Construction (Completion) of Multi-Purpose Alumni Hall, Barotac Viejo NHS, Brgy. Poblacion, Barotac Viejo, Iloilo","category":"Buildings and Facilities","district":"3rd District","implementing_office":"DPWH - Iloilo 3rd DEO","status":"Completed","year":2018,"date":"2018-04-02","budget_allocated":622000.0,"budget_spent":497820.3,"completion_percentage":100,"contractor":"WINCES CONSTRUCTION & SUPPLY","image_path":""},
    {"id":121,"project_name":"Construction of Barotac Viejo River Control, Brgy. Poblacion Ilawod, Barotac Viejo, Iloilo","category":"Flood Control and Drainage","district":"3rd District","implementing_office":"DPWH - Iloilo 3rd DEO","status":"Completed","year":2018,"date":"2018-10-07","budget_allocated":63021000.0,"budget_spent":50416442.89,"completion_percentage":100,"contractor":"UNITEC BUILDER, INCORPORATED","image_path":""},
    {"id":122,"project_name":"Concreting/Rehabilitation of Banasig Malayu-an Road, Sitio Banasig, Malayu-an, Ajuy, Iloilo","category":"Roads","district":"3rd District","implementing_office":"DPWH - Iloilo 3rd DEO","status":"Completed","year":2018,"date":"2018-08-30","budget_allocated":6117000.0,"budget_spent":4893205.98,"completion_percentage":100,"contractor":"JHALL MARKETING & SERVICES","image_path":""},
    {"id":123,"project_name":"Widening of Tamangi Bridge (B00206PN) Along Iloilo East Coast-Capiz Road, San Dionisio, Iloilo","category":"Bridges","district":"3rd District","implementing_office":"DPWH - Iloilo 3rd DEO","status":"Completed","year":2019,"date":"2020-07-04","budget_allocated":45323000.0,"budget_spent":36258524.08,"completion_percentage":100,"contractor":"A.D. PENDON CONSTRUCTION & SUPPLY, INC.","image_path":""},
    {"id":124,"project_name":"Construction of Multi-Purpose Building (Barangay Hall), Brgy. Poblacion Zone 1, Estancia, Iloilo","category":"Buildings and Facilities","district":"3rd District","implementing_office":"DPWH - Iloilo 3rd DEO","status":"Completed","year":2019,"date":"2019-10-03","budget_allocated":3079000.0,"budget_spent":2463498.28,"completion_percentage":100,"contractor":"JHALL MARKETING & SERVICES","image_path":""},
    {"id":125,"project_name":"Construction of Flood Mitigation Structure - Reconstruction of Seawall, Brgy. Poblacion, Carles, Iloilo","category":"Flood Control and Drainage","district":"3rd District","implementing_office":"DPWH - Iloilo 3rd DEO","status":"Completed","year":2019,"date":"2019-12-29","budget_allocated":29554000.0,"budget_spent":23643114.11,"completion_percentage":100,"contractor":"A.C. RIVERO DEVELOPMENT CORPORATION","image_path":""},
    {"id":126,"project_name":"Construction of Drainage Along National Roads - Barotac Viejo-San Rafael Road, Barotac Viejo, Iloilo","category":"Roads","district":"3rd District","implementing_office":"DPWH - Iloilo 3rd DEO","status":"Completed","year":2019,"date":"2019-12-02","budget_allocated":9563000.0,"budget_spent":7650692.61,"completion_percentage":100,"contractor":"WINCES CONSTRUCTION & SUPPLY","image_path":""},
    {"id":127,"project_name":"Widening of Iyang Bridge (B00103PN) Along Concepcion-San Dionisio Road, Concepcion, Iloilo","category":"Bridges","district":"3rd District","implementing_office":"DPWH - Iloilo 3rd DEO","status":"Completed","year":2020,"date":"2020-11-29","budget_allocated":51450000.0,"budget_spent":41160000.0,"completion_percentage":100,"contractor":"A.D. PENDON CONSTRUCTION & SUPPLY, INC.","image_path":""},
    {"id":128,"project_name":"Construction of Multi-Purpose Building, Aglosong, Concepcion, Iloilo","category":"Buildings and Facilities","district":"3rd District","implementing_office":"DPWH - Iloilo 3rd DEO","status":"Completed","year":2020,"date":"2021-01-11","budget_allocated":2938000.0,"budget_spent":2350035.02,"completion_percentage":100,"contractor":"WINCES CONSTRUCTION & SUPPLY","image_path":""},
    {"id":129,"project_name":"Construction of Barotac Viejo River Control, Brgy. Poblacion Ilawod, Barotac Viejo, Iloilo","category":"Flood Control and Drainage","district":"3rd District","implementing_office":"DPWH - Iloilo 3rd DEO","status":"Completed","year":2020,"date":"2020-08-28","budget_allocated":56402000.0,"budget_spent":45121937.02,"completion_percentage":100,"contractor":"C'ZARLES CONSTRUCTION & SUPPLY","image_path":""},
    {"id":130,"project_name":"Construction of Concrete Road - NRJ Batad-Lumbia-Tanza-Estancia Road Leading to Gigantes Islands, Carles, Iloilo","category":"Roads","district":"3rd District","implementing_office":"DPWH - Iloilo 3rd DEO","status":"Completed","year":2020,"date":"2020-05-11","budget_allocated":17540000.0,"budget_spent":14031931.77,"completion_percentage":100,"contractor":"WOODLAND CONSTRUCTION & SUPPLY, INC.","image_path":""},
    {"id":131,"project_name":"Construction of Multi-Purpose Building, Barangay Poblacion Southeast Zone, Lemery, Iloilo","category":"Buildings and Facilities","district":"3rd District","implementing_office":"DPWH - Iloilo 3rd DEO","status":"Completed","year":2021,"date":"2021-06-05","budget_allocated":3092000.0,"budget_spent":2473708.14,"completion_percentage":100,"contractor":"5'S CONSTRUCTION & SUPPLY","image_path":""},
    {"id":132,"project_name":"Construction of Barotac Viejo River Control, Barangay Poblacion Ilawod, Barotac Viejo, Iloilo","category":"Flood Control and Drainage","district":"3rd District","implementing_office":"DPWH - Iloilo 3rd DEO","status":"Completed","year":2021,"date":"2022-09-28","budget_allocated":33593000.0,"budget_spent":26874537.53,"completion_percentage":100,"contractor":"F. GURREA CONSTRUCTION, INCORPORATED","image_path":""},
    {"id":133,"project_name":"Construction of Concrete Road - Langub-Piagao-Asluman Road Leading to Gigantes Islands, North Gigantes, Brgy. Granada, Carles, Iloilo","category":"Roads","district":"3rd District","implementing_office":"DPWH - Iloilo 3rd DEO","status":"Completed","year":2021,"date":"2022-02-24","budget_allocated":14197000.0,"budget_spent":11357984.01,"completion_percentage":100,"contractor":"VIRGIN BUILDERS CONSTRUCTION","image_path":""},
    {"id":134,"project_name":"Rehabilitation/Major Repair of Hinay-an Bridge (B00226PN) Along Barotac Viejo-San Rafael Road, San Rafael, Iloilo","category":"Bridges","district":"3rd District","implementing_office":"DPWH - Iloilo 3rd DEO","status":"Completed","year":2022,"date":"2022-10-01","budget_allocated":3920000.0,"budget_spent":3135792.33,"completion_percentage":100,"contractor":"1 BEATUS BUILDERS CORP.","image_path":""},
    {"id":135,"project_name":"Construction of DPWH Iloilo 3rd DEO Employees Quarters Building, Barotac Viejo, Iloilo","category":"Buildings and Facilities","district":"3rd District","implementing_office":"DPWH - Iloilo 3rd DEO","status":"Completed","year":2022,"date":"2022-07-01","budget_allocated":8575000.0,"budget_spent":6859998.01,"completion_percentage":100,"contractor":"WINCES CONSTRUCTION & SUPPLY","image_path":""},
    {"id":136,"project_name":"Construction of Seawall Along Iloilo East Coast Estancia Wharf Road, Brgy. Botongon, Estancia, Iloilo","category":"Flood Control and Drainage","district":"3rd District","implementing_office":"DPWH - Iloilo 3rd DEO","status":"Completed","year":2022,"date":"2023-04-07","budget_allocated":24125000.0,"budget_spent":19300000.0,"completion_percentage":100,"contractor":"PANAY EAST COAST CONSTRUCTION & SUPPLY","image_path":""},
    {"id":137,"project_name":"Preventive Maintenance of Road: Asphalt Overlay - Iloilo East Coast-Capiz Road, Barotac Viejo, Iloilo","category":"Roads","district":"3rd District","implementing_office":"DPWH - Iloilo 3rd DEO","status":"Completed","year":2022,"date":"2022-06-03","budget_allocated":18381000.0,"budget_spent":14704900.0,"completion_percentage":100,"contractor":"GOLDEN ROADRUNNER INTERNATIONAL CORP.","image_path":""},
    {"id":138,"project_name":"Rehabilitation/Major Repair of Aswe Bridge (B0053PN) Along Iloilo East Coast Capiz Road","category":"Bridges","district":"3rd District","implementing_office":"DPWH - Iloilo 3rd DEO","status":"Completed","year":2023,"date":"2023-07-25","budget_allocated":4222000.0,"budget_spent":3377500.0,"completion_percentage":100,"contractor":"SBF CONSTRUCTION & DEVELOPMENT CORPORATION","image_path":""},
    {"id":139,"project_name":"Construction (Completion) of Multi-Purpose Building, Barangay San Diego, Lemery, Iloilo","category":"Buildings and Facilities","district":"3rd District","implementing_office":"DPWH - Iloilo 3rd DEO","status":"Completed","year":2023,"date":"2023-04-25","budget_allocated":2475000.0,"budget_spent":1980000.0,"completion_percentage":100,"contractor":"BINJO CONSTRUCTION SERVICES","image_path":""},
    {"id":140,"project_name":"Construction of Flood Mitigation Structure, Barangay Poblacion Ilawod, Barotac Viejo, Iloilo","category":"Flood Control and Drainage","district":"3rd District","implementing_office":"DPWH - Iloilo 3rd DEO","status":"Completed","year":2023,"date":"2024-05-20","budget_allocated":108080000.0,"budget_spent":86464000.0,"completion_percentage":100,"contractor":"F. GURREA CONSTRUCTION, INCORPORATED","image_path":""},
    {"id":141,"project_name":"Road Widening Along Iloilo East Coast-Capiz Road","category":"Roads","district":"3rd District","implementing_office":"DPWH - Iloilo 3rd DEO","status":"Completed","year":2023,"date":"2023-11-28","budget_allocated":62729825.0,"budget_spent":50183860.0,"completion_percentage":100,"contractor":"CONTE BUILDERS & CONSTRUCTION SUPPLY","image_path":""},
    {"id":142,"project_name":"Construction of Concrete Bridge - Barotac Viejo Bypass Road, Barotac Viejo, Iloilo","category":"Bridges","district":"3rd District","implementing_office":"DPWH - Iloilo 3rd DEO","status":"Ongoing","year":2024,"date":"2024-01-01","budget_allocated":120625000.0,"budget_spent":96499953.21,"completion_percentage":30.05,"contractor":"F. GURREA CONSTRUCTION, INCORPORATED","image_path":""},
    {"id":143,"project_name":"Construction (Completion) of Multi-Purpose Building, Barangay Cawayan Elementary School, Carles, Iloilo","category":"Buildings and Facilities","district":"3rd District","implementing_office":"DPWH - Iloilo 3rd DEO","status":"Completed","year":2024,"date":"2024-06-21","budget_allocated":2475000.0,"budget_spent":1980000.0,"completion_percentage":100,"contractor":"BRPRIME CONSTRUCTION SUPPLIES","image_path":""},
    {"id":144,"project_name":"Construction of Flood Control Structure, Barangay Pili, Ajuy, Iloilo","category":"Flood Control and Drainage","district":"3rd District","implementing_office":"DPWH - Iloilo 3rd DEO","status":"Completed","year":2024,"date":"2024-12-10","budget_allocated":36749000.0,"budget_spent":29399525.91,"completion_percentage":100,"contractor":"C'ZARLES CONSTRUCTION & SUPPLY","image_path":""},
    {"id":145,"project_name":"Off-Carriageway Improvement: Paving of Shoulders - Langub-Piagao-Asluman Road, North Gigantes Islands, Brgy. Granada, Carles, Iloilo","category":"Roads","district":"3rd District","implementing_office":"DPWH - Iloilo 3rd DEO","status":"Completed","year":2024,"date":"2024-08-20","budget_allocated":18375000.0,"budget_spent":14700000.0,"completion_percentage":100,"contractor":"VIRGIN BUILDERS CONSTRUCTION","image_path":""},
    {"id":146,"project_name":"Construction of Concrete Bridge - Barotac Viejo Bypass Road Phase 2, Barotac Viejo, Iloilo","category":"Bridges","district":"3rd District","implementing_office":"DPWH - Iloilo 3rd DEO","status":"Ongoing","year":2025,"date":"2025-01-01","budget_allocated":162594000.0,"budget_spent":130074999.93,"completion_percentage":9.94,"contractor":"F. GURREA CONSTRUCTION, INCORPORATED","image_path":""},
    {"id":147,"project_name":"Construction (Completion) of Multi-Purpose Building, Barangay Daan Banwa, Estancia, Iloilo","category":"Buildings and Facilities","district":"3rd District","implementing_office":"DPWH - Iloilo 3rd DEO","status":"Completed","year":2025,"date":"2025-07-06","budget_allocated":3700000.0,"budget_spent":2959990.34,"completion_percentage":100,"contractor":"BLOCK 15 CONSTRUCTION SERVICES","image_path":""},
    {"id":148,"project_name":"Construction of Flood Control Structure, Barangay Poblacion Ilawod, Barotac Viejo, Iloilo","category":"Flood Control and Drainage","district":"3rd District","implementing_office":"DPWH - Iloilo 3rd DEO","status":"Ongoing","year":2025,"date":"2025-01-01","budget_allocated":92374000.0,"budget_spent":73899574.17,"completion_percentage":65.06,"contractor":"A.D. PENDON CONSTRUCTION & SUPPLY, INC.","image_path":""},
    {"id":149,"project_name":"Preventive Maintenance of Road: Asphalt Overlay - Iloilo East Coast Capiz Road","category":"Roads","district":"3rd District","implementing_office":"DPWH - Iloilo 3rd DEO","status":"Ongoing","year":2025,"date":"2025-01-01","budget_allocated":42849000.0,"budget_spent":34279174.08,"completion_percentage":88.66,"contractor":"A.D. PENDON CONSTRUCTION & SUPPLY, INC.","image_path":""},
    # ---- 4th DISTRICT -----
    {"id":150,"project_name":"Rehabilitation/Major Repair of Lanag 1 Bridge (B00476PN) Along New Lucena-Sta. Barbara Road, Sta. Barbara, Iloilo","category":"Bridges","district":"4th District","implementing_office":"DPWH - Iloilo 4th DEO","status":"Completed","year":2016,"date":"2016-05-09","budget_allocated":6732000.0,"budget_spent":5385736.58,"completion_percentage":100,"contractor":"CONTE BUILDERS & CONSTRUCTION SUPPLY","image_path":""},
    {"id":151,"project_name":"Construction of 1 Unit 2-Storey 4-Classroom School Building, Jelicuon-Cabugao NHS, New Lucena, Iloilo","category":"Buildings and Facilities","district":"4th District","implementing_office":"DPWH - Iloilo 4th DEO","status":"Completed","year":2016,"date":"2017-12-29","budget_allocated":7684000.0,"budget_spent":6174334.53,"completion_percentage":100,"contractor":"CHEDMARYL CONSTRUCTION & SUPPLIES","image_path":""},
    {"id":152,"project_name":"Construction/Rehabilitation of Aganan Flood Control Project (Jaro-Aganan River), Poblacion, San Miguel, Iloilo","category":"Flood Control and Drainage","district":"4th District","implementing_office":"DPWH - Iloilo 4th DEO","status":"Completed","year":2016,"date":"2017-05-10","budget_allocated":58064000.0,"budget_spent":46541396.45,"completion_percentage":100,"contractor":"F. GURREA CONSTRUCTION, INCORPORATED","image_path":""},
    {"id":153,"project_name":"Concreting of Brgy. Talacuan FMR (Sitio Takasi), Brgy. Talacuan, Leon, Iloilo","category":"Roads","district":"4th District","implementing_office":"DPWH - Iloilo 4th DEO","status":"Completed","year":2016,"date":"2016-11-13","budget_allocated":2140000.0,"budget_spent":1711958.79,"completion_percentage":100,"contractor":"PESOM CONSTRUCTION SERVICES","image_path":""},
    {"id":154,"project_name":"Replacement of Cabugao Norte Bridge (B00480PN) Along Leganes-Sta. Barbara Road","category":"Bridges","district":"4th District","implementing_office":"DPWH - Iloilo 4th DEO","status":"Completed","year":2017,"date":"2018-03-24","budget_allocated":13357000.0,"budget_spent":10685200.71,"completion_percentage":100,"contractor":"WOODLAND CONSTRUCTION & SUPPLY, INC.","image_path":""},
    {"id":155,"project_name":"Construction of Technical and Vocational Workshop Buildings/Laboratories, Leganes NHS, Leganes, Iloilo","category":"Buildings and Facilities","district":"4th District","implementing_office":"DPWH - Iloilo 4th DEO","status":"Completed","year":2017,"date":"2018-01-13","budget_allocated":3546000.0,"budget_spent":2837067.48,"completion_percentage":100,"contractor":"MAKANA BUILDERS & SUPPLY","image_path":""},
    {"id":156,"project_name":"Construction of Aganan Flood Control Project (Jaro-Aganan River) Brgy. 9 to Brgy. 14, San Miguel, Iloilo","category":"Flood Control and Drainage","district":"4th District","implementing_office":"DPWH - Iloilo 4th DEO","status":"Completed","year":2017,"date":"2018-03-10","budget_allocated":58049000.0,"budget_spent":46539449.75,"completion_percentage":100,"contractor":"ED1SON DEVELOPMENT & CONSTRUCTION INC.","image_path":""},
    {"id":157,"project_name":"Construction/Opening of Brgy. Bobon, Leon to Brgy. Manasa, Alimodian FMR, Leon, Iloilo","category":"Roads","district":"4th District","implementing_office":"DPWH - Iloilo 4th DEO","status":"Completed","year":2017,"date":"2018-11-30","budget_allocated":21268000.0,"budget_spent":17014497.91,"completion_percentage":100,"contractor":"PATRILA BUILDERS, INC.","image_path":""},
    {"id":158,"project_name":"Widening of Morobwan Bridge, JCT. Tabucan-Cabatuan-Consolacion-San Miguel Leading to Iloilo International Airport, Iloilo","category":"Bridges","district":"4th District","implementing_office":"DPWH - Iloilo 4th DEO","status":"Completed","year":2018,"date":"2019-04-02","budget_allocated":17150000.0,"budget_spent":13719649.69,"completion_percentage":100,"contractor":"SBF CONSTRUCTION & DEVELOPMENT CORPORATION","image_path":""},
    {"id":159,"project_name":"Completion of Multi-Purpose Building (Legislative Building), Brgy. Poblacion, Leganes, Iloilo","category":"Buildings and Facilities","district":"4th District","implementing_office":"DPWH - Iloilo 4th DEO","status":"Completed","year":2018,"date":"2018-05-25","budget_allocated":1763000.0,"budget_spent":1410742.78,"completion_percentage":100,"contractor":"J E G CONSTRUCTION FIRM CORPORATION","image_path":""},
    {"id":160,"project_name":"Construction of Aganan Flood Control Project (Jaro-Aganan River), Brgy. 14, San Miguel, Iloilo","category":"Flood Control and Drainage","district":"4th District","implementing_office":"DPWH - Iloilo 4th DEO","status":"Completed","year":2018,"date":"2018-12-07","budget_allocated":52368000.0,"budget_spent":41894279.74,"completion_percentage":100,"contractor":"ED1SON DEVELOPMENT & CONSTRUCTION INC. / PATRILA BUILDERS, INC.","image_path":""},
    {"id":161,"project_name":"Reconstruction from Paved to Concrete - Iloilo-Capiz Road (New Route)","category":"Roads","district":"4th District","implementing_office":"DPWH - Iloilo 4th DEO","status":"Completed","year":2018,"date":"2019-01-03","budget_allocated":95742000.0,"budget_spent":76593451.88,"completion_percentage":100,"contractor":"IBC INTERNATIONAL BUILDERS CORPORATION","image_path":""},
    {"id":162,"project_name":"Rehabilitation/Major Repair of Aganan Bridge (B00450PN) Along Mandurriao-San Miguel-Alimodian-Maasin-Cabatuan Road","category":"Bridges","district":"4th District","implementing_office":"DPWH - Iloilo 4th DEO","status":"Completed","year":2019,"date":"2019-08-28","budget_allocated":3839000.0,"budget_spent":3071432.52,"completion_percentage":100,"contractor":"SBF CONSTRUCTION & DEVELOPMENT CORPORATION","image_path":""},
    {"id":163,"project_name":"Construction of Multi-Purpose Building, Brgy. Tigum, Pavia, Iloilo","category":"Buildings and Facilities","district":"4th District","implementing_office":"DPWH - Iloilo 4th DEO","status":"Completed","year":2019,"date":"2019-11-02","budget_allocated":3073000.0,"budget_spent":2458236.03,"completion_percentage":100,"contractor":"J.J.S. CONSTRUCTION","image_path":""},
    {"id":164,"project_name":"Rehabilitation of Buntatala Creek, Leganes, Iloilo","category":"Flood Control and Drainage","district":"4th District","implementing_office":"DPWH - Iloilo 4th DEO","status":"Completed","year":2019,"date":"2020-06-03","budget_allocated":36749000.0,"budget_spent":29398941.83,"completion_percentage":100,"contractor":"J.S. LAYSON & CO., INC.","image_path":""},
    {"id":165,"project_name":"Reconstruction to Concrete Pavement - New Lucena-Sta. Barbara Road","category":"Roads","district":"4th District","implementing_office":"DPWH - Iloilo 4th DEO","status":"Completed","year":2019,"date":"2020-01-18","budget_allocated":57143000.0,"budget_spent":45714784.6,"completion_percentage":100,"contractor":"J E G CONSTRUCTION FIRM CORPORATION","image_path":""},
    {"id":166,"project_name":"Construction of Concrete Bridge - Baguingin Bridge Along JCT. Bancal-Leon-Antique Boundary Road","category":"Bridges","district":"4th District","implementing_office":"DPWH - Iloilo 4th DEO","status":"Completed","year":2020,"date":"2020-07-30","budget_allocated":9800000.0,"budget_spent":7839995.6,"completion_percentage":100,"contractor":"PATRILA BUILDERS, INC.","image_path":""},
    {"id":167,"project_name":"Construction of Aganan Flood Control Project (Jaro-Aganan River), Brgy. Bagumbayan, Alimodian, Iloilo","category":"Flood Control and Drainage","district":"4th District","implementing_office":"DPWH - Iloilo 4th DEO","status":"Completed","year":2020,"date":"2020-12-28","budget_allocated":61250000.0,"budget_spent":48999985.88,"completion_percentage":100,"contractor":"IBC INTERNATIONAL BUILDERS CORPORATION","image_path":""},
    {"id":168,"project_name":"Reconstruction to Concrete Pavement - JCT Bancal-Leon-Antique Boundary Road","category":"Roads","district":"4th District","implementing_office":"DPWH - Iloilo 4th DEO","status":"Completed","year":2020,"date":"2021-07-30","budget_allocated":36750000.0,"budget_spent":29399999.55,"completion_percentage":100,"contractor":"EAST ASIA CONSTRUCTION, INC.","image_path":""},
    {"id":169,"project_name":"Construction of 1 Unit 1-Storey 5-Classroom School Building, Don Benjamin Jalandoni Sr. MNHS, Zarraga, Iloilo","category":"Buildings and Facilities","district":"4th District","implementing_office":"DPWH - Iloilo 4th DEO","status":"Completed","year":2020,"date":"2020-12-31","budget_allocated":13815892.33,"budget_spent":13815873.78,"completion_percentage":100,"contractor":"MAKANA BUILDERS & SUPPLY","image_path":""},
    {"id":170,"project_name":"Construction/Rehabilitation/Improvement of Facilities for Persons with Disabilities (PWD) and Senior Citizens","category":"Buildings and Facilities","district":"4th District","implementing_office":"DPWH - Iloilo 4th DEO","status":"Completed","year":2021,"date":"2021-06-26","budget_allocated":22164000.0,"budget_spent":1773159.68,"completion_percentage":100,"contractor":"1 BEATUS BUILDERS CORP.","image_path":""},
    {"id":171,"project_name":"Completion of Hanging Foot Bridge, Balabag, Sta. Barbara, Iloilo","category":"Bridges","district":"4th District","implementing_office":"DPWH - Iloilo 4th DEO","status":"Completed","year":2021,"date":"2022-03-23","budget_allocated":1244000.0,"budget_spent":994881.35,"completion_percentage":100,"contractor":"VEONG CONSTRUCTION & SUPPLY","image_path":""},
    {"id":172,"project_name":"Construction of Sibalom Flood Control Project (Sibalom River), Barangay Nagbangi, Leon, Iloilo","category":"Flood Control and Drainage","district":"4th District","implementing_office":"DPWH - Iloilo 4th DEO","status":"Completed","year":2021,"date":"2021-11-25","budget_allocated":94079000.0,"budget_spent":75263578.46,"completion_percentage":100,"contractor":"F. GURREA CONSTRUCTION, INCORPORATED","image_path":""},
    {"id":173,"project_name":"Concreting of Agony Hill Road, Taban-Manguining, Alimodian, Iloilo","category":"Roads","district":"4th District","implementing_office":"DPWH - Iloilo 4th DEO","status":"Completed","year":2021,"date":"2022-02-05","budget_allocated":3706000.0,"budget_spent":2964925.09,"completion_percentage":100,"contractor":"1 BEATUS BUILDERS CORP.","image_path":""},
    {"id":174,"project_name":"Rehabilitation of Guimbal Steel Bridge, Guimbal, Iloilo","category":"Bridges","district":"4th District","implementing_office":"DPWH - Iloilo 1st DEO","status":"Completed","year":2022,"date":"2023-04-05","budget_allocated":18450000.0,"budget_spent":14759847.52,"completion_percentage":100,"contractor":"NOE'S BUILDERS","image_path":""},
    {"id":175,"project_name":"Construction of Multi-Purpose Building, Barangay Ingay, Leon, Iloilo","category":"Buildings and Facilities","district":"4th District","implementing_office":"DPWH - Iloilo 4th DEO","status":"Completed","year":2022,"date":"2023-03-15","budget_allocated":6184000.0,"budget_spent":4946854.62,"completion_percentage":100,"contractor":"AXL BUILDERS AND CONSTRUCTION SUPPLIES INC.","image_path":""},
    {"id":176,"project_name":"Construction of Aganan Flood Control Structure (Jaro-Aganan River), Brgy. Poblacion, Alimodian, Iloilo","category":"Flood Control and Drainage","district":"4th District","implementing_office":"DPWH - Iloilo 4th DEO","status":"Completed","year":2022,"date":"2022-12-19","budget_allocated":120624000.0,"budget_spent":96499040.75,"completion_percentage":100,"contractor":"A.D. PENDON CONSTRUCTION & SUPPLY, INC.","image_path":""},
    {"id":177,"project_name":"Construction of Access Road from Brgy. Guihaman to Brgy. Buntatala Road, Leganes, Iloilo","category":"Roads","district":"4th District","implementing_office":"DPWH - Iloilo 4th DEO","status":"Completed","year":2022,"date":"2022-04-22","budget_allocated":11879000.0,"budget_spent":9503169.82,"completion_percentage":100,"contractor":"BANSOY CONSTRUCTION AND SUPPLY","image_path":""},
    {"id":178,"project_name":"Rehabilitation/Major Repair of Isian Bridge (B00171PN) Along Guimbal-Igbaras-Tubungan-Leon Road","category":"Bridges","district":"4th District","implementing_office":"DPWH - Iloilo 4th DEO","status":"Completed","year":2023,"date":"2023-05-07","budget_allocated":5880000.0,"budget_spent":5821051.63,"completion_percentage":100,"contractor":"SBF CONSTRUCTION & DEVELOPMENT CORPORATION","image_path":""},
    {"id":179,"project_name":"Construction of Aganan Flood Control Structure (Jaro-Aganan River), Barangay Poblacion, Alimodian, Iloilo","category":"Flood Control and Drainage","district":"4th District","implementing_office":"DPWH - Iloilo 4th DEO","status":"Completed","year":2023,"date":"2024-02-17","budget_allocated":96500000.0,"budget_spent":96499391.23,"completion_percentage":100,"contractor":"A.D. PENDON CONSTRUCTION & SUPPLY, INC.","image_path":""},
    {"id":180,"project_name":"Preventive Maintenance of Road: Asphalt Overlay - Iloilo-Capiz Road (New Route)","category":"Roads","district":"4th District","implementing_office":"DPWH - Iloilo 4th DEO","status":"Completed","year":2023,"date":"2023-07-31","budget_allocated":63036695.0,"budget_spent":62320000.0,"completion_percentage":100,"contractor":"IBC INTERNATIONAL BUILDERS CORPORATION","image_path":""},
    {"id":181,"project_name":"Construction of Multi-Purpose Building, Brgy. Poblacion, Leganes, Iloilo (2023)","category":"Buildings and Facilities","district":"4th District","implementing_office":"DPWH - Iloilo 4th DEO","status":"Completed","year":2023,"date":"2023-07-31","budget_allocated":63036695.0,"budget_spent":62320000.0,"completion_percentage":100,"contractor":"IBC INTERNATIONAL BUILDERS CORPORATION","image_path":""},
    {"id":182,"project_name":"Construction of Bridge, Barangay Camandag, Leon, Iloilo","category":"Bridges","district":"4th District","implementing_office":"DPWH - Iloilo 4th DEO","status":"Ongoing","year":2024,"date":"2024-01-01","budget_allocated":4950000.0,"budget_spent":4949328.85,"completion_percentage":89.92,"contractor":"PESOM CONSTRUCTION SERVICES","image_path":""},
    {"id":183,"project_name":"Construction of Multi-Purpose Building, Barangay Tacuyong Norte, Leon, Iloilo","category":"Buildings and Facilities","district":"4th District","implementing_office":"DPWH - Iloilo 4th DEO","status":"Completed","year":2024,"date":"2024-08-02","budget_allocated":4950000.0,"budget_spent":4941661.75,"completion_percentage":100,"contractor":"RBA CONSTRUCTION SERVICES","image_path":""},
    {"id":184,"project_name":"Construction of Aganan Flood Control Structure (Jaro-Aganan River), Barangay Balabago, Alimodian, Iloilo","category":"Flood Control and Drainage","district":"4th District","implementing_office":"DPWH - Iloilo 4th DEO","status":"Completed","year":2024,"date":"2024-12-17","budget_allocated":97510000.0,"budget_spent":97509993.65,"completion_percentage":100,"contractor":"IBC INTERNATIONAL BUILDERS CORPORATION","image_path":""},
    {"id":185,"project_name":"Construction of Road, Barangay Pungsod to Buayahon, Sta. Barbara, Iloilo","category":"Roads","district":"4th District","implementing_office":"DPWH - Iloilo 4th DEO","status":"Completed","year":2024,"date":"2024-03-19","budget_allocated":4950000.0,"budget_spent":4947074.86,"completion_percentage":100,"contractor":"A MAQUILING CONSTRUCTION AND SUPPLY","image_path":""},
    {"id":186,"project_name":"Rehabilitation/Major Repair of Janipa-an Bridge (B00178PN) Along Iloilo-Capiz Road (New Route)","category":"Bridges","district":"4th District","implementing_office":"DPWH - Iloilo 4th DEO","status":"Completed","year":2025,"date":"2025-05-09","budget_allocated":8820000.0,"budget_spent":8783845.13,"completion_percentage":100,"contractor":"1 BEATUS BUILDERS CORP.","image_path":""},
    {"id":187,"project_name":"Construction of Multi-Purpose Building, Barangay Igcadios, Leon, Iloilo","category":"Buildings and Facilities","district":"4th District","implementing_office":"DPWH - Iloilo 4th DEO","status":"Ongoing","year":2025,"date":"2025-01-01","budget_allocated":4950000.0,"budget_spent":4900499.44,"completion_percentage":94.32,"contractor":"E C GOLDEN CONSTRUCTION SERVICES CO.","image_path":""},
    {"id":188,"project_name":"Construction of Slope Protection and Sabo Dam, Sibalom River Irrigation System, Leon, Iloilo","category":"Flood Control and Drainage","district":"4th District","implementing_office":"DPWH - Iloilo 4th DEO","status":"Completed","year":2025,"date":"2025-07-22","budget_allocated":29400000.0,"budget_spent":29099264.46,"completion_percentage":100,"contractor":"G. UY CONSTRUCTION","image_path":""},
    {"id":189,"project_name":"Construction of Road, Barangay Poblacion, Leganes, Iloilo","category":"Roads","district":"4th District","implementing_office":"DPWH - Iloilo 4th DEO","status":"Ongoing","year":2025,"date":"2025-01-01","budget_allocated":19800000.0,"budget_spent":19700941.62,"completion_percentage":96.4,"contractor":"MDG CONSTRUCTION","image_path":""},
]


# ════════════════════════════════════════════════════════════════════════════
# ── SECTION B: DEVELOPER CRUD HELPERS ────────────────────────────────────
# ════════════════════════════════════════════════════════════════════════════
def get_logo_src():
    try:
        data = pathlib.Path(LOGO_PATH).read_bytes()
        b64  = base64.b64encode(data).decode()
        return f"data:image/png;base64,{b64}"
    except Exception:
        return ""

LOGO_SRC = get_logo_src()

def get_image_base64(path, mime="image/jpeg"):
    try:
        with open(path, "rb") as image_file:
            encoded = base64.b64encode(image_file.read()).decode()
            return f"data:{mime};base64,{encoded}"
    except Exception:
        return ""
    
LOGO_SRC = get_logo_src()

def get_image_base64(path, mime="image/jpeg"):
    try:
        with open(path, "rb") as image_file:
            encoded = base64.b64encode(image_file.read()).decode()
            return f"data:{mime};base64,{encoded}"
    except Exception:
        return ""

def add_project(project_dict: dict) -> None:
    if "id" not in project_dict:
        project_dict["id"] = max(p.get("id", 0) for p in PROJECTS) + 1
    PROJECTS.append(project_dict)


def update_project(project_id: int, updated_dict: dict) -> bool:
    for project in PROJECTS:
        if project.get("id") == project_id:
            project.update(updated_dict)
            return True
    return False


# ════════════════════════════════════════════════════════════════════════════
# ── SECTION C: LOCAL IMAGE HELPER  ───────────────────────────────────────
# ════════════════════════════════════════════════════════════════════════════

def _resolve_image(image_path: str) -> str:
    if not image_path:
        return ""
    if image_path.startswith("http://") or image_path.startswith("https://"):
        return image_path
    p = pathlib.Path(image_path)
    if not p.is_absolute():
        p = pathlib.Path(__file__).parent / p
    if p.exists():
        ext = p.suffix.lower().lstrip(".")
        mime = {
            "jpg": "image/jpeg", "jpeg": "image/jpeg",
            "png": "image/png", "gif": "image/gif",
            "webp": "image/webp", "svg": "image/svg+xml",
        }.get(ext, "image/jpeg")
        with open(p, "rb") as f:
            b64 = base64.b64encode(f.read()).decode()
        return f"data:{mime};base64,{b64}"
    return ""

# Resolve images
for _p in PROJECTS:
    _p["image_path"] = _resolve_image(_p.get("image_path", ""))

# ════════════════════════════════════════════════════════════════════════════
# ── SECTION D: RANDOMISATION ─────────────────────────────────────────────
# ════════════════════════════════════════════════════════════════════════════

random.shuffle(PROJECTS)

# ════════════════════════════════════════════════════════════════════════════
# ── SECTION E: DERIVED STATS  ────────────────────────────────────────────
# ════════════════════════════════════════════════════════════════════════════

def _get_category_counts() -> dict:
    cats = ["Bridges", "Roads", "Buildings and Facilities", "Flood Control and Drainage"]
    return {c: sum(1 for p in PROJECTS if p.get("category") == c) for c in cats}


def _get_summary_stats() -> dict:
    years     = sorted({p["year"] for p in PROJECTS if p.get("year")})
    districts = sorted({p["district"] for p in PROJECTS if p.get("district")})
    return {
        "total_projects":  len(PROJECTS),
        "total_districts": len(districts),
        "total_allocated": sum(p.get("budget_allocated", 0) for p in PROJECTS),
        "total_spent":     sum(p.get("budget_spent", 0) for p in PROJECTS),
        "years":           years,
        "districts":       districts,
    }

def fmt_budget(v: float) -> str:
    if v >= 1e9: return f"₱{v/1e9:.1f}B"
    if v >= 1e6: return f"₱{v/1e6:.0f}M"
    return f"₱{v:,.0f}"


# Compute stats
CAT_COUNTS      = _get_category_counts()
STATS           = _get_summary_stats()
TOTAL_PROJECTS  = STATS["total_projects"]
TOTAL_DISTRICTS = STATS["total_districts"]
TOTAL_ALLOCATED = STATS["total_allocated"]
TOTAL_SPENT     = STATS["total_spent"]
YEAR_LIST       = STATS["years"]
DISTRICTS       = STATS["districts"]

PROJECTS_JSON = json.dumps(PROJECTS)

year_options = "".join(f'<option>{y}</option>' for y in sorted(YEAR_LIST, reverse=True))
dist_options = "".join(f'<option value="{d}">{d}</option>' for d in DISTRICTS)

# ════════════════════════════════════════════════════════════════════════════
# ── SECTION F: STREAMLIT CHROME HIDE + NAVIGATION LISTENER ───────────────
# ════════════════════════════════════════════════════════════════════════════

st.markdown("""
<style>
#MainMenu, footer, header,
[data-testid="stToolbar"],
[data-testid="stDecoration"],
[data-testid="stStatusWidget"],
[data-testid="stHeader"],
[data-testid="stSidebarNav"],
[data-testid="collapsedControl"] { display: none !important; }
            

html, body,
[data-testid="stApp"],
[data-testid="stAppViewContainer"],
[data-testid="stAppViewBlockContainer"],
[data-testid="block-container"],
.main, .main > div,
section.main, section.main > div,
div[class*="css"] {
    padding: 0 !important;
    margin: 0 !important;
    max-width: 100% !important;
    width: 100% !important;
    background: #060517 !important;
    height: 100vh;
    overflow-y: auto;  
    overflow-x: hidden;
    overflow: hidden !important;        
}

iframe {
    display: block !important;
    width: 100vw !important;
    height: 100vh !important;
    border: none !important;
    position: fixed !important;
    top: 0 !important;
    left: 0 !important;
    z-index: 999 !important;
    overflow: hidden !important;
}
</style>
""", unsafe_allow_html=True)


if LOGO_SRC:
    LOGO_TAG = f'<img src="{LOGO_SRC}" alt="DPWH Logo" style="height:44px;width:auto;object-fit:contain;">'
else:
    LOGO_TAG = '<div class="nav-logo-icon">DPWH</div>'

# ════════════════════════════════════════════════════════════════════════════
# ── SECTION G: MAIN HTML / CSS / JS  ─────────────────────────────────────
# ════════════════════════════════════════════════════════════════════════════

HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>DPWH Iloilo Infrastructure Dashboard</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@300;400;500;600;700;800;900&family=Barlow:wght@300;400;500;600&display=swap" rel="stylesheet">
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.min.js"></script>
<style>
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
:root{{
  --bg:#060517;--bg2:#0a0a1a;
  --fire:#D05B37;
  --accent:#D05B37;
  --accent2:#e85c1a;
  --accent-dim:rgba(208,91,55,.15);
  --accent-glow:rgba(208,91,55,.35);
  --text:#fff;--text-sec:#A9A9B3;
  --card:#ffffff08;--card-hover:#ffffff0e;
  --border:#ffffff0d;--border-hover:rgba(208,91,55,.5);
  --radius:12px;--radius-sm:8px;
}}

html{{scroll-behavior:smooth;scroll-padding-top:64px}}

body{{
  background:var(--bg);color:var(--text);
  font-family:'Barlow Condensed',sans-serif;
  overflow-x:hidden;min-height:100vh;
  padding-top:64px;
}}
::-webkit-scrollbar{{width:5px}}
::-webkit-scrollbar-track{{background:transparent}}
::-webkit-scrollbar-thumb{{background:rgba(208,91,55,.35);border-radius:3px}}

/* ── NAVBAR ── */
.nav {{
    position: fixed; top: 0; left: 0; right: 0; z-index: 1000;
    display: flex; align-items: center; justify-content: space-between;
    padding: 0 40px; height: 68px;
    background: rgba(6,5,23,0.88);
    backdrop-filter: blur(14px);
    border-bottom: 1px solid rgba(208,91,55,0.18);
}}

.nav-logo {{
    display: flex; align-items: center; gap: 12px;
    text-decoration: none; cursor: pointer;
}}

.nav-logo-icon {{
    width: 44px; height: 44px;
    background: var(--fire);
    clip-path: polygon(50% 0%,100% 25%,100% 75%,50% 100%,0% 75%,0% 25%);
    display: flex; align-items: center; justify-content: center;
    font-family: 'Barlow Condensed', sans-serif;
    font-weight: 800; font-size: 11px; color: #fff;
    letter-spacing: .5px; flex-shrink: 0;
}}

.nav-logo-text {{ display: flex; flex-direction: column; line-height: 1.1; }}
.nav-logo-text .t1 {{
    font-family: 'Barlow Condensed', sans-serif;
    font-weight: 800; font-size: 17px;
    color: var(--fire); letter-spacing: 1.5px;
}}
.nav-logo-text .t2 {{
    font-size: 9px; color: var(--muted);
    letter-spacing: 2px; text-transform: uppercase;
}}

.nav-links {{ display: flex; gap: 36px; list-style: none; }}
.nav-links a {{
    font-family: 'Barlow Condensed', sans-serif;
    font-weight: 600; font-size: 14px;
    letter-spacing: 2px; text-transform: uppercase;
    color: var(--light); text-decoration: none;
    position: relative; padding-bottom: 3px;
    transition: color .25s;
    cursor: pointer;
}}

.nav-links a::after {{
    content: ''; position: absolute;
    bottom: 0; left: 0; width: 0; height: 2px;
    background: var(--fire); transition: width .3s ease;
    }}

.nav-links a:hover,
.nav-links a.active {{ color: var(--fire); }}
.nav-links a:hover::after,
.nav-links a.active::after {{ width: 100%; }}


/* ── HERO ── */
.hero-wrap {{
    position: relative;
    overflow: visible;
    background: var(--bg);
}}

.bg-grid{{
  position:absolute;inset:0;
  background-image:
    linear-gradient(rgba(208,91,55,.03) 1px,transparent 1px),
    linear-gradient(90deg,rgba(208,91,55,.03) 1px,transparent 1px);
  background-size:60px 60px;pointer-events:none;
}}
.bg-glow{{
  position:absolute;top:30%;left:50%;
  transform:translate(-50%,-50%);
  width:700px;height:700px;
  background:radial-gradient(ellipse,rgba(208,91,55,.07) 0%,transparent 70%);
  pointer-events:none;
}}
.services-wrap{{position:relative;overflow:visible}}
.services{{
  display:grid;
  grid-template-columns:1fr 280px 1fr;
  grid-template-rows:290px 290px;
  overflow:visible;
}}
.quad{{
  position:relative;overflow:hidden;
  display:flex;flex-direction:column;
  justify-content:center;align-items:center;
  padding:28px 32px;cursor:pointer;transition:filter .3s;
}}
.quad:hover{{filter:brightness(1.12)}}
.quad::before{{
  content:'';position:absolute;inset:0;
  background:linear-gradient(to bottom,rgba(0,0,0,.55) 0%,rgba(0,0,0,.18) 40%,rgba(0,0,0,.65) 100%);
  z-index:1;transition:background .3s;
}}
.quad:hover::before{{background:linear-gradient(to bottom,rgba(0,0,0,.4) 0%,rgba(0,0,0,.1) 40%,rgba(0,0,0,.5) 100%)}}

.quad-inner{{
  position:relative;z-index:2;
  display:flex;flex-direction:column;
  align-items:center;justify-content:center;
  gap:14px;height:100%;width:100%;text-align:center;
}}

.quad-icon{{font-size:2.4rem;filter:drop-shadow(0 2px 8px rgba(0,0,0,.7))}}
.quad-title{{font-size:1.75rem;font-weight:800;letter-spacing:.1em;color:#fff;text-transform:uppercase;text-shadow:0 2px 12px rgba(0,0,0,.85)}}
.quad-count {{
  font-size: 2.4rem;
  font-weight: 900;
  color:var(--accent);
  line-height: 1;
  text-shadow: 0 0 20px rgba(0,0,0,0.4);
}}

.btn-more{{
  display:inline-block;padding:6px 24px;
  border:1.5px solid #fff;color:#fff;
  font-family:'Barlow Condensed',sans-serif;
  font-size:.72rem;letter-spacing:.2em;text-transform:uppercase;
  background:transparent;
  cursor:pointer;transition:all .2s;
}}
.btn-more:hover{{background:var(--accent);border-color:var(--accent)}}

.q-bridges{{
  grid-column:1;grid-row:1;
  background:url('https://www.iloilotoday.com/wp-content/uploads/2016/01/muelleloneybridge.jpg') center/cover;
  border-right:2px solid var(--bg);border-bottom:2px solid var(--bg);
}}
.q-flood{{
  grid-column:3;grid-row:1;
  background:url('https://i0.wp.com/www.imtnews.ph/wp-content/uploads/2025/08/IMG_20250812_214906.jpg?resize=1280%2C640&ssl=1') center/cover;
  border-bottom:2px solid var(--bg);
}}
.q-buildings{{
  grid-column:1;grid-row:2;
  background:url('https://upload.wikimedia.org/wikipedia/commons/4/4d/Iloilo_Business_Park%2C_Megaworld_Boulevard%2C_ICC_top_view_%28Mandurriao%2C_Iloilo_City%3B_04-05-2024%29_%28cropped%29~3.jpg') center/cover;
  border-right:2px solid var(--bg);
}}
.q-roads{{
  grid-column:3;grid-row:2;
  background:url('https://upload.wikimedia.org/wikipedia/commons/5/57/Iloilo_Airport_Access_Road.jpg') center/cover;
}}
.center-banner{{
  grid-column:2;grid-row:1/3;
  background:linear-gradient(160deg,#e85c1a,#c94d10);
  display:flex;flex-direction:column;
  align-items:center;justify-content:center;
  padding:44px 24px 36px;text-align:center;
  position:relative;z-index:10;overflow:visible;
}}
.center-banner::after{{
  content:'';position:absolute;bottom:-68px;left:50%;
  transform:translateX(-50%);width:0;height:0;
  border-left:140px solid transparent;
  border-right:140px solid transparent;
  border-top:68px solid #c94d10;z-index:10;
}}
.pulse-ring{{
  position:absolute;top:50%;left:50%;
  transform:translate(-50%,-50%);
  width:180px;height:180px;
  border:1px solid rgba(255,255,255,.12);border-radius:50%;
  animation:pulse-ring 3s ease-out infinite;pointer-events:none;
}}
.pulse-ring:nth-child(2){{animation-delay:1s}}
.pulse-ring:nth-child(3){{animation-delay:2s}}
@keyframes pulse-ring{{
  0%{{transform:translate(-50%,-50%) scale(.3);opacity:.6}}
  100%{{transform:translate(-50%,-50%) scale(1.6);opacity:0}}
}}
.banner-label{{font-size:.72rem;letter-spacing:.22em;color:rgba(255,255,255,.8);text-transform:uppercase;font-weight:600;margin-bottom:10px}}
.banner-title{{font-size:2.2rem;font-weight:900;letter-spacing:.06em;color:#fff;text-transform:uppercase;line-height:1.05;margin-bottom:16px}}
.banner-desc{{font-size:.8rem;color:rgba(255,255,255,.88);line-height:1.7;margin-bottom:22px;font-family:'Barlow',sans-serif}}
.btn-all{{
  display:inline-block;padding:10px 36px;
  background:var(--bg);color:#fff;
  font-size:.8rem;letter-spacing:.2em;text-transform:uppercase;
  border:none;cursor:pointer;transition:background .2s;
}}
.btn-all:hover{{background:#0f0e2a}}

/* ── Stats Bar ── */
.stats{{
  background:var(--bg2);border-top:2px solid var(--accent2);
  display:flex;position:relative;z-index:1;padding-top:58px;
}}
.stat{{flex:1;padding:10px 20px 32px;text-align:center;display:flex;flex-direction:column;align-items:center}}
.stat-num{{font-size:3.2rem;font-weight:900;color:#fff;line-height:1}}
.stat-label{{font-size:.68rem;font-weight:400;letter-spacing:.25em;color:var(--text-sec);text-transform:uppercase;margin-top:10px;font-family:'Barlow',sans-serif}}
.stat-line{{width:32px;height:2px;background:var(--accent);margin-top:10px}}
.scroll-hint{{text-align:center;padding:24px 0 32px;font-size:.72rem;letter-spacing:.18em;text-transform:uppercase;color:var(--text-sec);cursor:pointer}}
.scroll-arrow{{display:inline-block;width:20px;height:20px;border-right:2px solid var(--accent);border-bottom:2px solid var(--accent);transform:rotate(45deg);margin:6px auto 0;animation:bounce 2s ease-in-out infinite}}
@keyframes bounce{{0%,100%{{transform:rotate(45deg) translateY(0)}}50%{{transform:rotate(45deg) translateY(5px)}}}}

.sec-divider{{height:2px;background:linear-gradient(90deg,transparent,var(--accent),transparent);opacity:.4}}
.chart-card-wide{{background:var(--card);border:1px solid var(--border);border-radius:var(--radius);padding:18px;transition:border-color .25s;margin-bottom:28px}}
.chart-card-wide:hover{{border-color:rgba(208,91,55,.25)}}

/* ── Section ── */
#sec-projects{{min-height:100vh;background:var(--bg);position:relative}}
.projects-content{{padding:60px 48px}}
.sec-header{{display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:16px;margin-bottom:28px}}
.sec-title-group{{display:flex;align-items:center;gap:14px}}
.sec-icon{{width:46px;height:46px;background:var(--accent-dim);border:1px solid var(--accent);border-radius:var(--radius-sm);display:flex;align-items:center;justify-content:center;font-size:20px}}
.sec-title{{font-size:2.4rem;font-weight:900;text-transform:uppercase;letter-spacing:.05em}}
.sec-subtitle{{font-size:.8rem;color:var(--text-sec);font-family:'Barlow',sans-serif;margin-top:2px}}
.controls-bar{{display:flex;align-items:center;gap:8px;flex-wrap:wrap}}
.view-toggle{{display:flex;border:1px solid var(--border);border-radius:var(--radius-sm);overflow:hidden}}
.view-btn{{padding:8px 13px;background:transparent;border:none;color:var(--text-sec);cursor:pointer;font-size:1rem;transition:background .2s,color .2s}}
.view-btn.active{{background:var(--accent);color:#fff}}
.ctrl-select,.ctrl-input{{
  background:var(--card);border:1px solid var(--border);
  border-radius:var(--radius-sm);color:var(--text);
  font-family:'Barlow Condensed',sans-serif;
  font-size:.88rem;padding:8px 12px;
  cursor:pointer;outline:none;transition:border-color .2s;
}}
.ctrl-select{{
  appearance:none;
  background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='8'%3E%3Cpath d='M1 1l5 5 5-5' stroke='%23A9A9B3' stroke-width='1.5' fill='none'/%3E%3C/svg%3E");
  background-repeat:no-repeat;background-position:right 10px center;padding-right:30px;
}}
.ctrl-select option{{background:#0f0e2a}}
.ctrl-select:focus,.ctrl-input:focus{{border-color:var(--accent)}}
.ctrl-input::placeholder{{color:var(--text-sec)}}
.kpi-row{{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin-bottom:24px}}
.kpi-mini{{background:var(--card);border:1px solid var(--border);border-radius:var(--radius-sm);padding:14px 18px;transition:border-color .2s}}
.kpi-mini:hover{{border-color:rgba(208,91,55,.3)}}
.kpi-mini-label{{font-size:.72rem;color:var(--text-sec);letter-spacing:.12em;text-transform:uppercase;margin-bottom:5px}}
.kpi-mini-val{{font-size:1.7rem;font-weight:800;color:var(--accent)}}
.cat-pills{{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:18px}}
.cat-pill{{padding:5px 16px;border-radius:20px;border:1px solid var(--border);font-size:.82rem;font-weight:600;letter-spacing:.05em;cursor:pointer;transition:all .2s;color:var(--text-sec);background:var(--card)}}
.cat-pill:hover,.cat-pill.active{{border-color:var(--accent);color:var(--accent);background:var(--accent-dim)}}
.charts-row{{display:grid;grid-template-columns:1fr 1fr 1.2fr;gap:12px;margin-bottom:28px}}
.chart-card{{background:var(--card);border:1px solid var(--border);border-radius:var(--radius);padding:18px;transition:border-color .25s}}
.chart-card:hover{{border-color:rgba(208,91,55,.25)}}
.chart-title{{font-size:.78rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--text-sec);margin-bottom:14px}}
#list-header{{
  display:none;
  background:rgba(208,91,55,.1);border:1px solid rgba(208,91,55,.25);
  border-radius:var(--radius-sm);padding:10px 18px;
  grid-template-columns:2.5fr 1.1fr 1fr 1fr 110px 1.2fr;
  gap:12px;margin-bottom:6px;
  font-size:.72rem;font-weight:700;letter-spacing:.13em;text-transform:uppercase;color:var(--text-sec);
}}
#list-header.visible{{display:grid}}
.pagination{{display:flex;align-items:center;justify-content:center;gap:6px;margin-top:24px;flex-wrap:wrap}}
.page-btn{{min-width:36px;height:36px;padding:0 10px;background:var(--card);border:1px solid var(--border);border-radius:var(--radius-sm);color:var(--text-sec);font-family:'Barlow Condensed',sans-serif;font-size:.88rem;cursor:pointer;transition:all .2s;display:flex;align-items:center;justify-content:center}}
.page-btn:hover{{border-color:var(--accent);color:var(--accent)}}
.page-btn.active{{background:var(--accent);border-color:var(--accent);color:#fff;font-weight:700}}
.page-btn:disabled{{opacity:.3;cursor:default;pointer-events:none}}
.page-info{{font-size:.78rem;color:var(--text-sec);padding:0 8px}}
#cards-container{{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;transition:all .3s}}
#cards-container.list-mode{{grid-template-columns:1fr;gap:6px}}
.proj-card{{
  background:var(--card);border:1px solid var(--border);
  border-radius:var(--radius);cursor:pointer;
  position:relative;overflow:visible;
  transition:transform .32s cubic-bezier(.4,0,.2,1),border-color .3s,box-shadow .32s cubic-bezier(.4,0,.2,1);
  animation:cardIn .35s ease forwards;z-index:1;backface-visibility:hidden;
}}
.proj-card:hover{{transform:scale(1.04);z-index:100;border-color:rgba(208,91,55,.7);box-shadow:0 16px 48px rgba(0,0,0,.7),0 0 0 1px rgba(208,91,55,.2)}}
@keyframes cardIn{{from{{opacity:0;transform:translateY(10px)}}to{{opacity:1;transform:none}}}}
.card-face{{background:#0e0d22;border-radius:var(--radius);overflow:hidden;padding:0}}
.card-img-wrap{{width:100%;height:120px;overflow:hidden;transition:height .35s cubic-bezier(.4,0,.2,1);position:relative}}
.proj-card:hover .card-img-wrap{{height:200px}}
.card-img-wrap img{{width:100%;height:100%;object-fit:cover;display:block;transition:transform .4s ease}}
.proj-card:hover .card-img-wrap img{{transform:scale(1.05)}}
.card-body{{padding:14px 16px 14px}}
.card-extra{{max-height:0;overflow:hidden;opacity:0;transition:max-height .28s ease .08s,opacity .22s ease .12s;padding:0 16px}}
.proj-card:hover .card-extra{{max-height:120px;opacity:1;padding-bottom:14px}}
.proj-card::after{{
  content:'';position:absolute;bottom:0;left:0;right:0;height:2px;
  background:linear-gradient(90deg,var(--accent),transparent);
  transform:scaleX(0);transform-origin:left;
  transition:transform .3s;border-radius:0 0 var(--radius) var(--radius);z-index:2;
}}
.proj-card:hover::after{{transform:scaleX(1)}}
.card-header{{display:flex;justify-content:space-between;align-items:flex-start;gap:8px;margin-bottom:10px}}
.card-name{{font-size:.92rem;font-weight:700;line-height:1.3;text-transform:uppercase;letter-spacing:.02em;flex:1}}
.status-badge{{font-size:.65rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;padding:3px 9px;border-radius:20px;white-space:nowrap;flex-shrink:0}}
.s-completed{{background:rgba(39,174,96,.18);color:#27ae60;border:1px solid rgba(39,174,96,.3)}}
.s-ongoing{{background:rgba(52,152,219,.18);color:#3498db;border:1px solid rgba(52,152,219,.3)}}
.s-delayed{{background:rgba(231,76,60,.18);color:#e74c3c;border:1px solid rgba(231,76,60,.3)}}
.s-planned{{background:rgba(241,196,15,.18);color:#f1c40f;border:1px solid rgba(241,196,15,.3)}}
.card-meta{{display:grid;grid-template-columns:1fr 1fr;gap:6px;font-size:.78rem;color:var(--text-sec)}}
.meta-item{{display:flex;flex-direction:column;gap:1px}}
.meta-item strong{{font-size:.65rem;text-transform:uppercase;letter-spacing:.09em;color:rgba(169,169,179,.65)}}
.meta-item span{{color:var(--text);font-weight:500;font-size:.82rem}}
.meta-contractor{{display:flex;flex-direction:column;gap:1px;margin-top:6px;font-size:.78rem;color:var(--text-sec)}}
.meta-contractor strong{{font-size:.65rem;text-transform:uppercase;letter-spacing:.09em;color:rgba(169,169,179,.65)}}
.meta-contractor span{{color:var(--text);font-weight:500;font-size:.82rem}}
.progress-wrap{{margin-top:10px}}
.progress-label{{display:flex;justify-content:space-between;font-size:.7rem;color:var(--text-sec);margin-bottom:4px}}
.progress-bar{{height:4px;background:rgba(255,255,255,.07);border-radius:4px;overflow:hidden}}
.progress-fill{{height:100%;background:var(--accent);border-radius:4px;transition:width .6s ease}}
.card-budget{{margin-top:10px;padding-top:8px;border-top:1px solid var(--border);display:flex;justify-content:space-between;font-size:.78rem}}
.budget-item{{display:flex;flex-direction:column;gap:1px}}
.budget-item strong{{color:var(--text-sec);font-size:.65rem;text-transform:uppercase;letter-spacing:.08em}}
.budget-item span{{color:var(--accent);font-weight:700;font-size:.88rem}}
#cards-container.list-mode .proj-card{{padding:11px 18px;display:grid;grid-template-columns:2.5fr 1.1fr 1fr 1fr 110px 1.2fr;align-items:center;gap:12px}}
#cards-container.list-mode .proj-card:hover{{transform:none;box-shadow:none}}
#cards-container.list-mode .card-face{{background:transparent;display:contents}}
#cards-container.list-mode .card-img-wrap,
#cards-container.list-mode .card-meta,
#cards-container.list-mode .meta-contractor,
#cards-container.list-mode .progress-wrap,
#cards-container.list-mode .card-budget,
#cards-container.list-mode .card-extra{{display:none !important}}
#cards-container.list-mode .card-header{{margin:0;flex-direction:column;align-items:flex-start;gap:1px}}
#cards-container.list-mode .card-name{{font-size:.82rem}}
.footer{{background:#050413;border-top:1px solid rgba(208,91,55,.2);padding:44px 52px 36px}}
.footer-heading{{font-size:.72rem;letter-spacing:.25em;color:var(--accent);text-transform:uppercase;margin-bottom:22px;font-weight:600}}
.footer-grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:14px 44px;margin-bottom:36px}}
.footer-item{{display:flex;gap:10px;align-items:flex-start;font-size:.84rem;color:var(--text-sec);line-height:1.65;font-family:'Barlow',sans-serif}}
.footer-bullet{{color:var(--accent);flex-shrink:0;padding-top:3px}}
.footer-item strong{{color:#f0f6fc}}
.footer-bottom{{border-top:1px solid rgba(255,255,255,.05);padding-top:18px;display:flex;justify-content:space-between;align-items:center}}
.footer-copy{{font-size:.72rem;color:#3d444d;letter-spacing:.05em}}
.footer-brand{{font-size:1rem;font-weight:800;color:var(--accent);letter-spacing:.22em;opacity:.4}}

@media (max-width: 768px) {{
  .nav {{ padding: 0 16px; height: 56px; }}
  .nav-links {{ gap: 14px; }}
  .nav-links a {{ font-size: 11px; letter-spacing: 1px; }}
  .nav-logo-text .t2 {{ display: none; }}

  .services {{
    grid-template-columns: 1fr !important;
    grid-template-rows: auto !important;
  }}
  .center-banner {{
    grid-column: 1 !important;
    grid-row: 1 !important;
    padding: 32px 18px !important;
  }}
  .center-banner::after {{ display: none !important; }}
  .q-bridges  {{ grid-column: 1 !important; grid-row: 2 !important; height: 200px; }}
  .q-flood    {{ grid-column: 1 !important; grid-row: 3 !important; height: 200px; }}
  .q-buildings{{ grid-column: 1 !important; grid-row: 4 !important; height: 200px; }}
  .q-roads    {{ grid-column: 1 !important; grid-row: 5 !important; height: 200px; }}

  .stats {{ flex-wrap: wrap; padding-top: 32px !important; }}
  .stat {{ flex: 0 0 50%; padding: 10px 12px 20px; }}
  .stat-num {{ font-size: 2rem; }}

  .projects-content {{ padding: 24px 14px !important; }}
  .kpi-row {{ grid-template-columns: 1fr 1fr !important; }}
  .charts-row {{ grid-template-columns: 1fr !important; }}
  #cards-container {{ grid-template-columns: 1fr !important; }}

  .controls-bar {{
    flex-direction: column;
    align-items: stretch !important;
    width: 100%;
  }}
  .ctrl-select, .ctrl-input {{ width: 100% !important; }}
  .sec-header {{
    flex-direction: column;
    align-items: flex-start !important;
  }}
  .cat-pills {{
    overflow-x: auto;
    flex-wrap: nowrap !important;
    padding-bottom: 6px;
  }}
  .footer {{ padding: 28px 16px !important; }}
  .footer-grid {{ grid-template-columns: 1fr !important; }}
}}

@media (max-width: 480px) {{
  .nav-links a {{ font-size: 10px; letter-spacing: 0.5px; }}
  .sec-title {{ font-size: 1.6rem !important; }}
  .banner-title {{ font-size: 1.6rem !important; }}
  .stat-num {{ font-size: 1.6rem !important; }}
}}

</style>
</head>
<body>

<!-- ══════════ NAVBAR ══════════ -->
<nav class="nav">
  <a class="nav-logo" onclick="navigate('home')">
        %%DPWH_LOGO%%
        <div class="nav-logo-text">
            <span class="t1">DPWH</span>
            <span class="t2">Republic of the Philippines</span>
        </div>
    </a>

  </div>
  <ul class="nav-links">
    <li><a id="nav-home"     onclick="navigate('home')">Home</a></li>
    <li><a id="nav-about"    onclick="navigate('about')">About</a></li>
    <li><a id="nav-projects" class="active" onclick="navigate('projects')">Projects</a></li>
    <li><a id="nav-contacts" onclick="navigate('contacts')">Contacts</a></li>
  </ul>
</nav>

<section id="sec-projects">

  <!-- HERO -->
  <div class="hero-wrap">
    <div class="bg-grid"></div>
    <div class="bg-glow"></div>
    <div class="services-wrap">
      <div class="services">

        <div class="quad q-bridges" onclick="filterAndScroll('Bridges')">
          <div class="quad-inner">
            <div class="quad-icon">🌉</div>
            <div class="quad-count">{CAT_COUNTS['Bridges']}</div>
            <div class="quad-title">Bridges</div>
            <button class="btn-more">More →</button>
          </div>
        </div>

        <div class="center-banner">
          <div class="pulse-ring"></div>
          <div class="pulse-ring"></div>
          <div class="pulse-ring"></div>
          <div class="banner-label">Department of Public Works and Highways</div>
          <div class="banner-title">OUR<br>SERVICES</div>
          <div class="banner-desc">
            This platform is a dedicated public transparency initiative
            providing direct access to comprehensive data on the
            Department of Public Works and Highways (DPWH) infrastructure projects.
            We ensure full public accountability by offering real-time,
            detailed tracking of the total number of active projects, overall financial costs,
            and precise construction timelines from initial planning to final completion.
          </div>
          <button class="btn-all" onclick="document.getElementById('projects-anchor').scrollIntoView({{behavior:'smooth'}})">
            View All Projects
          </button>
        </div>

        <div class="quad q-flood" onclick="filterAndScroll('Flood Control and Drainage')">
          <div class="quad-inner">
            <div class="quad-icon">🌊</div>
            <div class="quad-count">{CAT_COUNTS['Flood Control and Drainage']}</div>
            <div class="quad-title">Flood Control</div>
            <button class="btn-more">More →</button>
          </div>
        </div>

        <div class="quad q-buildings" onclick="filterAndScroll('Buildings and Facilities')">
          <div class="quad-inner">
            <div class="quad-icon">🏛️</div>
            <div class="quad-count">{CAT_COUNTS['Buildings and Facilities']}</div>
            <div class="quad-title">Buildings</div>
            <button class="btn-more">More →</button>
          </div>
        </div>

        <div class="quad q-roads" onclick="filterAndScroll('Roads')">
          <div class="quad-inner">
            <div class="quad-icon">🛣️</div>
            <div class="quad-count">{CAT_COUNTS['Roads']}</div>
            <div class="quad-title">Roads</div>
            <button class="btn-more">More →</button>
          </div>
        </div>

      </div>
    </div>

    <!-- Stats Bar -->
    <div class="stats">
      <div class="stat">
        <div class="stat-num">{TOTAL_PROJECTS}</div>
        <div class="stat-label">Total Projects</div>
        <div class="stat-line"></div>
      </div>
      <div class="stat">
        <div class="stat-num">{TOTAL_DISTRICTS}</div>
        <div class="stat-label">Districts</div>
        <div class="stat-line"></div>
      </div>
      <div class="stat">
        <div class="stat-num">{fmt_budget(TOTAL_ALLOCATED)}</div>
        <div class="stat-label">Budget Allocated</div>
        <div class="stat-line"></div>
      </div>
      <div class="stat">
        <div class="stat-num">{fmt_budget(TOTAL_SPENT)}</div>
        <div class="stat-label">Budget Spent</div>
        <div class="stat-line"></div>
      </div>
    </div>

    <!-- Scroll Hint -->
    <div class="scroll-hint"
         onclick="document.getElementById('projects-anchor').scrollIntoView({{behavior:'smooth'}})">
      <div>Scroll down to explore projects</div>
      <div class="scroll-arrow"></div>
    </div>
  </div>

  <div class="sec-divider"></div>

  <div id="projects-anchor"></div>
  <div class="projects-content">

    <div class="sec-header">
      <div class="sec-title-group">
        <div class="sec-icon">📋</div>
        <div>
          <div class="sec-title">All Projects</div>
          <div class="sec-subtitle" id="results-count">Showing all {TOTAL_PROJECTS} projects</div>
        </div>
      </div>
      <div class="controls-bar">
        <div class="view-toggle">
          <button class="view-btn active" id="grid-btn" onclick="setView('grid')" title="Grid View">⊞</button>
          <button class="view-btn"        id="list-btn" onclick="setView('list')" title="List View">☰</button>
        </div>
        <input class="ctrl-input" type="text" id="search-input"
               placeholder="Search project…" oninput="applyFilters()" style="min-width:200px">
        <select class="ctrl-select" id="sort-select"   onchange="applyFilters()">
          <option value="all">↕ Display All</option>
          <option value="latest">↓ Latest First</option>
          <option value="oldest">↑ Oldest First</option>
          <option value="budget-desc">₱ Budget: High → Low</option>
          <option value="budget-asc">₱ Budget: Low → High</option>
          <option value="status">◉ By Status</option>
        </select>
        <select class="ctrl-select" id="year-filter"   onchange="applyFilters()">
          <option value="">All Years</option>
          {year_options}
        </select>
        <select class="ctrl-select" id="cat-filter"    onchange="applyFilters()">
          <option value="">All Categories</option>
          <option>Bridges</option>
          <option>Roads</option>
          <option>Buildings and Facilities</option>
          <option>Flood Control and Drainage</option>
        </select>
        <select class="ctrl-select" id="dist-filter"   onchange="applyFilters()">
          <option value="">All Districts</option>
          {dist_options}
        </select>
        <select class="ctrl-select" id="status-filter" onchange="applyFilters()">
          <option value="">◉ All Status</option>
          <option>Completed</option>
          <option>Ongoing</option>
          <option>Delayed</option>
          <option>Planned</option>
        </select>
      </div>
    </div>

    <div class="kpi-row">
      <div class="kpi-mini"><div class="kpi-mini-label">Filtered Projects</div><div class="kpi-mini-val" id="kpi-count">0</div></div>
      <div class="kpi-mini"><div class="kpi-mini-label">Completed</div><div class="kpi-mini-val" id="kpi-completed">0</div></div>
      <div class="kpi-mini"><div class="kpi-mini-label">Ongoing</div><div class="kpi-mini-val" id="kpi-ongoing">0</div></div>
      <div class="kpi-mini"><div class="kpi-mini-label">Filtered Budget</div><div class="kpi-mini-val" id="kpi-budget">₱0</div></div>
    </div>

    <div class="cat-pills">
      <div class="cat-pill active" onclick="setCatPill(this,'')">All</div>
      <div class="cat-pill" onclick="setCatPill(this,'Bridges')">🌉 Bridges</div>
      <div class="cat-pill" onclick="setCatPill(this,'Roads')">🛣️ Roads</div>
      <div class="cat-pill" onclick="setCatPill(this,'Buildings and Facilities')">🏛️ Buildings</div>
      <div class="cat-pill" onclick="setCatPill(this,'Flood Control and Drainage')">🌊 Flood Control</div>
    </div>

    <div class="charts-row">
      <div class="chart-card">
        <div class="chart-title">Projects by Category</div>
        <canvas id="chart-cat" height="190"></canvas>
      </div>
      <div class="chart-card">
        <div class="chart-title">Status Breakdown</div>
        <canvas id="chart-status" height="190"></canvas>
      </div>
      <div class="chart-card">
        <div class="chart-title">Yearly Distribution 2016–2026</div>
        <canvas id="chart-year" height="190"></canvas>
      </div>
    </div>

    <!-- ── CONTRACTOR CHART ── -->
    <div class="chart-card-wide">
      <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:10px;margin-bottom:12px">
        <div class="chart-title" style="margin:0">Top Contractors by Number of Projects</div>
        <div style="display:flex;align-items:center;gap:8px;flex-wrap:wrap">
          <span style="font-size:.72rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--text-sec)">Show top</span>
          <select class="ctrl-select" id="contractor-top-n" onchange="updateContractorChart()" style="padding:6px 28px 6px 10px">
            <option value="10">10</option>
            <option value="15" selected>15</option>
            <option value="20">20</option>
            <option value="30">30</option>
            <option value="999">All</option>
          </select>
        </div>
      </div>
      <div id="contractor-chart-wrap" style="position:relative;width:100%;height:600px">
        <canvas id="chart-contractor" role="img" aria-label="Horizontal bar chart showing top contractors by number of projects implemented"></canvas>
      </div>
    </div>

    <div id="list-header">
      <span>Project Name</span>
      <span>Category</span>
      <span>District</span>
      <span>Date</span>
      <span>Status</span>
      <span>Implementing Office</span>
    </div>

    <div id="cards-container"></div>
    <div class="pagination" id="pagination"></div>

  </div>
</section>

<!-- ── FOOTER ── -->
<div class="footer">
  <div class="footer-heading">Project Overview &amp; Notes</div>
  <div class="footer-grid">
    <div class="footer-item"><span class="footer-bullet">▶</span><span><strong>Total Projects:</strong> {TOTAL_PROJECTS} infrastructure projects across all districts.</span></div>
    <div class="footer-item"><span class="footer-bullet">▶</span><span><strong>Districts:</strong> Covers {TOTAL_DISTRICTS} engineering districts of Iloilo City and surrounding municipalities.</span></div>
    <div class="footer-item"><span class="footer-bullet">▶</span><span><strong>Budget Allocated:</strong> {fmt_budget(TOTAL_ALLOCATED)} committed for infrastructure development.</span></div>
    <div class="footer-item"><span class="footer-bullet">▶</span><span><strong>Budget Spent:</strong> {fmt_budget(TOTAL_SPENT)} disbursed with full accountability.</span></div>
    <div class="footer-item"><span class="footer-bullet">▶</span><span><strong>Services:</strong> Bridges, flood-control systems, buildings &amp; facilities, and road networks.</span></div>
    <div class="footer-item"><span class="footer-bullet">▶</span><span><strong>Period:</strong> Projects monitored from 2016 through 2026 — full decade of infrastructure delivery.</span></div>
  </div>
  <div class="footer-bottom">
    <span class="footer-copy">© 2025 DPWH · Iloilo City District — All Rights Reserved</span>
    <span class="footer-brand">DPWH</span>
  </div>
</div>

<script>
// ─── Data ────────────────────────────────────────────────────────────────
const PROJECTS = {PROJECTS_JSON};

const CATS     = ["Bridges","Roads","Buildings and Facilities","Flood Control and Drainage"];
const STATUSES = ["Completed","Ongoing","Delayed","Planned"];
const PAGE_SIZE = 21;

const CAT_FALLBACK = {{
  "Bridges":                    "https://www.iloilotoday.com/wp-content/uploads/2016/01/muelleloneybridge.jpg",
  "Roads":                      "https://upload.wikimedia.org/wikipedia/commons/5/57/Iloilo_Airport_Access_Road.jpg",
  "Buildings and Facilities":   "https://upload.wikimedia.org/wikipedia/commons/4/4d/Iloilo_Business_Park%2C_Megaworld_Boulevard%2C_ICC_top_view_%28Mandurriao%2C_Iloilo_City%3B_04-05-2024%29_%28cropped%29~3.jpg",
  "Flood Control and Drainage": "https://i0.wp.com/www.imtnews.ph/wp-content/uploads/2025/08/IMG_20250812_214906.jpg?resize=1280%2C640&ssl=1",
}};

function getPhoto(p) {{
  const devPath = p.image_path ? p.image_path.trim() : "";
  if (devPath) return devPath;
  return CAT_FALLBACK[p.category] || CAT_FALLBACK["Bridges"];
}}

// ── Contractor name normaliser ────────────────────────────────────────────
// Strips ID numbers e.g. "(12345)", strips "(FORMERLY: ...)" clauses,
// uppercases everything, then applies canonical aliases.
function normalizeContractor(raw) {{
  if (!raw) return "UNKNOWN";
  let s = raw.trim().toUpperCase();
  s = s.replace(/\s*\(FORMERLY:[^)]*\)/gi, "");
  s = s.replace(/\s*\([^)]*\)/g, "");
  s = s.replace(/\s+/g, " ").trim();
  const ALIASES = {{
    "ADP CONSTRUCTION & SUPPLY":             "A.D. PENDON CONSTRUCTION & SUPPLY, INC.",
    "A.D. PENDON CONSTRUCTION & SUPPLY, INC.": "A.D. PENDON CONSTRUCTION & SUPPLY, INC.",
    "PESOM BUILDERS AND CONSTRUCTION SUPPLY": "PESOM CONSTRUCTION SERVICES",
    "PESOM CONSTRUCTION SERVICES":           "PESOM CONSTRUCTION SERVICES",
    "5'S CONSTRUCTION & SUPPLY":             "5'S CONSTRUCTION & SUPPLY",
    "S.T. SALCEDO CONSTRUCTION CORP.":       "S.T. SALCEDO CONSTRUCTION CORP.",
    "F. GURREA CONSTRUCTION, INCORPORATED":  "F. GURREA CONSTRUCTION, INCORPORATED",
    "WOODLAND CONSTRUCTION & SUPPLY, INC.":  "WOODLAND CONSTRUCTION & SUPPLY, INC.",
    "IBC INTERNATIONAL BUILDERS CORPORATION":"IBC INTERNATIONAL BUILDERS CORPORATION",
    "GALENO CONSTRUCTION, INC.":             "GALENO CONSTRUCTION, INC.",
    "GALENO CONSTRUCTION":                   "GALENO CONSTRUCTION, INC.",
    "VANNIE CONSTRUCTION AND SUPPLY":        "VANNIE CONSTRUCTION AND SUPPLY",
    "JHALL MARKETING & SERVICES":            "JHALL MARKETING & SERVICES",
  }};
  return ALIASES[s] || s;
}}

function buildContractorMap(projects) {{
  const map = {{}};
  projects.forEach(p => {{
    const parts = (p.contractor || "").split(/\s*\/\s*/);
    parts.forEach(part => {{
      const key = normalizeContractor(part);
      if (!key || key === "UNKNOWN") return;
      map[key] = (map[key] || 0) + 1;
    }});
  }});
  return map;
}}

// ─── State ───────────────────────────────────────────────────────────────
let filtered = [...PROJECTS];
let view     = 'grid';
let page     = 1;

// ─── Formatters ──────────────────────────────────────────────────────────
function fmtBudget(v) {{
  if (v >= 1e9) return '₱' + (v/1e9).toFixed(1) + 'B';
  if (v >= 1e6) return '₱' + Math.round(v/1e6) + 'M';
  return '₱' + v.toLocaleString();
}}
function fmtDate(d) {{
  if (!d || d === '-' || d === '') return 'N/A';
  const parts = d.split('-');
  if (parts.length < 3) return d;
  const mn = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
  const month = mn[+parts[1]-1];
  if (!month) return d;
  return month + ' ' + +parts[2] + ', ' + parts[0];
}}
function statusClass(s) {{
  if (!s) return 's-planned';
  return 's-' + s.toLowerCase().replace(/\s+/g,'-');
}}
function escHtml(str) {{
  if (!str) return '';
  return str
    .replace(/&/g,'&amp;')
    .replace(/</g,'&lt;')
    .replace(/>/g,'&gt;')
    .replace(/"/g,'&quot;')
    .replace(/'/g,'&#039;');
}}

// ─── Navigation ──────────────────────────────────────────────────────────
function navigate(page) {{
    try {{
        window.top.location.href = "/?navigate=" + page;
    }} catch(e) {{
        window.location.href = "/?navigate=" + page;
    }}
}}

// ─── Filtering ───────────────────────────────────────────────────────────
function applyFilters() {{
  const year   = document.getElementById('year-filter').value;
  const cat    = document.getElementById('cat-filter').value;
  const dist   = document.getElementById('dist-filter').value;
  const status = document.getElementById('status-filter').value;
  const sort   = document.getElementById('sort-select').value;
  const search = document.getElementById('search-input').value.trim().toLowerCase();

  let r = PROJECTS.filter(p => {{
    if (year   && +p.year     !== +year)  return false;
    if (cat    && p.category  !== cat)    return false;
    if (dist   && p.district  !== dist)   return false;
    if (status && p.status    !== status) return false;
    if (search && !(p.project_name||'').toLowerCase().includes(search)) return false;
    return true;
  }});

  if      (sort === 'latest')      r.sort((a,b) => (b.date||'').localeCompare(a.date||''));
  else if (sort === 'oldest')      r.sort((a,b) => (a.date||'').localeCompare(b.date||''));
  else if (sort === 'budget-desc') r.sort((a,b) => b.budget_allocated - a.budget_allocated);
  else if (sort === 'budget-asc')  r.sort((a,b) => a.budget_allocated - b.budget_allocated);
  else if (sort === 'status')      r.sort((a,b) => (a.status||'').localeCompare(b.status||''));

  filtered = r;
  page     = 1;
  renderAll();
}}

// ─── KPIs ─────────────────────────────────────────────────────────────────
function updateKPIs() {{
  document.getElementById('kpi-count').textContent     = filtered.length;
  document.getElementById('kpi-completed').textContent = filtered.filter(p=>p.status==='Completed').length;
  document.getElementById('kpi-ongoing').textContent   = filtered.filter(p=>p.status==='Ongoing').length;
  const tot = filtered.reduce((s,p) => s + (p.budget_allocated||0), 0);
  document.getElementById('kpi-budget').textContent    = fmtBudget(tot);
  document.getElementById('results-count').textContent =
    'Showing ' + filtered.length + ' of ' + PROJECTS.length + ' projects';
}}

// ─── Charts ──────────────────────────────────────────────────────────────
let charts = {{}};

function initCharts() {{
  const base = {{
    plugins: {{ legend: {{ display: false }} }},
    scales: {{
      x: {{ ticks:{{color:'#A9A9B3',font:{{family:'Barlow Condensed',size:11}}}}, grid:{{color:'rgba(255,255,255,.04)'}} }},
      y: {{ ticks:{{color:'#A9A9B3',font:{{family:'Barlow Condensed',size:11}}}}, grid:{{color:'rgba(255,255,255,.06)'}} }},
    }},
    responsive: true, maintainAspectRatio: true,
  }};

  charts.cat = new Chart(document.getElementById('chart-cat'), {{
    type: 'bar',
    data: {{
      labels: CATS.map(c => c.split(' ')[0]),
      datasets: [{{ data:[], backgroundColor:['#D05B37','#e07a5f','#f2cc8f','#81b29a'], borderRadius:6, borderSkipped:false }}],
    }},
    options: {{ ...base }},
  }});

  charts.status = new Chart(document.getElementById('chart-status'), {{
    type: 'doughnut',
    data: {{
      labels: STATUSES,
      datasets: [{{ data:[], backgroundColor:['#27ae60','#3498db','#e74c3c','#f1c40f'], borderWidth:0 }}],
    }},
    options: {{
      responsive:true, maintainAspectRatio:true, cutout:'68%',
      plugins: {{ legend:{{ position:'bottom', labels:{{color:'#A9A9B3',font:{{family:'Barlow Condensed',size:11}},padding:8}} }} }},
    }},
  }});

  const years = Array.from({{length:11}}, (_,i) => 2016+i);
  const ctx   = document.getElementById('chart-year').getContext('2d');
  const grad  = ctx.createLinearGradient(0,0,0,180);
  grad.addColorStop(0,'rgba(208,91,55,.38)');
  grad.addColorStop(1,'rgba(208,91,55,0)');
  charts.year = new Chart(ctx, {{
    type: 'line',
    data: {{
      labels: years,
      datasets: [{{ data:[], borderColor:'#D05B37', backgroundColor:grad, tension:.4, fill:true, pointRadius:4, pointBackgroundColor:'#D05B37' }}],
    }},
    options: {{ ...base, plugins:{{ legend:{{ display:false }} }} }},
  }});

  // ── Contractor chart init ─────────────────────────────────────────────
  charts.contractor = new Chart(document.getElementById('chart-contractor'), {{
    type: 'bar',
    data: {{ labels: [], datasets: [{{ data: [], backgroundColor: [], borderRadius: 4, borderSkipped: false }}] }},
    options: {{
      indexAxis: 'y',
      responsive: true,
      maintainAspectRatio: false,
      plugins: {{
        legend: {{ display: false }},
        tooltip: {{
          callbacks: {{
            label: ctx => ' ' + ctx.parsed.x + ' project' + (ctx.parsed.x !== 1 ? 's' : ''),
          }},
        }},
      }},
      scales: {{
        x: {{
          ticks: {{ color:'#A9A9B3', font:{{family:'Barlow Condensed',size:11}}, stepSize:1 }},
          grid:  {{ color:'rgba(255,255,255,.06)' }},
          title: {{ display:true, text:'Number of Projects', color:'#A9A9B3', font:{{family:'Barlow Condensed',size:11}} }},
        }},
        y: {{
          ticks: {{
            color:'#A9A9B3',
            font: {{ family:'Barlow Condensed', size:11 }},
            callback: function(val) {{
              const label = this.getLabelForValue(val);
              return label.length > 45 ? label.slice(0, 43) + '...' : label;
            }},
          }},
          grid: {{ color:'rgba(255,255,255,.04)' }},
        }},
      }},
      layout: {{ padding: {{ right: 20 }} }},
    }},
  }});
}}

// ── Contractor chart update ───────────────────────────────────────────────
function updateContractorChart() {{
  const topN   = parseInt(document.getElementById('contractor-top-n').value, 10);
  const map    = buildContractorMap(filtered);
  const sorted = Object.entries(map).sort((a,b) => b[1]-a[1]).slice(0, topN);
  const labels = sorted.map(([name]) => name);
  const values = sorted.map(([,count]) => count);
  const n      = labels.length || 1;
  const colors = values.map((_,i) => {{
    const t = i / (n - 1 || 1);
    const r = Math.round(208 - t * 118);
    const g = Math.round(91  - t * 54);
    const b = Math.round(55  - t * 39);
    return 'rgb(' + r + ',' + g + ',' + b + ')';
  }});
  const barHeight  = 38;
  const chartHeight = Math.max(200, labels.length * barHeight + 60);
  document.getElementById('contractor-chart-wrap').style.height = chartHeight + 'px';
  charts.contractor.data.labels                      = labels;
  charts.contractor.data.datasets[0].data            = values;
  charts.contractor.data.datasets[0].backgroundColor = colors;
  charts.contractor.update();
}}

function updateCharts() {{
  charts.cat.data.datasets[0].data    = CATS.map(c => filtered.filter(p=>p.category===c).length);
  charts.cat.update();
  charts.status.data.datasets[0].data = STATUSES.map(s => filtered.filter(p=>p.status===s).length);
  charts.status.update();
  const years = Array.from({{length:11}}, (_,i) => 2016+i);
  charts.year.data.datasets[0].data   = years.map(y => filtered.filter(p=>p.year===y).length);
  charts.year.update();
  updateContractorChart();
}}

// ─── Pagination ───────────────────────────────────────────────────────────
function totalPages() {{ return Math.max(1, Math.ceil(filtered.length / PAGE_SIZE)); }}

function renderPagination() {{
  const pg = document.getElementById('pagination');
  const tp = totalPages();
  pg.innerHTML = '';
  if (tp <= 1) return;

  const prevBtn = document.createElement('button');
  prevBtn.className = 'page-btn';
  prevBtn.textContent = '←';
  if (page === 1) prevBtn.disabled = true;
  prevBtn.onclick = () => {{ page--; renderCards(); renderPagination(); window.scrollTo
                        ({{top: document.getElementById('projects-anchor').offsetTop - 80, behavior: 'smooth'}}); }};
  pg.appendChild(prevBtn);

  let start = Math.max(1, page - 4);
  let end   = Math.min(tp, start + 9);
  if (end - start < 9) start = Math.max(1, end - 9);

  for (let i = start; i <= end; i++) {{
    const btn = document.createElement('button');
    btn.className = 'page-btn' + (i === page ? ' active' : '');
    btn.textContent = i;
    const pi = i;
    btn.onclick = () => {{ page = pi; renderCards(); renderPagination(); 
                        document.getElementById('projects-anchor').scrollIntoView({{behavior: 'smooth'}}); }};
    pg.appendChild(btn);
  }}

  const info = document.createElement('span');
  info.className = 'page-info';
  info.textContent = page + ' / ' + tp;
  pg.appendChild(info);

  const nextBtn = document.createElement('button');
  nextBtn.className = 'page-btn';
  nextBtn.textContent = '→';
  if (page === tp) nextBtn.disabled = true;
  nextBtn.onclick = () => {{ page++; renderCards(); renderPagination(); 
                         document.getElementById('projects-anchor').scrollIntoView({{behavior: 'smooth'}}); }};
  pg.appendChild(nextBtn);
}}

// ─── Cards ────────────────────────────────────────────────────────────────
function renderCards() {{
  const con = document.getElementById('cards-container');
  const lh  = document.getElementById('list-header');

  con.classList.toggle('list-mode', view === 'list');
  lh.classList.toggle('visible',   view === 'list');
  con.innerHTML = '';

  if (!filtered.length) {{
    con.innerHTML = '<div style="grid-column:1/-1;text-align:center;padding:60px;color:var(--text-sec)"><div style="font-size:3rem;margin-bottom:14px">🔍</div><div style="font-size:1.1rem;font-weight:600">No projects match your filters</div></div>';
    return;
  }}

  const start = (page - 1) * PAGE_SIZE;
  const slice = filtered.slice(start, start + PAGE_SIZE);

  slice.forEach((p, i) => {{
    const d  = document.createElement('div');
    d.className = 'proj-card';
    d.style.animationDelay = Math.min(i, PAGE_SIZE - 1) * 0.03 + 's';
    const sc    = statusClass(p.status);
    const photo = getPhoto(p);
    const rem   = Math.max(0, (p.budget_allocated||0) - (p.budget_spent||0));
    const name  = escHtml(p.project_name || '');
    const cat   = escHtml(p.category || '');
    const dist  = escHtml(p.district || '');
    const office= escHtml(p.implementing_office || '');
    const contr = escHtml(p.contractor || '—');
    const pct   = p.completion_percentage || 0;
    const alloc = p.budget_allocated || 0;
    const spent = p.budget_spent || 0;
    const dateStr = fmtDate(p.date || '');

    if (view === 'grid') {{
      d.innerHTML = '<div class="card-face">' +
        '<div class="card-img-wrap"><img src="' + photo + '" alt="' + cat + '" loading="lazy"></div>' +
        '<div class="card-body">' +
          '<div class="card-header">' +
            '<div class="card-name">' + name + '</div>' +
            '<span class="status-badge ' + sc + '">' + escHtml(p.status||'') + '</span>' +
          '</div>' +
          '<div class="card-meta">' +
            '<div class="meta-item"><strong>ID</strong><span>#' + (p.id||'') + '</span></div>' +
            '<div class="meta-item"><strong>Category</strong><span>' + cat + '</span></div>' +
            '<div class="meta-item"><strong>Date</strong><span>' + dateStr + '</span></div>' +
            '<div class="meta-item"><strong>District</strong><span>' + dist + '</span></div>' +
            '<div class="meta-item" style="grid-column:1/-1"><strong>Office</strong><span>' + office + '</span></div>' +
          '</div>' +
          '<div class="meta-contractor"><strong>Contractor</strong><span>' + contr + '</span></div>' +
          '<div class="progress-wrap">' +
            '<div class="progress-label"><span>Completion</span><span>' + pct + '%</span></div>' +
            '<div class="progress-bar"><div class="progress-fill" style="width:' + pct + '%"></div></div>' +
          '</div>' +
          '<div class="card-budget">' +
            '<div class="budget-item"><strong>Allocated</strong><span>' + fmtBudget(alloc) + '</span></div>' +
            '<div class="budget-item" style="text-align:right"><strong>Spent</strong><span>' + fmtBudget(spent) + '</span></div>' +
          '</div>' +
        '</div>' +
        '<div class="card-extra">' +
          '<div style="display:flex;justify-content:space-between;padding:8px 0 10px;border-top:1px solid rgba(208,91,55,.2);gap:10px">' +
            '<div class="budget-item"><strong>Allocated</strong><span>' + fmtBudget(alloc) + '</span></div>' +
            '<div class="budget-item" style="text-align:center"><strong>Spent</strong><span>' + fmtBudget(spent) + '</span></div>' +
            '<div class="budget-item" style="text-align:right"><strong>Remaining</strong><span style="color:#27ae60">' + fmtBudget(rem) + '</span></div>' +
          '</div>' +
        '</div>' +
      '</div>';
    }} else {{
      d.innerHTML =
        '<div class="card-header" style="flex-direction:column;align-items:flex-start;gap:1px;margin:0">' +
          '<div class="card-name">' + name + '</div>' +
        '</div>' +
        '<div style="font-size:.8rem;color:var(--text-sec)">' + cat + '</div>' +
        '<div style="font-size:.8rem;color:var(--text-sec)">' + dist + '</div>' +
        '<div style="font-size:.8rem;color:var(--text-sec)">' + dateStr + '</div>' +
        '<span class="status-badge ' + sc + '">' + escHtml(p.status||'') + '</span>' +
        '<div style="font-size:.75rem;color:var(--text-sec)">' + office + '<br><span style="color:rgba(208,91,55,.8)">👷</span> ' + contr + '</div>';
    }}
    con.appendChild(d);
  }});
}}

// ─── Render all ───────────────────────────────────────────────────────────
function renderAll() {{
  updateKPIs();
  updateCharts();
  renderCards();
  renderPagination();
}}

function setView(v) {{
  view = v;
  document.getElementById('grid-btn').classList.toggle('active', v==='grid');
  document.getElementById('list-btn').classList.toggle('active', v==='list');
  renderCards();
}}

function setCatPill(el, cat) {{
  document.querySelectorAll('.cat-pill').forEach(p => p.classList.remove('active'));
  el.classList.add('active');
  document.getElementById('cat-filter').value = cat;
  applyFilters();
}}

function filterAndScroll(cat) {{
  document.getElementById('cat-filter').value = cat;
  document.querySelectorAll('.cat-pill').forEach(p => {{
    const matches = cat
      ? p.textContent.includes(cat.split(' ')[0])
      : p.textContent.trim() === 'All';
    p.classList.toggle('active', matches);
  }});
  applyFilters();
  setTimeout(() => document.getElementById('projects-anchor').scrollIntoView({{behavior:'smooth'}}), 80);
}}

// ─── Nav scroll highlight ─────────────────────────────────────────────────
window.addEventListener('scroll', () => {{
  document.getElementById('nav-home').classList.remove('active');
  document.getElementById('nav-projects').classList.add('active');
}});

// ─── Boot ─────────────────────────────────────────────────────────────────
document.addEventListener('DOMContentLoaded', () => {{
  initCharts();
  renderAll();
}});
</script>
</body>
</html>"""


HTML = HTML.replace("%%DPWH_LOGO%%",  LOGO_TAG)

components.html(HTML, height=0, scrolling=True)