# coding:utf8

from bs4 import BeautifulSoup
import json

job = {}
f = open('job.json', 'a')--

html_doc = open('parserHTML.html', 'r')
soup = BeautifulSoup(html_doc, 'html.parser')

table = soup.find("table", {"class":"search-results__results"})
rows = table.findAll("tr")
for row in rows:
    cells = row.findAll("td", "serp-vacancy__cell")
    step = 1

    for cell in cells:

        if step == 1:

            jobName = cell.contents[0]
            jobUrl = cell.contents[0].h3.a["href"]

            try:
                jobGraphik = cell.contents[1].contents[0].contents[1]
                jobCompany = cell.contents[1].contents[0].div
            except IndexError:
                jobCompany = ''
                jobGraphik = cell.contents[1].contents[0].div

            jobReguir = cell.contents[2]

            job["A"] = jobName.text
            job["B"] = jobUrl
            if jobCompany != '':
                job["C"] = jobCompany.text

            job["D"] = jobGraphik.text
            job["E"] = jobReguir.text

            step = 2
        else:
            jobSalary = cell.contents[0]
            job["F"] = jobSalary.text

    if step == 2:
        jobSave = json.dumps(job, ensure_ascii=False)
        f.write(jobSave)
        job.clear()

f.close()