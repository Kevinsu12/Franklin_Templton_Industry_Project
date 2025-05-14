from typing import Optional
from pydantic import BaseModel, Field

class Enrollment2024_25(BaseModel):
    Undergraduate_Headcount: Optional[int] = Field(
        description=(
            "Total undergraduate headcount for the 2024–2025 academic year "
            "(Different than undergraduate FTE. Sometimes you need to combine both full-time and part time)."
            "Search around the tables to locate what type of enrollment information it is."
            "Ex: Texas A&M's first table is just says 'total enrollment headcount', but if you look around the table, it's for "
            "combination of undergraduate and graduate, so it doesn't belong to this undergraduate_headcount, it should be total headcount."
            "DO NOT include the first table information on Texas A&M for this field, it should be for total headcount."
            "Only extract data for the 2024–2025 year or terms labeled Fall 2024, etc"
            "ignore any data from other years or terms (e.g., 2023–2024, Fall 2023). "
            "it's possible for a school to have multiple campuses, so combine all campuses' count or online and in-person count if applicable."
            " Do not derive or hallucinate the data unless the field is actually in the document."
        )
    )
    
    Undergraduate_Headcount_Full_Time: Optional[int] = Field(
        description=(
            "Undergraduate full-time or FT headcount for the 2024–2025 academic year. "
            "This is different than FTE(full-time equivalent)."
            "Only extract data for the 2024–2025 year or terms labeled Fall 2024, etc. "
            "Ignore any data from other years or terms. "
            "Combine across all campuses if the institution has multiple locations."
            " Do not derive or hallucinate the data unless the field is actually in the document."
        )
    )
    Undergraduate_Headcount_Part_Time: Optional[int] = Field(
        description=(
            "Undergraduate part-time (PT) headcount for the 2024–2025 academic year. "
            "Only extract data for the 2024–2025 year or terms labeled Fall 2024, etc. "
            "Ignore any data from other years or terms. "
            "Combine across all campuses if the institution has multiple locations."
            " Do not derive or hallucinate the data unless the field is actually in the document."
        )
    )
    Graduate_Headcount: Optional[int] = Field(
        description=(
            "Total graduate headcount for the 2024–2025 academic year "
            "(Different than graduate FTE. Sometimes you need to combine both full-time and part time), "
            "Combine enrollment across all graduate schools (e.g. Business, Education, etc.), "
            "which may be labeled “GR”, “Grad”, or “Graduate”. "
            "Only extract data for the 2024–2025 year or terms labeled Fall 2024, etc"
            "ignore any data from other years or terms (e.g., 2023–2024, Fall 2023). "
            "it's possible for a school to have multiple campuses, so combine all campuses' count or online and in-person count if applicable."
            " Do not derive or hallucinate the data unless the field is actually in the document."
        )
    )
    Graduate_Headcount_Full_Time: Optional[int] = Field(
        description=(
            "Graduate full-time (FT) headcount for the 2024–2025 academic year. "
            "This is different than FTE(full-time equivalent)."
            "Combine across all graduate schools. "
            "Only extract data for the 2024–2025 year or terms labeled Fall 2024, etc. "
            "Ignore any data from other years or terms. "
            "Combine across campuses if needed."
            " Do not derive or hallucinate the data unless the field is actually in the document."
        )
    )
    Graduate_Headcount_Part_Time: Optional[int] = Field(
        description=(
            "Graduate part-time (PT) headcount for the 2024–2025 academic year. "
            "Combine across all graduate schools. "
            "Only extract data for the 2024–2025 year or terms labeled Fall 2024, etc. "
            "Ignore any data from other years or terms. "
            "Combine across campuses if needed."
            " Do not derive or hallucinate the data unless the field is actually in the document."
        )
    )
    Professional_Headcount: Optional[int] = Field(
        description=(
            "Combined professional school headcount (e.g. med, law) for 2024–2025 "
            "(Different than professional FTE. Sometimes you need to combine both full-time and part time)."
            "Only extract data for the 2024–2025 year or terms labeled Fall 2024, etc"
            "ignore any data from other years or terms (e.g., 2023–2024, Fall 2023). "
            "it's possible for a school to have multiple campuses, so combine all campuses' count if applicable."
            " Do not derive or hallucinate the data unless the field is actually in the document."
        )
    )

    Non_Degree_Headcount: Optional[int] = Field(
        description=(
            "(Different than Non-Degree FTE. Sometimes you need to combine both full-time and part time)."
            "Sometimes, Non-Degree is listed as Non-credit"
            "Only extract data for the 2024–2025 year or terms labeled Fall 2024, etc"
            "ignore any data from other years or terms (e.g., 2023–2024, Fall 2023). "
            "it's possible for a school to have multiple campuses, so combine all campuses' count if applicable."
            " Do not derive or hallucinate the data unless the field is actually in the document."
        )
    )
    Total_Headcount: Optional[int] = Field(
        description=(
            "Overall student headcount for 2024–2025 "
            "do **not** compute it by adding Undergraduate, Graduate, Professional, etc."
            "Only extract data for the 2024–2025 year or terms labeled Fall 2024, etc"
            "ignore any data from other years or terms (e.g., 2023–2024, Fall 2023). "
            "it's possible for a school to have multiple campuses, so combine all campuses' count if applicable."
            " Do not derive or hallucinate the data unless the field is actually in the document."
        )
    )

    Total_Headcount_Full_Time: Optional[int] = Field(
        description=(
            "Total full-time headcount for 2024–2025 across all student categories. "
            "This is different than FTE(full-time equivalent)."
            "If not explicitly provided, sum Undergraduate_Headcount_Full_Time + Graduate_Headcount_Full_Time. "
            "Only extract data for the 2024–2025 year or terms labeled Fall 2024. "
            "Ignore any data from other years or terms."
            "do **not** derive it by summing individual full‑time headcounts."
            " Do not derive or hallucinate the data unless the field is actually in the document."

        )
    )
    Total_Headcount_Part_Time: Optional[int] = Field(
        description=(
            "Total part-time headcount for 2024–2025 across all student categories. "
            "If not explicitly provided, sum Undergraduate_Headcount_Part_Time + Graduate_Headcount_Part_Time. "
            "Only extract data for the 2024–2025 year or terms labeled Fall 2024. "
            "Ignore any data from other years or terms."
            "do **not** derive it by summing individual part‑time headcounts."
            " Do not derive or hallucinate the data unless the field is actually in the document."

        )
    )

    Undergraduate_FTE: Optional[int] = Field(
        description=(
            "Undergraduate full-time equivalent headcount or FTE for 2024–2025 "
            "FTE (full-time equivalent) is different than full-time, or FT."
            "Only extract data for the 2024–2025 year or terms labeled Fall 2024, etc"
            "ignore any data from other years or terms (e.g., 2023–2024, Fall 2023). "
            "it's possible for a school to have multiple campuses, so combine all campuses' count if applicable."
            " Do not derive or hallucinate the data unless the field is actually in the document."
        )
    )
    Graduate_FTE: Optional[int] = Field(
        description=(
            "Graduate full-time headcount or FTE for 2024–2025 "
            "FTE (full-time equivalent) is different than full-time, or FT."
            "Combine enrollment across all graduate schools (e.g. Business, Education, etc.), "
            "which may be labeled “GR”, “Grad”, or “Graduate”. "
            "Only extract data for the 2024–2025 year or terms labeled Fall 2024, etc"
            "ignore any data from other years or terms (e.g., 2023–2024, Fall 2023). "
            "it's possible for a school to have multiple campuses, so combine all campuses' count if applicable."
            " Do not derive or hallucinate the data unless the field is actually in the document."
        )
    )
    Professional_FTE: Optional[int] = Field(
        description=(
            "Professional school full-time headcount or FTE for 2024–2025 "
            "FTE (full-time equivalent) is different than full-time, or FT."
            "Only extract data for the 2024–2025 year or terms labeled Fall 2024, etc"
            "ignore any data from other years or terms (e.g., 2023–2024, Fall 2023). "
            "it's possible for a school to have multiple campuses, so combine all campuses' count if applicable."
            " Do not derive or hallucinate the data unless the field is actually in the document."
        )
    )
    Total_Full_Time_Equivalent_Students: Optional[int] = Field(
        description=(
            "Total full-time equivalent students (FTE) for the 2024–2025 academic year."
            "Only extract data for the 2024–2025 year or terms labeled Fall 2024, etc"
            "ignore any data from other years or terms (e.g., 2023–2024, Fall 2023). "
            "it's possible for a school to have multiple campuses, so combine all campuses' count if applicable."
            "do **not** derive it by summing the individual FTE fields."
            " Do not derive or hallucinate the data unless the field is actually in the document."
        )
    )

    Undergraduate_Applications_Rcvd: Optional[int] = Field(
        description=(
            "Total undergraduate applications received for the 2024–2025 cycle "
            "(e.g. Fall 2024). Ignore other years/terms. "
            "Combine all campuses if applicable."
            " Do not derive or hallucinate the data unless the field is actually in the document."
        )
    )
    Graduate_Applications_Rcvd: Optional[int] = Field(
        description=(
            "Total graduate applications received for the 2024–2025 cycle "
            "(e.g. Fall 2024). Ignore other years/terms. "
            "Combine all campuses if applicable."
            " Do not derive or hallucinate the data unless the field is actually in the document."
        )
    )
    Transfer_Applications_Rcvd: Optional[int] = Field(
        description=(
            "Total transfer applications received for the 2024–2025 cycle "
            "(e.g. Fall 2024). Ignore other years/terms. "
            "Combine all campuses if applicable."
            " Do not derive or hallucinate the data unless the field is actually in the document."
        )
    )

    Undergraduate_Acceptances: Optional[int] = Field(
        description=(
            "Total undergraduate acceptances for the 2024–2025 cycle "
            "(e.g. Fall 2024). Ignore other years/terms. "
            "Combine all campuses if applicable."
            " Do not derive or hallucinate the data unless the field is actually in the document."
        )
    )
    Graduate_Acceptances: Optional[int] = Field(
        description=(
            "Total graduate acceptances for the 2024–2025 cycle "
            "(e.g. Fall 2024). Ignore other years/terms. "
            "Combine all campuses if applicable."
            " Do not derive or hallucinate the data unless the field is actually in the document."
        )
    )
    Transfer_Acceptances: Optional[int] = Field(
        description=(
            "Total transfer acceptances for the 2024–2025 cycle "
            "(e.g. Fall 2024). Ignore other years/terms. "
            "Combine all campuses if applicable."
            " Do not derive or hallucinate the data unless the field is actually in the document."
        )
    )

    Undergraduate_Matriculants: Optional[int] = Field(
        description=(
            "Number of undergraduate students who matriculated in Fall 2024 / 2024–2025. "
            "Ignore other years/terms. "
            "Combine all campuses if applicable."
            " Do not derive or hallucinate the data unless the field is actually in the document."
        )
    )
    Graduate_Matriculants: Optional[int] = Field(
        description=(
            "Number of graduate students who matriculated in Fall 2024 / 2024–2025. "
            "Ignore other years/terms. "
            "Combine all campuses if applicable."
            " Do not derive or hallucinate the data unless the field is actually in the document."
        )
    )
    Transfer_Matriculants: Optional[int] = Field(
        description=(
            "Number of transfer students who matriculated in Fall 2024 / 2024–2025. "
            "Ignore other years/terms. "
            "Combine all campuses if applicable."
            " Do not derive or hallucinate the data unless the field is actually in the document."
        )
    )
    Retention_Rate: Optional[float] = Field(
        description=(
            "Retention rate % for the 2024–2025 entering class. "
            "Only extract data for the 2024–2025 year or terms labeled Fall 2024, etc.; "
            "ignore any data from other years or terms (e.g., 2023–2024, Fall 2023)."
            "it's possible for a school to have multiple campuses, so combine all campuses' count if applicable."
            " Do not derive or hallucinate the data unless the field is actually in the document."
        )
    )

    Full_Time_Employee_Equivalents: Optional[int] = Field(
        description=(
            "Full-time employee equivalents (staff/faculty) in 2024–2025. "
            "Only extract data for the 2024–2025 year or terms labeled Fall 2024, etc.; "
            "ignore any data from other years or terms (e.g., 2023–2024, Fall 2023)."
            "it's possible for a school to have multiple campuses, so combine all campuses' count if applicable."
            " Do not derive or hallucinate the data unless the field is actually in the document."
        )
    )
    Tuition: Optional[int] = Field(
        description=(
            "Undergraduate tuition rate for the 2024–2025 academic year. "
            "This is different than revenue generated by tuition or any financial accounting data"
            "Only extract data for the 2024–2025 year or terms labeled Fall 2024, etc.; "
            "ignore any data from other years or terms (e.g., 2023–2024, Fall 2023)."
            "it's possible for a school to have multiple campuses, so average the tuition per student per campus."
            " Do not derive or hallucinate the data unless the field is actually in the document."
        )
    )
    Room_and_Board_20_meals: Optional[int] = Field(
        description=(
            "Room & board cost (20-meal plan) for the 2024–2025 year. "
            "Only extract data for the 2024–2025 year or terms labeled Fall 2024, etc.; "
            "ignore any data from other years or terms (e.g., 2023–2024, Fall 2023)."
            "it's possible for a school to have multiple campuses, so combine all campuses' count if applicable."
            " Do not derive or hallucinate the data unless the field is actually in the document."
        )
    )



