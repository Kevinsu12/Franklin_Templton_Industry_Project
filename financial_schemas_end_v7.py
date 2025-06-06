from typing import Optional
from pydantic import BaseModel, Field

class EndowmentAndInvestmentLevels_2024_25(BaseModel):
    # ───── ENDOWMENT ASSETS ─────
    endowment_net_assets_eoy_total: Optional[int] = Field(
        description=(
            "Total endowment net assets for the 2024–2025 fiscal year (in thousands). "
            "Only extract from a table labeled 'Changes in Endowment Net Assets' in the Notes section. "
            "**Include only values clearly labeled as 2024, FY2024, or 'as of June 30, 2024'. Ignore 2023 and earlier values.** "
            "Do not extract from general balance sheets or summaries. Values must be standardized to $000s."
        )
    )

    endowment_net_assets_eoy_with_donor_restrictions: Optional[int] = Field(
        description=(
            "Total donor-restricted endowment net assets as of the end of fiscal year 2024–2025 (in thousands). "
            "Must be from a 'Changes in Endowment Net Assets' table in the Notes section. "
            "**Exclude any data from 2023 or earlier.**"
        )
    )

    endowment_net_assets_eoy_with_donor_restrictions_temporarily_restricted: Optional[int] = Field(
        description=(
            "Temporarily restricted portion of endowment net assets (in thousands), for fiscal year 2024–2025. "
            "Only extract if labeled as 2024 or 'June 30, 2024'. Must come from detailed note tables."
        )
    )

    endowment_net_assets_eoy_with_donor_restrictions_permanently_restricted: Optional[int] = Field(
        description=(
            "Permanently restricted portion of endowment net assets (in thousands), for fiscal year 2024–2025. "
            "Only extract if clearly labeled and appears in a table in the notes section. Exclude 2023 data."
        )
    )

    endowment_net_assets_eoy_without_donor_restrictions: Optional[int] = Field(
        description=(
            "Unrestricted endowment net assets (in thousands), for the 2024–2025 fiscal year. "
            "Must come from a detailed endowment activity table in the Notes. Ignore earlier years."
        )
    )

    # ───── ENDOWMENT SPENDING ─────
    appropriation_of_endowment_for_expenditure_total: Optional[int] = Field(
        description=(
            "Total appropriation/spending from endowment for 2024–2025 (in thousands). "
            "Must be from a table labeled 'Changes in Endowment Net Assets' or similar, and clearly labeled as 2024. "
            "**Ignore 2023 and earlier values.**"
        )
    )

    appropriation_of_endowment_for_expenditure_with_donor_restrictions: Optional[int] = Field(
        description=(
            "Endowment appropriation from donor-restricted funds during fiscal year 2024–2025 (in thousands). "
            "Only extract if the table specifies 2024. Exclude values from previous fiscal years."
        )
    )

    appropriation_of_endowment_for_expenditure_without_donor_restrictions: Optional[int] = Field(
        description=(
            "Appropriated endowment spending from unrestricted sources during fiscal year 2024–2025 (in thousands). "
            "Only extract from the Notes and labeled clearly as 2024. Ignore prior years."
        )
    )

    # ───── INVESTMENT VALUATION (FAIR VALUE HIERARCHY) ─────
    investment_level_1: Optional[int] = Field(
        description=(
            "Fair value of Level 1 investments (quoted market prices) at year-end 2024–2025 (in thousands). "
            "Only extract from fair value hierarchy tables in the Notes labeled with 2024. "
            "Check the same table that has Fair Value as a header or a similar label."
            "**Do not extract values from 2023 tables or unrelated entities (e.g., ASU Enterprise Partners).**"
        )
    )

    investment_level_2: Optional[int] = Field(
        description=(
            "Fair value of Level 2 investments (observable inputs) at fiscal year end 2024–2025 (in thousands). "
            "Check the same table that has Fair Value as a header or a similar label."
            "Must come from the university’s own Notes. Ensure 2024 label is visible. Exclude prior years."
        )
    )

    investment_level_3: Optional[int] = Field(
        description=(
            "Fair value of Level 3 investments (unobservable inputs) at June 30, 2024 (in thousands). "
            "Check the same table that has Fair Value as a header or a similar label."
            "Must be labeled with 2024 and come from the fair value hierarchy tables under Notes. "
            "Do not mix sources across years."
        )
    )

    # ───── NAV & TOTAL FAIR VALUE ─────
    investments_measured_at_nav: Optional[int] = Field(
        description=(
            "Total value of university investments measured at NAV as of fiscal year 2024–2025 (in thousands). "
            "Must come from a Fair Value table in Notes. "
            "Include Life Insurance Cash Surrender value if it appears separately. "
            "Check the same table that has Fair Value as a header or a similar label."
            "**Only use 2024 figures.**"
        )
    )

    investments_total_fair_value: Optional[int] = Field(
        description=(
            "Grand total fair value of all university investments at end of 2024–2025 (in thousands). "
            "Check the same table that has Fair Value as a header or a similar label."
            "Only extract if clearly labeled and appears in the university’s fair value hierarchy table in the Notes. "
            "**Ignore totals from other years, foundations, or systems.**"
        )
    )
