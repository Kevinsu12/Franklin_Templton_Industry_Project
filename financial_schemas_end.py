from typing import Optional
from pydantic import BaseModel, Field

class EndowmentAndInvestmentLevels_2024_25(BaseModel):
    endowment_net_assets_eoy: Optional[int] = Field(
        description=(
            "Total endowment net assets at the end of fiscal year 2024–2025. "
            "May be labeled as 'Endowment Net Assets', 'EOY Endowment', 'Total Endowment Assets', etc. "
            "Only extract if the amount clearly refers to end-of-year value. "
            "Ignore data from prior years or interim periods. "
            "Do not derive or assume this value unless clearly labeled in the document."
            "Standardize all values to $000s using table metadata or heuristics."
        )
    )

    """
    appropriation_of_endowment_for_expenditure: Optional[int] = Field(
        description=(
            "Appropriations from endowment for expenditure in 2024–2025. "
            "May appear as 'Spending from Endowment', 'Appropriation of Endowment Income', "
            "'Endowment Draw', or similar. "
            "Only extract if this relates to the 2024–2025 period. "
            "Do not derive or infer this amount if not explicitly reported."
            "Standardize all values to $000s using table metadata or heuristics."
        )
    )
    """
    endowment_net_assets_eoy_with_donor_restrictions: Optional[int] = Field(
        description=(
            "Total donor-restricted endowment net assets as of June 30, 2024 (in thousands). "
            "Must be extracted from a 'Changes in Endowment Net Assets' table in the Notes section. "
            "Exclude all 2023 or earlier data. Must be clearly labeled as 2024."
            "Standardize all values to $000s using table metadata or heuristics."
        )
    )

    endowment_net_assets_eoy_with_donor_restrictions_temporarily_restricted: Optional[int] = Field(
        description=(
            "Temporarily restricted portion of donor-restricted endowment net assets for FY2024 (in thousands). "
            "Must appear in a table under Notes with a clear 2024 label. Ignore unlabeled or earlier year data."
            "Standardize all values to $000s using table metadata or heuristics."
        )
    )

    endowment_net_assets_eoy_with_donor_restrictions_permanently_restricted: Optional[int] = Field(
        description=(
            "Permanently restricted portion of donor-restricted endowment net assets for FY2024 (in thousands). "
            "Only extract from Notes where clearly labeled as 2024. Exclude all values from 2023 or earlier."
            "Standardize all values to $000s using table metadata or heuristics."
        )
    )

    endowment_net_assets_eoy_without_donor_restrictions: Optional[int] = Field(
        description=(
            "Unrestricted portion of endowment net assets for the 2024–2025 fiscal year (in thousands). "
            "Must be pulled from a 'Changes in Endowment Net Assets' table in Notes. "
            "Only extract if labeled as 2024. Ignore prior-year or aggregated system data."
            "Standardize all values to $000s using table metadata or heuristics."
        )
    )
    investment_level_1: Optional[int] = Field(
        description=(
            "Fair value of investments categorized under Level 1 (quoted prices in active markets) "
            "as of the end of the 2024–2025 fiscal year. "
            "Labels may include 'Level 1 Inputs', 'Quoted Market Prices', or similar. "
            "Only extract if explicitly stated. Combine across segments if needed."
            "Standardize all values to $000s using table metadata or heuristics."
        )
    )

    investment_level_2: Optional[int] = Field(
        description=(
            "Fair value of investments categorized under Level 2 (observable inputs other than quoted prices) "
            "for the 2024–2025 fiscal year. "
            "May be labeled 'Level 2 Fair Value', 'Observable Inputs', or similar. "
            "Only extract explicitly provided values. Combine all segments if applicable."
            "Standardize all values to $000s using table metadata or heuristics."
        )
    )

    investment_level_3: Optional[int] = Field(
        description=(
            "Fair value of investments categorized under Level 3 (significant unobservable inputs) "
            "as of the 2024–2025 fiscal year. "
            "Labels may include 'Level 3 Investments', 'Unobservable Inputs', etc. "
            "Only extract if the value is explicitly stated."
            "Standardize all values to $000s using table metadata or heuristics."
        )
    )

    investments_measured_at_nav: Optional[int] = Field(
        description=(
            "Investments measured at Net Asset Value (NAV) for the 2024–2025 fiscal year. "
            "May be labeled 'NAV Investments', 'Measured at NAV', or similar. "
            "Only extract if this specific classification is present."
            "Standardize all values to $000s using table metadata or heuristics."
        )
    )

    investments_total_fair_value: Optional[int] = Field(
        description=(
            "Total fair value of all investments for the 2024–2025 fiscal year. "
            "Only extract if explicitly provided. "
            "Do not compute by summing Levels 1–3 and NAV unless the document confirms equivalence."
            "Standardize all values to $000s using table metadata or heuristics."
        )
    )

