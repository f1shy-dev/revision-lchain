import json
import requests
import os
data = """
{
    "Topic 1: Particles": {
        "1.1 The Particle Model (H) QP": "https://pmt.physicsandmathstutor.com/download/Chemistry/GCSE/Topic-Qs/OCR-A/1-Particles/Set-B/Higher/1.1%20The%20Particle%20Model%20(H)%20QP.pdf",
        "1.2 Atomic Structure (H) QP": "https://pmt.physicsandmathstutor.com/download/Chemistry/GCSE/Topic-Qs/OCR-A/1-Particles/Set-B/Higher/1.2%20Atomic%20Structure%20(H)%20QP.pdf",
        "Atomic Structure QP": "https://pmt.physicsandmathstutor.com/download/Chemistry/GCSE/Topic-Qs/OCR-A/1-Particles/Set-A/Atomic%20Structure%20QP.pdf",
        "The Particle Model QP": "https://pmt.physicsandmathstutor.com/download/Chemistry/GCSE/Topic-Qs/OCR-A/1-Particles/Set-A/The%20Particle%20Model%20QP.pdf"
    },
    "Topic 2: Elements, Compounds and Mixtures": {
        "2.1 Purity and Separating Mixtures (H) QP": "https://pmt.physicsandmathstutor.com/download/Chemistry/GCSE/Topic-Qs/OCR-A/2-Elements-Compounds-and-Mixtures/Set-B/Higher/2.1%20Purity%20and%20Separating%20Mixtures%20(H)%20QP.pdf",
        "2.2 Bonding (H) QP": "https://pmt.physicsandmathstutor.com/download/Chemistry/GCSE/Topic-Qs/OCR-A/2-Elements-Compounds-and-Mixtures/Set-B/Higher/2.2%20Bonding%20(H)%20QP.pdf",
        "2.3 Properties of Materials (H) QP": "https://pmt.physicsandmathstutor.com/download/Chemistry/GCSE/Topic-Qs/OCR-A/2-Elements-Compounds-and-Mixtures/Set-B/Higher/2.3%20Properties%20of%20Materials%20(H)%20QP.pdf",
        "Bonding QP": "https://pmt.physicsandmathstutor.com/download/Chemistry/GCSE/Topic-Qs/OCR-A/2-Elements-Compounds-and-Mixtures/Set-A/Bonding%20QP.pdf",
        "Properties of Materials QP": "https://pmt.physicsandmathstutor.com/download/Chemistry/GCSE/Topic-Qs/OCR-A/2-Elements-Compounds-and-Mixtures/Set-A/Properties%20of%20Materials%20QP.pdf",
        "Purity and Separating Mixtures QP": "https://pmt.physicsandmathstutor.com/download/Chemistry/GCSE/Topic-Qs/OCR-A/2-Elements-Compounds-and-Mixtures/Set-A/Purity%20and%20Separating%20Mixtures%20QP.pdf"
    },
    "Topic 3: Chemical Reactions": {
        "3.1 Introducing Chemical Reactions (H) QP": "https://pmt.physicsandmathstutor.com/download/Chemistry/GCSE/Topic-Qs/OCR-A/3-Chemical-Reactions/Set-B/Higher/3.1%20Introducing%20Chemical%20Reactions%20(H)%20QP.pdf",
        "3.2 Energetics (H) QP": "https://pmt.physicsandmathstutor.com/download/Chemistry/GCSE/Topic-Qs/OCR-A/3-Chemical-Reactions/Set-B/Higher/3.2%20Energetics%20(H)%20QP.pdf",
        "3.3 Types of Reactions (H) QP": "https://pmt.physicsandmathstutor.com/download/Chemistry/GCSE/Topic-Qs/OCR-A/3-Chemical-Reactions/Set-B/Higher/3.3%20Types%20of%20Reactions%20(H)%20QP.pdf",
        "3.4 Electrolysis (H) QP": "https://pmt.physicsandmathstutor.com/download/Chemistry/GCSE/Topic-Qs/OCR-A/3-Chemical-Reactions/Set-B/Higher/3.4%20Electrolysis%20(H)%20QP.pdf",
        "Electrolysis QP": "https://pmt.physicsandmathstutor.com/download/Chemistry/GCSE/Topic-Qs/OCR-A/3-Chemical-Reactions/Set-A/Electrolysis%20QP.pdf",
        "Energetics QP": "https://pmt.physicsandmathstutor.com/download/Chemistry/GCSE/Topic-Qs/OCR-A/3-Chemical-Reactions/Set-A/Energetics%20QP.pdf",
        "Introducing Chemical Reactions QP": "https://pmt.physicsandmathstutor.com/download/Chemistry/GCSE/Topic-Qs/OCR-A/3-Chemical-Reactions/Set-A/Introducing%20Chemical%20Reactions%20QP.pdf",
        "Types of Chemical Reactions 1 QP": "https://pmt.physicsandmathstutor.com/download/Chemistry/GCSE/Topic-Qs/OCR-A/3-Chemical-Reactions/Set-A/Types%20of%20Chemical%20Reactions%201%20QP.pdf",
        "Types of Chemical Reactions 2 QP": "https://pmt.physicsandmathstutor.com/download/Chemistry/GCSE/Topic-Qs/OCR-A/3-Chemical-Reactions/Set-A/Types%20of%20Chemical%20Reactions%202%20QP.pdf"
    },
    "Topic 4: Predicting and Identifying Reactions and Products": {
        "4.1 Predicting Chemical Reactions (H) QP": "https://pmt.physicsandmathstutor.com/download/Chemistry/GCSE/Topic-Qs/OCR-A/4-Predicting-and-Identifying-Reactions-and-Products/Set-B/Higher/4.1%20Predicting%20Chemical%20Reactions%20(H)%20QP.pdf",
        "4.2 Identifying the Products of Chemical Reactions (H) QP": "https://pmt.physicsandmathstutor.com/download/Chemistry/GCSE/Topic-Qs/OCR-A/4-Predicting-and-Identifying-Reactions-and-Products/Set-B/Higher/4.2%20Identifying%20the%20Products%20of%20Chemical%20Reactions%20(H)%20QP.pdf",
        "Identifying the Products of Chemical Reactions QP": "https://pmt.physicsandmathstutor.com/download/Chemistry/GCSE/Topic-Qs/OCR-A/4-Predicting-and-Identifying-Reactions-and-Products/Set-A/Identifying%20the%20Products%20of%20Chemical%20Reactions%20QP.pdf",
        "Predicting Chemical Reactions QP": "https://pmt.physicsandmathstutor.com/download/Chemistry/GCSE/Topic-Qs/OCR-A/4-Predicting-and-Identifying-Reactions-and-Products/Set-A/Predicting%20Chemical%20Reactions%20QP.pdf"
    },
    "Topic 5: Monitoring and Controlling Chemical Reactions": {
        "5.1 Monitoring Chemical Reactions (H) QP": "https://pmt.physicsandmathstutor.com/download/Chemistry/GCSE/Topic-Qs/OCR-A/5-Monitoring-and-Controlling-Chemical-Reactions/Set-B/Higher/5.1%20Monitoring%20Chemical%20Reactions%20(H)%20QP.pdf",
        "5.2 Controlling Reactions (H) QP": "https://pmt.physicsandmathstutor.com/download/Chemistry/GCSE/Topic-Qs/OCR-A/5-Monitoring-and-Controlling-Chemical-Reactions/Set-B/Higher/5.2%20Controlling%20Reactions%20(H)%20QP.pdf",
        "5.3 Equilibria (H) QP": "https://pmt.physicsandmathstutor.com/download/Chemistry/GCSE/Topic-Qs/OCR-A/5-Monitoring-and-Controlling-Chemical-Reactions/Set-B/Higher/5.3%20Equilibria%20(H)%20QP.pdf",
        "Controlling Reactions QP": "https://pmt.physicsandmathstutor.com/download/Chemistry/GCSE/Topic-Qs/OCR-A/5-Monitoring-and-Controlling-Chemical-Reactions/Set-A/Controlling%20Reactions%20QP.pdf",
        "Equilibria QP": "https://pmt.physicsandmathstutor.com/download/Chemistry/GCSE/Topic-Qs/OCR-A/5-Monitoring-and-Controlling-Chemical-Reactions/Set-A/Equilibria%20QP.pdf",
        "Monitoring Chemical Reactions 1 QP": "https://pmt.physicsandmathstutor.com/download/Chemistry/GCSE/Topic-Qs/OCR-A/5-Monitoring-and-Controlling-Chemical-Reactions/Set-A/Monitoring%20Chemical%20Reactions%201%20QP.pdf",
        "Monitoring Chemical Reactions 2 QP": "https://pmt.physicsandmathstutor.com/download/Chemistry/GCSE/Topic-Qs/OCR-A/5-Monitoring-and-Controlling-Chemical-Reactions/Set-A/Monitoring%20Chemical%20Reactions%202%20QP.pdf"
    },
    "Topic 6: Global Challenges": {
        "6.1 Improving Processes and Products (H) QP": "https://pmt.physicsandmathstutor.com/download/Chemistry/GCSE/Topic-Qs/OCR-A/6-Global-Challenges/Set-B/Higher/6.1%20Improving%20Processes%20and%20Products%20(H)%20QP.pdf",
        "6.2 Organic Chemistry (H) QP": "https://pmt.physicsandmathstutor.com/download/Chemistry/GCSE/Topic-Qs/OCR-A/6-Global-Challenges/Set-B/Higher/6.2%20Organic%20Chemistry%20(H)%20QP.pdf",
        "6.3 Interpreting and Interacting with Earth Systems (H) QP": "https://pmt.physicsandmathstutor.com/download/Chemistry/GCSE/Topic-Qs/OCR-A/6-Global-Challenges/Set-B/Higher/6.3%20Interpreting%20and%20Interacting%20with%20Earth%20Systems%20(H)%20QP.pdf",
        "Improving Processes & Products 1 QP": "https://pmt.physicsandmathstutor.com/download/Chemistry/GCSE/Topic-Qs/OCR-A/6-Global-Challenges/Set-A/Improving%20Processes%20&%20Products%201%20QP.pdf",
        "Improving Processes & Products 2 QP": "https://pmt.physicsandmathstutor.com/download/Chemistry/GCSE/Topic-Qs/OCR-A/6-Global-Challenges/Set-A/Improving%20Processes%20&%20Products%202%20QP.pdf",
        "Interpreting & Interacting with Earth Systems 1 QP": "https://pmt.physicsandmathstutor.com/download/Chemistry/GCSE/Topic-Qs/OCR-A/6-Global-Challenges/Set-A/Interpreting%20&%20Interacting%20with%20Earth%20Systems%201%20QP.pdf",
        "Interpreting & Interacting with Earth Systems 2 QP": "https://pmt.physicsandmathstutor.com/download/Chemistry/GCSE/Topic-Qs/OCR-A/6-Global-Challenges/Set-A/Interpreting%20&%20Interacting%20with%20Earth%20Systems%202%20QP.pdf",
        "Organic Chemistry 1 QP": "https://pmt.physicsandmathstutor.com/download/Chemistry/GCSE/Topic-Qs/OCR-A/6-Global-Challenges/Set-A/Organic%20Chemistry%201%20QP.pdf",
        "Organic Chemistry 2 QP": "https://pmt.physicsandmathstutor.com/download/Chemistry/GCSE/Topic-Qs/OCR-A/6-Global-Challenges/Set-A/Organic%20Chemistry%202%20QP.pdf",
        "Organic Chemistry 3 QP": "https://pmt.physicsandmathstutor.com/download/Chemistry/GCSE/Topic-Qs/OCR-A/6-Global-Challenges/Set-A/Organic%20Chemistry%203%20QP.pdf"
    }
}
"""


# for each topic, for each question paper, download the pdf to pdfs/physics/<question paper name as lowercase, no spaces and no QP or (H)>.pdf

parsed = json.loads(data)
for topic in parsed:
    for qp in parsed[topic]:
        url = parsed[topic][qp]
        filename = "t" + topic.split(":")[0].split("Topic").pop().strip().replace(" ", "_") + "_" + qp.replace("QP", "").replace(
            "(H)", "").strip().lower().replace(" ", "_").split(".").pop() + ".pdf"
        # print(f"Downloading {filename}")
        with open(f"./pdfs/chem-pmt/{filename}", "wb") as f:
            f.write(requests.get(url).content)
        print(f"Downloaded {filename}!")
