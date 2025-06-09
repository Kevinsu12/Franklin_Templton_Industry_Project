from typing import Optional
from pydantic import BaseModel, Field

class EndowmentAndInvestmentLevels_2024_25(BaseModel):
    # ───── ENDOWMENT ASSETS ─────
    endowment_net_assets_eoy_total: Optional[int] = Field(
        description=(
            "Total endowment net assets for the 2024–2025 fiscal year (in thousands). "
            "Only extract from a table titled 'Changes in Endowment Net Assets' located in the Notes section. "
            "Only use data explicitly labeled as '2024', 'FY2024', or 'as of June 30, 2024'. "
            "Do not extract from general balance sheets, rollforwards, or systemwide summaries. "
            "Standardize all values to $000s using table metadata or heuristics."
        )
    )

    endowment_net_assets_eoy_with_donor_restrictions: Optional[int] = Field(
        description=(
            "Total donor-restricted endowment net assets as of June 30, 2024 (in thousands). "
            "Must be extracted from a 'Changes in Endowment Net Assets' table in the Notes section. "
            "Exclude all 2023 or earlier data. Must be clearly labeled as 2024."
        )
    )

    endowment_net_assets_eoy_with_donor_restrictions_temporarily_restricted: Optional[int] = Field(
        description=(
            "Temporarily restricted portion of donor-restricted endowment net assets for FY2024 (in thousands). "
            "Must appear in a table under Notes with a clear 2024 label. Ignore unlabeled or earlier year data."
        )
    )

    endowment_net_assets_eoy_with_donor_restrictions_permanently_restricted: Optional[int] = Field(
        description=(
            "Permanently restricted portion of donor-restricted endowment net assets for FY2024 (in thousands). "
            "Only extract from Notes where clearly labeled as 2024."
        )
    )

    endowment_net_assets_eoy_without_donor_restrictions: Optional[int] = Field(
        description=(
            "Unrestricted portion of endowment net assets for the 2024–2025 fiscal year (in thousands). "
            "Must be pulled from a 'Changes in Endowment Net Assets' table in Notes. "
            "Only extract if labeled as 2024. Ignore prior-year or aggregated system data."
        )
    )

    # ───── ENDOWMENT SPENDING ─────
    appropriation_of_endowment_for_expenditure_total: Optional[int] = Field(
        description=(
            "Total appropriations or spending from the endowment during 2024–2025 (in thousands). "
            "Only extract from the 'Changes in Endowment Net Assets' table in the Notes section. "
            "Do not infer from general text or extract from unlabeled rows."
        )
    )

    appropriation_of_endowment_for_expenditure_with_donor_restrictions: Optional[int] = Field(
        description=(
            "Appropriations from donor-restricted endowment funds for FY2024 (in thousands). "
            "Must appear in a 2024-labeled row of the Notes. Ignore prior years and total-only rows."
        )
    )

    appropriation_of_endowment_for_expenditure_without_donor_restrictions: Optional[int] = Field(
        description=(
            "Appropriations from unrestricted endowment funds during 2024–2025 (in thousands). "
            "Must appear in a 'Changes in Endowment Net Assets' table and be labeled 2024. Ignore earlier data."
        )
    )

    # ───── INVESTMENT VALUATION (FAIR VALUE HIERARCHY) ─────
    investment_level_1: Optional[int] = Field(
        description=(
            "Fair value of Level 1 investments (quoted market prices) at June 30, 2024 (in thousands). "
            "Only extract from a fair value hierarchy table in the Notes section. "
            "Ensure the table is for the university, not an enterprise or foundation. "
            
        )
    )

    investment_level_2: Optional[int] = Field(
        description=(
            "Fair value of Level 2 investments (observable inputs) as of the end of FY2024 (in thousands). "
            "Must be extracted from the same fair value hierarchy table in the Notes section. "
            "Only use data labeled 2024. Avoid mixing rows from different years or sources."
        )
    )

    investment_level_3: Optional[int] = Field(
        description=(
            "Fair value of Level 3 investments (unobservable inputs) at year-end 2024 (in thousands). "
            "Only extract from 2024-labeled fair value tables in the Notes. Ignore mixed-year summaries."
        )
    )

    # ───── NAV & TOTAL FAIR VALUE ─────
    investments_measured_at_nav: Optional[int] = Field(
        description=(
            "Total value of investments measured at Net Asset Value (NAV) at June 30, 2024 (in thousands). "
            "Must be extracted from a Fair Value Hierarchy table in the Notes. "
            "Include Life Insurance Cash Surrender value if presented separately and applicable. "
            "Ensure values are labeled as 2024 and not drawn from system-wide or multi-entity tables."
        )
    )

    investments_total_fair_value: Optional[int] = Field(
        description=(
            "Total fair value of all university investments as of fiscal year end 2024–2025 (in thousands). "
            "Must be sourced from the same fair value hierarchy table as NAV and Levels 1–3. "
            "Do not infer from text, and ignore totals from earlier years, foundations, or consolidated entities."
        )
    )
