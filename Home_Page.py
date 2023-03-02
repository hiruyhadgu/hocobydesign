import streamlit as st
import pandas as pd
import sqlite3 as db
from PIL import Image

image = Image.open('combined.jpeg')
# st.sidebar.image("combined.jpeg", use_column_width=True)
st.set_page_config(page_title='HoCo By Design Fiscal Impact Analysis Explorer', page_icon=image)

st.header('HoCoByDesign Fiscal Impact Analysis Independent Evaluation')

st.markdown('---')

st.markdown("""
The County's six-page fiscal impact analysis result incorporates the FY2023 adopted operating and capital budget.\
 The two sets of primary inputs are residential unit types and job types by planning area. The HoCo By Design fiscal\
fiscal impact methodology and assumptions outputs an 18-year projection of revenues and expenses for various categories\
of sources of funds and obligations, respectively.
            
The fiscal impact analysis concludes that *new growth would generate more revenues than costs for services and\
infrastructure.* Several assumptions are made in the entire analysis about residential development, which also\
revealed county budgeting practices, to enable this assertion. Before delving in to the other assumptions, a financial\
analyst would look at the results table and immediately notice somethign strange. The **Average Annual** column of the results\
table takes the simple average of the annual revenue and expenditure results and takes their difference to obtain \\$52,466,000 in\
net average revenues. Next, the first year net revenue is shown to be \\$30,264,000.
""")

st.markdown("#### Two Basic Major Issues")

st.markdown("As a long-term *Pro Forma* financial projection these two results are problematic:")
            

st.markdown("""
First, the simple average of an 18-year financial projection ignores the time value of money. For example, in year 18,\
the County's result says revenues of \\$304,732,000 are expected. This is a meaningless number. For instance, the expected\
revenue in year 18 when discounted to 2023 at the 20-year U.S. Treasury Bond yield of 4.118% is approximatly \\$147.6 million.

Second, the projected net revenue in year one needs to be placed in perspective. The FY2023 General Fund revenues total\
$1.29 Billion. That means, the projected net revenue is just 2.35% of the total revenue not counting the rest of the budget.\
 No amount of predicition can provide this level of precision, especially with the level of variablity encountered when dealing\
with amount of assumptions used.

This leads to the next point.

""")

st.markdown("#### Additional Major Issues")

st.markdown("*The Fiscal Analysis Does not Employ Representative Historical Values*")

st.markdown("""
Howard County's budget and financial history did not start in 2023. The biggest predictor of the future is the past. In statistics\
one data point is useless. In order to gain a degree of statistical confidence, more data points are needed. This is a standard practice\
in the task of predictive statistics. For example, drug trials rely on multiple trial participants of various ages and backgrounds. If\
the test subject for a drug trial is one 25-year old white male, the drug company cannot say with any degree of confidence that whether or\
not the drug works. If the trial has multiple 25-year old white males, the degree of confidence improves, but it does not say how it will\
affect 25-year old white females, black males, or black females. It also does not say how it will affect older males, younger males, older\
females, younger females, children, or any other demographic group.

This simple analogy can be applied to the county's fiscal impact analysis. The FY2023 budget represents one economic period in time.\
It does not explain Howard County's economic and fiscal experience in 2022, 2021, 2020, and beyond. Each annual budget is a\
reflection of the set of zoning and land-use decisions that took place in the previous years. Therefore, it only makes sense to use\
a representative number with some sort of associated variablity to capture the range of possible outcomes. In other words, an *average* and a\
*standard deviation.*
""")

st.markdown("The next set of analyses pertain to specific sections of the county's fiscal impact results.")

st.markdown("#### HCPSS Operating and Capital Expenditure")

st.markdown("*Per Student Operating Costs*")

st.markdown("""
The county's analysis uses a per-student operating cost of \\$11,341.32 using the FY23 enrollment of 59,367 students as its basis.\
Meanwhile, the county states that the **total** per-student operating cost is \\$17,353, which includes State and other funding. The\
county states that only the local funding is taken into account because this is what is accounted for in the County General Fund.\
 There are two issues with this assumption and methodology.
            
First, the per-student cost uses FY23 enrollment numbers while the per-student debt financing cost (discussed later) uses 57,325 is\
a basis. Using a higher number of students here depresses the per-student cost.

"Second, why is only the County General Fund taken into account? The assumption the county takes should reflect what would happen if\
the county is required to cover shortfalls due to decline in state funding. This leads to the suggestion that the county should use\
**total** per-student cost; not partial per-student cost. Every additional residential home with a student incurs an operational demand of\
\\$17,353.
""")