class FinancialPosition_2024_25(BaseModel):
    year: int = Field(
        description=(
            "Fiscal year for which the data applies (e.g., 2024–2025). "
            "Only extract data for the 2024–2025 fiscal year; ignore data from other years or periods."
        )
    )
    cash_and_short_term_investments: Optional[int] = Field(
        description=(
            "Unrestricted cash, cash equivalents, and short‑term investments as of the end of the 2024–2025 fiscal year. "
            "Only extract 2024–2025 data; exclude restricted cash reported separately and any other periods. "
            "If the institution reports multiple segments or campuses, combine all."
        )
    )
    student_receivables_net: Optional[int] = Field(
        description=(
            "Net student receivables for the 2024–2025 fiscal year (after allowance for doubtful accounts). "
            "Only extract net figures; ignore gross receivables or allowances reported separately. "
            "Combine across campuses if applicable."
        )
    )
    accounts_receivable: Optional[int] = Field(
        description=(
            "Total accounts receivable as of the end of the 2024–2025 fiscal year. "
            "Only extract data for 2024–2025; exclude intercompany balances if reported separately. "
            "Combine across all reporting units."
        )
    )
    contributions_receivable: Optional[int] = Field(
        description=(
            "Pledges and contributions receivable for the 2024–2025 fiscal year. "
            "Only extract receivable amounts net of allowance; ignore contributions from other periods. "
            "Combine across campuses or programs."
        )
    )
    notes_receivable: Optional[int] = Field(
        description=(
            "Notes receivable outstanding as of the end of the 2024–2025 fiscal year. "
            "Only extract 2024–2025 amounts; combine across all segments if reported separately."
        )
    )
    loans_receivable_net: Optional[int] = Field(
        description=(
            "Net loans receivable (after allowance) for the 2024–2025 fiscal year. "
            "Only extract net figures; ignore loan loss reserves or gross balances. "
            "Combine across campuses if applicable."
        )
    )
    other_assets: Optional[int] = Field(
        description=(
            "Other assets not classified elsewhere for the 2024–2025 fiscal year. "
            "Only extract 2024–2025 data; review footnotes to avoid overlap with other categories."
        )
    )
    investments: Optional[int] = Field(
        description=(
            "Short‑ and long‑term investments as of the end of the 2024–2025 fiscal year. "
            "Only extract fair‑value amounts; exclude restricted or endowment investments if reported separately."
        )
    )
    right_of_use_assets: Optional[int] = Field(
        description=(
            "Total right‑of‑use assets recognized under ASC 842 for the 2024–2025 fiscal year. "
            "Only extract lease assets; ignore associated lease liabilities."
        )
    )
    land_buildings_equipment_net: Optional[int] = Field(
        description=(
            "Property, plant, and equipment, net of accumulated depreciation, as of the end of the 2024–2025 fiscal year. "
            "Only extract net PP&E; accumulated depreciation is reported separately. "
            "Combine across all locations if the institution has multiple campuses."
        )
    )
    accumulated_depreciation: Optional[int] = Field(
        description=(
            "Total accumulated depreciation (contra‑asset) as of the end of the 2024–2025 fiscal year. "
            "Only extract depreciation related to PP&E; confirm sign convention."
        )
    )
    rou_assets_finance_lease: Optional[int] = Field(
        description=(
            "Right‑of‑use assets under finance leases for the 2024–2025 fiscal year. "
            "Only extract finance‑lease assets; exclude operating leases."
        )
    )
    rou_assets_operating_lease: Optional[int] = Field(
        description=(
            "Right‑of‑use assets under operating leases for the 2024–2025 fiscal year. "
            "Only extract operating‑lease assets; exclude finance leases."
        )
    )
    current_portion_long_term_debt: Optional[int] = Field(
        description=(
            "Portion of long‑term debt due within one year as of the 2024–2025 fiscal year end. "
            "Only extract current maturities; ignore total long‑term debt lines."
        )
    )
    current_portion_operating_lease: Optional[int] = Field(
        description=(
            "Current portion of lease liabilities under operating leases for the 2024–2025 fiscal year. "
            "Only extract amounts due within one year; the long‑term portion is reported separately."
        )
    )
    short_term_debt: Optional[int] = Field(
        description=(
            "Short‑term borrowings (e.g., commercial paper) as of the 2024–2025 fiscal year end. "
            "Only extract amounts maturing within one year; ignore long‑term borrowings."
        )
    )
    total_assets: Optional[int] = Field(
        description=(
            "Total assets for the 2024–2025 fiscal year. "
            "Only extract if explicitly provided; otherwise sum all individual asset line items."
        )
    )
    accounts_payable: Optional[int] = Field(
        description=(
            "Trade and other payables as of the end of the 2024–2025 fiscal year. "
            "Only extract accounts payable; exclude accrued expenses."
        )
    )
    student_deposits_and_deferred_revenue: Optional[int] = Field(
        description=(
            "Student deposits and deferred revenue balances for the 2024–2025 fiscal year. "
            "Only extract deferred tuition/fees; ignore deposits from other sources."
        )
    )
    tenant_capital_improvements: Optional[int] = Field(
        description=(
            "Liabilities for tenant capital improvements as of the 2024–2025 fiscal year end. "
            "Only extract capital improvement obligations; confirm classification via footnotes."
        )
    )
    bonds_payable_net: Optional[int] = Field(
        description=(
            "Bonds payable, net of unamortized discount/premium, as of the 2024–2025 fiscal year end. "
            "Only extract net bond amounts; ignore gross issue amounts."
        )
    )
    refundable_advances_us_govt: Optional[int] = Field(
        description=(
            "Refundable government advances (e.g., Pell grants) for the 2024–2025 fiscal year. "
            "Only extract refundable advance balances; exclude nonrefundable grants."
        )
    )
    lease_obligations: Optional[int] = Field(
        description=(
            "Total lease liabilities recognized under ASC 842 for the 2024–2025 fiscal year. "
            "Only extract combined current and non‑current lease obligations."
        )
    )
    liabilities_under_split_interest_agreements: Optional[int] = Field(
        description=(
            "Liabilities under split‑interest agreements for the 2024–2025 fiscal year. "
            "Only extract these obligations; consult footnotes for detail."
        )
    )
    liabilities_associated_with_investments: Optional[int] = Field(
        description=(
            "Investment‑related liabilities (e.g., margin loans) for the 2024–2025 fiscal year. "
            "Only extract liabilities tied to investment activities; ignore other financing liabilities."
        )
    )
    non_controlling_interests: Optional[int] = Field(
        description=(
            "Non‑controlling (minority) interests in consolidated subsidiaries as of the 2024–2025 fiscal year end. "
            "Only extract equity attributable to minority shareholders."
        )
    )
    total_liabilities: Optional[int] = Field(
        description=(
            "Total liabilities for the 2024–2025 fiscal year. "
            "Only extract if provided; otherwise sum all individual liability line items."
        )
    )
    net_assets_with_donor_restrictions: Optional[int] = Field(
        description=(
            "Net assets subject to donor restrictions as of the 2024–2025 fiscal year end. "
            "Only extract donor‑restricted amounts; exclude board‑designated funds."
        )
    )
    net_assets_without_donor_restrictions: Optional[int] = Field(
        description=(
            "Net assets without donor restrictions for the 2024–2025 fiscal year. "
            "Only extract unrestricted net assets; ignore temporarily restricted categories."
        )
    )
    total_net_assets: Optional[int] = Field(
        description=(
            "Total net assets (with and without donor restrictions) for the 2024–2025 fiscal year. "
            "Only extract if provided; otherwise sum net asset lines."
        )
    )
    total_liabilities_and_net_assets: Optional[int] = Field(
        description=(
            "Total liabilities and net assets (should equal total assets) for the 2024–2025 fiscal year. "
            "Only extract provided totals; verify the balance sheet equation holds."
        )
    )