st.markdown("*Per Student Capital Costs*")

st.markdown("""
The school capital budget calculation and assumptions also face similar challenges. State aid to build schools is part of the cost to \
build a school and the primary responsibility of building a school falls on the county; not on the state. Therefore, excluding it assumes \
that the dollars to cover the balance after the county's general fund contribution will always be available and this is obviously not true.\
If the state doesnt award the aid, the county defers much needed school construction.

Next, there are serious flaws on how the county calcualtes the per-student construction costs. For example the county estimates highschools \
cost roughly \\$130 million based on Guilford Park High School. Excluding state funding it estimates a general fund obligation of \\$77,686,000. \
 However, this seriously underestimates the cost. For example, while the school construction project at Hammond High School added 200 and cost\
\\$106,554,000 it was also a renovation project. Recognizing this distinction, there is still a significant cost to the county to **add** seats to an\
 existing school than to build a new one.

Nobody beneifts from undercounting or not recognizing this impact. In fact, it provides a much better and accurate picture. Afterall, the need to \
add 200 seats are due to new residential development. As a result, the per-student cost to build highschool is closer to \\$127,315 without recognizing \
state aid. Even assuming state aid, the actual cost is closer to \\$77,000.

Another major glaring flaw of the methodology is the assumption that only 50% of the capital costs for schools will be PayGo and the remaining 50% \
would come from debt financing over 20 years. The county justifies this approach by claiming that a portion of the school surcharge collect pays old\
debt. The county says:

"Even though the majority of school surcharge revenues are paying debt service from previous projects, new development still pays \
this surcharge so should get credit to offset school capacity costs incurred."

This is a rather shocking and false claim. If someone pays of their previous month's credit card debt using this month's paycheck, while incurring \
new debt for this month to cover living expenses, did they actually pay off all their debt? No.

Just in 2023 alone, the county spent \\$48,747,588 in debt service for school captial costs. There is no scenario under which significant amounts of\
county dollars are allocated to finance debt incurred for school construction to accomodate previous years' new residential development would be\
lead to a conclusion that "residential development pays for itself."

""")

st.markdown("*Systemic Renovations Assumptions*")

st.markdown("""
The county's accumulated systemic renovation costs are over \\$500 million. The analysis assumes a per-student basis of \\$580.90 based on a total\
spending of \\$33,300,000. There is no indication that this amount will help reduce the accumulated deferred maintenance over the next 18 years. In fact\
it will most-assuredly not, given that every year more facilities need upkeep.
""")
st.markdown("*Student Generation Rates*")

st.markdown("""
Student generation rates have long been contentious. The county assumes that a student from a new residential development is no longer tracked as such for \
planning and amoritzation purposes after the first year. In other words, after the first year, a new student is no longer from a new residential\
development. Further, in the past, the county has shared data that large amount of the fifty plus communities create resales. Retirees sell their \
home to a young family and move to a fifty plus community. The new student from that resale is clearly tied to the new construction and should be \
treated accordingly.
""")

st.markdown("### Road Expenditure")

st.markdown("""
The county's analysis of road expenditure has several flaws. 

First it adjusts to inflation total annual historical spending on roads. As mentioned earlier, neglecting to employ some sort of a net-present value\
 methodology to the 18-year projection is one of the analysis flows in projecting future revenue and expenditure. So it is interesting that this\
 section applies the time value of money to adjust old spending to 2022 dollars.

Next, the county uses an incorrect 2010 county population. In 2010 the county population was 288,627. Not 247,842. Using this lower value reduces the per-capita\
spending that is used to project future expenditure. While the analysis uses \\$1,388 per capita and jobs created, the real number is \\$2,087 per capita and jobs.\
This would underestimate the spending by over 33%.

Finally, the fiscal analysis says "it is assumed that 100% of capital costs for new roads and related capacity expanding improvements will be debt-financed\
over 20 years..." It is assumed that there is no PayGo funding for these future roads given that all future Road Excise Tax revenues are currently being used\
to pay back existing Road Excise Bonds." In other words, residential development does not pay for itself.

""")

# Use Local CSS File
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)